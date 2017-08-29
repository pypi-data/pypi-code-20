
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class igmp_multicast_snooping_vlans(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mc-hms-operational - based on the path /igmp-snooping-state/igmp-multicast-snooping-vlans/igmp-multicast-snooping-vlans. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Multicast snooping vlan
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__vlan_id','__pim_sn_status','__igmp_sn_status','__igmp_version',)

  _yang_name = 'igmp-multicast-snooping-vlans'
  _rest_name = 'igmp-multicast-snooping-vlans'

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
    self.__igmp_sn_status = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="igmp-sn-status", rest_name="igmp-sn-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)
    self.__pim_sn_status = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="pim-sn-status", rest_name="pim-sn-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)
    self.__igmp_version = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="igmp-version", rest_name="igmp-version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)

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
      return [u'igmp-snooping-state', u'igmp-multicast-snooping-vlans', u'igmp-multicast-snooping-vlans']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'igmp-snooping-state', u'igmp-multicast-snooping-vlans', u'igmp-multicast-snooping-vlans']

  def _get_vlan_id(self):
    """
    Getter method for vlan_id, mapped from YANG variable /igmp_snooping_state/igmp_multicast_snooping_vlans/igmp_multicast_snooping_vlans/vlan_id (uint32)

    YANG Description: vlan id
    """
    return self.__vlan_id
      
  def _set_vlan_id(self, v, load=False):
    """
    Setter method for vlan_id, mapped from YANG variable /igmp_snooping_state/igmp_multicast_snooping_vlans/igmp_multicast_snooping_vlans/vlan_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_id() directly.

    YANG Description: vlan id
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)""",
        })

    self.__vlan_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_id(self):
    self.__vlan_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="vlan-id", rest_name="vlan-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint32', is_config=False)


  def _get_pim_sn_status(self):
    """
    Getter method for pim_sn_status, mapped from YANG variable /igmp_snooping_state/igmp_multicast_snooping_vlans/igmp_multicast_snooping_vlans/pim_sn_status (uint8)

    YANG Description: Is pim snooping enabled
    """
    return self.__pim_sn_status
      
  def _set_pim_sn_status(self, v, load=False):
    """
    Setter method for pim_sn_status, mapped from YANG variable /igmp_snooping_state/igmp_multicast_snooping_vlans/igmp_multicast_snooping_vlans/pim_sn_status (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pim_sn_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pim_sn_status() directly.

    YANG Description: Is pim snooping enabled
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="pim-sn-status", rest_name="pim-sn-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pim_sn_status must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="pim-sn-status", rest_name="pim-sn-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)""",
        })

    self.__pim_sn_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pim_sn_status(self):
    self.__pim_sn_status = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="pim-sn-status", rest_name="pim-sn-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)


  def _get_igmp_sn_status(self):
    """
    Getter method for igmp_sn_status, mapped from YANG variable /igmp_snooping_state/igmp_multicast_snooping_vlans/igmp_multicast_snooping_vlans/igmp_sn_status (uint8)

    YANG Description: Is igmp snooping enabled
    """
    return self.__igmp_sn_status
      
  def _set_igmp_sn_status(self, v, load=False):
    """
    Setter method for igmp_sn_status, mapped from YANG variable /igmp_snooping_state/igmp_multicast_snooping_vlans/igmp_multicast_snooping_vlans/igmp_sn_status (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmp_sn_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmp_sn_status() directly.

    YANG Description: Is igmp snooping enabled
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="igmp-sn-status", rest_name="igmp-sn-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmp_sn_status must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="igmp-sn-status", rest_name="igmp-sn-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)""",
        })

    self.__igmp_sn_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmp_sn_status(self):
    self.__igmp_sn_status = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="igmp-sn-status", rest_name="igmp-sn-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)


  def _get_igmp_version(self):
    """
    Getter method for igmp_version, mapped from YANG variable /igmp_snooping_state/igmp_multicast_snooping_vlans/igmp_multicast_snooping_vlans/igmp_version (uint8)

    YANG Description: IGMP version enabled on a vlan
    """
    return self.__igmp_version
      
  def _set_igmp_version(self, v, load=False):
    """
    Setter method for igmp_version, mapped from YANG variable /igmp_snooping_state/igmp_multicast_snooping_vlans/igmp_multicast_snooping_vlans/igmp_version (uint8)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_igmp_version is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_igmp_version() directly.

    YANG Description: IGMP version enabled on a vlan
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="igmp-version", rest_name="igmp-version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """igmp_version must be of a type compatible with uint8""",
          'defined-type': "uint8",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="igmp-version", rest_name="igmp-version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)""",
        })

    self.__igmp_version = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_igmp_version(self):
    self.__igmp_version = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..255']}, int_size=8), is_leaf=True, yang_name="igmp-version", rest_name="igmp-version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mc-hms-operational', defining_module='brocade-mc-hms-operational', yang_type='uint8', is_config=False)

  vlan_id = __builtin__.property(_get_vlan_id)
  pim_sn_status = __builtin__.property(_get_pim_sn_status)
  igmp_sn_status = __builtin__.property(_get_igmp_sn_status)
  igmp_version = __builtin__.property(_get_igmp_version)


  _pyangbind_elements = {'vlan_id': vlan_id, 'pim_sn_status': pim_sn_status, 'igmp_sn_status': igmp_sn_status, 'igmp_version': igmp_version, }


