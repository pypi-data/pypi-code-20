# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/any_test.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from appdynamics_bindeps.google.protobuf import descriptor as _descriptor
from appdynamics_bindeps.google.protobuf import message as _message
from appdynamics_bindeps.google.protobuf import reflection as _reflection
from appdynamics_bindeps.google.protobuf import symbol_database as _symbol_database
from appdynamics_bindeps.google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from appdynamics_bindeps.google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/protobuf/any_test.proto',
  package='protobuf_unittest',
  syntax='proto3',
  serialized_pb=_b('\n\x1egoogle/protobuf/any_test.proto\x12\x11protobuf_unittest\x1a\x19google/protobuf/any.proto\"y\n\x07TestAny\x12\x13\n\x0bint32_value\x18\x01 \x01(\x05\x12\'\n\tany_value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x30\n\x12repeated_any_value\x18\x03 \x03(\x0b\x32\x14.google.protobuf.Anyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TESTANY = _descriptor.Descriptor(
  name='TestAny',
  full_name='protobuf_unittest.TestAny',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='int32_value', full_name='protobuf_unittest.TestAny.int32_value', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='any_value', full_name='protobuf_unittest.TestAny.any_value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='repeated_any_value', full_name='protobuf_unittest.TestAny.repeated_any_value', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=201,
)

_TESTANY.fields_by_name['any_value'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_TESTANY.fields_by_name['repeated_any_value'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['TestAny'] = _TESTANY

TestAny = _reflection.GeneratedProtocolMessageType('TestAny', (_message.Message,), dict(
  DESCRIPTOR = _TESTANY,
  __module__ = 'google.protobuf.any_test_pb2'
  # @@protoc_insertion_point(class_scope:protobuf_unittest.TestAny)
  ))
_sym_db.RegisterMessage(TestAny)


# @@protoc_insertion_point(module_scope)
