# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/rapl.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11protos/rapl.proto\x12\x18smaragdine.protos.sample\"V\n\x0bRaplReading\x12\x0e\n\x06socket\x18\x01 \x02(\r\x12\x0b\n\x03\x63pu\x18\x02 \x01(\x04\x12\x0f\n\x07package\x18\x03 \x01(\x04\x12\x0c\n\x04\x64ram\x18\x04 \x01(\x04\x12\x0b\n\x03gpu\x18\x05 \x01(\x04\"W\n\nRaplSample\x12\x11\n\ttimestamp\x18\x01 \x02(\x04\x12\x36\n\x07reading\x18\x02 \x03(\x0b\x32%.smaragdine.protos.sample.RaplReadingB\x1c\n\x18smaragdine.protos.sampleP\x01')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.rapl_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\030smaragdine.protos.sampleP\001'
  _globals['_RAPLREADING']._serialized_start=47
  _globals['_RAPLREADING']._serialized_end=133
  _globals['_RAPLSAMPLE']._serialized_start=135
  _globals['_RAPLSAMPLE']._serialized_end=222
# @@protoc_insertion_point(module_scope)
