# -*- coding: utf-8 -*-
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from copy import copy
from tabulator import Stream
from functools import partial
from importlib import import_module
from .schema import Schema
from . import exceptions


# Module API

class Table(object):

    # Public

    def __init__(self, source, schema=None, strict=False, references={},
                 post_cast=[], storage=None, **options):
        """https://github.com/frictionlessdata/tableschema-py#schema
        """

        # Set attributes
        self.__source = source
        self.__stream = None
        self.__schema = None
        self.__headers = None
        self.__storage = None
        self.__references = references
        self.__post_cast = copy(post_cast)

        # Schema
        if schema is not None:
            self.__schema = Schema(schema)

        # Stream (tabulator)
        if storage is None:
            options.setdefault('headers', 1)
            self.__stream = Stream(source,  **options)

        # Stream (storage)
        else:
            module = 'tableschema.plugins.%s' % storage
            storage = import_module(module).Storage(**options)
            if self.__schema:
                storage.describe(source, self.__schema.descriptor)
            headers = Schema(storage.describe(source)).field_names
            self.__stream = Stream(partial(storage.iter, source), headers=headers)
            self.__storage = storage

    @property
    def headers(self):
        """https://github.com/frictionlessdata/tableschema-py#schema
        """
        return self.__headers

    @property
    def schema(self):
        """https://github.com/frictionlessdata/tableschema-py#schema
        """
        return self.__schema

    def iter(self, keyed=False, extended=False, cast=True, check=True):
        """https://github.com/frictionlessdata/tableschema-py#schema
        """

        # Resolve references
        if check:
            if callable(self.__references):
                self.__references = self.__references()

        # Prepare unique checks
        if check:
            unique_fields_cache = {}
            if self.schema:
                unique_fields_cache = _create_unique_fields_cache(self.schema)

        # Open/iterate stream
        self.__stream.open()
        iterator = self.__stream.iter(extended=True)
        iterator = self.__apply_processors(iterator, cast=cast)
        for row_number, headers, row in iterator:

            # Get headers
            if not self.__headers:
                self.__headers = headers

            # Check headers
            if check:
                if self.schema and self.headers:
                    if self.headers != self.schema.field_names:
                        message = 'Table headers don\'t match schema field names'
                        raise exceptions.CheckError(message)

            # Check unique
            if check:
                for index, cache in unique_fields_cache.items():
                    if row[index] in cache:
                        field_name = self.schema.fields[index].name
                        message = 'Field "%s" duplicates in row "%s"'
                        message = message % (field_name, row_number)
                        raise exceptions.TableSchemaException(message)
                    cache.add(row[index])

            # Check foreign
            if check:
                if self.schema and self.schema.foreign_keys:
                    keyed_row = dict(zip(headers, row))
                    for fk in self.schema.foreign_keys:
                        reference = self.__references.get(fk['reference']['resource'])
                        if not reference:
                            continue
                        values = {}
                        fields = zip(fk['fields'], fk['reference']['fields'])
                        for field, ref_field in fields:
                            if field and ref_field:
                                values[ref_field] = keyed_row[field]
                        empty = all(map(lambda value: value is None, values.values()))
                        valid = any(map(partial(_is_match, values), reference))
                        if not empty and not valid:
                            message = 'Foreign key "%s" violation in row "%s"'
                            message = message % (fk['fields'], row_number)
                            raise exceptions.CheckError(message)

            # Form row
            if extended:
                yield (row_number, headers, row)
            elif keyed:
                yield dict(zip(headers, row))
            else:
                yield row

        # Close stream
        self.__stream.close()

    def read(self, keyed=False, extended=False, cast=True, limit=None, check=True):
        """https://github.com/frictionlessdata/tableschema-py#schema
        """
        result = []
        rows = self.iter(keyed=keyed, extended=extended, cast=cast, check=check)
        for count, row in enumerate(rows, start=1):
            result.append(row)
            if count == limit:
                break
        return result

    def infer(self, limit=100):
        """https://github.com/frictionlessdata/tableschema-py#schema
        """
        if self.__schema is None or self.__headers is None:

            # Infer (tabulator)
            if not self.__storage:
                with self.__stream as stream:
                    if self.__schema is None:
                        self.__schema = Schema()
                        self.__schema.infer(stream.sample[:limit], headers=stream.headers)
                    if self.__headers is None:
                        self.__headers = stream.headers

            # Infer (storage)
            else:
                descriptor = self.__storage.describe(self.__source)
                if self.__schema is None:
                    self.__schema = Schema(descriptor)
                if self.__headers is None:
                    self.__headers = self.__schema.field_names

        return self.__schema.descriptor

    def save(self, target, storage=None, **options):
        """https://github.com/frictionlessdata/tableschema-py#schema
        """

        # Save (tabulator)
        if storage is None:
            with Stream(self.iter, headers=self.__schema.headers) as stream:
                stream.save(target, **options)
            return True

        # Save (storage)
        else:
            module = 'tableschema.plugins.%s' % storage
            storage = import_module(module).Storage(**options)
            storage.create(target, self.__schema.descriptor, force=True)
            storage.write(target, self.iter())
            return storage

    # Private

    def __apply_processors(self, iterator, cast=True):

        # Apply processors to iterator
        def builtin_processor(extended_rows):
            for row_number, headers, row in extended_rows:
                if self.__schema and cast:
                    row = self.__schema.cast_row(row)
                yield (row_number, headers, row)
        processors = [builtin_processor] + self.__post_cast
        for processor in processors:
            iterator = processor(iterator)

        return iterator


# Internal

def _create_unique_fields_cache(schema):
    cache = {}
    for index, field in enumerate(schema.fields):
        if field.constraints.get('unique') or field.name in schema.primary_key:
            cache[index] = set()
    return cache


def _is_match(subset, superset):
    return set(subset.items()).issubset(set(superset.items()))
