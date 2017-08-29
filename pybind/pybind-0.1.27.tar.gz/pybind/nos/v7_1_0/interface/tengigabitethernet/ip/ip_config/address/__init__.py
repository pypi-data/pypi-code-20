
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class address(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/tengigabitethernet/ip/ip-config/address. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__address','__secondary','__ospf_passive','__ospf_ignore',)

  _yang_name = 'address'
  _rest_name = 'address'

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
    self.__ospf_ignore = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ospf-ignore", rest_name="ospf-ignore", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'ospf active address on the specific interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='empty', is_config=True)
    self.__secondary = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="secondary", rest_name="secondary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Secondary ip address on the specific interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='empty', is_config=True)
    self.__ospf_passive = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ospf-passive", rest_name="ospf-passive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'ospf pasive address on the specific interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='empty', is_config=True)
    self.__address = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([1-9])|([1-2][0-9])|(3[0-1]))'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),], is_leaf=True, yang_name="address", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A.B.C.D/M IP address in dotted decimal/Mask'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='union', is_config=True)

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
      return [u'interface', u'tengigabitethernet', u'ip', u'ip-config', u'address']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'TenGigabitEthernet', u'ip', u'address']

  def _get_address(self):
    """
    Getter method for address, mapped from YANG variable /interface/tengigabitethernet/ip/ip_config/address/address (union)
    """
    return self.__address
      
  def _set_address(self, v, load=False):
    """
    Setter method for address, mapped from YANG variable /interface/tengigabitethernet/ip/ip_config/address/address (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_address() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([1-9])|([1-2][0-9])|(3[0-1]))'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),], is_leaf=True, yang_name="address", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A.B.C.D/M IP address in dotted decimal/Mask'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='union', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """address must be of a type compatible with union""",
          'defined-type': "brocade-ip-config:union",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([1-9])|([1-2][0-9])|(3[0-1]))'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),], is_leaf=True, yang_name="address", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A.B.C.D/M IP address in dotted decimal/Mask'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='union', is_config=True)""",
        })

    self.__address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_address(self):
    self.__address = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.)(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){2}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([1-9])|([1-2][0-9])|(3[0-1]))'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}),], is_leaf=True, yang_name="address", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A.B.C.D/M IP address in dotted decimal/Mask'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='union', is_config=True)


  def _get_secondary(self):
    """
    Getter method for secondary, mapped from YANG variable /interface/tengigabitethernet/ip/ip_config/address/secondary (empty)
    """
    return self.__secondary
      
  def _set_secondary(self, v, load=False):
    """
    Setter method for secondary, mapped from YANG variable /interface/tengigabitethernet/ip/ip_config/address/secondary (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_secondary is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_secondary() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="secondary", rest_name="secondary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Secondary ip address on the specific interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """secondary must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="secondary", rest_name="secondary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Secondary ip address on the specific interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='empty', is_config=True)""",
        })

    self.__secondary = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_secondary(self):
    self.__secondary = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="secondary", rest_name="secondary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Secondary ip address on the specific interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='empty', is_config=True)


  def _get_ospf_passive(self):
    """
    Getter method for ospf_passive, mapped from YANG variable /interface/tengigabitethernet/ip/ip_config/address/ospf_passive (empty)
    """
    return self.__ospf_passive
      
  def _set_ospf_passive(self, v, load=False):
    """
    Setter method for ospf_passive, mapped from YANG variable /interface/tengigabitethernet/ip/ip_config/address/ospf_passive (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ospf_passive is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ospf_passive() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ospf-passive", rest_name="ospf-passive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'ospf pasive address on the specific interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ospf_passive must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ospf-passive", rest_name="ospf-passive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'ospf pasive address on the specific interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='empty', is_config=True)""",
        })

    self.__ospf_passive = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ospf_passive(self):
    self.__ospf_passive = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ospf-passive", rest_name="ospf-passive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'ospf pasive address on the specific interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='empty', is_config=True)


  def _get_ospf_ignore(self):
    """
    Getter method for ospf_ignore, mapped from YANG variable /interface/tengigabitethernet/ip/ip_config/address/ospf_ignore (empty)
    """
    return self.__ospf_ignore
      
  def _set_ospf_ignore(self, v, load=False):
    """
    Setter method for ospf_ignore, mapped from YANG variable /interface/tengigabitethernet/ip/ip_config/address/ospf_ignore (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ospf_ignore is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ospf_ignore() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ospf-ignore", rest_name="ospf-ignore", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'ospf active address on the specific interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ospf_ignore must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ospf-ignore", rest_name="ospf-ignore", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'ospf active address on the specific interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='empty', is_config=True)""",
        })

    self.__ospf_ignore = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ospf_ignore(self):
    self.__ospf_ignore = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ospf-ignore", rest_name="ospf-ignore", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'ospf active address on the specific interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='empty', is_config=True)

  address = __builtin__.property(_get_address, _set_address)
  secondary = __builtin__.property(_get_secondary, _set_secondary)
  ospf_passive = __builtin__.property(_get_ospf_passive, _set_ospf_passive)
  ospf_ignore = __builtin__.property(_get_ospf_ignore, _set_ospf_ignore)


  _pyangbind_elements = {'address': address, 'secondary': secondary, 'ospf_passive': ospf_passive, 'ospf_ignore': ospf_ignore, }


