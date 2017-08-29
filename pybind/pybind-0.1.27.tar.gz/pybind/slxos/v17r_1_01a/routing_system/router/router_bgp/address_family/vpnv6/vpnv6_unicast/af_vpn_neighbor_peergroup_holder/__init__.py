
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import af_vpn_neighbor_peergroup
class af_vpn_neighbor_peergroup_holder(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/address-family/vpnv6/vpnv6-unicast/af-vpn-neighbor-peergroup-holder. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__af_vpn_neighbor_peergroup',)

  _yang_name = 'af-vpn-neighbor-peergroup-holder'
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
    self.__af_vpn_neighbor_peergroup = YANGDynClass(base=YANGListType("af_vpn_neighbor_peergroup_address",af_vpn_neighbor_peergroup.af_vpn_neighbor_peergroup, yang_name="af-vpn-neighbor-peergroup", rest_name="neighbor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='af-vpn-neighbor-peergroup-address', extensions={u'tailf-common': {u'info': u'Specify a neighbor router', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'callpoint': u'AfVpnV6NeighborsPeerGroup', u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'alt-name': u'neighbor'}}), is_container='list', yang_name="af-vpn-neighbor-peergroup", rest_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify a neighbor router', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'callpoint': u'AfVpnV6NeighborsPeerGroup', u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'alt-name': u'neighbor'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'address-family', u'vpnv6', u'vpnv6-unicast', u'af-vpn-neighbor-peergroup-holder']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'bgp', u'address-family', u'vpnv6', u'unicast']

  def _get_af_vpn_neighbor_peergroup(self):
    """
    Getter method for af_vpn_neighbor_peergroup, mapped from YANG variable /routing_system/router/router_bgp/address_family/vpnv6/vpnv6_unicast/af_vpn_neighbor_peergroup_holder/af_vpn_neighbor_peergroup (list)
    """
    return self.__af_vpn_neighbor_peergroup
      
  def _set_af_vpn_neighbor_peergroup(self, v, load=False):
    """
    Setter method for af_vpn_neighbor_peergroup, mapped from YANG variable /routing_system/router/router_bgp/address_family/vpnv6/vpnv6_unicast/af_vpn_neighbor_peergroup_holder/af_vpn_neighbor_peergroup (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_af_vpn_neighbor_peergroup is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_af_vpn_neighbor_peergroup() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("af_vpn_neighbor_peergroup_address",af_vpn_neighbor_peergroup.af_vpn_neighbor_peergroup, yang_name="af-vpn-neighbor-peergroup", rest_name="neighbor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='af-vpn-neighbor-peergroup-address', extensions={u'tailf-common': {u'info': u'Specify a neighbor router', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'callpoint': u'AfVpnV6NeighborsPeerGroup', u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'alt-name': u'neighbor'}}), is_container='list', yang_name="af-vpn-neighbor-peergroup", rest_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify a neighbor router', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'callpoint': u'AfVpnV6NeighborsPeerGroup', u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'alt-name': u'neighbor'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """af_vpn_neighbor_peergroup must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("af_vpn_neighbor_peergroup_address",af_vpn_neighbor_peergroup.af_vpn_neighbor_peergroup, yang_name="af-vpn-neighbor-peergroup", rest_name="neighbor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='af-vpn-neighbor-peergroup-address', extensions={u'tailf-common': {u'info': u'Specify a neighbor router', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'callpoint': u'AfVpnV6NeighborsPeerGroup', u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'alt-name': u'neighbor'}}), is_container='list', yang_name="af-vpn-neighbor-peergroup", rest_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify a neighbor router', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'callpoint': u'AfVpnV6NeighborsPeerGroup', u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'alt-name': u'neighbor'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)""",
        })

    self.__af_vpn_neighbor_peergroup = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_af_vpn_neighbor_peergroup(self):
    self.__af_vpn_neighbor_peergroup = YANGDynClass(base=YANGListType("af_vpn_neighbor_peergroup_address",af_vpn_neighbor_peergroup.af_vpn_neighbor_peergroup, yang_name="af-vpn-neighbor-peergroup", rest_name="neighbor", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='af-vpn-neighbor-peergroup-address', extensions={u'tailf-common': {u'info': u'Specify a neighbor router', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'callpoint': u'AfVpnV6NeighborsPeerGroup', u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'alt-name': u'neighbor'}}), is_container='list', yang_name="af-vpn-neighbor-peergroup", rest_name="neighbor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify a neighbor router', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'callpoint': u'AfVpnV6NeighborsPeerGroup', u'cli-suppress-key-abbreviation': None, u'cli-incomplete-command': None, u'alt-name': u'neighbor'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='list', is_config=True)

  af_vpn_neighbor_peergroup = __builtin__.property(_get_af_vpn_neighbor_peergroup, _set_af_vpn_neighbor_peergroup)


  _pyangbind_elements = {'af_vpn_neighbor_peergroup': af_vpn_neighbor_peergroup, }


