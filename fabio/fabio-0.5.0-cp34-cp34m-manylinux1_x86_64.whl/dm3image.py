# coding: utf-8
#
#    Project: X-ray image reader
#             https://github.com/silx-kit/fabio
#
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Jérôme Kieffer (Jerome.Kieffer@ESRF.eu)
#
#  Permission is hereby granted, free of charge, to any person
#  obtaining a copy of this software and associated documentation files
#  (the "Software"), to deal in the Software without restriction,
#  including without limitation the rights to use, copy, modify, merge,
#  publish, distribute, sublicense, and/or sell copies of the Software,
#  and to permit persons to whom the Software is furnished to do so,
#  subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be
#  included in all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#  OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#  NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#  HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#  WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION W

"""
Authors: Henning O. Sorensen & Erik Knudsen
         Center for Fundamental Research: Metal Structures in Four Dimensions
         Risoe National Laboratory
         Frederiksborgvej 399
         DK-4000 Roskilde
         email:erik.knudsen@risoe.dk

        + Jon Wright, ESRF
"""
# get ready for python3
from __future__ import with_statement, print_function

import logging
import numpy
from .fabioimage import FabioImage
logger = logging.getLogger(__name__)

DATA_TYPES = {  2     : numpy.int16,
                4     : numpy.uint16,
                3     : numpy.int32,
                5     : numpy.uint32,
                6     : numpy.float32,
                7     : numpy.float,
                8     : numpy.int8,
                9     : None,
                10    : None,
                15    : 'Struct',
                18    : None,
                20    : None
                }

DATA_BYTES = {  2     : 2,
                4     : 2,
                3     : 4,
                5     : 4,
                6     : 4,
                7     : 8,
                8     : 1,
                9     : None,
                10    : None,
                15    : 'Struct',
                18    : None,
                20    : None
                }


class Dm3Image(FabioImage):
    """ Read and try to write the dm3 data format """

    DESCRIPTION = "Digital Micrograph DM3 file format"

    DEFAULT_EXTENTIONS = ["dm3"]

    def __init__(self, *args, **kwargs):
        FabioImage.__init__(self, *args, **kwargs)
        self.encoded_datatype = None
        self.no_data_elements = None
        self.grouptag_is_sorted = None
        self.grouptag_is_open = None
        self.tag_encoded_type = None
        self.tag_data_type = None
        self.tag_is_data = None
        self.grouptag_no_tags = None
        self.bytes_in_file = None
        self.tag_label_length = None
        self.go_on = None

    def _readheader(self):
        self.infile.seek(0)
        file_format = self.readbytes(4, numpy.uint32)[0]  # should be 3
        assert file_format == 3, 'Wrong file type '
        self.bytes_in_file = self.readbytes(4, numpy.uint32)[0]
        self.byte_order = self.readbytes(4, numpy.uint32)[0]  # 0 = big, 1= little
        logger.info('read dm3 file - file format %s' % file_format)
        logger.info('Bytes in file: %s' % self.bytes_in_file)
        logger.info('Byte order: %s  - 0 = bigEndian , 1 = littleEndian' % self.byte_order)

        if self.byte_order == 0:
            self.swap = True
        elif self.byte_order == 1:
            self.swap = False
        else:
            raise ValueError

    def read(self, fname, frame=None):
        self.header = self.check_header()
        self.resetvals()
        self.infile = self._open(fname, "rb")
        self._readheader()
        self.go_on = True
        while self.go_on:
            self.read_tag_group()
            self.read_tag_entry()
            if self.infile.tell() > self.bytes_in_file:
                break

            while self.tag_is_data == 21:
                self.read_tag_entry()
                if self.infile.tell() > self.bytes_in_file:
                    self.go_on = False

        (dim1_raw, dim2_raw) = self.header['Active Size (pixels)'].split()
        (dim1_raw, dim2_raw) = (eval(dim1_raw), eval(dim2_raw))
        (dim1_binning, dim2_binning) = self.header['Binning'].split()
        (dim1_binning, dim2_binning) = (eval(dim1_binning), eval(dim2_binning))
        self.dim1 = dim1_raw / dim1_binning
        self.dim2 = dim2_raw / dim2_binning
        # print dim1,dim2
        if "Data" in self.header:
            self.data = self.header['Data'].reshape(self.dim1, self.dim2)

    def readbytes(self, bytes_to_read, format, swap=True):
        raw = self.infile.read(bytes_to_read)
        if format is not None:
            data = numpy.fromstring(raw, format)
        else:
            data = raw
        if swap:
            data = data.byteswap()
        return data

    def read_tag_group(self):

        self.grouptag_is_sorted = self.readbytes(1, numpy.uint8)[0]
        self.grouptag_is_open = self.readbytes(1, numpy.uint8)[0]
        self.grouptag_no_tags = self.readbytes(4, numpy.uint32)[0]
        logger.debug('TagGroup is sorted? %s', self.grouptag_is_sorted)
        logger.debug('TagGroup is open? %s', self.grouptag_is_open)
        logger.debug('no of tags in TagGroup %s', self.grouptag_no_tags)

    def read_tag_entry(self):

        self.tag_is_data = self.readbytes(1, numpy.uint8)[0]
        self.tag_label_length = self.readbytes(2, numpy.uint16)[0]
        logger.debug('does Tag have data ? %s  -  20 = Tag group , 21 = data ', self.tag_is_data)
        logger.debug('length of tag_label %s', self.tag_label_length)
        if self.tag_label_length != 0:
            tag_label = self.infile.read(self.tag_label_length)
        else:
            tag_label = None

        if self.tag_is_data == 21:
            # This is data
            self.header[tag_label] = self.read_tag_type()
            logger.debug("%s: %s", tag_label, self.header[tag_label])

    def read_tag_type(self):
        if self.infile.read(4) != '%%%%':
            raise IOError
        self.tag_data_type = self.readbytes(4, numpy.uint32)[0]
        logger.debug('data is of type : %s - 1 = simple, 2 = string, 3 = array, >3 structs', self.tag_data_type)
        self.tag_encoded_type = self.readbytes(4, numpy.uint32)[0]
        logger.debug('encode type: %s %s', self.tag_encoded_type, DATA_TYPES[self.tag_encoded_type])
        if self.tag_data_type == 1:
            # simple type
            return self.readbytes(DATA_BYTES[self.tag_encoded_type],
                                  DATA_TYPES[self.tag_encoded_type],
                                  swap=self.swap)[0]
        # are the data stored in a simple array?
        if self.tag_encoded_type == 20 and self.tag_data_type == 3:
            self.data_type = self.readbytes(4, numpy.uint32)[0]
            self.no_data_elements = self.readbytes(4, numpy.uint32)[0]
            if self.data_type == 10:
                logger.debug('skip bytes %s', self.no_data_elements)
                _dump = self.infile.read(self.no_data_elements)
                return None

            logger.debug('Data are stored as a simple a array -')
            logger.debug('%s data elemets stored as %s', self.no_data_elements, self.data_type)
            read_no_bytes = DATA_BYTES[self.data_type] * self.no_data_elements
            fmt = DATA_TYPES[self.data_type]
            return self.readbytes(read_no_bytes, fmt, swap=self.swap)

        # are the data stored in a complex array ?
        # print 'tag_type + data_type', self.tag_encoded_type,self.tag_data_type

        # print self.tag_encoded_type , self.tag_data_type
        if self.tag_encoded_type == 20 and self.tag_data_type > 3:
            self.tag_encoded_type = self.readbytes(4, numpy.uint32)[0]
            logger.debug('found array - new tag_encoded_type %s', self.tag_encoded_type)
            if self.tag_encoded_type == 15:  # struct type
                # ##type = self.readbytes(4,numpy.int32)
                _struct_name_length = self.readbytes(4, numpy.int32)[0]
                struct_number_fields = self.readbytes(4, numpy.int32)[0]
                # print 'struct - name_length, number_field',  struct_name_length,struct_number_fields
                # print self.infile.read(_struct_name_length)
                field_info = []
                for i in range(struct_number_fields):
                    field_info.append([self.readbytes(4, numpy.int32)[0], self.readbytes(4, numpy.int32)[0]])
                # print field_info
                self.no_data_elements = self.readbytes(4, numpy.int32)[0]
                # print '%i data elemets stored as ' %self.no_data_elements
                bytes_in_struct = 0
                for i in range(struct_number_fields):
                    bytes_in_struct += DATA_BYTES[field_info[i][1]]
                logger.debug('skip bytes %s', self.no_data_elements * bytes_in_struct)
                _dump = self.infile.read(self.no_data_elements * bytes_in_struct)
                return None

        if self.tag_encoded_type == 15:  # struct type
            # ##type = self.readbytes(4,numpy.int32)
            _struct_name_length = self.readbytes(4, numpy.int32)[0]
            struct_number_fields = self.readbytes(4, numpy.int32)[0]
            # print 'struct - name_length, number_field', _struct_name_length,struct_number_fields
            # print self.infile.read(struct_name_length)
            field_info = []
            for i in range(struct_number_fields):
                field_info.append([self.readbytes(4, numpy.int32)[0], self.readbytes(4, numpy.int32)[0]])
            # print field_info
            field_data = ''
            for i in range(struct_number_fields):
                # print type(i)
                field_data = field_data + self.readbytes(field_info[i][0], None, swap=False) + ' '
                field_data = field_data + '%i  ' % self.readbytes(DATA_BYTES[field_info[i][1]],
                                                                  DATA_TYPES[field_info[i][1]],
                                                                  swap=self.swap)[0]
            return field_data

    def read_data(self):
        self.encoded_datatype = numpy.fromstring(self.infile.read(4), numpy.uint32).byteswap()


dm3image = Dm3Image
