
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class shutdown(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/router-bgp/address-family/ipv6/ipv6-unicast/af-ipv6-vrf/neighbor/af-ipv6-vrf-neighbor-address-holder/af-ipv6-neighbor-addr/shutdown. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__shutdown_status','__generate_rib_out',)

  _yang_name = 'shutdown'
  _rest_name = 'shutdown'

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
    self.__shutdown_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="shutdown-status", rest_name="shutdown-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__generate_rib_out = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="generate-rib-out", rest_name="generate-rib-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Generate rib-out routes'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

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
      return [u'rbridge-id', u'router', u'router-bgp', u'address-family', u'ipv6', u'ipv6-unicast', u'af-ipv6-vrf', u'neighbor', u'af-ipv6-vrf-neighbor-address-holder', u'af-ipv6-neighbor-addr', u'shutdown']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'bgp', u'address-family', u'ipv6', u'unicast', u'vrf', u'neighbor', u'af-ipv6-neighbor-addr', u'shutdown']

  def _get_shutdown_status(self):
    """
    Getter method for shutdown_status, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/neighbor/af_ipv6_vrf_neighbor_address_holder/af_ipv6_neighbor_addr/shutdown/shutdown_status (empty)
    """
    return self.__shutdown_status
      
  def _set_shutdown_status(self, v, load=False):
    """
    Setter method for shutdown_status, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/neighbor/af_ipv6_vrf_neighbor_address_holder/af_ipv6_neighbor_addr/shutdown/shutdown_status (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_shutdown_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_shutdown_status() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="shutdown-status", rest_name="shutdown-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """shutdown_status must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="shutdown-status", rest_name="shutdown-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__shutdown_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_shutdown_status(self):
    self.__shutdown_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="shutdown-status", rest_name="shutdown-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_generate_rib_out(self):
    """
    Getter method for generate_rib_out, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/neighbor/af_ipv6_vrf_neighbor_address_holder/af_ipv6_neighbor_addr/shutdown/generate_rib_out (empty)
    """
    return self.__generate_rib_out
      
  def _set_generate_rib_out(self, v, load=False):
    """
    Setter method for generate_rib_out, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv6/ipv6_unicast/af_ipv6_vrf/neighbor/af_ipv6_vrf_neighbor_address_holder/af_ipv6_neighbor_addr/shutdown/generate_rib_out (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_generate_rib_out is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_generate_rib_out() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="generate-rib-out", rest_name="generate-rib-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Generate rib-out routes'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """generate_rib_out must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="generate-rib-out", rest_name="generate-rib-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Generate rib-out routes'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__generate_rib_out = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_generate_rib_out(self):
    self.__generate_rib_out = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="generate-rib-out", rest_name="generate-rib-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Generate rib-out routes'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

  shutdown_status = __builtin__.property(_get_shutdown_status, _set_shutdown_status)
  generate_rib_out = __builtin__.property(_get_generate_rib_out, _set_generate_rib_out)


  _pyangbind_elements = {'shutdown_status': shutdown_status, 'generate_rib_out': generate_rib_out, }


