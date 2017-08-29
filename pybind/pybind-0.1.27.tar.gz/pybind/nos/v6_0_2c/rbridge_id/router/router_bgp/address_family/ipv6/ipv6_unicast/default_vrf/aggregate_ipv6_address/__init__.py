
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class aggregate_ipv6_address(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/router-bgp/address-family/ipv6/ipv6-unicast/default-vrf/aggregate-ipv6-address. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__aggregate_ip_prefix','__advertise_map','__as_set','__attribute_map','__summary_only','__suppress_map',)

  _yang_name = 'aggregate-ipv6-address'
  _rest_name = 'aggregate-address'

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
    self.__suppress_map = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="suppress-map", rest_name="suppress-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Conditionally filter more specific routes from updates', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='suppress-map', is_config=True)
    self.__aggregate_ip_prefix = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="aggregate-ip-prefix", rest_name="aggregate-ip-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='inet:ipv6-prefix', is_config=True)
    self.__advertise_map = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="advertise-map", rest_name="advertise-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route map to control attribute advertisement', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='advertise-map', is_config=True)
    self.__attribute_map = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="attribute-map", rest_name="attribute-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route map for parameter control', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='attribute-map', is_config=True)
    self.__as_set = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="as-set", rest_name="as-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Generate AS set path information', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__summary_only = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="summary-only", rest_name="summary-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Filter more specific routes from updates', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

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
      return [u'rbridge-id', u'router', u'router-bgp', u'address-family', u'ipv6', u'ipv6-unicast', u'default-vrf', u'aggregate-ipv6-address']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'bgp', u'address-family', u'ipv6', u'unicast', u'aggregate-address']

  def _get_aggregate_ip_prefix(self):
    """
    Getter method for aggregate_ip_prefix, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/aggregate_ipv6_address/aggregate_ip_prefix (inet:ipv6-prefix)
    """
    return self.__aggregate_ip_prefix
      
  def _set_aggregate_ip_prefix(self, v, load=False):
    """
    Setter method for aggregate_ip_prefix, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/aggregate_ipv6_address/aggregate_ip_prefix (inet:ipv6-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_aggregate_ip_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_aggregate_ip_prefix() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="aggregate-ip-prefix", rest_name="aggregate-ip-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='inet:ipv6-prefix', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """aggregate_ip_prefix must be of a type compatible with inet:ipv6-prefix""",
          'defined-type': "inet:ipv6-prefix",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="aggregate-ip-prefix", rest_name="aggregate-ip-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='inet:ipv6-prefix', is_config=True)""",
        })

    self.__aggregate_ip_prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_aggregate_ip_prefix(self):
    self.__aggregate_ip_prefix = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'}), is_leaf=True, yang_name="aggregate-ip-prefix", rest_name="aggregate-ip-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='inet:ipv6-prefix', is_config=True)


  def _get_advertise_map(self):
    """
    Getter method for advertise_map, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/aggregate_ipv6_address/advertise_map (advertise-map)
    """
    return self.__advertise_map
      
  def _set_advertise_map(self, v, load=False):
    """
    Setter method for advertise_map, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/aggregate_ipv6_address/advertise_map (advertise-map)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_advertise_map is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_advertise_map() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="advertise-map", rest_name="advertise-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route map to control attribute advertisement', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='advertise-map', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """advertise_map must be of a type compatible with advertise-map""",
          'defined-type': "brocade-bgp:advertise-map",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="advertise-map", rest_name="advertise-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route map to control attribute advertisement', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='advertise-map', is_config=True)""",
        })

    self.__advertise_map = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_advertise_map(self):
    self.__advertise_map = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="advertise-map", rest_name="advertise-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route map to control attribute advertisement', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='advertise-map', is_config=True)


  def _get_as_set(self):
    """
    Getter method for as_set, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/aggregate_ipv6_address/as_set (empty)
    """
    return self.__as_set
      
  def _set_as_set(self, v, load=False):
    """
    Setter method for as_set, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/aggregate_ipv6_address/as_set (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_as_set is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_as_set() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="as-set", rest_name="as-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Generate AS set path information', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """as_set must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="as-set", rest_name="as-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Generate AS set path information', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__as_set = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_as_set(self):
    self.__as_set = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="as-set", rest_name="as-set", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Generate AS set path information', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_attribute_map(self):
    """
    Getter method for attribute_map, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/aggregate_ipv6_address/attribute_map (attribute-map)
    """
    return self.__attribute_map
      
  def _set_attribute_map(self, v, load=False):
    """
    Setter method for attribute_map, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/aggregate_ipv6_address/attribute_map (attribute-map)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_attribute_map is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_attribute_map() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="attribute-map", rest_name="attribute-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route map for parameter control', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='attribute-map', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """attribute_map must be of a type compatible with attribute-map""",
          'defined-type': "brocade-bgp:attribute-map",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="attribute-map", rest_name="attribute-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route map for parameter control', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='attribute-map', is_config=True)""",
        })

    self.__attribute_map = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_attribute_map(self):
    self.__attribute_map = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="attribute-map", rest_name="attribute-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Route map for parameter control', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='attribute-map', is_config=True)


  def _get_summary_only(self):
    """
    Getter method for summary_only, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/aggregate_ipv6_address/summary_only (empty)
    """
    return self.__summary_only
      
  def _set_summary_only(self, v, load=False):
    """
    Setter method for summary_only, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/aggregate_ipv6_address/summary_only (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_summary_only is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_summary_only() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="summary-only", rest_name="summary-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Filter more specific routes from updates', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """summary_only must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="summary-only", rest_name="summary-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Filter more specific routes from updates', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__summary_only = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_summary_only(self):
    self.__summary_only = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="summary-only", rest_name="summary-only", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Filter more specific routes from updates', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_suppress_map(self):
    """
    Getter method for suppress_map, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/aggregate_ipv6_address/suppress_map (suppress-map)
    """
    return self.__suppress_map
      
  def _set_suppress_map(self, v, load=False):
    """
    Setter method for suppress_map, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/aggregate_ipv6_address/suppress_map (suppress-map)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_suppress_map is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_suppress_map() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="suppress-map", rest_name="suppress-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Conditionally filter more specific routes from updates', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='suppress-map', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """suppress_map must be of a type compatible with suppress-map""",
          'defined-type': "brocade-bgp:suppress-map",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="suppress-map", rest_name="suppress-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Conditionally filter more specific routes from updates', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='suppress-map', is_config=True)""",
        })

    self.__suppress_map = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_suppress_map(self):
    self.__suppress_map = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..63']}), is_leaf=True, yang_name="suppress-map", rest_name="suppress-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Conditionally filter more specific routes from updates', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='suppress-map', is_config=True)

  aggregate_ip_prefix = __builtin__.property(_get_aggregate_ip_prefix, _set_aggregate_ip_prefix)
  advertise_map = __builtin__.property(_get_advertise_map, _set_advertise_map)
  as_set = __builtin__.property(_get_as_set, _set_as_set)
  attribute_map = __builtin__.property(_get_attribute_map, _set_attribute_map)
  summary_only = __builtin__.property(_get_summary_only, _set_summary_only)
  suppress_map = __builtin__.property(_get_suppress_map, _set_suppress_map)


  _pyangbind_elements = {'aggregate_ip_prefix': aggregate_ip_prefix, 'advertise_map': advertise_map, 'as_set': as_set, 'attribute_map': attribute_map, 'summary_only': summary_only, 'suppress_map': suppress_map, }


