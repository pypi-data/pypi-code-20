
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class tacacs_server_options(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-aaa - based on the path /tacacs-server/host/tacacs-server-options. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__port','__protocol','__key','__encryption_level','__retries','__timeout',)

  _yang_name = 'tacacs-server-options'
  _rest_name = ''

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    path_helper_ = kwargs.pop("path_helper", None)
    if path_helper_ is False:
      self._path_helper = False
    elif path_helper_ is not None and isinstance(path_helper_, xpathhelper.YANGPathHelper):
      self._path_helper = path_helper_
    elif hasattr(self, "_parent"):
      path_helper_ = getattr(self._parent, "_path_helper", False)
      self._path_helper = path_helper_
    else:
      self._path_helper = False

    extmethods = kwargs.pop("extmethods", None)
    if extmethods is False:
      self._extmethods = False
    elif extmethods is not None and isinstance(extmethods, dict):
      self._extmethods = extmethods
    elif hasattr(self, "_parent"):
      extmethods = getattr(self._parent, "_extmethods", None)
      self._extmethods = extmethods
    else:
      self._extmethods = False
    self.__encryption_level = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'0': {'value': 0}, u'7': {'value': 7}},), is_leaf=True, yang_name="encryption-level", rest_name="encryption-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Level of encryption of the key (default=7)'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='enumeration', is_config=True)
    self.__retries = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 100']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(5), is_leaf=True, yang_name="retries", rest_name="retries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number of retries for this server connection\n (default=5)'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='uint8', is_config=True)
    self.__protocol = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'pap': {'value': 1}, u'chap': {'value': 0}},), default=unicode("chap"), is_leaf=True, yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Authentication protocol to be used\n (default=CHAP)'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='tac-auth-protocols', is_config=True)
    self.__key = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. max']}), is_leaf=True, yang_name="key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u"Secret shared with this server\n (default='sharedsecret')"}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)
    self.__timeout = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1 .. 60']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(5), is_leaf=True, yang_name="timeout", rest_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Wait time for this server to respond\n (default=5 sec)'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='uint8', is_config=True)
    self.__port = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1 .. 65535']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(49), is_leaf=True, yang_name="port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'TCP Port for Authentication (default=49)'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='tac-auth-port', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'tacacs-server', u'host', u'tacacs-server-options']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'tacacs-server', u'host']

  def _get_port(self):
    """
    Getter method for port, mapped from YANG variable /tacacs_server/host/tacacs_server_options/port (tac-auth-port)
    """
    return self.__port
      
  def _set_port(self, v, load=False):
    """
    Setter method for port, mapped from YANG variable /tacacs_server/host/tacacs_server_options/port (tac-auth-port)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1 .. 65535']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(49), is_leaf=True, yang_name="port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'TCP Port for Authentication (default=49)'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='tac-auth-port', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port must be of a type compatible with tac-auth-port""",
          'defined-type': "brocade-aaa:tac-auth-port",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1 .. 65535']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(49), is_leaf=True, yang_name="port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'TCP Port for Authentication (default=49)'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='tac-auth-port', is_config=True)""",
        })

    self.__port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port(self):
    self.__port = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'1 .. 65535']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16)(49), is_leaf=True, yang_name="port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'TCP Port for Authentication (default=49)'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='tac-auth-port', is_config=True)


  def _get_protocol(self):
    """
    Getter method for protocol, mapped from YANG variable /tacacs_server/host/tacacs_server_options/protocol (tac-auth-protocols)
    """
    return self.__protocol
      
  def _set_protocol(self, v, load=False):
    """
    Setter method for protocol, mapped from YANG variable /tacacs_server/host/tacacs_server_options/protocol (tac-auth-protocols)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protocol is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protocol() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'pap': {'value': 1}, u'chap': {'value': 0}},), default=unicode("chap"), is_leaf=True, yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Authentication protocol to be used\n (default=CHAP)'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='tac-auth-protocols', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protocol must be of a type compatible with tac-auth-protocols""",
          'defined-type': "brocade-aaa:tac-auth-protocols",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'pap': {'value': 1}, u'chap': {'value': 0}},), default=unicode("chap"), is_leaf=True, yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Authentication protocol to be used\n (default=CHAP)'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='tac-auth-protocols', is_config=True)""",
        })

    self.__protocol = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protocol(self):
    self.__protocol = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'pap': {'value': 1}, u'chap': {'value': 0}},), default=unicode("chap"), is_leaf=True, yang_name="protocol", rest_name="protocol", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Authentication protocol to be used\n (default=CHAP)'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='tac-auth-protocols', is_config=True)


  def _get_key(self):
    """
    Getter method for key, mapped from YANG variable /tacacs_server/host/tacacs_server_options/key (string)
    """
    return self.__key
      
  def _set_key(self, v, load=False):
    """
    Setter method for key, mapped from YANG variable /tacacs_server/host/tacacs_server_options/key (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_key is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_key() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. max']}), is_leaf=True, yang_name="key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u"Secret shared with this server\n (default='sharedsecret')"}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """key must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. max']}), is_leaf=True, yang_name="key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u"Secret shared with this server\n (default='sharedsecret')"}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)""",
        })

    self.__key = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_key(self):
    self.__key = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. max']}), is_leaf=True, yang_name="key", rest_name="key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u"Secret shared with this server\n (default='sharedsecret')"}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='string', is_config=True)


  def _get_encryption_level(self):
    """
    Getter method for encryption_level, mapped from YANG variable /tacacs_server/host/tacacs_server_options/encryption_level (enumeration)
    """
    return self.__encryption_level
      
  def _set_encryption_level(self, v, load=False):
    """
    Setter method for encryption_level, mapped from YANG variable /tacacs_server/host/tacacs_server_options/encryption_level (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_encryption_level is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_encryption_level() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'0': {'value': 0}, u'7': {'value': 7}},), is_leaf=True, yang_name="encryption-level", rest_name="encryption-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Level of encryption of the key (default=7)'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """encryption_level must be of a type compatible with enumeration""",
          'defined-type': "brocade-aaa:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'0': {'value': 0}, u'7': {'value': 7}},), is_leaf=True, yang_name="encryption-level", rest_name="encryption-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Level of encryption of the key (default=7)'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='enumeration', is_config=True)""",
        })

    self.__encryption_level = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_encryption_level(self):
    self.__encryption_level = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'0': {'value': 0}, u'7': {'value': 7}},), is_leaf=True, yang_name="encryption-level", rest_name="encryption-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Level of encryption of the key (default=7)'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='enumeration', is_config=True)


  def _get_retries(self):
    """
    Getter method for retries, mapped from YANG variable /tacacs_server/host/tacacs_server_options/retries (uint8)
    """
    return self.__retries
      
  def _set_retries(self, v, load=False):
    """
    Setter method for retries, mapped from YANG variable /tacacs_server/host/tacacs_server_options/retries (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_retries is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_retries() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 100']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(5), is_leaf=True, yang_name="retries", rest_name="retries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number of retries for this server connection\n (default=5)'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """retries must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 100']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(5), is_leaf=True, yang_name="retries", rest_name="retries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number of retries for this server connection\n (default=5)'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='uint8', is_config=True)""",
        })

    self.__retries = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_retries(self):
    self.__retries = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'0 .. 100']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(5), is_leaf=True, yang_name="retries", rest_name="retries", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number of retries for this server connection\n (default=5)'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='uint8', is_config=True)


  def _get_timeout(self):
    """
    Getter method for timeout, mapped from YANG variable /tacacs_server/host/tacacs_server_options/timeout (uint8)
    """
    return self.__timeout
      
  def _set_timeout(self, v, load=False):
    """
    Setter method for timeout, mapped from YANG variable /tacacs_server/host/tacacs_server_options/timeout (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_timeout is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_timeout() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1 .. 60']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(5), is_leaf=True, yang_name="timeout", rest_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Wait time for this server to respond\n (default=5 sec)'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='uint8', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """timeout must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1 .. 60']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(5), is_leaf=True, yang_name="timeout", rest_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Wait time for this server to respond\n (default=5 sec)'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='uint8', is_config=True)""",
        })

    self.__timeout = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_timeout(self):
    self.__timeout = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), restriction_dict={'range': [u'1 .. 60']}), default=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8)(5), is_leaf=True, yang_name="timeout", rest_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Wait time for this server to respond\n (default=5 sec)'}}, namespace='urn:brocade.com:mgmt:brocade-aaa', defining_module='brocade-aaa', yang_type='uint8', is_config=True)

  port = __builtin__.property(_get_port, _set_port)
  protocol = __builtin__.property(_get_protocol, _set_protocol)
  key = __builtin__.property(_get_key, _set_key)
  encryption_level = __builtin__.property(_get_encryption_level, _set_encryption_level)
  retries = __builtin__.property(_get_retries, _set_retries)
  timeout = __builtin__.property(_get_timeout, _set_timeout)


  _pyangbind_elements = {'port': port, 'protocol': protocol, 'key': key, 'encryption_level': encryption_level, 'retries': retries, 'timeout': timeout, }


