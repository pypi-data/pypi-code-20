
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class auth_key_table(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/interface/ve/ip/interface-vlan-ospf-conf/ospf1/authentication-key/auth-key-table. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__encrypttype','__auth_key',)

  _yang_name = 'auth-key-table'
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
    self.__encrypttype = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0', u'2', u'255']}), is_leaf=True, yang_name="encrypttype", rest_name="encrypttype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='key-type', is_config=True)
    self.__auth_key = YANGDynClass(base=unicode, is_leaf=True, yang_name="auth-key", rest_name="auth-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'The OSPF password (key)'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='ospf-auth-psswd-string', is_config=True)

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
      return [u'routing-system', u'interface', u've', u'ip', u'interface-vlan-ospf-conf', u'ospf1', u'authentication-key', u'auth-key-table']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ve', u'ip', u'ospf', u'authentication-key']

  def _get_encrypttype(self):
    """
    Getter method for encrypttype, mapped from YANG variable /routing_system/interface/ve/ip/interface_vlan_ospf_conf/ospf1/authentication_key/auth_key_table/encrypttype (key-type)
    """
    return self.__encrypttype
      
  def _set_encrypttype(self, v, load=False):
    """
    Setter method for encrypttype, mapped from YANG variable /routing_system/interface/ve/ip/interface_vlan_ospf_conf/ospf1/authentication_key/auth_key_table/encrypttype (key-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_encrypttype is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_encrypttype() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0', u'2', u'255']}), is_leaf=True, yang_name="encrypttype", rest_name="encrypttype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='key-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """encrypttype must be of a type compatible with key-type""",
          'defined-type': "brocade-ospf:key-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0', u'2', u'255']}), is_leaf=True, yang_name="encrypttype", rest_name="encrypttype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='key-type', is_config=True)""",
        })

    self.__encrypttype = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_encrypttype(self):
    self.__encrypttype = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0', u'2', u'255']}), is_leaf=True, yang_name="encrypttype", rest_name="encrypttype", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='key-type', is_config=True)


  def _get_auth_key(self):
    """
    Getter method for auth_key, mapped from YANG variable /routing_system/interface/ve/ip/interface_vlan_ospf_conf/ospf1/authentication_key/auth_key_table/auth_key (ospf-auth-psswd-string)
    """
    return self.__auth_key
      
  def _set_auth_key(self, v, load=False):
    """
    Setter method for auth_key, mapped from YANG variable /routing_system/interface/ve/ip/interface_vlan_ospf_conf/ospf1/authentication_key/auth_key_table/auth_key (ospf-auth-psswd-string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auth_key is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auth_key() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="auth-key", rest_name="auth-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'The OSPF password (key)'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='ospf-auth-psswd-string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auth_key must be of a type compatible with ospf-auth-psswd-string""",
          'defined-type': "brocade-ospf:ospf-auth-psswd-string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="auth-key", rest_name="auth-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'The OSPF password (key)'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='ospf-auth-psswd-string', is_config=True)""",
        })

    self.__auth_key = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auth_key(self):
    self.__auth_key = YANGDynClass(base=unicode, is_leaf=True, yang_name="auth-key", rest_name="auth-key", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'The OSPF password (key)'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='ospf-auth-psswd-string', is_config=True)

  encrypttype = __builtin__.property(_get_encrypttype, _set_encrypttype)
  auth_key = __builtin__.property(_get_auth_key, _set_auth_key)


  _pyangbind_elements = {'encrypttype': encrypttype, 'auth_key': auth_key, }


