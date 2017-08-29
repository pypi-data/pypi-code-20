
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import icmp
import address
import gateway
import oper_address
import oper_gateway_con
import access_group
class ip(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/management/ip. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The IPv4 configurations for this management 
interface.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__icmp','__address','__gateway','__oper_address','__oper_gateway_con','__access_group',)

  _yang_name = 'ip'
  _rest_name = 'ip'

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
    self.__oper_address = YANGDynClass(base=oper_address.oper_address, is_container='container', presence=False, yang_name="oper-address", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The assigned IP address.', u'alt-name': u'address'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__oper_gateway_con = YANGDynClass(base=oper_gateway_con.oper_gateway_con, is_container='container', presence=False, yang_name="oper-gateway-con", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__access_group = YANGDynClass(base=access_group.access_group, is_container='container', presence=False, yang_name="access-group", rest_name="access-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IP Access group', u'sort-priority': u'115', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'callpoint': u'ip_acl_config_cp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='container', is_config=True)
    self.__address = YANGDynClass(base=address.address, is_container='container', presence=False, yang_name="address", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The IPv4 address configuration for this \nmanagement interface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__icmp = YANGDynClass(base=icmp.icmp, is_container='container', presence=False, yang_name="icmp", rest_name="icmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The ICMP control for this management interface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__gateway = YANGDynClass(base=gateway.gateway, is_container='container', presence=False, yang_name="gateway", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The IP gateway configurations for this \nmanagement interface.', u'cli-drop-node-name': None, u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)

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
      return [u'interface', u'management', u'ip']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Management', u'ip']

  def _get_icmp(self):
    """
    Getter method for icmp, mapped from YANG variable /interface/management/ip/icmp (container)

    YANG Description: The ICMP control for this management interface.
    """
    return self.__icmp
      
  def _set_icmp(self, v, load=False):
    """
    Setter method for icmp, mapped from YANG variable /interface/management/ip/icmp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_icmp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_icmp() directly.

    YANG Description: The ICMP control for this management interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=icmp.icmp, is_container='container', presence=False, yang_name="icmp", rest_name="icmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The ICMP control for this management interface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """icmp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=icmp.icmp, is_container='container', presence=False, yang_name="icmp", rest_name="icmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The ICMP control for this management interface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__icmp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_icmp(self):
    self.__icmp = YANGDynClass(base=icmp.icmp, is_container='container', presence=False, yang_name="icmp", rest_name="icmp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The ICMP control for this management interface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_address(self):
    """
    Getter method for address, mapped from YANG variable /interface/management/ip/address (container)

    YANG Description: The IPv4 address configuration for this 
management interface.
    """
    return self.__address
      
  def _set_address(self, v, load=False):
    """
    Setter method for address, mapped from YANG variable /interface/management/ip/address (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_address() directly.

    YANG Description: The IPv4 address configuration for this 
management interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=address.address, is_container='container', presence=False, yang_name="address", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The IPv4 address configuration for this \nmanagement interface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """address must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=address.address, is_container='container', presence=False, yang_name="address", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The IPv4 address configuration for this \nmanagement interface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_address(self):
    self.__address = YANGDynClass(base=address.address, is_container='container', presence=False, yang_name="address", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The IPv4 address configuration for this \nmanagement interface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_gateway(self):
    """
    Getter method for gateway, mapped from YANG variable /interface/management/ip/gateway (container)

    YANG Description: The IP gateway configurations for this 
management interface.
    """
    return self.__gateway
      
  def _set_gateway(self, v, load=False):
    """
    Setter method for gateway, mapped from YANG variable /interface/management/ip/gateway (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_gateway is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_gateway() directly.

    YANG Description: The IP gateway configurations for this 
management interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=gateway.gateway, is_container='container', presence=False, yang_name="gateway", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The IP gateway configurations for this \nmanagement interface.', u'cli-drop-node-name': None, u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """gateway must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=gateway.gateway, is_container='container', presence=False, yang_name="gateway", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The IP gateway configurations for this \nmanagement interface.', u'cli-drop-node-name': None, u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__gateway = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_gateway(self):
    self.__gateway = YANGDynClass(base=gateway.gateway, is_container='container', presence=False, yang_name="gateway", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The IP gateway configurations for this \nmanagement interface.', u'cli-drop-node-name': None, u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_oper_address(self):
    """
    Getter method for oper_address, mapped from YANG variable /interface/management/ip/oper_address (container)
    """
    return self.__oper_address
      
  def _set_oper_address(self, v, load=False):
    """
    Setter method for oper_address, mapped from YANG variable /interface/management/ip/oper_address (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_oper_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_oper_address() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=oper_address.oper_address, is_container='container', presence=False, yang_name="oper-address", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The assigned IP address.', u'alt-name': u'address'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """oper_address must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=oper_address.oper_address, is_container='container', presence=False, yang_name="oper-address", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The assigned IP address.', u'alt-name': u'address'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__oper_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_oper_address(self):
    self.__oper_address = YANGDynClass(base=oper_address.oper_address, is_container='container', presence=False, yang_name="oper-address", rest_name="address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The assigned IP address.', u'alt-name': u'address'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_oper_gateway_con(self):
    """
    Getter method for oper_gateway_con, mapped from YANG variable /interface/management/ip/oper_gateway_con (container)
    """
    return self.__oper_gateway_con
      
  def _set_oper_gateway_con(self, v, load=False):
    """
    Setter method for oper_gateway_con, mapped from YANG variable /interface/management/ip/oper_gateway_con (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_oper_gateway_con is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_oper_gateway_con() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=oper_gateway_con.oper_gateway_con, is_container='container', presence=False, yang_name="oper-gateway-con", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """oper_gateway_con must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=oper_gateway_con.oper_gateway_con, is_container='container', presence=False, yang_name="oper-gateway-con", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__oper_gateway_con = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_oper_gateway_con(self):
    self.__oper_gateway_con = YANGDynClass(base=oper_gateway_con.oper_gateway_con, is_container='container', presence=False, yang_name="oper-gateway-con", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_access_group(self):
    """
    Getter method for access_group, mapped from YANG variable /interface/management/ip/access_group (container)
    """
    return self.__access_group
      
  def _set_access_group(self, v, load=False):
    """
    Setter method for access_group, mapped from YANG variable /interface/management/ip/access_group (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_access_group is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_access_group() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=access_group.access_group, is_container='container', presence=False, yang_name="access-group", rest_name="access-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IP Access group', u'sort-priority': u'115', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'callpoint': u'ip_acl_config_cp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """access_group must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=access_group.access_group, is_container='container', presence=False, yang_name="access-group", rest_name="access-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IP Access group', u'sort-priority': u'115', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'callpoint': u'ip_acl_config_cp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='container', is_config=True)""",
        })

    self.__access_group = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_access_group(self):
    self.__access_group = YANGDynClass(base=access_group.access_group, is_container='container', presence=False, yang_name="access-group", rest_name="access-group", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure IP Access group', u'sort-priority': u'115', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'callpoint': u'ip_acl_config_cp'}}, namespace='urn:brocade.com:mgmt:brocade-ip-access-list', defining_module='brocade-ip-access-list', yang_type='container', is_config=True)

  icmp = __builtin__.property(_get_icmp, _set_icmp)
  address = __builtin__.property(_get_address, _set_address)
  gateway = __builtin__.property(_get_gateway, _set_gateway)
  oper_address = __builtin__.property(_get_oper_address, _set_oper_address)
  oper_gateway_con = __builtin__.property(_get_oper_gateway_con, _set_oper_gateway_con)
  access_group = __builtin__.property(_get_access_group, _set_access_group)


  _pyangbind_elements = {'icmp': icmp, 'address': address, 'gateway': gateway, 'oper_address': oper_address, 'oper_gateway_con': oper_gateway_con, 'access_group': access_group, }


