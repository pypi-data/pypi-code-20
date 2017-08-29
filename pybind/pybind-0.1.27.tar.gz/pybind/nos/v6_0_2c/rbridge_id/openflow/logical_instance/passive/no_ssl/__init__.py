
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class no_ssl(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/openflow/logical-instance/passive/no-ssl. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: No ssl connection
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__passive_controller_flag','__passive_controller_ip_address','__passive_controller_port',)

  _yang_name = 'no-ssl'
  _rest_name = 'no-ssl'

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
    self.__passive_controller_flag = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="passive-controller-flag", rest_name="passive-controller-flag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='empty', is_config=True)
    self.__passive_controller_ip_address = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="passive-controller-ip-address", rest_name="ip-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP address of OpenFlow controller', u'alt-name': u'ip-address'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='inet:ip-address', is_config=True)
    self.__passive_controller_port = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="passive-controller-port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Passive controller port', u'alt-name': u'port'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='uint32', is_config=True)

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
      return [u'rbridge-id', u'openflow', u'logical-instance', u'passive', u'no-ssl']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'openflow', u'logical-instance', u'passive', u'no-ssl']

  def _get_passive_controller_flag(self):
    """
    Getter method for passive_controller_flag, mapped from YANG variable /rbridge_id/openflow/logical_instance/passive/no_ssl/passive_controller_flag (empty)
    """
    return self.__passive_controller_flag
      
  def _set_passive_controller_flag(self, v, load=False):
    """
    Setter method for passive_controller_flag, mapped from YANG variable /rbridge_id/openflow/logical_instance/passive/no_ssl/passive_controller_flag (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_passive_controller_flag is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_passive_controller_flag() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="passive-controller-flag", rest_name="passive-controller-flag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """passive_controller_flag must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="passive-controller-flag", rest_name="passive-controller-flag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='empty', is_config=True)""",
        })

    self.__passive_controller_flag = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_passive_controller_flag(self):
    self.__passive_controller_flag = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="passive-controller-flag", rest_name="passive-controller-flag", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='empty', is_config=True)


  def _get_passive_controller_ip_address(self):
    """
    Getter method for passive_controller_ip_address, mapped from YANG variable /rbridge_id/openflow/logical_instance/passive/no_ssl/passive_controller_ip_address (inet:ip-address)

    YANG Description: IP address of the OpenFlow controller. Only IPv4 address
is supported.
    """
    return self.__passive_controller_ip_address
      
  def _set_passive_controller_ip_address(self, v, load=False):
    """
    Setter method for passive_controller_ip_address, mapped from YANG variable /rbridge_id/openflow/logical_instance/passive/no_ssl/passive_controller_ip_address (inet:ip-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_passive_controller_ip_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_passive_controller_ip_address() directly.

    YANG Description: IP address of the OpenFlow controller. Only IPv4 address
is supported.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="passive-controller-ip-address", rest_name="ip-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP address of OpenFlow controller', u'alt-name': u'ip-address'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='inet:ip-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """passive_controller_ip_address must be of a type compatible with inet:ip-address""",
          'defined-type': "inet:ip-address",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="passive-controller-ip-address", rest_name="ip-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP address of OpenFlow controller', u'alt-name': u'ip-address'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='inet:ip-address', is_config=True)""",
        })

    self.__passive_controller_ip_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_passive_controller_ip_address(self):
    self.__passive_controller_ip_address = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="passive-controller-ip-address", rest_name="ip-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IP address of OpenFlow controller', u'alt-name': u'ip-address'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='inet:ip-address', is_config=True)


  def _get_passive_controller_port(self):
    """
    Getter method for passive_controller_port, mapped from YANG variable /rbridge_id/openflow/logical_instance/passive/no_ssl/passive_controller_port (uint32)
    """
    return self.__passive_controller_port
      
  def _set_passive_controller_port(self, v, load=False):
    """
    Setter method for passive_controller_port, mapped from YANG variable /rbridge_id/openflow/logical_instance/passive/no_ssl/passive_controller_port (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_passive_controller_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_passive_controller_port() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="passive-controller-port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Passive controller port', u'alt-name': u'port'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """passive_controller_port must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="passive-controller-port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Passive controller port', u'alt-name': u'port'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='uint32', is_config=True)""",
        })

    self.__passive_controller_port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_passive_controller_port(self):
    self.__passive_controller_port = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="passive-controller-port", rest_name="port", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Passive controller port', u'alt-name': u'port'}}, namespace='urn:brocade.com:mgmt:brocade-openflow', defining_module='brocade-openflow', yang_type='uint32', is_config=True)

  passive_controller_flag = __builtin__.property(_get_passive_controller_flag, _set_passive_controller_flag)
  passive_controller_ip_address = __builtin__.property(_get_passive_controller_ip_address, _set_passive_controller_ip_address)
  passive_controller_port = __builtin__.property(_get_passive_controller_port, _set_passive_controller_port)


  _pyangbind_elements = {'passive_controller_flag': passive_controller_flag, 'passive_controller_ip_address': passive_controller_ip_address, 'passive_controller_port': passive_controller_port, }


