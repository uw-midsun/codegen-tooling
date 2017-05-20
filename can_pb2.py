# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: can.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='can.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\tcan.proto\"Z\n\tDataframe\x12\x1d\n\x04type\x18\x01 \x01(\x0e\x32\x0f.Dataframe.Type\x12\r\n\x05start\x18\x02 \x01(\r\x12\x0b\n\x03\x65nd\x18\x03 \x01(\r\"\x12\n\x04Type\x12\n\n\x06UINT64\x10\x00\"2\n\x07\x43\x61nData\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x04\x12\x19\n\x05\x66rame\x18\x02 \x03(\x0b\x32\n.Dataframe\"\x99\x02\n\x06\x43\x61nMsg\x12\n\n\x02id\x18\x01 \x01(\r\x12\x1e\n\x06source\x18\x02 \x01(\x0e\x32\x0e.CanMsg.Source\x12\x0e\n\x06is_ack\x18\x03 \x01(\x08\x12\x15\n\rglobal_msg_id\x18\x04 \x01(\r\x12\x10\n\x08msg_name\x18\x05 \x01(\t\x12\x1a\n\x08\x63\x61n_data\x18\x06 \x01(\x0b\x32\x08.CanData\"\x8d\x01\n\x06Source\x12\n\n\x06PLUTUS\x10\x00\x12\t\n\x05\x43HAOS\x10\x01\x12\r\n\tTELEMETRY\x10\x02\x12\n\n\x06LIGHTS\x10\x03\x12\x14\n\x10MOTOR_CONTROLLER\x10\x04\x12\n\n\x06THEMIS\x10\x05\x12\x10\n\x0cRASPBERRY_PI\x10\x06\x12\x0e\n\nMPPT_FRONT\x10\x07\x12\r\n\tMPPT_REAR\x10\x08\"!\n\tCanSchema\x12\x14\n\x03msg\x18\x01 \x03(\x0b\x32\x07.CanMsgb\x06proto3')
)



_DATAFRAME_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='Dataframe.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UINT64', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=85,
  serialized_end=103,
)
_sym_db.RegisterEnumDescriptor(_DATAFRAME_TYPE)

_CANMSG_SOURCE = _descriptor.EnumDescriptor(
  name='Source',
  full_name='CanMsg.Source',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PLUTUS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHAOS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TELEMETRY', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LIGHTS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOTOR_CONTROLLER', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='THEMIS', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RASPBERRY_PI', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MPPT_FRONT', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MPPT_REAR', index=8, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=298,
  serialized_end=439,
)
_sym_db.RegisterEnumDescriptor(_CANMSG_SOURCE)


_DATAFRAME = _descriptor.Descriptor(
  name='Dataframe',
  full_name='Dataframe',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Dataframe.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='Dataframe.start', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='Dataframe.end', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DATAFRAME_TYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13,
  serialized_end=103,
)


_CANDATA = _descriptor.Descriptor(
  name='CanData',
  full_name='CanData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='CanData.data', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='frame', full_name='CanData.frame', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=105,
  serialized_end=155,
)


_CANMSG = _descriptor.Descriptor(
  name='CanMsg',
  full_name='CanMsg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='CanMsg.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='CanMsg.source', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_ack', full_name='CanMsg.is_ack', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='global_msg_id', full_name='CanMsg.global_msg_id', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg_name', full_name='CanMsg.msg_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='can_data', full_name='CanMsg.can_data', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CANMSG_SOURCE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=158,
  serialized_end=439,
)


_CANSCHEMA = _descriptor.Descriptor(
  name='CanSchema',
  full_name='CanSchema',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='CanSchema.msg', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=441,
  serialized_end=474,
)

_DATAFRAME.fields_by_name['type'].enum_type = _DATAFRAME_TYPE
_DATAFRAME_TYPE.containing_type = _DATAFRAME
_CANDATA.fields_by_name['frame'].message_type = _DATAFRAME
_CANMSG.fields_by_name['source'].enum_type = _CANMSG_SOURCE
_CANMSG.fields_by_name['can_data'].message_type = _CANDATA
_CANMSG_SOURCE.containing_type = _CANMSG
_CANSCHEMA.fields_by_name['msg'].message_type = _CANMSG
DESCRIPTOR.message_types_by_name['Dataframe'] = _DATAFRAME
DESCRIPTOR.message_types_by_name['CanData'] = _CANDATA
DESCRIPTOR.message_types_by_name['CanMsg'] = _CANMSG
DESCRIPTOR.message_types_by_name['CanSchema'] = _CANSCHEMA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Dataframe = _reflection.GeneratedProtocolMessageType('Dataframe', (_message.Message,), dict(
  DESCRIPTOR = _DATAFRAME,
  __module__ = 'can_pb2'
  # @@protoc_insertion_point(class_scope:Dataframe)
  ))
_sym_db.RegisterMessage(Dataframe)

CanData = _reflection.GeneratedProtocolMessageType('CanData', (_message.Message,), dict(
  DESCRIPTOR = _CANDATA,
  __module__ = 'can_pb2'
  # @@protoc_insertion_point(class_scope:CanData)
  ))
_sym_db.RegisterMessage(CanData)

CanMsg = _reflection.GeneratedProtocolMessageType('CanMsg', (_message.Message,), dict(
  DESCRIPTOR = _CANMSG,
  __module__ = 'can_pb2'
  # @@protoc_insertion_point(class_scope:CanMsg)
  ))
_sym_db.RegisterMessage(CanMsg)

CanSchema = _reflection.GeneratedProtocolMessageType('CanSchema', (_message.Message,), dict(
  DESCRIPTOR = _CANSCHEMA,
  __module__ = 'can_pb2'
  # @@protoc_insertion_point(class_scope:CanSchema)
  ))
_sym_db.RegisterMessage(CanSchema)


# @@protoc_insertion_point(module_scope)
