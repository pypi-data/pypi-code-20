
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import mode
import port_security
import access
import access_mac_group_vlan_classification
import access_mac_vlan_classification
import trunk_private_vlan_classification
import trunk
import private_vlan
import access_mac_rspan_vlan_classification
import access_mac_group_rspan_vlan_classification
class switchport(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/tengigabitethernet/switchport. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The L2 switching characteristics of an interface.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__mode','__port_security','__access','__access_mac_group_vlan_classification','__access_mac_vlan_classification','__trunk_private_vlan_classification','__trunk','__private_vlan','__access_mac_rspan_vlan_classification','__access_mac_group_rspan_vlan_classification',)

  _yang_name = 'switchport'
  _rest_name = 'switchport'

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
    self.__trunk_private_vlan_classification = YANGDynClass(base=trunk_private_vlan_classification.trunk_private_vlan_classification, is_container='container', presence=False, yang_name="trunk-private-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'ctag-pvlan-classification-phy-config'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__private_vlan = YANGDynClass(base=private_vlan.private_vlan, is_container='container', presence=False, yang_name="private-vlan", rest_name="private-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set Private-Vlan Configuration'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__access_mac_vlan_classification = YANGDynClass(base=access_mac_vlan_classification.access_mac_vlan_classification, is_container='container', presence=False, yang_name="access-mac-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'gvlan-access-port-config-phy'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__access = YANGDynClass(base=access.access, is_container='container', presence=False, yang_name="access", rest_name="access", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as Access', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__access_mac_group_vlan_classification = YANGDynClass(base=access_mac_group_vlan_classification.access_mac_group_vlan_classification, is_container='container', presence=False, yang_name="access-mac-group-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'mac-group-vlan-classification-config-phy'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__port_security = YANGDynClass(base=port_security.port_security, is_container='container', presence=True, yang_name="port-security", rest_name="port-security", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable port-security feature', u'callpoint': u'interface_portsecurity'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__access_mac_group_rspan_vlan_classification = YANGDynClass(base=access_mac_group_rspan_vlan_classification.access_mac_group_rspan_vlan_classification, is_container='container', presence=False, yang_name="access-mac-group-rspan-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__mode = YANGDynClass(base=mode.mode, is_container='container', presence=False, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set mode of the Layer2 interface', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__trunk = YANGDynClass(base=trunk.trunk, is_container='container', presence=False, yang_name="trunk", rest_name="trunk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as trunk', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__access_mac_rspan_vlan_classification = YANGDynClass(base=access_mac_rspan_vlan_classification.access_mac_rspan_vlan_classification, is_container='container', presence=False, yang_name="access-mac-rspan-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)

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
      return [u'interface', u'tengigabitethernet', u'switchport']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'TenGigabitEthernet', u'switchport']

  def _get_mode(self):
    """
    Getter method for mode, mapped from YANG variable /interface/tengigabitethernet/switchport/mode (container)

    YANG Description: The mode of the Layer2 interface.
    """
    return self.__mode
      
  def _set_mode(self, v, load=False):
    """
    Setter method for mode, mapped from YANG variable /interface/tengigabitethernet/switchport/mode (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mode() directly.

    YANG Description: The mode of the Layer2 interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=mode.mode, is_container='container', presence=False, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set mode of the Layer2 interface', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mode must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=mode.mode, is_container='container', presence=False, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set mode of the Layer2 interface', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mode(self):
    self.__mode = YANGDynClass(base=mode.mode, is_container='container', presence=False, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set mode of the Layer2 interface', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_port_security(self):
    """
    Getter method for port_security, mapped from YANG variable /interface/tengigabitethernet/switchport/port_security (container)

    YANG Description: Enable port-security feature
    """
    return self.__port_security
      
  def _set_port_security(self, v, load=False):
    """
    Setter method for port_security, mapped from YANG variable /interface/tengigabitethernet/switchport/port_security (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_security is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_security() directly.

    YANG Description: Enable port-security feature
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=port_security.port_security, is_container='container', presence=True, yang_name="port-security", rest_name="port-security", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable port-security feature', u'callpoint': u'interface_portsecurity'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_security must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=port_security.port_security, is_container='container', presence=True, yang_name="port-security", rest_name="port-security", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable port-security feature', u'callpoint': u'interface_portsecurity'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__port_security = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_security(self):
    self.__port_security = YANGDynClass(base=port_security.port_security, is_container='container', presence=True, yang_name="port-security", rest_name="port-security", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable port-security feature', u'callpoint': u'interface_portsecurity'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_access(self):
    """
    Getter method for access, mapped from YANG variable /interface/tengigabitethernet/switchport/access (container)

    YANG Description: The access layer characteristics of this 
interface.
    """
    return self.__access
      
  def _set_access(self, v, load=False):
    """
    Setter method for access, mapped from YANG variable /interface/tengigabitethernet/switchport/access (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_access is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_access() directly.

    YANG Description: The access layer characteristics of this 
interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=access.access, is_container='container', presence=False, yang_name="access", rest_name="access", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as Access', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """access must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=access.access, is_container='container', presence=False, yang_name="access", rest_name="access", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as Access', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__access = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_access(self):
    self.__access = YANGDynClass(base=access.access, is_container='container', presence=False, yang_name="access", rest_name="access", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as Access', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_access_mac_group_vlan_classification(self):
    """
    Getter method for access_mac_group_vlan_classification, mapped from YANG variable /interface/tengigabitethernet/switchport/access_mac_group_vlan_classification (container)
    """
    return self.__access_mac_group_vlan_classification
      
  def _set_access_mac_group_vlan_classification(self, v, load=False):
    """
    Setter method for access_mac_group_vlan_classification, mapped from YANG variable /interface/tengigabitethernet/switchport/access_mac_group_vlan_classification (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_access_mac_group_vlan_classification is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_access_mac_group_vlan_classification() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=access_mac_group_vlan_classification.access_mac_group_vlan_classification, is_container='container', presence=False, yang_name="access-mac-group-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'mac-group-vlan-classification-config-phy'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """access_mac_group_vlan_classification must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=access_mac_group_vlan_classification.access_mac_group_vlan_classification, is_container='container', presence=False, yang_name="access-mac-group-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'mac-group-vlan-classification-config-phy'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__access_mac_group_vlan_classification = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_access_mac_group_vlan_classification(self):
    self.__access_mac_group_vlan_classification = YANGDynClass(base=access_mac_group_vlan_classification.access_mac_group_vlan_classification, is_container='container', presence=False, yang_name="access-mac-group-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'mac-group-vlan-classification-config-phy'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_access_mac_vlan_classification(self):
    """
    Getter method for access_mac_vlan_classification, mapped from YANG variable /interface/tengigabitethernet/switchport/access_mac_vlan_classification (container)
    """
    return self.__access_mac_vlan_classification
      
  def _set_access_mac_vlan_classification(self, v, load=False):
    """
    Setter method for access_mac_vlan_classification, mapped from YANG variable /interface/tengigabitethernet/switchport/access_mac_vlan_classification (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_access_mac_vlan_classification is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_access_mac_vlan_classification() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=access_mac_vlan_classification.access_mac_vlan_classification, is_container='container', presence=False, yang_name="access-mac-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'gvlan-access-port-config-phy'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """access_mac_vlan_classification must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=access_mac_vlan_classification.access_mac_vlan_classification, is_container='container', presence=False, yang_name="access-mac-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'gvlan-access-port-config-phy'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__access_mac_vlan_classification = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_access_mac_vlan_classification(self):
    self.__access_mac_vlan_classification = YANGDynClass(base=access_mac_vlan_classification.access_mac_vlan_classification, is_container='container', presence=False, yang_name="access-mac-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'gvlan-access-port-config-phy'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_trunk_private_vlan_classification(self):
    """
    Getter method for trunk_private_vlan_classification, mapped from YANG variable /interface/tengigabitethernet/switchport/trunk_private_vlan_classification (container)
    """
    return self.__trunk_private_vlan_classification
      
  def _set_trunk_private_vlan_classification(self, v, load=False):
    """
    Setter method for trunk_private_vlan_classification, mapped from YANG variable /interface/tengigabitethernet/switchport/trunk_private_vlan_classification (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trunk_private_vlan_classification is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trunk_private_vlan_classification() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=trunk_private_vlan_classification.trunk_private_vlan_classification, is_container='container', presence=False, yang_name="trunk-private-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'ctag-pvlan-classification-phy-config'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trunk_private_vlan_classification must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=trunk_private_vlan_classification.trunk_private_vlan_classification, is_container='container', presence=False, yang_name="trunk-private-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'ctag-pvlan-classification-phy-config'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__trunk_private_vlan_classification = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trunk_private_vlan_classification(self):
    self.__trunk_private_vlan_classification = YANGDynClass(base=trunk_private_vlan_classification.trunk_private_vlan_classification, is_container='container', presence=False, yang_name="trunk-private-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'callpoint': u'ctag-pvlan-classification-phy-config'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_trunk(self):
    """
    Getter method for trunk, mapped from YANG variable /interface/tengigabitethernet/switchport/trunk (container)

    YANG Description: The trunking characteristics of this interface.
    """
    return self.__trunk
      
  def _set_trunk(self, v, load=False):
    """
    Setter method for trunk, mapped from YANG variable /interface/tengigabitethernet/switchport/trunk (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trunk is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trunk() directly.

    YANG Description: The trunking characteristics of this interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=trunk.trunk, is_container='container', presence=False, yang_name="trunk", rest_name="trunk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as trunk', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trunk must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=trunk.trunk, is_container='container', presence=False, yang_name="trunk", rest_name="trunk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as trunk', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__trunk = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trunk(self):
    self.__trunk = YANGDynClass(base=trunk.trunk, is_container='container', presence=False, yang_name="trunk", rest_name="trunk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the Layer2 interface as trunk', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_private_vlan(self):
    """
    Getter method for private_vlan, mapped from YANG variable /interface/tengigabitethernet/switchport/private_vlan (container)

    YANG Description: Set Private-Vlan Configuration
    """
    return self.__private_vlan
      
  def _set_private_vlan(self, v, load=False):
    """
    Setter method for private_vlan, mapped from YANG variable /interface/tengigabitethernet/switchport/private_vlan (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_private_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_private_vlan() directly.

    YANG Description: Set Private-Vlan Configuration
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=private_vlan.private_vlan, is_container='container', presence=False, yang_name="private-vlan", rest_name="private-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set Private-Vlan Configuration'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """private_vlan must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=private_vlan.private_vlan, is_container='container', presence=False, yang_name="private-vlan", rest_name="private-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set Private-Vlan Configuration'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__private_vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_private_vlan(self):
    self.__private_vlan = YANGDynClass(base=private_vlan.private_vlan, is_container='container', presence=False, yang_name="private-vlan", rest_name="private-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set Private-Vlan Configuration'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_access_mac_rspan_vlan_classification(self):
    """
    Getter method for access_mac_rspan_vlan_classification, mapped from YANG variable /interface/tengigabitethernet/switchport/access_mac_rspan_vlan_classification (container)
    """
    return self.__access_mac_rspan_vlan_classification
      
  def _set_access_mac_rspan_vlan_classification(self, v, load=False):
    """
    Setter method for access_mac_rspan_vlan_classification, mapped from YANG variable /interface/tengigabitethernet/switchport/access_mac_rspan_vlan_classification (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_access_mac_rspan_vlan_classification is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_access_mac_rspan_vlan_classification() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=access_mac_rspan_vlan_classification.access_mac_rspan_vlan_classification, is_container='container', presence=False, yang_name="access-mac-rspan-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """access_mac_rspan_vlan_classification must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=access_mac_rspan_vlan_classification.access_mac_rspan_vlan_classification, is_container='container', presence=False, yang_name="access-mac-rspan-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__access_mac_rspan_vlan_classification = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_access_mac_rspan_vlan_classification(self):
    self.__access_mac_rspan_vlan_classification = YANGDynClass(base=access_mac_rspan_vlan_classification.access_mac_rspan_vlan_classification, is_container='container', presence=False, yang_name="access-mac-rspan-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_access_mac_group_rspan_vlan_classification(self):
    """
    Getter method for access_mac_group_rspan_vlan_classification, mapped from YANG variable /interface/tengigabitethernet/switchport/access_mac_group_rspan_vlan_classification (container)
    """
    return self.__access_mac_group_rspan_vlan_classification
      
  def _set_access_mac_group_rspan_vlan_classification(self, v, load=False):
    """
    Setter method for access_mac_group_rspan_vlan_classification, mapped from YANG variable /interface/tengigabitethernet/switchport/access_mac_group_rspan_vlan_classification (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_access_mac_group_rspan_vlan_classification is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_access_mac_group_rspan_vlan_classification() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=access_mac_group_rspan_vlan_classification.access_mac_group_rspan_vlan_classification, is_container='container', presence=False, yang_name="access-mac-group-rspan-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """access_mac_group_rspan_vlan_classification must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=access_mac_group_rspan_vlan_classification.access_mac_group_rspan_vlan_classification, is_container='container', presence=False, yang_name="access-mac-group-rspan-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__access_mac_group_rspan_vlan_classification = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_access_mac_group_rspan_vlan_classification(self):
    self.__access_mac_group_rspan_vlan_classification = YANGDynClass(base=access_mac_group_rspan_vlan_classification.access_mac_group_rspan_vlan_classification, is_container='container', presence=False, yang_name="access-mac-group-rspan-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)

  mode = __builtin__.property(_get_mode, _set_mode)
  port_security = __builtin__.property(_get_port_security, _set_port_security)
  access = __builtin__.property(_get_access, _set_access)
  access_mac_group_vlan_classification = __builtin__.property(_get_access_mac_group_vlan_classification, _set_access_mac_group_vlan_classification)
  access_mac_vlan_classification = __builtin__.property(_get_access_mac_vlan_classification, _set_access_mac_vlan_classification)
  trunk_private_vlan_classification = __builtin__.property(_get_trunk_private_vlan_classification, _set_trunk_private_vlan_classification)
  trunk = __builtin__.property(_get_trunk, _set_trunk)
  private_vlan = __builtin__.property(_get_private_vlan, _set_private_vlan)
  access_mac_rspan_vlan_classification = __builtin__.property(_get_access_mac_rspan_vlan_classification, _set_access_mac_rspan_vlan_classification)
  access_mac_group_rspan_vlan_classification = __builtin__.property(_get_access_mac_group_rspan_vlan_classification, _set_access_mac_group_rspan_vlan_classification)


  _pyangbind_elements = {'mode': mode, 'port_security': port_security, 'access': access, 'access_mac_group_vlan_classification': access_mac_group_vlan_classification, 'access_mac_vlan_classification': access_mac_vlan_classification, 'trunk_private_vlan_classification': trunk_private_vlan_classification, 'trunk': trunk, 'private_vlan': private_vlan, 'access_mac_rspan_vlan_classification': access_mac_rspan_vlan_classification, 'access_mac_group_rspan_vlan_classification': access_mac_group_rspan_vlan_classification, }


