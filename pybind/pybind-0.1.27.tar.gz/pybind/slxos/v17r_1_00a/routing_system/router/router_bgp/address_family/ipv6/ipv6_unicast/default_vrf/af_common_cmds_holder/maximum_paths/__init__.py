
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class maximum_paths(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/ipv6/ipv6-unicast/default-vrf/af-common-cmds-holder/maximum-paths. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__load_sharing_value','__ebgp','__ibgp','__use_load_sharing',)

  _yang_name = 'maximum-paths'
  _rest_name = 'maximum-paths'

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
    self.__ibgp = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..64']}), is_leaf=True, yang_name="ibgp", rest_name="ibgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number of IBGP paths for load sharing', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='ibgp-paths', is_config=True)
    self.__load_sharing_value = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..64']}), is_leaf=True, yang_name="load-sharing-value", rest_name="load-sharing-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='uint32', is_config=True)
    self.__ebgp = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..64']}), is_leaf=True, yang_name="ebgp", rest_name="ebgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number of EBGP paths for load sharing', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='ebgp-paths', is_config=True)
    self.__use_load_sharing = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="use-load-sharing", rest_name="use-load-sharing", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Number of load-sharing paths: using load-sharing value'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'ipv6', u'ipv6-unicast', u'default-vrf', u'af-common-cmds-holder', u'maximum-paths']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'bgp', u'address-family', u'ipv6', u'unicast', u'maximum-paths']

  def _get_load_sharing_value(self):
    """
    Getter method for load_sharing_value, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_common_cmds_holder/maximum_paths/load_sharing_value (uint32)
    """
    return self.__load_sharing_value
      
  def _set_load_sharing_value(self, v, load=False):
    """
    Setter method for load_sharing_value, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_common_cmds_holder/maximum_paths/load_sharing_value (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_load_sharing_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_load_sharing_value() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..64']}), is_leaf=True, yang_name="load-sharing-value", rest_name="load-sharing-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """load_sharing_value must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..64']}), is_leaf=True, yang_name="load-sharing-value", rest_name="load-sharing-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='uint32', is_config=True)""",
        })

    self.__load_sharing_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_load_sharing_value(self):
    self.__load_sharing_value = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..64']}), is_leaf=True, yang_name="load-sharing-value", rest_name="load-sharing-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='uint32', is_config=True)


  def _get_ebgp(self):
    """
    Getter method for ebgp, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_common_cmds_holder/maximum_paths/ebgp (ebgp-paths)
    """
    return self.__ebgp
      
  def _set_ebgp(self, v, load=False):
    """
    Setter method for ebgp, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_common_cmds_holder/maximum_paths/ebgp (ebgp-paths)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ebgp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ebgp() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..64']}), is_leaf=True, yang_name="ebgp", rest_name="ebgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number of EBGP paths for load sharing', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='ebgp-paths', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ebgp must be of a type compatible with ebgp-paths""",
          'defined-type': "brocade-bgp:ebgp-paths",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..64']}), is_leaf=True, yang_name="ebgp", rest_name="ebgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number of EBGP paths for load sharing', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='ebgp-paths', is_config=True)""",
        })

    self.__ebgp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ebgp(self):
    self.__ebgp = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..64']}), is_leaf=True, yang_name="ebgp", rest_name="ebgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number of EBGP paths for load sharing', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='ebgp-paths', is_config=True)


  def _get_ibgp(self):
    """
    Getter method for ibgp, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_common_cmds_holder/maximum_paths/ibgp (ibgp-paths)
    """
    return self.__ibgp
      
  def _set_ibgp(self, v, load=False):
    """
    Setter method for ibgp, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_common_cmds_holder/maximum_paths/ibgp (ibgp-paths)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ibgp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ibgp() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..64']}), is_leaf=True, yang_name="ibgp", rest_name="ibgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number of IBGP paths for load sharing', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='ibgp-paths', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ibgp must be of a type compatible with ibgp-paths""",
          'defined-type': "brocade-bgp:ibgp-paths",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..64']}), is_leaf=True, yang_name="ibgp", rest_name="ibgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number of IBGP paths for load sharing', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='ibgp-paths', is_config=True)""",
        })

    self.__ibgp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ibgp(self):
    self.__ibgp = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..64']}), is_leaf=True, yang_name="ibgp", rest_name="ibgp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Number of IBGP paths for load sharing', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='ibgp-paths', is_config=True)


  def _get_use_load_sharing(self):
    """
    Getter method for use_load_sharing, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_common_cmds_holder/maximum_paths/use_load_sharing (empty)
    """
    return self.__use_load_sharing
      
  def _set_use_load_sharing(self, v, load=False):
    """
    Setter method for use_load_sharing, mapped from YANG variable /routing_system/router/router_bgp/address_family/ipv6/ipv6_unicast/default_vrf/af_common_cmds_holder/maximum_paths/use_load_sharing (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_use_load_sharing is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_use_load_sharing() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="use-load-sharing", rest_name="use-load-sharing", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Number of load-sharing paths: using load-sharing value'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """use_load_sharing must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="use-load-sharing", rest_name="use-load-sharing", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Number of load-sharing paths: using load-sharing value'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__use_load_sharing = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_use_load_sharing(self):
    self.__use_load_sharing = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="use-load-sharing", rest_name="use-load-sharing", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Number of load-sharing paths: using load-sharing value'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

  load_sharing_value = __builtin__.property(_get_load_sharing_value, _set_load_sharing_value)
  ebgp = __builtin__.property(_get_ebgp, _set_ebgp)
  ibgp = __builtin__.property(_get_ibgp, _set_ibgp)
  use_load_sharing = __builtin__.property(_get_use_load_sharing, _set_use_load_sharing)


  _pyangbind_elements = {'load_sharing_value': load_sharing_value, 'ebgp': ebgp, 'ibgp': ibgp, 'use_load_sharing': use_load_sharing, }


