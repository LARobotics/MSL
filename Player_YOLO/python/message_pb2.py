# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rmessage.proto\x12\x02pb\"M\n\rObject_Kinect\x12\n\n\x02id\x18\x01 \x01(\r\x12\t\n\x01x\x18\x02 \x01(\r\x12\t\n\x01y\x18\x03 \x01(\r\x12\x0c\n\x04\x64ist\x18\x04 \x01(\r\x12\x0c\n\x04\x63onf\x18\x05 \x01(\r\"K\n\x0bObject_Omni\x12\n\n\x02id\x18\x01 \x01(\r\x12\t\n\x01x\x18\x02 \x01(\r\x12\t\n\x01y\x18\x03 \x01(\r\x12\x0c\n\x04\x64ist\x18\x04 \x01(\r\x12\x0c\n\x04\x63onf\x18\x06 \x01(\r\"2\n\x12Request_Omni_Calib\x12\r\n\x05\x63heck\x18\x01 \x01(\x08\x12\r\n\x05image\x18\x02 \x01(\x0c\"\x18\n\x07Request\x12\r\n\x05\x63heck\x18\x01 \x01(\x08\"\x1b\n\nRequest_BS\x12\r\n\x05\x63heck\x18\x01 \x01(\r\"T\n\rResponse_Omni\x12\x0c\n\x04omni\x18\x01 \x01(\x0c\x12\x13\n\x0bimg_to_send\x18\x02 \x01(\r\x12 \n\x07objects\x18\x03 \x03(\x0b\x32\x0f.pb.Object_Omni\"[\n\x0fResponse_Kinect\x12\x0e\n\x06kinect\x18\x01 \x01(\x0c\x12\x14\n\x0ckinect_depth\x18\x02 \x01(\x0c\x12\"\n\x07objects\x18\x03 \x03(\x0b\x32\x11.pb.Object_Kinect\".\n\x0eResponse_to_BS\x12\r\n\x05image\x18\x01 \x01(\x0c\x12\r\n\x05\x63ount\x18\x02 \x01(\r2E\n\tYolo_Omni\x12\x38\n\tSend_Omni\x12\x16.pb.Request_Omni_Calib\x1a\x11.pb.Response_Omni\"\x00\x32@\n\x0bYolo_Kinect\x12\x31\n\x0bSend_Kinect\x12\x0b.pb.Request\x1a\x13.pb.Response_Kinect\"\x00\x32\x43\n\rBase_Satation\x12\x32\n\nSend_to_BS\x12\x0e.pb.Request_BS\x1a\x12.pb.Response_to_BS\"\x00\x42(Z&github.com/ardanlabs/python-go/grpc/pbb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'message_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z&github.com/ardanlabs/python-go/grpc/pb'
  _OBJECT_KINECT._serialized_start=21
  _OBJECT_KINECT._serialized_end=98
  _OBJECT_OMNI._serialized_start=100
  _OBJECT_OMNI._serialized_end=175
  _REQUEST_OMNI_CALIB._serialized_start=177
  _REQUEST_OMNI_CALIB._serialized_end=227
  _REQUEST._serialized_start=229
  _REQUEST._serialized_end=253
  _REQUEST_BS._serialized_start=255
  _REQUEST_BS._serialized_end=282
  _RESPONSE_OMNI._serialized_start=284
  _RESPONSE_OMNI._serialized_end=368
  _RESPONSE_KINECT._serialized_start=370
  _RESPONSE_KINECT._serialized_end=461
  _RESPONSE_TO_BS._serialized_start=463
  _RESPONSE_TO_BS._serialized_end=509
  _YOLO_OMNI._serialized_start=511
  _YOLO_OMNI._serialized_end=580
  _YOLO_KINECT._serialized_start=582
  _YOLO_KINECT._serialized_end=646
  _BASE_SATATION._serialized_start=648
  _BASE_SATATION._serialized_end=715
# @@protoc_insertion_point(module_scope)