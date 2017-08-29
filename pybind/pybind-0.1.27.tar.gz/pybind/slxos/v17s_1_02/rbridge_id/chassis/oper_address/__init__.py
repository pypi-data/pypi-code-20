
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class oper_address(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/chassis/oper-address. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__virtual_oper_Vip_address','__virtual_oper_VipV6_address',)

  _yang_name = 'oper-address'
  _rest_name = 'virtual-ip'

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
    self.__virtual_oper_Vip_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((0|(1[0-9]{0,2})|(2(([0-4][0-9]?)|(5[0-5]?)|([6-9]?)))|([3-9][0-9]?))\\.){3}(0|(1[0-9]{0,2})|(2(([0-4][0-9]?)|(5[0-5]?)|([6-9]?)))|([3-9][0-9]?))/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="virtual-oper-Vip-address", rest_name="v4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'alt-name': u'v4'}}, namespace='urn:brocade.com:mgmt:brocade-chassis', defining_module='brocade-chassis', yang_type='common-def:ipv4-address-prefix-type', is_config=False)
    self.__virtual_oper_VipV6_address = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="virtual-oper-VipV6-address", rest_name="v6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'alt-name': u'v6'}}, namespace='urn:brocade.com:mgmt:brocade-chassis', defining_module='brocade-chassis', yang_type='string', is_config=False)

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
      return [u'rbridge-id', u'chassis', u'oper-address']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'chassis', u'virtual-ip']

  def _get_virtual_oper_Vip_address(self):
    """
    Getter method for virtual_oper_Vip_address, mapped from YANG variable /rbridge_id/chassis/oper_address/virtual_oper_Vip_address (common-def:ipv4-address-prefix-type)

    YANG Description: The assigned chassis IPv4 address.
    """
    return self.__virtual_oper_Vip_address
      
  def _set_virtual_oper_Vip_address(self, v, load=False):
    """
    Setter method for virtual_oper_Vip_address, mapped from YANG variable /rbridge_id/chassis/oper_address/virtual_oper_Vip_address (common-def:ipv4-address-prefix-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_virtual_oper_Vip_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_virtual_oper_Vip_address() directly.

    YANG Description: The assigned chassis IPv4 address.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((0|(1[0-9]{0,2})|(2(([0-4][0-9]?)|(5[0-5]?)|([6-9]?)))|([3-9][0-9]?))\\.){3}(0|(1[0-9]{0,2})|(2(([0-4][0-9]?)|(5[0-5]?)|([6-9]?)))|([3-9][0-9]?))/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="virtual-oper-Vip-address", rest_name="v4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'alt-name': u'v4'}}, namespace='urn:brocade.com:mgmt:brocade-chassis', defining_module='brocade-chassis', yang_type='common-def:ipv4-address-prefix-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """virtual_oper_Vip_address must be of a type compatible with common-def:ipv4-address-prefix-type""",
          'defined-type': "common-def:ipv4-address-prefix-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((0|(1[0-9]{0,2})|(2(([0-4][0-9]?)|(5[0-5]?)|([6-9]?)))|([3-9][0-9]?))\\.){3}(0|(1[0-9]{0,2})|(2(([0-4][0-9]?)|(5[0-5]?)|([6-9]?)))|([3-9][0-9]?))/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="virtual-oper-Vip-address", rest_name="v4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'alt-name': u'v4'}}, namespace='urn:brocade.com:mgmt:brocade-chassis', defining_module='brocade-chassis', yang_type='common-def:ipv4-address-prefix-type', is_config=False)""",
        })

    self.__virtual_oper_Vip_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_virtual_oper_Vip_address(self):
    self.__virtual_oper_Vip_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((0|(1[0-9]{0,2})|(2(([0-4][0-9]?)|(5[0-5]?)|([6-9]?)))|([3-9][0-9]?))\\.){3}(0|(1[0-9]{0,2})|(2(([0-4][0-9]?)|(5[0-5]?)|([6-9]?)))|([3-9][0-9]?))/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="virtual-oper-Vip-address", rest_name="v4", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'alt-name': u'v4'}}, namespace='urn:brocade.com:mgmt:brocade-chassis', defining_module='brocade-chassis', yang_type='common-def:ipv4-address-prefix-type', is_config=False)


  def _get_virtual_oper_VipV6_address(self):
    """
    Getter method for virtual_oper_VipV6_address, mapped from YANG variable /rbridge_id/chassis/oper_address/virtual_oper_VipV6_address (string)

    YANG Description: The assigned chassis IPv6 address.
    """
    return self.__virtual_oper_VipV6_address
      
  def _set_virtual_oper_VipV6_address(self, v, load=False):
    """
    Setter method for virtual_oper_VipV6_address, mapped from YANG variable /rbridge_id/chassis/oper_address/virtual_oper_VipV6_address (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_virtual_oper_VipV6_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_virtual_oper_VipV6_address() directly.

    YANG Description: The assigned chassis IPv6 address.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="virtual-oper-VipV6-address", rest_name="v6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'alt-name': u'v6'}}, namespace='urn:brocade.com:mgmt:brocade-chassis', defining_module='brocade-chassis', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """virtual_oper_VipV6_address must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="virtual-oper-VipV6-address", rest_name="v6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'alt-name': u'v6'}}, namespace='urn:brocade.com:mgmt:brocade-chassis', defining_module='brocade-chassis', yang_type='string', is_config=False)""",
        })

    self.__virtual_oper_VipV6_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_virtual_oper_VipV6_address(self):
    self.__virtual_oper_VipV6_address = YANGDynClass(base=TypedListType(allowed_type=unicode), is_leaf=False, yang_name="virtual-oper-VipV6-address", rest_name="v6", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'alt-name': u'v6'}}, namespace='urn:brocade.com:mgmt:brocade-chassis', defining_module='brocade-chassis', yang_type='string', is_config=False)

  virtual_oper_Vip_address = __builtin__.property(_get_virtual_oper_Vip_address)
  virtual_oper_VipV6_address = __builtin__.property(_get_virtual_oper_VipV6_address)


  _pyangbind_elements = {'virtual_oper_Vip_address': virtual_oper_Vip_address, 'virtual_oper_VipV6_address': virtual_oper_VipV6_address, }


