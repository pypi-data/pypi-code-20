
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import vlan
import vlanoper
import rspan_vlan
import trunk_rspan_vlan_classification
class allowed(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/hundredgigabitethernet/switchport/trunk/allowed. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Set the VLANs that will Xmit/Rx through the Layer2
interface
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__vlan','__vlanoper','__rspan_vlan','__trunk_rspan_vlan_classification',)

  _yang_name = 'allowed'
  _rest_name = 'allowed'

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
    self.__trunk_rspan_vlan_classification = YANGDynClass(base=trunk_rspan_vlan_classification.trunk_rspan_vlan_classification, is_container='container', presence=False, yang_name="trunk-rspan-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__vlan = YANGDynClass(base=vlan.vlan, is_container='container', presence=False, yang_name="vlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_MODE_SWITCHPORT_VLANOPER_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__rspan_vlan = YANGDynClass(base=rspan_vlan.rspan_vlan, is_container='container', presence=False, yang_name="rspan-vlan", rest_name="rspan-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__vlanoper = YANGDynClass(base=vlanoper.vlanoper, is_container='container', presence=False, yang_name="vlanoper", rest_name="vlanoper", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'hidden': u'netconfonly'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)

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
      return [u'interface', u'hundredgigabitethernet', u'switchport', u'trunk', u'allowed']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'HundredGigabitEthernet', u'switchport', u'trunk', u'allowed']

  def _get_vlan(self):
    """
    Getter method for vlan, mapped from YANG variable /interface/hundredgigabitethernet/switchport/trunk/allowed/vlan (container)
    """
    return self.__vlan
      
  def _set_vlan(self, v, load=False):
    """
    Setter method for vlan, mapped from YANG variable /interface/hundredgigabitethernet/switchport/trunk/allowed/vlan (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=vlan.vlan, is_container='container', presence=False, yang_name="vlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_MODE_SWITCHPORT_VLANOPER_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=vlan.vlan, is_container='container', presence=False, yang_name="vlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_MODE_SWITCHPORT_VLANOPER_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan(self):
    self.__vlan = YANGDynClass(base=vlan.vlan, is_container='container', presence=False, yang_name="vlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'sort-priority': u'RUNNCFG_INTERFACE_LEVEL_MODE_SWITCHPORT_VLANOPER_CONFIG'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_vlanoper(self):
    """
    Getter method for vlanoper, mapped from YANG variable /interface/hundredgigabitethernet/switchport/trunk/allowed/vlanoper (container)

    YANG Description: DEPRECATED
NOS2.1.0 style data model for allowed vlans.
Do not use in edit-config.
    """
    return self.__vlanoper
      
  def _set_vlanoper(self, v, load=False):
    """
    Setter method for vlanoper, mapped from YANG variable /interface/hundredgigabitethernet/switchport/trunk/allowed/vlanoper (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlanoper is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlanoper() directly.

    YANG Description: DEPRECATED
NOS2.1.0 style data model for allowed vlans.
Do not use in edit-config.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=vlanoper.vlanoper, is_container='container', presence=False, yang_name="vlanoper", rest_name="vlanoper", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'hidden': u'netconfonly'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlanoper must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=vlanoper.vlanoper, is_container='container', presence=False, yang_name="vlanoper", rest_name="vlanoper", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'hidden': u'netconfonly'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__vlanoper = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlanoper(self):
    self.__vlanoper = YANGDynClass(base=vlanoper.vlanoper, is_container='container', presence=False, yang_name="vlanoper", rest_name="vlanoper", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'hidden': u'netconfonly'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_rspan_vlan(self):
    """
    Getter method for rspan_vlan, mapped from YANG variable /interface/hundredgigabitethernet/switchport/trunk/allowed/rspan_vlan (container)

    YANG Description: configure a rspan-vlan
    """
    return self.__rspan_vlan
      
  def _set_rspan_vlan(self, v, load=False):
    """
    Setter method for rspan_vlan, mapped from YANG variable /interface/hundredgigabitethernet/switchport/trunk/allowed/rspan_vlan (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rspan_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rspan_vlan() directly.

    YANG Description: configure a rspan-vlan
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=rspan_vlan.rspan_vlan, is_container='container', presence=False, yang_name="rspan-vlan", rest_name="rspan-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rspan_vlan must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=rspan_vlan.rspan_vlan, is_container='container', presence=False, yang_name="rspan-vlan", rest_name="rspan-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__rspan_vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rspan_vlan(self):
    self.__rspan_vlan = YANGDynClass(base=rspan_vlan.rspan_vlan, is_container='container', presence=False, yang_name="rspan-vlan", rest_name="rspan-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)


  def _get_trunk_rspan_vlan_classification(self):
    """
    Getter method for trunk_rspan_vlan_classification, mapped from YANG variable /interface/hundredgigabitethernet/switchport/trunk/allowed/trunk_rspan_vlan_classification (container)
    """
    return self.__trunk_rspan_vlan_classification
      
  def _set_trunk_rspan_vlan_classification(self, v, load=False):
    """
    Setter method for trunk_rspan_vlan_classification, mapped from YANG variable /interface/hundredgigabitethernet/switchport/trunk/allowed/trunk_rspan_vlan_classification (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trunk_rspan_vlan_classification is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trunk_rspan_vlan_classification() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=trunk_rspan_vlan_classification.trunk_rspan_vlan_classification, is_container='container', presence=False, yang_name="trunk-rspan-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trunk_rspan_vlan_classification must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=trunk_rspan_vlan_classification.trunk_rspan_vlan_classification, is_container='container', presence=False, yang_name="trunk-rspan-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__trunk_rspan_vlan_classification = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trunk_rspan_vlan_classification(self):
    self.__trunk_rspan_vlan_classification = YANGDynClass(base=trunk_rspan_vlan_classification.trunk_rspan_vlan_classification, is_container='container', presence=False, yang_name="trunk-rspan-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)

  vlan = __builtin__.property(_get_vlan, _set_vlan)
  vlanoper = __builtin__.property(_get_vlanoper, _set_vlanoper)
  rspan_vlan = __builtin__.property(_get_rspan_vlan, _set_rspan_vlan)
  trunk_rspan_vlan_classification = __builtin__.property(_get_trunk_rspan_vlan_classification, _set_trunk_rspan_vlan_classification)


  _pyangbind_elements = {'vlan': vlan, 'vlanoper': vlanoper, 'rspan_vlan': rspan_vlan, 'trunk_rspan_vlan_classification': trunk_rspan_vlan_classification, }


