
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ethernet_container(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/route-map/content/precedence/set/interface/ethernet-container. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ethernet','__strip_vlan_eth',)

  _yang_name = 'ethernet-container'
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
    self.__strip_vlan_eth = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'outer': {'value': 1}},), is_leaf=True, yang_name="strip-vlan-eth", rest_name="strip-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Vlan Header stripping config', u'alt-name': u'strip-vlan'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='enumeration', is_config=True)
    self.__ethernet = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="ethernet", rest_name="ethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ethernet Interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:interface-type', is_config=True)

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
      return [u'routing-system', u'route-map', u'content', u'precedence', u'set', u'interface', u'ethernet-container']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'route-map', u'precedence', u'set', u'interface']

  def _get_ethernet(self):
    """
    Getter method for ethernet, mapped from YANG variable /routing_system/route_map/content/precedence/set/interface/ethernet_container/ethernet (interface:interface-type)
    """
    return self.__ethernet
      
  def _set_ethernet(self, v, load=False):
    """
    Setter method for ethernet, mapped from YANG variable /routing_system/route_map/content/precedence/set/interface/ethernet_container/ethernet (interface:interface-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ethernet is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ethernet() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="ethernet", rest_name="ethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ethernet Interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:interface-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ethernet must be of a type compatible with interface:interface-type""",
          'defined-type': "interface:interface-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="ethernet", rest_name="ethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ethernet Interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:interface-type', is_config=True)""",
        })

    self.__ethernet = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ethernet(self):
    self.__ethernet = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}), is_leaf=True, yang_name="ethernet", rest_name="ethernet", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Ethernet Interface'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='interface:interface-type', is_config=True)


  def _get_strip_vlan_eth(self):
    """
    Getter method for strip_vlan_eth, mapped from YANG variable /routing_system/route_map/content/precedence/set/interface/ethernet_container/strip_vlan_eth (enumeration)
    """
    return self.__strip_vlan_eth
      
  def _set_strip_vlan_eth(self, v, load=False):
    """
    Setter method for strip_vlan_eth, mapped from YANG variable /routing_system/route_map/content/precedence/set/interface/ethernet_container/strip_vlan_eth (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_strip_vlan_eth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_strip_vlan_eth() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'outer': {'value': 1}},), is_leaf=True, yang_name="strip-vlan-eth", rest_name="strip-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Vlan Header stripping config', u'alt-name': u'strip-vlan'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """strip_vlan_eth must be of a type compatible with enumeration""",
          'defined-type': "brocade-ip-policy:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'outer': {'value': 1}},), is_leaf=True, yang_name="strip-vlan-eth", rest_name="strip-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Vlan Header stripping config', u'alt-name': u'strip-vlan'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='enumeration', is_config=True)""",
        })

    self.__strip_vlan_eth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_strip_vlan_eth(self):
    self.__strip_vlan_eth = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'outer': {'value': 1}},), is_leaf=True, yang_name="strip-vlan-eth", rest_name="strip-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Vlan Header stripping config', u'alt-name': u'strip-vlan'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='enumeration', is_config=True)

  ethernet = __builtin__.property(_get_ethernet, _set_ethernet)
  strip_vlan_eth = __builtin__.property(_get_strip_vlan_eth, _set_strip_vlan_eth)


  _pyangbind_elements = {'ethernet': ethernet, 'strip_vlan_eth': strip_vlan_eth, }


