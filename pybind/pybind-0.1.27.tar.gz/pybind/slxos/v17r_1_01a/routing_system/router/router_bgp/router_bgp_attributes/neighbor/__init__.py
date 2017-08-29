
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import peer_grps
import neighbor_ipv6s
import neighbor_ips
class neighbor(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/router-bgp/router-bgp-attributes/neighbor. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__peer_grps','__neighbor_ipv6s','__neighbor_ips',)

  _yang_name = 'neighbor'
  _rest_name = 'neighbor'

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
    self.__neighbor_ips = YANGDynClass(base=neighbor_ips.neighbor_ips, is_container='container', presence=False, yang_name="neighbor-ips", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__peer_grps = YANGDynClass(base=peer_grps.peer_grps, is_container='container', presence=False, yang_name="peer-grps", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    self.__neighbor_ipv6s = YANGDynClass(base=neighbor_ipv6s.neighbor_ipv6s, is_container='container', presence=False, yang_name="neighbor-ipv6s", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

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
      return [u'routing-system', u'router', u'router-bgp', u'router-bgp-attributes', u'neighbor']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'bgp', u'neighbor']

  def _get_peer_grps(self):
    """
    Getter method for peer_grps, mapped from YANG variable /routing_system/router/router_bgp/router_bgp_attributes/neighbor/peer_grps (container)
    """
    return self.__peer_grps
      
  def _set_peer_grps(self, v, load=False):
    """
    Setter method for peer_grps, mapped from YANG variable /routing_system/router/router_bgp/router_bgp_attributes/neighbor/peer_grps (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_peer_grps is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_peer_grps() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=peer_grps.peer_grps, is_container='container', presence=False, yang_name="peer-grps", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """peer_grps must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=peer_grps.peer_grps, is_container='container', presence=False, yang_name="peer-grps", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__peer_grps = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_peer_grps(self):
    self.__peer_grps = YANGDynClass(base=peer_grps.peer_grps, is_container='container', presence=False, yang_name="peer-grps", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_neighbor_ipv6s(self):
    """
    Getter method for neighbor_ipv6s, mapped from YANG variable /routing_system/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ipv6s (container)
    """
    return self.__neighbor_ipv6s
      
  def _set_neighbor_ipv6s(self, v, load=False):
    """
    Setter method for neighbor_ipv6s, mapped from YANG variable /routing_system/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ipv6s (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbor_ipv6s is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbor_ipv6s() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=neighbor_ipv6s.neighbor_ipv6s, is_container='container', presence=False, yang_name="neighbor-ipv6s", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbor_ipv6s must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=neighbor_ipv6s.neighbor_ipv6s, is_container='container', presence=False, yang_name="neighbor-ipv6s", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__neighbor_ipv6s = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbor_ipv6s(self):
    self.__neighbor_ipv6s = YANGDynClass(base=neighbor_ipv6s.neighbor_ipv6s, is_container='container', presence=False, yang_name="neighbor-ipv6s", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)


  def _get_neighbor_ips(self):
    """
    Getter method for neighbor_ips, mapped from YANG variable /routing_system/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ips (container)
    """
    return self.__neighbor_ips
      
  def _set_neighbor_ips(self, v, load=False):
    """
    Setter method for neighbor_ips, mapped from YANG variable /routing_system/router/router_bgp/router_bgp_attributes/neighbor/neighbor_ips (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_neighbor_ips is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_neighbor_ips() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=neighbor_ips.neighbor_ips, is_container='container', presence=False, yang_name="neighbor-ips", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """neighbor_ips must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=neighbor_ips.neighbor_ips, is_container='container', presence=False, yang_name="neighbor-ips", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)""",
        })

    self.__neighbor_ips = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_neighbor_ips(self):
    self.__neighbor_ips = YANGDynClass(base=neighbor_ips.neighbor_ips, is_container='container', presence=False, yang_name="neighbor-ips", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='container', is_config=True)

  peer_grps = __builtin__.property(_get_peer_grps, _set_peer_grps)
  neighbor_ipv6s = __builtin__.property(_get_neighbor_ipv6s, _set_neighbor_ipv6s)
  neighbor_ips = __builtin__.property(_get_neighbor_ips, _set_neighbor_ips)


  _pyangbind_elements = {'peer_grps': peer_grps, 'neighbor_ipv6s': neighbor_ipv6s, 'neighbor_ips': neighbor_ips, }


