# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: metadata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import fee_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='metadata.proto',
  package='',
  serialized_pb=_b('\n\x0emetadata.proto\x1a\tfee.proto\"\xcd\x02\n\x08Metadata\x12\"\n\x07version\x18\x01 \x02(\x0e\x32\x11.Metadata.Version\x12$\n\x08language\x18\x02 \x02(\x0e\x32\x12.Metadata.Language\x12\r\n\x05title\x18\x03 \x02(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x02(\t\x12\x0e\n\x06\x61uthor\x18\x05 \x02(\t\x12\x0f\n\x07license\x18\x06 \x02(\t\x12\x0c\n\x04nsfw\x18\x07 \x02(\x08\x12\x11\n\x03\x66\x65\x65\x18\x08 \x01(\x0b\x32\x04.Fee\x12\x11\n\tthumbnail\x18\t \x01(\t\x12\x0f\n\x07preview\x18\n \x01(\t\x12\x12\n\nlicenseUrl\x18\x0b \x01(\t\"9\n\x07Version\x12\n\n\x06_0_0_1\x10\x00\x12\n\n\x06_0_0_2\x10\x01\x12\n\n\x06_0_0_3\x10\x02\x12\n\n\x06_0_1_0\x10\x03\"\x1e\n\x08Language\x12\x06\n\x02\x45N\x10\x00\x12\x06\n\x02\x65n\x10\x00\x1a\x02\x10\x01')
  ,
  dependencies=[fee_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_METADATA_VERSION = _descriptor.EnumDescriptor(
  name='Version',
  full_name='Metadata.Version',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='_0_0_1', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='_0_0_2', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='_0_0_3', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='_0_1_0', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=274,
  serialized_end=331,
)
_sym_db.RegisterEnumDescriptor(_METADATA_VERSION)

_METADATA_LANGUAGE = _descriptor.EnumDescriptor(
  name='Language',
  full_name='Metadata.Language',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='en', index=1, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=_descriptor._ParseOptions(descriptor_pb2.EnumOptions(), _b('\020\001')),
  serialized_start=333,
  serialized_end=363,
)
_sym_db.RegisterEnumDescriptor(_METADATA_LANGUAGE)


_METADATA = _descriptor.Descriptor(
  name='Metadata',
  full_name='Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='Metadata.version', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language', full_name='Metadata.language', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='title', full_name='Metadata.title', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='Metadata.description', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='author', full_name='Metadata.author', index=4,
      number=5, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='license', full_name='Metadata.license', index=5,
      number=6, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nsfw', full_name='Metadata.nsfw', index=6,
      number=7, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fee', full_name='Metadata.fee', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='thumbnail', full_name='Metadata.thumbnail', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='preview', full_name='Metadata.preview', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='licenseUrl', full_name='Metadata.licenseUrl', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _METADATA_VERSION,
    _METADATA_LANGUAGE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=363,
)

_METADATA.fields_by_name['version'].enum_type = _METADATA_VERSION
_METADATA.fields_by_name['language'].enum_type = _METADATA_LANGUAGE
_METADATA.fields_by_name['fee'].message_type = fee_pb2._FEE
_METADATA_VERSION.containing_type = _METADATA
_METADATA_LANGUAGE.containing_type = _METADATA
DESCRIPTOR.message_types_by_name['Metadata'] = _METADATA

Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), dict(
  DESCRIPTOR = _METADATA,
  __module__ = 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:Metadata)
  ))
_sym_db.RegisterMessage(Metadata)


_METADATA_LANGUAGE.has_options = True
_METADATA_LANGUAGE._options = _descriptor._ParseOptions(descriptor_pb2.EnumOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
