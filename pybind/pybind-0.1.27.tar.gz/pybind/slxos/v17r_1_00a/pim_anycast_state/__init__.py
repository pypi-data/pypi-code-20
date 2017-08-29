
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import peer_list
class pim_anycast_state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-pim-operational - based on the path /pim-anycast-state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Pim Anycast Rp information
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__vrf_name','__anycast_rp','__prefix_name','__peer_list',)

  _yang_name = 'pim-anycast-state'
  _rest_name = 'pim-anycast-state'

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
    self.__anycast_rp = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="anycast-rp", rest_name="anycast-rp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='inet:ipv4-address', is_config=False)
    self.__vrf_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf-name", rest_name="vrf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)
    self.__prefix_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="prefix-name", rest_name="prefix-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)
    self.__peer_list = YANGDynClass(base=YANGListType("ipv4_addr",peer_list.peer_list, yang_name="peer-list", rest_name="peer-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv4-addr', extensions={u'tailf-common': {u'callpoint': u'pim-peer-ipv4-addr', u'cli-suppress-show-path': None}}), is_container='list', yang_name="peer-list", rest_name="peer-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'pim-peer-ipv4-addr', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='list', is_config=False)

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
      return [u'pim-anycast-state']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'pim-anycast-state']

  def _get_vrf_name(self):
    """
    Getter method for vrf_name, mapped from YANG variable /pim_anycast_state/vrf_name (string)

    YANG Description: vrf name
    """
    return self.__vrf_name
      
  def _set_vrf_name(self, v, load=False):
    """
    Setter method for vrf_name, mapped from YANG variable /pim_anycast_state/vrf_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vrf_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vrf_name() directly.

    YANG Description: vrf name
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vrf-name", rest_name="vrf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vrf_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf-name", rest_name="vrf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)""",
        })

    self.__vrf_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vrf_name(self):
    self.__vrf_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vrf-name", rest_name="vrf-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)


  def _get_anycast_rp(self):
    """
    Getter method for anycast_rp, mapped from YANG variable /pim_anycast_state/anycast_rp (inet:ipv4-address)

    YANG Description: ipv4 anycast rp address
    """
    return self.__anycast_rp
      
  def _set_anycast_rp(self, v, load=False):
    """
    Setter method for anycast_rp, mapped from YANG variable /pim_anycast_state/anycast_rp (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_anycast_rp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_anycast_rp() directly.

    YANG Description: ipv4 anycast rp address
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="anycast-rp", rest_name="anycast-rp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='inet:ipv4-address', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """anycast_rp must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="anycast-rp", rest_name="anycast-rp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='inet:ipv4-address', is_config=False)""",
        })

    self.__anycast_rp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_anycast_rp(self):
    self.__anycast_rp = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="anycast-rp", rest_name="anycast-rp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='inet:ipv4-address', is_config=False)


  def _get_prefix_name(self):
    """
    Getter method for prefix_name, mapped from YANG variable /pim_anycast_state/prefix_name (string)

    YANG Description: Prefix name
    """
    return self.__prefix_name
      
  def _set_prefix_name(self, v, load=False):
    """
    Setter method for prefix_name, mapped from YANG variable /pim_anycast_state/prefix_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_name() directly.

    YANG Description: Prefix name
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="prefix-name", rest_name="prefix-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="prefix-name", rest_name="prefix-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)""",
        })

    self.__prefix_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_name(self):
    self.__prefix_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="prefix-name", rest_name="prefix-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='string', is_config=False)


  def _get_peer_list(self):
    """
    Getter method for peer_list, mapped from YANG variable /pim_anycast_state/peer_list (list)

    YANG Description: A Simple UI32 MO for storing ip address in integer format
    """
    return self.__peer_list
      
  def _set_peer_list(self, v, load=False):
    """
    Setter method for peer_list, mapped from YANG variable /pim_anycast_state/peer_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peer_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peer_list() directly.

    YANG Description: A Simple UI32 MO for storing ip address in integer format
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("ipv4_addr",peer_list.peer_list, yang_name="peer-list", rest_name="peer-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv4-addr', extensions={u'tailf-common': {u'callpoint': u'pim-peer-ipv4-addr', u'cli-suppress-show-path': None}}), is_container='list', yang_name="peer-list", rest_name="peer-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'pim-peer-ipv4-addr', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peer_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ipv4_addr",peer_list.peer_list, yang_name="peer-list", rest_name="peer-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv4-addr', extensions={u'tailf-common': {u'callpoint': u'pim-peer-ipv4-addr', u'cli-suppress-show-path': None}}), is_container='list', yang_name="peer-list", rest_name="peer-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'pim-peer-ipv4-addr', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='list', is_config=False)""",
        })

    self.__peer_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peer_list(self):
    self.__peer_list = YANGDynClass(base=YANGListType("ipv4_addr",peer_list.peer_list, yang_name="peer-list", rest_name="peer-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ipv4-addr', extensions={u'tailf-common': {u'callpoint': u'pim-peer-ipv4-addr', u'cli-suppress-show-path': None}}), is_container='list', yang_name="peer-list", rest_name="peer-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'pim-peer-ipv4-addr', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-pim-operational', defining_module='brocade-pim-operational', yang_type='list', is_config=False)

  vrf_name = __builtin__.property(_get_vrf_name)
  anycast_rp = __builtin__.property(_get_anycast_rp)
  prefix_name = __builtin__.property(_get_prefix_name)
  peer_list = __builtin__.property(_get_peer_list)


  _pyangbind_elements = {'vrf_name': vrf_name, 'anycast_rp': anycast_rp, 'prefix_name': prefix_name, 'peer_list': peer_list, }


