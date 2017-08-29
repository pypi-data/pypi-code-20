
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import interface
class vlan(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface-ext - based on the path /brocade_interface_ext_rpc/get-vlan-brief/output/vlan. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The list of vlans. Each row represents a vlan  and 
its operational characteristics in the managed 
device.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__vlan_id','__vlan_type','__vlan_name','__vlan_state','__interface',)

  _yang_name = 'vlan'
  _rest_name = 'vlan'

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
    self.__interface = YANGDynClass(base=YANGListType("interface_type interface_name",interface.interface, yang_name="interface", rest_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-type interface-name', extensions=None), is_container='list', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='list', is_config=True)
    self.__vlan_state = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'active': {'value': 3}, u'members-down': {'value': 4}, u'suspend': {'value': 2}, u'invalid': {'value': 1}},), is_leaf=True, yang_name="vlan-state", rest_name="vlan-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='enumeration', is_config=True)
    self.__vlan_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'static': {'value': 2}, u'fcoe': {'value': 1}},), is_leaf=True, yang_name="vlan-type", rest_name="vlan-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='enumeration', is_config=True)
    self.__vlan_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vlan-name", rest_name="vlan-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='interface:vlan-type', is_config=True)

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
      return [u'brocade_interface_ext_rpc', u'get-vlan-brief', u'output', u'vlan']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-vlan-brief', u'output', u'vlan']

  def _get_vlan_id(self):
    """
    Getter method for vlan_id, mapped from YANG variable /brocade_interface_ext_rpc/get_vlan_brief/output/vlan/vlan_id (interface:vlan-type)

    YANG Description: This indicates the Vlan identifier of this
vlan.
    """
    return self.__vlan_id
      
  def _set_vlan_id(self, v, load=False):
    """
    Setter method for vlan_id, mapped from YANG variable /brocade_interface_ext_rpc/get_vlan_brief/output/vlan/vlan_id (interface:vlan-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_id() directly.

    YANG Description: This indicates the Vlan identifier of this
vlan.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='interface:vlan-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_id must be of a type compatible with interface:vlan-type""",
          'defined-type': "interface:vlan-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='interface:vlan-type', is_config=True)""",
        })

    self.__vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_id(self):
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='interface:vlan-type', is_config=True)


  def _get_vlan_type(self):
    """
    Getter method for vlan_type, mapped from YANG variable /brocade_interface_ext_rpc/get_vlan_brief/output/vlan/vlan_type (enumeration)

    YANG Description: This indicates the type of the vlan. 
The 'fcoe' value indicates that the vlan 
corresponding to it is an FCOE vlan.
The 'static' value indicates that the vlan 
corresponding to it is a Static vlan.
    """
    return self.__vlan_type
      
  def _set_vlan_type(self, v, load=False):
    """
    Setter method for vlan_type, mapped from YANG variable /brocade_interface_ext_rpc/get_vlan_brief/output/vlan/vlan_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_type() directly.

    YANG Description: This indicates the type of the vlan. 
The 'fcoe' value indicates that the vlan 
corresponding to it is an FCOE vlan.
The 'static' value indicates that the vlan 
corresponding to it is a Static vlan.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'static': {'value': 2}, u'fcoe': {'value': 1}},), is_leaf=True, yang_name="vlan-type", rest_name="vlan-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-interface-ext:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'static': {'value': 2}, u'fcoe': {'value': 1}},), is_leaf=True, yang_name="vlan-type", rest_name="vlan-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='enumeration', is_config=True)""",
        })

    self.__vlan_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_type(self):
    self.__vlan_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'static': {'value': 2}, u'fcoe': {'value': 1}},), is_leaf=True, yang_name="vlan-type", rest_name="vlan-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='enumeration', is_config=True)


  def _get_vlan_name(self):
    """
    Getter method for vlan_name, mapped from YANG variable /brocade_interface_ext_rpc/get_vlan_brief/output/vlan/vlan_name (string)

    YANG Description: The indicates administrative name of this 
vlan.
    """
    return self.__vlan_name
      
  def _set_vlan_name(self, v, load=False):
    """
    Setter method for vlan_name, mapped from YANG variable /brocade_interface_ext_rpc/get_vlan_brief/output/vlan/vlan_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_name() directly.

    YANG Description: The indicates administrative name of this 
vlan.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vlan-name", rest_name="vlan-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vlan-name", rest_name="vlan-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)""",
        })

    self.__vlan_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_name(self):
    self.__vlan_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vlan-name", rest_name="vlan-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='string', is_config=True)


  def _get_vlan_state(self):
    """
    Getter method for vlan_state, mapped from YANG variable /brocade_interface_ext_rpc/get_vlan_brief/output/vlan/vlan_state (enumeration)

    YANG Description: This indicates the operational state of this 
vlan.
    """
    return self.__vlan_state
      
  def _set_vlan_state(self, v, load=False):
    """
    Setter method for vlan_state, mapped from YANG variable /brocade_interface_ext_rpc/get_vlan_brief/output/vlan/vlan_state (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_state is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_state() directly.

    YANG Description: This indicates the operational state of this 
vlan.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'active': {'value': 3}, u'members-down': {'value': 4}, u'suspend': {'value': 2}, u'invalid': {'value': 1}},), is_leaf=True, yang_name="vlan-state", rest_name="vlan-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_state must be of a type compatible with enumeration""",
          'defined-type': "brocade-interface-ext:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'active': {'value': 3}, u'members-down': {'value': 4}, u'suspend': {'value': 2}, u'invalid': {'value': 1}},), is_leaf=True, yang_name="vlan-state", rest_name="vlan-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='enumeration', is_config=True)""",
        })

    self.__vlan_state = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_state(self):
    self.__vlan_state = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'active': {'value': 3}, u'members-down': {'value': 4}, u'suspend': {'value': 2}, u'invalid': {'value': 1}},), is_leaf=True, yang_name="vlan-state", rest_name="vlan-state", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='enumeration', is_config=True)


  def _get_interface(self):
    """
    Getter method for interface, mapped from YANG variable /brocade_interface_ext_rpc/get_vlan_brief/output/vlan/interface (list)

    YANG Description: This is a list of interfaces which form the 
membership for this vlan. Each row represents 
an interface (physical/logical) with relevant
operational details.
    """
    return self.__interface
      
  def _set_interface(self, v, load=False):
    """
    Setter method for interface, mapped from YANG variable /brocade_interface_ext_rpc/get_vlan_brief/output/vlan/interface (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface() directly.

    YANG Description: This is a list of interfaces which form the 
membership for this vlan. Each row represents 
an interface (physical/logical) with relevant
operational details.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("interface_type interface_name",interface.interface, yang_name="interface", rest_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-type interface-name', extensions=None), is_container='list', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("interface_type interface_name",interface.interface, yang_name="interface", rest_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-type interface-name', extensions=None), is_container='list', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='list', is_config=True)""",
        })

    self.__interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface(self):
    self.__interface = YANGDynClass(base=YANGListType("interface_type interface_name",interface.interface, yang_name="interface", rest_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-type interface-name', extensions=None), is_container='list', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='list', is_config=True)

  vlan_id = __builtin__.property(_get_vlan_id, _set_vlan_id)
  vlan_type = __builtin__.property(_get_vlan_type, _set_vlan_type)
  vlan_name = __builtin__.property(_get_vlan_name, _set_vlan_name)
  vlan_state = __builtin__.property(_get_vlan_state, _set_vlan_state)
  interface = __builtin__.property(_get_interface, _set_interface)


  _pyangbind_elements = {'vlan_id': vlan_id, 'vlan_type': vlan_type, 'vlan_name': vlan_name, 'vlan_state': vlan_state, 'interface': interface, }


