
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import vrf
import ip
import ipv6
import intf_isis
class loopback(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/interface/loopback. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__id','__vrf','__shutdown','__ip','__ipv6','__intf_isis',)

  _yang_name = 'loopback'
  _rest_name = 'Loopback'

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
    self.__ip = YANGDynClass(base=ip.ip, is_container='container', presence=False, yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Internet Protocol (IP).', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='container', is_config=True)
    self.__vrf = YANGDynClass(base=vrf.vrf, is_container='container', presence=False, yang_name="vrf", rest_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Assign VRF to this ethernet interface', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_VRF_BIND_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-intf-loopback', defining_module='brocade-intf-loopback', yang_type='container', is_config=True)
    self.__shutdown = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shut down interface loopback port', u'cli-show-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_SHUT_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-intf-loopback', defining_module='brocade-intf-loopback', yang_type='empty', is_config=True)
    self.__ipv6 = YANGDynClass(base=ipv6.ipv6, is_container='container', presence=False, yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Internet Protocol version 6(IPv6).', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IPv6_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='container', is_config=True)
    self.__intf_isis = YANGDynClass(base=intf_isis.intf_isis, is_container='container', presence=True, yang_name="intf-isis", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'IsisLoopbackInterface', u'sort-priority': u'129'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)
    self.__id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="id", rest_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'cli-custom-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-intf-loopback', defining_module='brocade-intf-loopback', yang_type='intf-loopback-port-type', is_config=True)

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
      return [u'routing-system', u'interface', u'loopback']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Loopback']

  def _get_id(self):
    """
    Getter method for id, mapped from YANG variable /routing_system/interface/loopback/id (intf-loopback-port-type)
    """
    return self.__id
      
  def _set_id(self, v, load=False):
    """
    Setter method for id, mapped from YANG variable /routing_system/interface/loopback/id (intf-loopback-port-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="id", rest_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'cli-custom-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-intf-loopback', defining_module='brocade-intf-loopback', yang_type='intf-loopback-port-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """id must be of a type compatible with intf-loopback-port-type""",
          'defined-type': "brocade-intf-loopback:intf-loopback-port-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="id", rest_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'cli-custom-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-intf-loopback', defining_module='brocade-intf-loopback', yang_type='intf-loopback-port-type', is_config=True)""",
        })

    self.__id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_id(self):
    self.__id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}), is_leaf=True, yang_name="id", rest_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'cli-custom-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-intf-loopback', defining_module='brocade-intf-loopback', yang_type='intf-loopback-port-type', is_config=True)


  def _get_vrf(self):
    """
    Getter method for vrf, mapped from YANG variable /routing_system/interface/loopback/vrf (container)
    """
    return self.__vrf
      
  def _set_vrf(self, v, load=False):
    """
    Setter method for vrf, mapped from YANG variable /routing_system/interface/loopback/vrf (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vrf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vrf() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=vrf.vrf, is_container='container', presence=False, yang_name="vrf", rest_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Assign VRF to this ethernet interface', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_VRF_BIND_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-intf-loopback', defining_module='brocade-intf-loopback', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vrf must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=vrf.vrf, is_container='container', presence=False, yang_name="vrf", rest_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Assign VRF to this ethernet interface', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_VRF_BIND_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-intf-loopback', defining_module='brocade-intf-loopback', yang_type='container', is_config=True)""",
        })

    self.__vrf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vrf(self):
    self.__vrf = YANGDynClass(base=vrf.vrf, is_container='container', presence=False, yang_name="vrf", rest_name="vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Assign VRF to this ethernet interface', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_VRF_BIND_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-intf-loopback', defining_module='brocade-intf-loopback', yang_type='container', is_config=True)


  def _get_shutdown(self):
    """
    Getter method for shutdown, mapped from YANG variable /routing_system/interface/loopback/shutdown (empty)
    """
    return self.__shutdown
      
  def _set_shutdown(self, v, load=False):
    """
    Setter method for shutdown, mapped from YANG variable /routing_system/interface/loopback/shutdown (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_shutdown is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_shutdown() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shut down interface loopback port', u'cli-show-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_SHUT_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-intf-loopback', defining_module='brocade-intf-loopback', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """shutdown must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shut down interface loopback port', u'cli-show-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_SHUT_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-intf-loopback', defining_module='brocade-intf-loopback', yang_type='empty', is_config=True)""",
        })

    self.__shutdown = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_shutdown(self):
    self.__shutdown = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="shutdown", rest_name="shutdown", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Shut down interface loopback port', u'cli-show-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_SHUT_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-intf-loopback', defining_module='brocade-intf-loopback', yang_type='empty', is_config=True)


  def _get_ip(self):
    """
    Getter method for ip, mapped from YANG variable /routing_system/interface/loopback/ip (container)
    """
    return self.__ip
      
  def _set_ip(self, v, load=False):
    """
    Setter method for ip, mapped from YANG variable /routing_system/interface/loopback/ip (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ip.ip, is_container='container', presence=False, yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Internet Protocol (IP).', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ip.ip, is_container='container', presence=False, yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Internet Protocol (IP).', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='container', is_config=True)""",
        })

    self.__ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip(self):
    self.__ip = YANGDynClass(base=ip.ip, is_container='container', presence=False, yang_name="ip", rest_name="ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Internet Protocol (IP).', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IP_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='container', is_config=True)


  def _get_ipv6(self):
    """
    Getter method for ipv6, mapped from YANG variable /routing_system/interface/loopback/ipv6 (container)
    """
    return self.__ipv6
      
  def _set_ipv6(self, v, load=False):
    """
    Setter method for ipv6, mapped from YANG variable /routing_system/interface/loopback/ipv6 (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ipv6.ipv6, is_container='container', presence=False, yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Internet Protocol version 6(IPv6).', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IPv6_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6 must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ipv6.ipv6, is_container='container', presence=False, yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Internet Protocol version 6(IPv6).', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IPv6_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='container', is_config=True)""",
        })

    self.__ipv6 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6(self):
    self.__ipv6 = YANGDynClass(base=ipv6.ipv6, is_container='container', presence=False, yang_name="ipv6", rest_name="ipv6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Internet Protocol version 6(IPv6).', u'cli-incomplete-no': None, u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IPv6_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='container', is_config=True)


  def _get_intf_isis(self):
    """
    Getter method for intf_isis, mapped from YANG variable /routing_system/interface/loopback/intf_isis (container)
    """
    return self.__intf_isis
      
  def _set_intf_isis(self, v, load=False):
    """
    Setter method for intf_isis, mapped from YANG variable /routing_system/interface/loopback/intf_isis (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_intf_isis is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_intf_isis() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=intf_isis.intf_isis, is_container='container', presence=True, yang_name="intf-isis", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'IsisLoopbackInterface', u'sort-priority': u'129'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """intf_isis must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=intf_isis.intf_isis, is_container='container', presence=True, yang_name="intf-isis", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'IsisLoopbackInterface', u'sort-priority': u'129'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)""",
        })

    self.__intf_isis = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_intf_isis(self):
    self.__intf_isis = YANGDynClass(base=intf_isis.intf_isis, is_container='container', presence=True, yang_name="intf-isis", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'IsisLoopbackInterface', u'sort-priority': u'129'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)

  id = __builtin__.property(_get_id, _set_id)
  vrf = __builtin__.property(_get_vrf, _set_vrf)
  shutdown = __builtin__.property(_get_shutdown, _set_shutdown)
  ip = __builtin__.property(_get_ip, _set_ip)
  ipv6 = __builtin__.property(_get_ipv6, _set_ipv6)
  intf_isis = __builtin__.property(_get_intf_isis, _set_intf_isis)


  _pyangbind_elements = {'id': id, 'vrf': vrf, 'shutdown': shutdown, 'ip': ip, 'ipv6': ipv6, 'intf_isis': intf_isis, }


