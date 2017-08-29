
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ipsec(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/port-channel/ipv6/interface-ospfv3-conf/authentication/ipsec. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configure ipsec authentication for the interface
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ipsec_authentication_disable','__ifc_key_add_remove_interval',)

  _yang_name = 'ipsec'
  _rest_name = 'ipsec'

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
    self.__ipsec_authentication_disable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipsec-authentication-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable ipsec authentication', u'cli-full-command': None, u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)
    self.__ifc_key_add_remove_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..14400']}), is_leaf=True, yang_name="ifc-key-add-remove-interval", rest_name="key-add-remove-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure OSPFv3 authentication key add/remove interval', u'alt-name': u'key-add-remove-interval'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)

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
      return [u'interface', u'port-channel', u'ipv6', u'interface-ospfv3-conf', u'authentication', u'ipsec']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Port-channel', u'ipv6', u'ospf', u'authentication', u'ipsec']

  def _get_ipsec_authentication_disable(self):
    """
    Getter method for ipsec_authentication_disable, mapped from YANG variable /interface/port_channel/ipv6/interface_ospfv3_conf/authentication/ipsec/ipsec_authentication_disable (empty)

    YANG Description: Disable ipsec authentication on the interface. For the purpose of troubleshooting, you can operationally disable IPsec on an interface using this command.This command disables IPsec on the interface whether its IPsec configuration is the area's IPsec configuration or is specific to that interface.
    """
    return self.__ipsec_authentication_disable
      
  def _set_ipsec_authentication_disable(self, v, load=False):
    """
    Setter method for ipsec_authentication_disable, mapped from YANG variable /interface/port_channel/ipv6/interface_ospfv3_conf/authentication/ipsec/ipsec_authentication_disable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipsec_authentication_disable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipsec_authentication_disable() directly.

    YANG Description: Disable ipsec authentication on the interface. For the purpose of troubleshooting, you can operationally disable IPsec on an interface using this command.This command disables IPsec on the interface whether its IPsec configuration is the area's IPsec configuration or is specific to that interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ipsec-authentication-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable ipsec authentication', u'cli-full-command': None, u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipsec_authentication_disable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipsec-authentication-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable ipsec authentication', u'cli-full-command': None, u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)""",
        })

    self.__ipsec_authentication_disable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipsec_authentication_disable(self):
    self.__ipsec_authentication_disable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipsec-authentication-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable ipsec authentication', u'cli-full-command': None, u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='empty', is_config=True)


  def _get_ifc_key_add_remove_interval(self):
    """
    Getter method for ifc_key_add_remove_interval, mapped from YANG variable /interface/port_channel/ipv6/interface_ospfv3_conf/authentication/ipsec/ifc_key_add_remove_interval (common-def:time-interval-sec)

    YANG Description: Used to determine the interval time when authentication addition and deletion will take effect
    """
    return self.__ifc_key_add_remove_interval
      
  def _set_ifc_key_add_remove_interval(self, v, load=False):
    """
    Setter method for ifc_key_add_remove_interval, mapped from YANG variable /interface/port_channel/ipv6/interface_ospfv3_conf/authentication/ipsec/ifc_key_add_remove_interval (common-def:time-interval-sec)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ifc_key_add_remove_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ifc_key_add_remove_interval() directly.

    YANG Description: Used to determine the interval time when authentication addition and deletion will take effect
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..14400']}), is_leaf=True, yang_name="ifc-key-add-remove-interval", rest_name="key-add-remove-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure OSPFv3 authentication key add/remove interval', u'alt-name': u'key-add-remove-interval'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ifc_key_add_remove_interval must be of a type compatible with common-def:time-interval-sec""",
          'defined-type': "common-def:time-interval-sec",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..14400']}), is_leaf=True, yang_name="ifc-key-add-remove-interval", rest_name="key-add-remove-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure OSPFv3 authentication key add/remove interval', u'alt-name': u'key-add-remove-interval'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)""",
        })

    self.__ifc_key_add_remove_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ifc_key_add_remove_interval(self):
    self.__ifc_key_add_remove_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..14400']}), is_leaf=True, yang_name="ifc-key-add-remove-interval", rest_name="key-add-remove-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure OSPFv3 authentication key add/remove interval', u'alt-name': u'key-add-remove-interval'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)

  ipsec_authentication_disable = __builtin__.property(_get_ipsec_authentication_disable, _set_ipsec_authentication_disable)
  ifc_key_add_remove_interval = __builtin__.property(_get_ifc_key_add_remove_interval, _set_ifc_key_add_remove_interval)


  _pyangbind_elements = {'ipsec_authentication_disable': ipsec_authentication_disable, 'ifc_key_add_remove_interval': ifc_key_add_remove_interval, }


