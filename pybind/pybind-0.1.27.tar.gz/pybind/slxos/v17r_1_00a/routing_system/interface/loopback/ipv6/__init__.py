
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ipv6_config
import intf_ipv6_router_isis
import interface_ospfv3_conf
class ipv6(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/interface/loopback/ipv6. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ipv6_config','__intf_ipv6_router_isis','__interface_ospfv3_conf',)

  _yang_name = 'ipv6'
  _rest_name = 'ipv6'

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
    self.__intf_ipv6_router_isis = YANGDynClass(base=intf_ipv6_router_isis.intf_ipv6_router_isis, is_container='container', presence=False, yang_name="intf-ipv6-router-isis", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'IsisLoopbackInterfaceIpv6Router'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)
    self.__interface_ospfv3_conf = YANGDynClass(base=interface_ospfv3_conf.interface_ospfv3_conf, is_container='container', presence=False, yang_name="interface-ospfv3-conf", rest_name="ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Open Shortest Path First version 3 (OSPFv3)', u'alt-name': u'ospf', u'cli-incomplete-no': None, u'callpoint': u'Ospfv3LoopbackInterfaceConfig', u'cli-incomplete-command': None, u'sort-priority': u'124', u'display-when': u'/vcsmode/vcs-mode = "false"'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    self.__ipv6_config = YANGDynClass(base=ipv6_config.ipv6_config, is_container='container', presence=False, yang_name="ipv6-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the IPv6 address of an interface', u'cli-drop-node-name': None, u'callpoint': u'lo-intf-ipv6-cfg-cp', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IPv6_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='container', is_config=True)

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
      return [u'routing-system', u'interface', u'loopback', u'ipv6']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Loopback', u'ipv6']

  def _get_ipv6_config(self):
    """
    Getter method for ipv6_config, mapped from YANG variable /routing_system/interface/loopback/ipv6/ipv6_config (container)
    """
    return self.__ipv6_config
      
  def _set_ipv6_config(self, v, load=False):
    """
    Setter method for ipv6_config, mapped from YANG variable /routing_system/interface/loopback/ipv6/ipv6_config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_config() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ipv6_config.ipv6_config, is_container='container', presence=False, yang_name="ipv6-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the IPv6 address of an interface', u'cli-drop-node-name': None, u'callpoint': u'lo-intf-ipv6-cfg-cp', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IPv6_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ipv6_config.ipv6_config, is_container='container', presence=False, yang_name="ipv6-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the IPv6 address of an interface', u'cli-drop-node-name': None, u'callpoint': u'lo-intf-ipv6-cfg-cp', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IPv6_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='container', is_config=True)""",
        })

    self.__ipv6_config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_config(self):
    self.__ipv6_config = YANGDynClass(base=ipv6_config.ipv6_config, is_container='container', presence=False, yang_name="ipv6-config", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the IPv6 address of an interface', u'cli-drop-node-name': None, u'callpoint': u'lo-intf-ipv6-cfg-cp', u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_IPv6_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-config', defining_module='brocade-ipv6-config', yang_type='container', is_config=True)


  def _get_intf_ipv6_router_isis(self):
    """
    Getter method for intf_ipv6_router_isis, mapped from YANG variable /routing_system/interface/loopback/ipv6/intf_ipv6_router_isis (container)
    """
    return self.__intf_ipv6_router_isis
      
  def _set_intf_ipv6_router_isis(self, v, load=False):
    """
    Setter method for intf_ipv6_router_isis, mapped from YANG variable /routing_system/interface/loopback/ipv6/intf_ipv6_router_isis (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_intf_ipv6_router_isis is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_intf_ipv6_router_isis() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=intf_ipv6_router_isis.intf_ipv6_router_isis, is_container='container', presence=False, yang_name="intf-ipv6-router-isis", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'IsisLoopbackInterfaceIpv6Router'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """intf_ipv6_router_isis must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=intf_ipv6_router_isis.intf_ipv6_router_isis, is_container='container', presence=False, yang_name="intf-ipv6-router-isis", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'IsisLoopbackInterfaceIpv6Router'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)""",
        })

    self.__intf_ipv6_router_isis = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_intf_ipv6_router_isis(self):
    self.__intf_ipv6_router_isis = YANGDynClass(base=intf_ipv6_router_isis.intf_ipv6_router_isis, is_container='container', presence=False, yang_name="intf-ipv6-router-isis", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'IsisLoopbackInterfaceIpv6Router'}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='container', is_config=True)


  def _get_interface_ospfv3_conf(self):
    """
    Getter method for interface_ospfv3_conf, mapped from YANG variable /routing_system/interface/loopback/ipv6/interface_ospfv3_conf (container)

    YANG Description: Open Shortest Path First version 3 (OSPFv3)
    """
    return self.__interface_ospfv3_conf
      
  def _set_interface_ospfv3_conf(self, v, load=False):
    """
    Setter method for interface_ospfv3_conf, mapped from YANG variable /routing_system/interface/loopback/ipv6/interface_ospfv3_conf (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface_ospfv3_conf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface_ospfv3_conf() directly.

    YANG Description: Open Shortest Path First version 3 (OSPFv3)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=interface_ospfv3_conf.interface_ospfv3_conf, is_container='container', presence=False, yang_name="interface-ospfv3-conf", rest_name="ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Open Shortest Path First version 3 (OSPFv3)', u'alt-name': u'ospf', u'cli-incomplete-no': None, u'callpoint': u'Ospfv3LoopbackInterfaceConfig', u'cli-incomplete-command': None, u'sort-priority': u'124', u'display-when': u'/vcsmode/vcs-mode = "false"'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface_ospfv3_conf must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=interface_ospfv3_conf.interface_ospfv3_conf, is_container='container', presence=False, yang_name="interface-ospfv3-conf", rest_name="ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Open Shortest Path First version 3 (OSPFv3)', u'alt-name': u'ospf', u'cli-incomplete-no': None, u'callpoint': u'Ospfv3LoopbackInterfaceConfig', u'cli-incomplete-command': None, u'sort-priority': u'124', u'display-when': u'/vcsmode/vcs-mode = "false"'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)""",
        })

    self.__interface_ospfv3_conf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface_ospfv3_conf(self):
    self.__interface_ospfv3_conf = YANGDynClass(base=interface_ospfv3_conf.interface_ospfv3_conf, is_container='container', presence=False, yang_name="interface-ospfv3-conf", rest_name="ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Open Shortest Path First version 3 (OSPFv3)', u'alt-name': u'ospf', u'cli-incomplete-no': None, u'callpoint': u'Ospfv3LoopbackInterfaceConfig', u'cli-incomplete-command': None, u'sort-priority': u'124', u'display-when': u'/vcsmode/vcs-mode = "false"'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='container', is_config=True)

  ipv6_config = __builtin__.property(_get_ipv6_config, _set_ipv6_config)
  intf_ipv6_router_isis = __builtin__.property(_get_intf_ipv6_router_isis, _set_intf_ipv6_router_isis)
  interface_ospfv3_conf = __builtin__.property(_get_interface_ospfv3_conf, _set_interface_ospfv3_conf)


  _pyangbind_elements = {'ipv6_config': ipv6_config, 'intf_ipv6_router_isis': intf_ipv6_router_isis, 'interface_ospfv3_conf': interface_ospfv3_conf, }


