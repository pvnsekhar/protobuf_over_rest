# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: calc.proto
# Protobuf Python Version: 5.28.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    3,
    '',
    'calc.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ncalc.proto\"*\n\x0c\x63\x61lc_request\x12\x0c\n\x04var1\x18\x01 \x01(\x05\x12\x0c\n\x04var2\x18\x02 \x01(\x05\"0\n\rcalc_response\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x0f\n\x07success\x18\x02 \x01(\x08\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'calc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CALC_REQUEST']._serialized_start=14
  _globals['_CALC_REQUEST']._serialized_end=56
  _globals['_CALC_RESPONSE']._serialized_start=58
  _globals['_CALC_RESPONSE']._serialized_end=106
# @@protoc_insertion_point(module_scope)
