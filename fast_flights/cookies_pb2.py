# type: ignore
# ruff: noqa

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cookies.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rcookies.proto\"*\n\x0bInformation\x12\x0b\n\x03gws\x18\x02 \x01(\t\x12\x0e\n\x06locale\x18\x03 \x01(\t\"\x1d\n\x08\x44\x61tetime\x12\x11\n\ttimestamp\x18\x01 \x01(\r\"?\n\x04SOCS\x12\x1a\n\x04info\x18\x02 \x01(\x0b\x32\x0c.Information\x12\x1b\n\x08\x64\x61tetime\x18\x03 \x01(\x0b\x32\t.Datetimeb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cookies_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INFORMATION._serialized_start=17
  _INFORMATION._serialized_end=59
  _DATETIME._serialized_start=61
  _DATETIME._serialized_end=90
  _SOCS._serialized_start=92
  _SOCS._serialized_end=155
# @@protoc_insertion_point(module_scope)
