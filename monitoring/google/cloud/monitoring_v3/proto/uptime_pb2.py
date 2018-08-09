# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/monitoring_v3/proto/uptime.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import monitored_resource_pb2 as google_dot_api_dot_monitored__resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/monitoring_v3/proto/uptime.proto',
  package='google.monitoring.v3',
  syntax='proto3',
  serialized_pb=_b('\n-google/cloud/monitoring_v3/proto/uptime.proto\x12\x14google.monitoring.v3\x1a#google/api/monitored_resource.proto\x1a\x1egoogle/protobuf/duration.proto\"\xb2\n\n\x11UptimeCheckConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12;\n\x12monitored_resource\x18\x03 \x01(\x0b\x32\x1d.google.api.MonitoredResourceH\x00\x12O\n\x0eresource_group\x18\x04 \x01(\x0b\x32\x35.google.monitoring.v3.UptimeCheckConfig.ResourceGroupH\x00\x12G\n\nhttp_check\x18\x05 \x01(\x0b\x32\x31.google.monitoring.v3.UptimeCheckConfig.HttpCheckH\x01\x12\x45\n\ttcp_check\x18\x06 \x01(\x0b\x32\x30.google.monitoring.v3.UptimeCheckConfig.TcpCheckH\x01\x12)\n\x06period\x18\x07 \x01(\x0b\x32\x19.google.protobuf.Duration\x12*\n\x07timeout\x18\x08 \x01(\x0b\x32\x19.google.protobuf.Duration\x12P\n\x10\x63ontent_matchers\x18\t \x03(\x0b\x32\x36.google.monitoring.v3.UptimeCheckConfig.ContentMatcher\x12\x41\n\x10selected_regions\x18\n \x03(\x0e\x32\'.google.monitoring.v3.UptimeCheckRegion\x12R\n\x11internal_checkers\x18\x0e \x03(\x0b\x32\x37.google.monitoring.v3.UptimeCheckConfig.InternalChecker\x1a\x61\n\rResourceGroup\x12\x10\n\x08group_id\x18\x01 \x01(\t\x12>\n\rresource_type\x18\x02 \x01(\x0e\x32\'.google.monitoring.v3.GroupResourceType\x1a\xe4\x02\n\tHttpCheck\x12\x0f\n\x07use_ssl\x18\x01 \x01(\x08\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x0c\n\x04port\x18\x03 \x01(\x05\x12X\n\tauth_info\x18\x04 \x01(\x0b\x32\x45.google.monitoring.v3.UptimeCheckConfig.HttpCheck.BasicAuthentication\x12\x14\n\x0cmask_headers\x18\x05 \x01(\x08\x12O\n\x07headers\x18\x06 \x03(\x0b\x32>.google.monitoring.v3.UptimeCheckConfig.HttpCheck.HeadersEntry\x1a\x39\n\x13\x42\x61sicAuthentication\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x18\n\x08TcpCheck\x12\x0c\n\x04port\x18\x01 \x01(\x05\x1a!\n\x0e\x43ontentMatcher\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x1ar\n\x0fInternalChecker\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0f\n\x07network\x18\x02 \x01(\t\x12\x10\n\x08gcp_zone\x18\x03 \x01(\t\x12\x12\n\nchecker_id\x18\x04 \x01(\t\x12\x14\n\x0c\x64isplay_name\x18\x05 \x01(\tB\n\n\x08resourceB\x14\n\x12\x63heck_request_type\"n\n\rUptimeCheckIp\x12\x37\n\x06region\x18\x01 \x01(\x0e\x32\'.google.monitoring.v3.UptimeCheckRegion\x12\x10\n\x08location\x18\x02 \x01(\t\x12\x12\n\nip_address\x18\x03 \x01(\t*e\n\x11UptimeCheckRegion\x12\x16\n\x12REGION_UNSPECIFIED\x10\x00\x12\x07\n\x03USA\x10\x01\x12\n\n\x06\x45UROPE\x10\x02\x12\x11\n\rSOUTH_AMERICA\x10\x03\x12\x10\n\x0c\x41SIA_PACIFIC\x10\x04*[\n\x11GroupResourceType\x12\x1d\n\x19RESOURCE_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08INSTANCE\x10\x01\x12\x19\n\x15\x41WS_ELB_LOAD_BALANCER\x10\x02\x42\xa3\x01\n\x18\x63om.google.monitoring.v3B\x0bUptimeProtoP\x01Z>google.golang.org/genproto/googleapis/monitoring/v3;monitoring\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_monitored__resource__pb2.DESCRIPTOR,google_dot_protobuf_dot_duration__pb2.DESCRIPTOR,])

_UPTIMECHECKREGION = _descriptor.EnumDescriptor(
  name='UptimeCheckRegion',
  full_name='google.monitoring.v3.UptimeCheckRegion',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REGION_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USA', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EUROPE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOUTH_AMERICA', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ASIA_PACIFIC', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1585,
  serialized_end=1686,
)
_sym_db.RegisterEnumDescriptor(_UPTIMECHECKREGION)

UptimeCheckRegion = enum_type_wrapper.EnumTypeWrapper(_UPTIMECHECKREGION)
_GROUPRESOURCETYPE = _descriptor.EnumDescriptor(
  name='GroupResourceType',
  full_name='google.monitoring.v3.GroupResourceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RESOURCE_TYPE_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INSTANCE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AWS_ELB_LOAD_BALANCER', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1688,
  serialized_end=1779,
)
_sym_db.RegisterEnumDescriptor(_GROUPRESOURCETYPE)

GroupResourceType = enum_type_wrapper.EnumTypeWrapper(_GROUPRESOURCETYPE)
REGION_UNSPECIFIED = 0
USA = 1
EUROPE = 2
SOUTH_AMERICA = 3
ASIA_PACIFIC = 4
RESOURCE_TYPE_UNSPECIFIED = 0
INSTANCE = 1
AWS_ELB_LOAD_BALANCER = 2



_UPTIMECHECKCONFIG_RESOURCEGROUP = _descriptor.Descriptor(
  name='ResourceGroup',
  full_name='google.monitoring.v3.UptimeCheckConfig.ResourceGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_id', full_name='google.monitoring.v3.UptimeCheckConfig.ResourceGroup.group_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource_type', full_name='google.monitoring.v3.UptimeCheckConfig.ResourceGroup.resource_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=804,
  serialized_end=901,
)

_UPTIMECHECKCONFIG_HTTPCHECK_BASICAUTHENTICATION = _descriptor.Descriptor(
  name='BasicAuthentication',
  full_name='google.monitoring.v3.UptimeCheckConfig.HttpCheck.BasicAuthentication',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='google.monitoring.v3.UptimeCheckConfig.HttpCheck.BasicAuthentication.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='google.monitoring.v3.UptimeCheckConfig.HttpCheck.BasicAuthentication.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=1155,
  serialized_end=1212,
)

_UPTIMECHECKCONFIG_HTTPCHECK_HEADERSENTRY = _descriptor.Descriptor(
  name='HeadersEntry',
  full_name='google.monitoring.v3.UptimeCheckConfig.HttpCheck.HeadersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='google.monitoring.v3.UptimeCheckConfig.HttpCheck.HeadersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.monitoring.v3.UptimeCheckConfig.HttpCheck.HeadersEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1214,
  serialized_end=1260,
)

_UPTIMECHECKCONFIG_HTTPCHECK = _descriptor.Descriptor(
  name='HttpCheck',
  full_name='google.monitoring.v3.UptimeCheckConfig.HttpCheck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='use_ssl', full_name='google.monitoring.v3.UptimeCheckConfig.HttpCheck.use_ssl', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='google.monitoring.v3.UptimeCheckConfig.HttpCheck.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='google.monitoring.v3.UptimeCheckConfig.HttpCheck.port', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auth_info', full_name='google.monitoring.v3.UptimeCheckConfig.HttpCheck.auth_info', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mask_headers', full_name='google.monitoring.v3.UptimeCheckConfig.HttpCheck.mask_headers', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='headers', full_name='google.monitoring.v3.UptimeCheckConfig.HttpCheck.headers', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPTIMECHECKCONFIG_HTTPCHECK_BASICAUTHENTICATION, _UPTIMECHECKCONFIG_HTTPCHECK_HEADERSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=904,
  serialized_end=1260,
)

_UPTIMECHECKCONFIG_TCPCHECK = _descriptor.Descriptor(
  name='TcpCheck',
  full_name='google.monitoring.v3.UptimeCheckConfig.TcpCheck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='port', full_name='google.monitoring.v3.UptimeCheckConfig.TcpCheck.port', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=1262,
  serialized_end=1286,
)

_UPTIMECHECKCONFIG_CONTENTMATCHER = _descriptor.Descriptor(
  name='ContentMatcher',
  full_name='google.monitoring.v3.UptimeCheckConfig.ContentMatcher',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='google.monitoring.v3.UptimeCheckConfig.ContentMatcher.content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=1288,
  serialized_end=1321,
)

_UPTIMECHECKCONFIG_INTERNALCHECKER = _descriptor.Descriptor(
  name='InternalChecker',
  full_name='google.monitoring.v3.UptimeCheckConfig.InternalChecker',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='google.monitoring.v3.UptimeCheckConfig.InternalChecker.project_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='network', full_name='google.monitoring.v3.UptimeCheckConfig.InternalChecker.network', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gcp_zone', full_name='google.monitoring.v3.UptimeCheckConfig.InternalChecker.gcp_zone', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checker_id', full_name='google.monitoring.v3.UptimeCheckConfig.InternalChecker.checker_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.monitoring.v3.UptimeCheckConfig.InternalChecker.display_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=1323,
  serialized_end=1437,
)

_UPTIMECHECKCONFIG = _descriptor.Descriptor(
  name='UptimeCheckConfig',
  full_name='google.monitoring.v3.UptimeCheckConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='google.monitoring.v3.UptimeCheckConfig.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_name', full_name='google.monitoring.v3.UptimeCheckConfig.display_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='monitored_resource', full_name='google.monitoring.v3.UptimeCheckConfig.monitored_resource', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource_group', full_name='google.monitoring.v3.UptimeCheckConfig.resource_group', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='http_check', full_name='google.monitoring.v3.UptimeCheckConfig.http_check', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tcp_check', full_name='google.monitoring.v3.UptimeCheckConfig.tcp_check', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='period', full_name='google.monitoring.v3.UptimeCheckConfig.period', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='google.monitoring.v3.UptimeCheckConfig.timeout', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content_matchers', full_name='google.monitoring.v3.UptimeCheckConfig.content_matchers', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='selected_regions', full_name='google.monitoring.v3.UptimeCheckConfig.selected_regions', index=9,
      number=10, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='internal_checkers', full_name='google.monitoring.v3.UptimeCheckConfig.internal_checkers', index=10,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_UPTIMECHECKCONFIG_RESOURCEGROUP, _UPTIMECHECKCONFIG_HTTPCHECK, _UPTIMECHECKCONFIG_TCPCHECK, _UPTIMECHECKCONFIG_CONTENTMATCHER, _UPTIMECHECKCONFIG_INTERNALCHECKER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='resource', full_name='google.monitoring.v3.UptimeCheckConfig.resource',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='check_request_type', full_name='google.monitoring.v3.UptimeCheckConfig.check_request_type',
      index=1, containing_type=None, fields=[]),
  ],
  serialized_start=141,
  serialized_end=1471,
)


_UPTIMECHECKIP = _descriptor.Descriptor(
  name='UptimeCheckIp',
  full_name='google.monitoring.v3.UptimeCheckIp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='region', full_name='google.monitoring.v3.UptimeCheckIp.region', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='google.monitoring.v3.UptimeCheckIp.location', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ip_address', full_name='google.monitoring.v3.UptimeCheckIp.ip_address', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=1473,
  serialized_end=1583,
)

_UPTIMECHECKCONFIG_RESOURCEGROUP.fields_by_name['resource_type'].enum_type = _GROUPRESOURCETYPE
_UPTIMECHECKCONFIG_RESOURCEGROUP.containing_type = _UPTIMECHECKCONFIG
_UPTIMECHECKCONFIG_HTTPCHECK_BASICAUTHENTICATION.containing_type = _UPTIMECHECKCONFIG_HTTPCHECK
_UPTIMECHECKCONFIG_HTTPCHECK_HEADERSENTRY.containing_type = _UPTIMECHECKCONFIG_HTTPCHECK
_UPTIMECHECKCONFIG_HTTPCHECK.fields_by_name['auth_info'].message_type = _UPTIMECHECKCONFIG_HTTPCHECK_BASICAUTHENTICATION
_UPTIMECHECKCONFIG_HTTPCHECK.fields_by_name['headers'].message_type = _UPTIMECHECKCONFIG_HTTPCHECK_HEADERSENTRY
_UPTIMECHECKCONFIG_HTTPCHECK.containing_type = _UPTIMECHECKCONFIG
_UPTIMECHECKCONFIG_TCPCHECK.containing_type = _UPTIMECHECKCONFIG
_UPTIMECHECKCONFIG_CONTENTMATCHER.containing_type = _UPTIMECHECKCONFIG
_UPTIMECHECKCONFIG_INTERNALCHECKER.containing_type = _UPTIMECHECKCONFIG
_UPTIMECHECKCONFIG.fields_by_name['monitored_resource'].message_type = google_dot_api_dot_monitored__resource__pb2._MONITOREDRESOURCE
_UPTIMECHECKCONFIG.fields_by_name['resource_group'].message_type = _UPTIMECHECKCONFIG_RESOURCEGROUP
_UPTIMECHECKCONFIG.fields_by_name['http_check'].message_type = _UPTIMECHECKCONFIG_HTTPCHECK
_UPTIMECHECKCONFIG.fields_by_name['tcp_check'].message_type = _UPTIMECHECKCONFIG_TCPCHECK
_UPTIMECHECKCONFIG.fields_by_name['period'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_UPTIMECHECKCONFIG.fields_by_name['timeout'].message_type = google_dot_protobuf_dot_duration__pb2._DURATION
_UPTIMECHECKCONFIG.fields_by_name['content_matchers'].message_type = _UPTIMECHECKCONFIG_CONTENTMATCHER
_UPTIMECHECKCONFIG.fields_by_name['selected_regions'].enum_type = _UPTIMECHECKREGION
_UPTIMECHECKCONFIG.fields_by_name['internal_checkers'].message_type = _UPTIMECHECKCONFIG_INTERNALCHECKER
_UPTIMECHECKCONFIG.oneofs_by_name['resource'].fields.append(
  _UPTIMECHECKCONFIG.fields_by_name['monitored_resource'])
_UPTIMECHECKCONFIG.fields_by_name['monitored_resource'].containing_oneof = _UPTIMECHECKCONFIG.oneofs_by_name['resource']
_UPTIMECHECKCONFIG.oneofs_by_name['resource'].fields.append(
  _UPTIMECHECKCONFIG.fields_by_name['resource_group'])
_UPTIMECHECKCONFIG.fields_by_name['resource_group'].containing_oneof = _UPTIMECHECKCONFIG.oneofs_by_name['resource']
_UPTIMECHECKCONFIG.oneofs_by_name['check_request_type'].fields.append(
  _UPTIMECHECKCONFIG.fields_by_name['http_check'])
_UPTIMECHECKCONFIG.fields_by_name['http_check'].containing_oneof = _UPTIMECHECKCONFIG.oneofs_by_name['check_request_type']
_UPTIMECHECKCONFIG.oneofs_by_name['check_request_type'].fields.append(
  _UPTIMECHECKCONFIG.fields_by_name['tcp_check'])
_UPTIMECHECKCONFIG.fields_by_name['tcp_check'].containing_oneof = _UPTIMECHECKCONFIG.oneofs_by_name['check_request_type']
_UPTIMECHECKIP.fields_by_name['region'].enum_type = _UPTIMECHECKREGION
DESCRIPTOR.message_types_by_name['UptimeCheckConfig'] = _UPTIMECHECKCONFIG
DESCRIPTOR.message_types_by_name['UptimeCheckIp'] = _UPTIMECHECKIP
DESCRIPTOR.enum_types_by_name['UptimeCheckRegion'] = _UPTIMECHECKREGION
DESCRIPTOR.enum_types_by_name['GroupResourceType'] = _GROUPRESOURCETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UptimeCheckConfig = _reflection.GeneratedProtocolMessageType('UptimeCheckConfig', (_message.Message,), dict(

  ResourceGroup = _reflection.GeneratedProtocolMessageType('ResourceGroup', (_message.Message,), dict(
    DESCRIPTOR = _UPTIMECHECKCONFIG_RESOURCEGROUP,
    __module__ = 'google.cloud.monitoring_v3.proto.uptime_pb2'
    ,
    __doc__ = """The resource submessage for group checks. It can be used instead of a
    monitored resource, when multiple resources are being monitored.
    
    
    Attributes:
        group_id:
            The group of resources being monitored. Should be only the
            group\_id, not projects//groups/.
        resource_type:
            The resource type of the group members.
    """,
    # @@protoc_insertion_point(class_scope:google.monitoring.v3.UptimeCheckConfig.ResourceGroup)
    ))
  ,

  HttpCheck = _reflection.GeneratedProtocolMessageType('HttpCheck', (_message.Message,), dict(

    BasicAuthentication = _reflection.GeneratedProtocolMessageType('BasicAuthentication', (_message.Message,), dict(
      DESCRIPTOR = _UPTIMECHECKCONFIG_HTTPCHECK_BASICAUTHENTICATION,
      __module__ = 'google.cloud.monitoring_v3.proto.uptime_pb2'
      ,
      __doc__ = """A type of authentication to perform against the specified resource or
      URL that uses username and password. Currently, only Basic
      authentication is supported in Uptime Monitoring.
      
      
      Attributes:
          username:
              The username to authenticate.
          password:
              The password to authenticate.
      """,
      # @@protoc_insertion_point(class_scope:google.monitoring.v3.UptimeCheckConfig.HttpCheck.BasicAuthentication)
      ))
    ,

    HeadersEntry = _reflection.GeneratedProtocolMessageType('HeadersEntry', (_message.Message,), dict(
      DESCRIPTOR = _UPTIMECHECKCONFIG_HTTPCHECK_HEADERSENTRY,
      __module__ = 'google.cloud.monitoring_v3.proto.uptime_pb2'
      # @@protoc_insertion_point(class_scope:google.monitoring.v3.UptimeCheckConfig.HttpCheck.HeadersEntry)
      ))
    ,
    DESCRIPTOR = _UPTIMECHECKCONFIG_HTTPCHECK,
    __module__ = 'google.cloud.monitoring_v3.proto.uptime_pb2'
    ,
    __doc__ = """Information involved in an HTTP/HTTPS uptime check request.
    
    
    Attributes:
        use_ssl:
            If true, use HTTPS instead of HTTP to run the check.
        path:
            The path to the page to run the check against. Will be
            combined with the host (specified within the
            MonitoredResource) and port to construct the full URL.
            Optional (defaults to "/").
        port:
            The port to the page to run the check against. Will be
            combined with host (specified within the MonitoredResource)
            and path to construct the full URL. Optional (defaults to 80
            without SSL, or 443 with SSL).
        auth_info:
            The authentication information. Optional when creating an HTTP
            check; defaults to empty.
        mask_headers:
            Boolean specifiying whether to encrypt the header information.
            Encryption should be specified for any headers related to
            authentication that you do not wish to be seen when retrieving
            the configuration. The server will be responsible for
            encrypting the headers. On Get/List calls, if mask\_headers is
            set to True then the headers will be obscured with
            \*\*\*\*\*\*.
        headers:
            The list of headers to send as part of the uptime check
            request. If two headers have the same key and different
            values, they should be entered as a single header, with the
            value being a comma-separated list of all the desired values
            as described at
            https://www.w3.org/Protocols/rfc2616/rfc2616.txt (page 31).
            Entering two separate headers with the same key in a Create
            call will cause the first to be overwritten by the second.
    """,
    # @@protoc_insertion_point(class_scope:google.monitoring.v3.UptimeCheckConfig.HttpCheck)
    ))
  ,

  TcpCheck = _reflection.GeneratedProtocolMessageType('TcpCheck', (_message.Message,), dict(
    DESCRIPTOR = _UPTIMECHECKCONFIG_TCPCHECK,
    __module__ = 'google.cloud.monitoring_v3.proto.uptime_pb2'
    ,
    __doc__ = """Information required for a TCP uptime check request.
    
    
    Attributes:
        port:
            The port to the page to run the check against. Will be
            combined with host (specified within the MonitoredResource) to
            construct the full URL. Required.
    """,
    # @@protoc_insertion_point(class_scope:google.monitoring.v3.UptimeCheckConfig.TcpCheck)
    ))
  ,

  ContentMatcher = _reflection.GeneratedProtocolMessageType('ContentMatcher', (_message.Message,), dict(
    DESCRIPTOR = _UPTIMECHECKCONFIG_CONTENTMATCHER,
    __module__ = 'google.cloud.monitoring_v3.proto.uptime_pb2'
    ,
    __doc__ = """Used to perform string matching. Currently, this matches on the exact
    content. In the future, it can be expanded to allow for regular
    expressions and more complex matching.
    
    
    Attributes:
        content:
            String content to match
    """,
    # @@protoc_insertion_point(class_scope:google.monitoring.v3.UptimeCheckConfig.ContentMatcher)
    ))
  ,

  InternalChecker = _reflection.GeneratedProtocolMessageType('InternalChecker', (_message.Message,), dict(
    DESCRIPTOR = _UPTIMECHECKCONFIG_INTERNALCHECKER,
    __module__ = 'google.cloud.monitoring_v3.proto.uptime_pb2'
    ,
    __doc__ = """Nimbus InternalCheckers.
    
    
    Attributes:
        project_id:
            The GCP project ID. Not necessarily the same as the
            project\_id for the config.
        network:
            The internal network to perform this uptime check on.
        gcp_zone:
            The GCP zone the uptime check should egress from. Only
            respected for internal uptime checks, where internal\_network
            is specified.
        checker_id:
            The checker ID.
        display_name:
            The checker's human-readable name.
    """,
    # @@protoc_insertion_point(class_scope:google.monitoring.v3.UptimeCheckConfig.InternalChecker)
    ))
  ,
  DESCRIPTOR = _UPTIMECHECKCONFIG,
  __module__ = 'google.cloud.monitoring_v3.proto.uptime_pb2'
  ,
  __doc__ = """This message configures which resources and services to monitor for
  availability.
  
  
  Attributes:
      name:
          A unique resource name for this UptimeCheckConfig. The format
          is:  ``projects/[PROJECT_ID]/uptimeCheckConfigs/[UPTIME_CHECK_
          ID]``.  This field should be omitted when creating the uptime
          check configuration; on create, the resource name is assigned
          by the server and included in the response.
      display_name:
          A human-friendly name for the uptime check configuration. The
          display name should be unique within a Stackdriver Account in
          order to make it easier to identify; however, uniqueness is
          not enforced. Required.
      resource:
          The resource the check is checking. Required.
      monitored_resource:
          The monitored resource associated with the configuration.
      resource_group:
          The group resource associated with the configuration.
      check_request_type:
          The type of uptime check request.
      http_check:
          Contains information needed to make an HTTP or HTTPS check.
      tcp_check:
          Contains information needed to make a TCP check.
      period:
          How often the uptime check is performed. Currently, only 1, 5,
          10, and 15 minutes are supported. Required.
      timeout:
          The maximum amount of time to wait for the request to complete
          (must be between 1 and 60 seconds). Required.
      content_matchers:
          The expected content on the page the check is run against.
          Currently, only the first entry in the list is supported, and
          other entries will be ignored. The server will look for an
          exact match of the string in the page response's content. This
          field is optional and should only be specified if a content
          match is required.
      selected_regions:
          The list of regions from which the check will be run. If this
          field is specified, enough regions to include a minimum of 3
          locations must be provided, or an error message is returned.
          Not specifying this field will result in uptime checks running
          from all regions.
      internal_checkers:
          The internal checkers that this check will egress from.
  """,
  # @@protoc_insertion_point(class_scope:google.monitoring.v3.UptimeCheckConfig)
  ))
_sym_db.RegisterMessage(UptimeCheckConfig)
_sym_db.RegisterMessage(UptimeCheckConfig.ResourceGroup)
_sym_db.RegisterMessage(UptimeCheckConfig.HttpCheck)
_sym_db.RegisterMessage(UptimeCheckConfig.HttpCheck.BasicAuthentication)
_sym_db.RegisterMessage(UptimeCheckConfig.HttpCheck.HeadersEntry)
_sym_db.RegisterMessage(UptimeCheckConfig.TcpCheck)
_sym_db.RegisterMessage(UptimeCheckConfig.ContentMatcher)
_sym_db.RegisterMessage(UptimeCheckConfig.InternalChecker)

UptimeCheckIp = _reflection.GeneratedProtocolMessageType('UptimeCheckIp', (_message.Message,), dict(
  DESCRIPTOR = _UPTIMECHECKIP,
  __module__ = 'google.cloud.monitoring_v3.proto.uptime_pb2'
  ,
  __doc__ = """Contains the region, location, and list of IP addresses where checkers
  in the location run from.
  
  
  Attributes:
      region:
          A broad region category in which the IP address is located.
      location:
          A more specific location within the region that typically
          encodes a particular city/town/metro (and its containing
          state/province or country) within the broader umbrella region
          category.
      ip_address:
          The IP address from which the uptime check originates. This is
          a full IP address (not an IP address range). Most IP
          addresses, as of this publication, are in IPv4 format;
          however, one should not rely on the IP addresses being in IPv4
          format indefinitely and should support interpreting this field
          in either IPv4 or IPv6 format.
  """,
  # @@protoc_insertion_point(class_scope:google.monitoring.v3.UptimeCheckIp)
  ))
_sym_db.RegisterMessage(UptimeCheckIp)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\030com.google.monitoring.v3B\013UptimeProtoP\001Z>google.golang.org/genproto/googleapis/monitoring/v3;monitoring\252\002\032Google.Cloud.Monitoring.V3\312\002\032Google\\Cloud\\Monitoring\\V3'))
_UPTIMECHECKCONFIG_HTTPCHECK_HEADERSENTRY.has_options = True
_UPTIMECHECKCONFIG_HTTPCHECK_HEADERSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
