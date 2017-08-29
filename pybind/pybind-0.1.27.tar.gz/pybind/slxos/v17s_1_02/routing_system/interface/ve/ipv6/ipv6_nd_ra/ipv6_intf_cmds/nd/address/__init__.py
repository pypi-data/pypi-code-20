
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import suppressing_address
class address(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/interface/ve/ipv6/ipv6-nd-ra/ipv6-intf-cmds/nd/address. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__suppressing_address','__address_suppress_all',)

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
    self.__suppressing_address = YANGDynClass(base=YANGListType("suppress_ipv6_address",suppressing_address.suppressing_address, yang_name="suppressing-address", rest_name="suppressing-address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='suppress-ipv6-address', extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'callpoint': u'IpV6NdRaAddressVlanIntf'}}), is_container='list', yang_name="suppressing-address", rest_name="suppressing-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'callpoint': u'IpV6NdRaAddressVlanIntf'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='list', is_config=True)
    self.__address_suppress_all = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="address-suppress-all", rest_name="suppress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Suppress all IPv6 addresses in router advertisement', u'cli-full-command': None, u'alt-name': u'suppress', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'interface', u've', u'ipv6', u'ipv6-nd-ra', u'ipv6-intf-cmds', u'nd', u'address']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ve', u'ipv6', u'nd', u'address']

  def _get_suppressing_address(self):
    """
    Getter method for suppressing_address, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/address/suppressing_address (list)
    """
    return self.__suppressing_address
      
  def _set_suppressing_address(self, v, load=False):
    """
    Setter method for suppressing_address, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/address/suppressing_address (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_suppressing_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_suppressing_address() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("suppress_ipv6_address",suppressing_address.suppressing_address, yang_name="suppressing-address", rest_name="suppressing-address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='suppress-ipv6-address', extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'callpoint': u'IpV6NdRaAddressVlanIntf'}}), is_container='list', yang_name="suppressing-address", rest_name="suppressing-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'callpoint': u'IpV6NdRaAddressVlanIntf'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """suppressing_address must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("suppress_ipv6_address",suppressing_address.suppressing_address, yang_name="suppressing-address", rest_name="suppressing-address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='suppress-ipv6-address', extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'callpoint': u'IpV6NdRaAddressVlanIntf'}}), is_container='list', yang_name="suppressing-address", rest_name="suppressing-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'callpoint': u'IpV6NdRaAddressVlanIntf'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='list', is_config=True)""",
        })

    self.__suppressing_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_suppressing_address(self):
    self.__suppressing_address = YANGDynClass(base=YANGListType("suppress_ipv6_address",suppressing_address.suppressing_address, yang_name="suppressing-address", rest_name="suppressing-address", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='suppress-ipv6-address', extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'callpoint': u'IpV6NdRaAddressVlanIntf'}}), is_container='list', yang_name="suppressing-address", rest_name="suppressing-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'cli-incomplete-no': None, u'cli-suppress-list-no': None, u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'callpoint': u'IpV6NdRaAddressVlanIntf'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='list', is_config=True)


  def _get_address_suppress_all(self):
    """
    Getter method for address_suppress_all, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/address/address_suppress_all (empty)
    """
    return self.__address_suppress_all
      
  def _set_address_suppress_all(self, v, load=False):
    """
    Setter method for address_suppress_all, mapped from YANG variable /routing_system/interface/ve/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/address/address_suppress_all (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_address_suppress_all is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_address_suppress_all() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="address-suppress-all", rest_name="suppress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Suppress all IPv6 addresses in router advertisement', u'cli-full-command': None, u'alt-name': u'suppress', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """address_suppress_all must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="address-suppress-all", rest_name="suppress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Suppress all IPv6 addresses in router advertisement', u'cli-full-command': None, u'alt-name': u'suppress', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)""",
        })

    self.__address_suppress_all = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_address_suppress_all(self):
    self.__address_suppress_all = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="address-suppress-all", rest_name="suppress", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Suppress all IPv6 addresses in router advertisement', u'cli-full-command': None, u'alt-name': u'suppress', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)

  suppressing_address = __builtin__.property(_get_suppressing_address, _set_suppressing_address)
  address_suppress_all = __builtin__.property(_get_address_suppress_all, _set_address_suppress_all)


  _pyangbind_elements = {'suppressing_address': suppressing_address, 'address_suppress_all': address_suppress_all, }


