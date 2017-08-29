
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import route_map
import send_community
class evpn_peer_group(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/router-bgp/address-family/l2vpn/evpn/neighbor/evpn-peer-group. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__evpn_neighbor_peergroup_name','__activate','__maximum_prefix','__route_reflector_client','__allowas_in','__next_hop_unchanged','__enable_peer_as_check','__route_map','__send_community',)

  _yang_name = 'evpn-peer-group'
  _rest_name = 'evpn-peer-group'

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
    self.__enable_peer_as_check = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable-peer-as-check", rest_name="enable-peer-as-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable routes advertise between peers in same AS', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__activate = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow exchange of route in the current family mode', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__send_community = YANGDynClass(base=send_community.send_community, is_container='container', presence=False, yang_name="send-community", rest_name="send-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Send community attribute to this neighbor', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__route_map = YANGDynClass(base=route_map.route_map, is_container='container', presence=False, yang_name="route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Apply route map', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__allowas_in = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..10']}), is_leaf=True, yang_name="allowas-in", rest_name="allowas-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disables the AS_PATH check of the routes learned from the AS', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='uint32', is_config=True)
    self.__evpn_neighbor_peergroup_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="evpn-neighbor-peergroup-name", rest_name="evpn-neighbor-peergroup-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Word:1-63;;Peer Group Name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bgp-peergroup', is_config=True)
    self.__maximum_prefix = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..2147483647']}), is_leaf=True, yang_name="maximum-prefix", rest_name="maximum-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='max-prefix-limit', is_config=True)
    self.__route_reflector_client = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="route-reflector-client", rest_name="route-reflector-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a neighbor as Route Reflector client', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__next_hop_unchanged = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="next-hop-unchanged", rest_name="next-hop-unchanged", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Next hop unchanged', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

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
      return [u'rbridge-id', u'router', u'router-bgp', u'address-family', u'l2vpn', u'evpn', u'neighbor', u'evpn-peer-group']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'bgp', u'address-family', u'l2vpn', u'evpn', u'neighbor', u'evpn-peer-group']

  def _get_evpn_neighbor_peergroup_name(self):
    """
    Getter method for evpn_neighbor_peergroup_name, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_peer_group/evpn_neighbor_peergroup_name (bgp-peergroup)
    """
    return self.__evpn_neighbor_peergroup_name
      
  def _set_evpn_neighbor_peergroup_name(self, v, load=False):
    """
    Setter method for evpn_neighbor_peergroup_name, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_peer_group/evpn_neighbor_peergroup_name (bgp-peergroup)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_evpn_neighbor_peergroup_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_evpn_neighbor_peergroup_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="evpn-neighbor-peergroup-name", rest_name="evpn-neighbor-peergroup-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Word:1-63;;Peer Group Name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bgp-peergroup', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """evpn_neighbor_peergroup_name must be of a type compatible with bgp-peergroup""",
          'defined-type': "brocade-bgp:bgp-peergroup",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="evpn-neighbor-peergroup-name", rest_name="evpn-neighbor-peergroup-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Word:1-63;;Peer Group Name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bgp-peergroup', is_config=True)""",
        })

    self.__evpn_neighbor_peergroup_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_evpn_neighbor_peergroup_name(self):
    self.__evpn_neighbor_peergroup_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,62})'}), is_leaf=True, yang_name="evpn-neighbor-peergroup-name", rest_name="evpn-neighbor-peergroup-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Word:1-63;;Peer Group Name'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='bgp-peergroup', is_config=True)


  def _get_activate(self):
    """
    Getter method for activate, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_peer_group/activate (empty)
    """
    return self.__activate
      
  def _set_activate(self, v, load=False):
    """
    Setter method for activate, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_peer_group/activate (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_activate is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_activate() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow exchange of route in the current family mode', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """activate must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow exchange of route in the current family mode', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__activate = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_activate(self):
    self.__activate = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="activate", rest_name="activate", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Allow exchange of route in the current family mode', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_maximum_prefix(self):
    """
    Getter method for maximum_prefix, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_peer_group/maximum_prefix (max-prefix-limit)
    """
    return self.__maximum_prefix
      
  def _set_maximum_prefix(self, v, load=False):
    """
    Setter method for maximum_prefix, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_peer_group/maximum_prefix (max-prefix-limit)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_maximum_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_maximum_prefix() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..2147483647']}), is_leaf=True, yang_name="maximum-prefix", rest_name="maximum-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='max-prefix-limit', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """maximum_prefix must be of a type compatible with max-prefix-limit""",
          'defined-type': "brocade-bgp:max-prefix-limit",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..2147483647']}), is_leaf=True, yang_name="maximum-prefix", rest_name="maximum-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='max-prefix-limit', is_config=True)""",
        })

    self.__maximum_prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_maximum_prefix(self):
    self.__maximum_prefix = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..2147483647']}), is_leaf=True, yang_name="maximum-prefix", rest_name="maximum-prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='max-prefix-limit', is_config=True)


  def _get_route_reflector_client(self):
    """
    Getter method for route_reflector_client, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_peer_group/route_reflector_client (empty)
    """
    return self.__route_reflector_client
      
  def _set_route_reflector_client(self, v, load=False):
    """
    Setter method for route_reflector_client, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_peer_group/route_reflector_client (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_reflector_client is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_reflector_client() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="route-reflector-client", rest_name="route-reflector-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a neighbor as Route Reflector client', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_reflector_client must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="route-reflector-client", rest_name="route-reflector-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a neighbor as Route Reflector client', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__route_reflector_client = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_reflector_client(self):
    self.__route_reflector_client = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="route-reflector-client", rest_name="route-reflector-client", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure a neighbor as Route Reflector client', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_allowas_in(self):
    """
    Getter method for allowas_in, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_peer_group/allowas_in (uint32)
    """
    return self.__allowas_in
      
  def _set_allowas_in(self, v, load=False):
    """
    Setter method for allowas_in, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_peer_group/allowas_in (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_allowas_in is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_allowas_in() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..10']}), is_leaf=True, yang_name="allowas-in", rest_name="allowas-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disables the AS_PATH check of the routes learned from the AS', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """allowas_in must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..10']}), is_leaf=True, yang_name="allowas-in", rest_name="allowas-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disables the AS_PATH check of the routes learned from the AS', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='uint32', is_config=True)""",
        })

    self.__allowas_in = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_allowas_in(self):
    self.__allowas_in = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..10']}), is_leaf=True, yang_name="allowas-in", rest_name="allowas-in", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disables the AS_PATH check of the routes learned from the AS', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='uint32', is_config=True)


  def _get_next_hop_unchanged(self):
    """
    Getter method for next_hop_unchanged, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_peer_group/next_hop_unchanged (empty)
    """
    return self.__next_hop_unchanged
      
  def _set_next_hop_unchanged(self, v, load=False):
    """
    Setter method for next_hop_unchanged, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_peer_group/next_hop_unchanged (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_next_hop_unchanged is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_next_hop_unchanged() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="next-hop-unchanged", rest_name="next-hop-unchanged", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Next hop unchanged', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """next_hop_unchanged must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="next-hop-unchanged", rest_name="next-hop-unchanged", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Next hop unchanged', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__next_hop_unchanged = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_next_hop_unchanged(self):
    self.__next_hop_unchanged = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="next-hop-unchanged", rest_name="next-hop-unchanged", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Next hop unchanged', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_enable_peer_as_check(self):
    """
    Getter method for enable_peer_as_check, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_peer_group/enable_peer_as_check (empty)
    """
    return self.__enable_peer_as_check
      
  def _set_enable_peer_as_check(self, v, load=False):
    """
    Setter method for enable_peer_as_check, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_peer_group/enable_peer_as_check (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enable_peer_as_check is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enable_peer_as_check() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="enable-peer-as-check", rest_name="enable-peer-as-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable routes advertise between peers in same AS', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enable_peer_as_check must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable-peer-as-check", rest_name="enable-peer-as-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable routes advertise between peers in same AS', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__enable_peer_as_check = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enable_peer_as_check(self):
    self.__enable_peer_as_check = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="enable-peer-as-check", rest_name="enable-peer-as-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable routes advertise between peers in same AS', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_route_map(self):
    """
    Getter method for route_map, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_peer_group/route_map (container)
    """
    return self.__route_map
      
  def _set_route_map(self, v, load=False):
    """
    Setter method for route_map, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_peer_group/route_map (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_route_map is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_route_map() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=route_map.route_map, is_container='container', presence=False, yang_name="route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Apply route map', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """route_map must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=route_map.route_map, is_container='container', presence=False, yang_name="route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Apply route map', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__route_map = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_route_map(self):
    self.__route_map = YANGDynClass(base=route_map.route_map, is_container='container', presence=False, yang_name="route-map", rest_name="route-map", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Apply route map', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_send_community(self):
    """
    Getter method for send_community, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_peer_group/send_community (container)
    """
    return self.__send_community
      
  def _set_send_community(self, v, load=False):
    """
    Setter method for send_community, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/l2vpn/evpn/neighbor/evpn_peer_group/send_community (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_send_community is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_send_community() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=send_community.send_community, is_container='container', presence=False, yang_name="send-community", rest_name="send-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Send community attribute to this neighbor', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """send_community must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=send_community.send_community, is_container='container', presence=False, yang_name="send-community", rest_name="send-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Send community attribute to this neighbor', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__send_community = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_send_community(self):
    self.__send_community = YANGDynClass(base=send_community.send_community, is_container='container', presence=False, yang_name="send-community", rest_name="send-community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Send community attribute to this neighbor', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

  evpn_neighbor_peergroup_name = __builtin__.property(_get_evpn_neighbor_peergroup_name, _set_evpn_neighbor_peergroup_name)
  activate = __builtin__.property(_get_activate, _set_activate)
  maximum_prefix = __builtin__.property(_get_maximum_prefix, _set_maximum_prefix)
  route_reflector_client = __builtin__.property(_get_route_reflector_client, _set_route_reflector_client)
  allowas_in = __builtin__.property(_get_allowas_in, _set_allowas_in)
  next_hop_unchanged = __builtin__.property(_get_next_hop_unchanged, _set_next_hop_unchanged)
  enable_peer_as_check = __builtin__.property(_get_enable_peer_as_check, _set_enable_peer_as_check)
  route_map = __builtin__.property(_get_route_map, _set_route_map)
  send_community = __builtin__.property(_get_send_community, _set_send_community)


  _pyangbind_elements = {'evpn_neighbor_peergroup_name': evpn_neighbor_peergroup_name, 'activate': activate, 'maximum_prefix': maximum_prefix, 'route_reflector_client': route_reflector_client, 'allowas_in': allowas_in, 'next_hop_unchanged': next_hop_unchanged, 'enable_peer_as_check': enable_peer_as_check, 'route_map': route_map, 'send_community': send_community, }


