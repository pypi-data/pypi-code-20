
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import nsap
class isis_system_info(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-isis-operational - based on the path /isis-state/router-isis-config/isis-system-info. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: information specific to a single instance of IS-IS protocol running on a router
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__protocol_enabled','__operation_mode','__system_id','__nsap',)

  _yang_name = 'isis-system-info'
  _rest_name = 'isis-system-info'

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
    self.__nsap = YANGDynClass(base=YANGListType("net_addr",nsap.nsap, yang_name="nsap", rest_name="nsap", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='net-addr', extensions={u'tailf-common': {u'callpoint': u'isis-net-address', u'cli-suppress-show-path': None}}), is_container='list', yang_name="nsap", rest_name="nsap", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'isis-net-address', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)
    self.__system_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="system-id", rest_name="system-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)
    self.__operation_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'isis-level1-2': {'value': 0}, u'isis-level1': {'value': 1}, u'isis-level2': {'value': 2}},), is_leaf=True, yang_name="operation-mode", rest_name="operation-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-level', is_config=False)
    self.__protocol_enabled = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="protocol-enabled", rest_name="protocol-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)

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
      return [u'isis-state', u'router-isis-config', u'isis-system-info']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'isis-state', u'router-isis-config', u'isis-system-info']

  def _get_protocol_enabled(self):
    """
    Getter method for protocol_enabled, mapped from YANG variable /isis_state/router_isis_config/isis_system_info/protocol_enabled (isis-status)

    YANG Description: If IS-IS protocol enabled
    """
    return self.__protocol_enabled
      
  def _set_protocol_enabled(self, v, load=False):
    """
    Setter method for protocol_enabled, mapped from YANG variable /isis_state/router_isis_config/isis_system_info/protocol_enabled (isis-status)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protocol_enabled is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protocol_enabled() directly.

    YANG Description: If IS-IS protocol enabled
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="protocol-enabled", rest_name="protocol-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protocol_enabled must be of a type compatible with isis-status""",
          'defined-type': "brocade-isis-operational:isis-status",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="protocol-enabled", rest_name="protocol-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)""",
        })

    self.__protocol_enabled = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protocol_enabled(self):
    self.__protocol_enabled = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'is-enabled': {'value': 1}, u'is-disabled': {'value': 0}},), is_leaf=True, yang_name="protocol-enabled", rest_name="protocol-enabled", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-status', is_config=False)


  def _get_operation_mode(self):
    """
    Getter method for operation_mode, mapped from YANG variable /isis_state/router_isis_config/isis_system_info/operation_mode (isis-level)

    YANG Description: IS-IS working level - Area(L1) or Domain(L2) or both(L12)
    """
    return self.__operation_mode
      
  def _set_operation_mode(self, v, load=False):
    """
    Setter method for operation_mode, mapped from YANG variable /isis_state/router_isis_config/isis_system_info/operation_mode (isis-level)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_operation_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_operation_mode() directly.

    YANG Description: IS-IS working level - Area(L1) or Domain(L2) or both(L12)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'isis-level1-2': {'value': 0}, u'isis-level1': {'value': 1}, u'isis-level2': {'value': 2}},), is_leaf=True, yang_name="operation-mode", rest_name="operation-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-level', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """operation_mode must be of a type compatible with isis-level""",
          'defined-type': "brocade-isis-operational:isis-level",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'isis-level1-2': {'value': 0}, u'isis-level1': {'value': 1}, u'isis-level2': {'value': 2}},), is_leaf=True, yang_name="operation-mode", rest_name="operation-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-level', is_config=False)""",
        })

    self.__operation_mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_operation_mode(self):
    self.__operation_mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'isis-level1-2': {'value': 0}, u'isis-level1': {'value': 1}, u'isis-level2': {'value': 2}},), is_leaf=True, yang_name="operation-mode", rest_name="operation-mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='isis-level', is_config=False)


  def _get_system_id(self):
    """
    Getter method for system_id, mapped from YANG variable /isis_state/router_isis_config/isis_system_info/system_id (string)

    YANG Description: System ID of the Intermediate System
    """
    return self.__system_id
      
  def _set_system_id(self, v, load=False):
    """
    Setter method for system_id, mapped from YANG variable /isis_state/router_isis_config/isis_system_info/system_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_system_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_system_id() directly.

    YANG Description: System ID of the Intermediate System
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="system-id", rest_name="system-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """system_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="system-id", rest_name="system-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)""",
        })

    self.__system_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_system_id(self):
    self.__system_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="system-id", rest_name="system-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='string', is_config=False)


  def _get_nsap(self):
    """
    Getter method for nsap, mapped from YANG variable /isis_state/router_isis_config/isis_system_info/nsap (list)

    YANG Description: IS-IS NSAP address
    """
    return self.__nsap
      
  def _set_nsap(self, v, load=False):
    """
    Setter method for nsap, mapped from YANG variable /isis_state/router_isis_config/isis_system_info/nsap (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_nsap is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_nsap() directly.

    YANG Description: IS-IS NSAP address
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("net_addr",nsap.nsap, yang_name="nsap", rest_name="nsap", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='net-addr', extensions={u'tailf-common': {u'callpoint': u'isis-net-address', u'cli-suppress-show-path': None}}), is_container='list', yang_name="nsap", rest_name="nsap", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'isis-net-address', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """nsap must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("net_addr",nsap.nsap, yang_name="nsap", rest_name="nsap", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='net-addr', extensions={u'tailf-common': {u'callpoint': u'isis-net-address', u'cli-suppress-show-path': None}}), is_container='list', yang_name="nsap", rest_name="nsap", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'isis-net-address', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)""",
        })

    self.__nsap = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_nsap(self):
    self.__nsap = YANGDynClass(base=YANGListType("net_addr",nsap.nsap, yang_name="nsap", rest_name="nsap", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='net-addr', extensions={u'tailf-common': {u'callpoint': u'isis-net-address', u'cli-suppress-show-path': None}}), is_container='list', yang_name="nsap", rest_name="nsap", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'isis-net-address', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-isis-operational', defining_module='brocade-isis-operational', yang_type='list', is_config=False)

  protocol_enabled = __builtin__.property(_get_protocol_enabled)
  operation_mode = __builtin__.property(_get_operation_mode)
  system_id = __builtin__.property(_get_system_id)
  nsap = __builtin__.property(_get_nsap)


  _pyangbind_elements = {'protocol_enabled': protocol_enabled, 'operation_mode': operation_mode, 'system_id': system_id, 'nsap': nsap, }


