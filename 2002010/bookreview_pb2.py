# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bookreview.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x62ookreview.proto\"*\n\x06review\x12\x10\n\x08\x62ookname\x18\x01 \x01(\t\x12\x0e\n\x06review\x18\x02 \x01(\t\"(\n\x0ereview_reponse\x12\x16\n\x0ereview_reponse\x18\x01 \x01(\t\"\x1d\n\tretrieval\x12\x10\n\x08retrieve\x18\x01 \x01(\t\"$\n\x10retrieve_reponse\x12\x10\n\x08\x62ooklist\x18\x01 \x03(\t\"\x18\n\x07queries\x12\r\n\x05query\x18\x01 \x01(\t\"\x1e\n\rquery_reponse\x12\r\n\x05query\x18\x01 \x01(\t2\x84\x01\n\nbookreview\x12+\n\rcreate_review\x12\x07.review\x1a\x0f.review_reponse\"\x00\x12+\n\x08retrieve\x12\n.retrieval\x1a\x11.retrieve_reponse\"\x00\x12\x1c\n\x05query\x12\x08.queries\x1a\x07.review\"\x00\x62\x06proto3')



_REVIEW = DESCRIPTOR.message_types_by_name['review']
_REVIEW_REPONSE = DESCRIPTOR.message_types_by_name['review_reponse']
_RETRIEVAL = DESCRIPTOR.message_types_by_name['retrieval']
_RETRIEVE_REPONSE = DESCRIPTOR.message_types_by_name['retrieve_reponse']
_QUERIES = DESCRIPTOR.message_types_by_name['queries']
_QUERY_REPONSE = DESCRIPTOR.message_types_by_name['query_reponse']
review = _reflection.GeneratedProtocolMessageType('review', (_message.Message,), {
  'DESCRIPTOR' : _REVIEW,
  '__module__' : 'bookreview_pb2'
  # @@protoc_insertion_point(class_scope:review)
  })
_sym_db.RegisterMessage(review)

review_reponse = _reflection.GeneratedProtocolMessageType('review_reponse', (_message.Message,), {
  'DESCRIPTOR' : _REVIEW_REPONSE,
  '__module__' : 'bookreview_pb2'
  # @@protoc_insertion_point(class_scope:review_reponse)
  })
_sym_db.RegisterMessage(review_reponse)

retrieval = _reflection.GeneratedProtocolMessageType('retrieval', (_message.Message,), {
  'DESCRIPTOR' : _RETRIEVAL,
  '__module__' : 'bookreview_pb2'
  # @@protoc_insertion_point(class_scope:retrieval)
  })
_sym_db.RegisterMessage(retrieval)

retrieve_reponse = _reflection.GeneratedProtocolMessageType('retrieve_reponse', (_message.Message,), {
  'DESCRIPTOR' : _RETRIEVE_REPONSE,
  '__module__' : 'bookreview_pb2'
  # @@protoc_insertion_point(class_scope:retrieve_reponse)
  })
_sym_db.RegisterMessage(retrieve_reponse)

queries = _reflection.GeneratedProtocolMessageType('queries', (_message.Message,), {
  'DESCRIPTOR' : _QUERIES,
  '__module__' : 'bookreview_pb2'
  # @@protoc_insertion_point(class_scope:queries)
  })
_sym_db.RegisterMessage(queries)

query_reponse = _reflection.GeneratedProtocolMessageType('query_reponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERY_REPONSE,
  '__module__' : 'bookreview_pb2'
  # @@protoc_insertion_point(class_scope:query_reponse)
  })
_sym_db.RegisterMessage(query_reponse)

_BOOKREVIEW = DESCRIPTOR.services_by_name['bookreview']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REVIEW._serialized_start=20
  _REVIEW._serialized_end=62
  _REVIEW_REPONSE._serialized_start=64
  _REVIEW_REPONSE._serialized_end=104
  _RETRIEVAL._serialized_start=106
  _RETRIEVAL._serialized_end=135
  _RETRIEVE_REPONSE._serialized_start=137
  _RETRIEVE_REPONSE._serialized_end=173
  _QUERIES._serialized_start=175
  _QUERIES._serialized_end=199
  _QUERY_REPONSE._serialized_start=201
  _QUERY_REPONSE._serialized_end=231
  _BOOKREVIEW._serialized_start=234
  _BOOKREVIEW._serialized_end=366
# @@protoc_insertion_point(module_scope)
