
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import allowed
import trunk_vlan_classification
import native_vlan_classification
class trunk(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-port-profile - based on the path /port-profile/vlan-profile/switchport/trunk. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This specifies that Layer2 interface in
trunking mode.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__allowed','__trunk_vlan_classification','__native_vlan_classification','__native_vlan',)

  _yang_name = 'trunk'
  _rest_name = 'trunk'

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
    self.__native_vlan_classification = YANGDynClass(base=native_vlan_classification.native_vlan_classification, is_container='container', presence=False, yang_name="native-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'callpoint': u'native_vlan_on_port_profile_conf'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    self.__native_vlan = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4090']}), is_leaf=True, yang_name="native-vlan", rest_name="native-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the native VLAN to classify\nuntagged traffic.', u'callpoint': u'native_vlan_on_port_profile_conf'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='uint32', is_config=True)
    self.__trunk_vlan_classification = YANGDynClass(base=trunk_vlan_classification.trunk_vlan_classification, is_container='container', presence=False, yang_name="trunk-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    self.__allowed = YANGDynClass(base=allowed.allowed, is_container='container', presence=False, yang_name="allowed", rest_name="allowed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the VLANs that will Xmit/Rx through the Layer2\ninterface', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)

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
      return [u'port-profile', u'vlan-profile', u'switchport', u'trunk']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'port-profile', u'vlan-profile', u'switchport', u'trunk']

  def _get_allowed(self):
    """
    Getter method for allowed, mapped from YANG variable /port_profile/vlan_profile/switchport/trunk/allowed (container)

    YANG Description: A set of Vlan related configuration elements.
    """
    return self.__allowed
      
  def _set_allowed(self, v, load=False):
    """
    Setter method for allowed, mapped from YANG variable /port_profile/vlan_profile/switchport/trunk/allowed (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_allowed is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_allowed() directly.

    YANG Description: A set of Vlan related configuration elements.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=allowed.allowed, is_container='container', presence=False, yang_name="allowed", rest_name="allowed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the VLANs that will Xmit/Rx through the Layer2\ninterface', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """allowed must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=allowed.allowed, is_container='container', presence=False, yang_name="allowed", rest_name="allowed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the VLANs that will Xmit/Rx through the Layer2\ninterface', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)""",
        })

    self.__allowed = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_allowed(self):
    self.__allowed = YANGDynClass(base=allowed.allowed, is_container='container', presence=False, yang_name="allowed", rest_name="allowed", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set the VLANs that will Xmit/Rx through the Layer2\ninterface', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)


  def _get_trunk_vlan_classification(self):
    """
    Getter method for trunk_vlan_classification, mapped from YANG variable /port_profile/vlan_profile/switchport/trunk/trunk_vlan_classification (container)
    """
    return self.__trunk_vlan_classification
      
  def _set_trunk_vlan_classification(self, v, load=False):
    """
    Setter method for trunk_vlan_classification, mapped from YANG variable /port_profile/vlan_profile/switchport/trunk/trunk_vlan_classification (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_trunk_vlan_classification is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_trunk_vlan_classification() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=trunk_vlan_classification.trunk_vlan_classification, is_container='container', presence=False, yang_name="trunk-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """trunk_vlan_classification must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=trunk_vlan_classification.trunk_vlan_classification, is_container='container', presence=False, yang_name="trunk-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)""",
        })

    self.__trunk_vlan_classification = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_trunk_vlan_classification(self):
    self.__trunk_vlan_classification = YANGDynClass(base=trunk_vlan_classification.trunk_vlan_classification, is_container='container', presence=False, yang_name="trunk-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)


  def _get_native_vlan_classification(self):
    """
    Getter method for native_vlan_classification, mapped from YANG variable /port_profile/vlan_profile/switchport/trunk/native_vlan_classification (container)
    """
    return self.__native_vlan_classification
      
  def _set_native_vlan_classification(self, v, load=False):
    """
    Setter method for native_vlan_classification, mapped from YANG variable /port_profile/vlan_profile/switchport/trunk/native_vlan_classification (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_native_vlan_classification is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_native_vlan_classification() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=native_vlan_classification.native_vlan_classification, is_container='container', presence=False, yang_name="native-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'callpoint': u'native_vlan_on_port_profile_conf'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """native_vlan_classification must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=native_vlan_classification.native_vlan_classification, is_container='container', presence=False, yang_name="native-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'callpoint': u'native_vlan_on_port_profile_conf'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)""",
        })

    self.__native_vlan_classification = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_native_vlan_classification(self):
    self.__native_vlan_classification = YANGDynClass(base=native_vlan_classification.native_vlan_classification, is_container='container', presence=False, yang_name="native-vlan-classification", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'callpoint': u'native_vlan_on_port_profile_conf'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)


  def _get_native_vlan(self):
    """
    Getter method for native_vlan, mapped from YANG variable /port_profile/vlan_profile/switchport/trunk/native_vlan (uint32)

    YANG Description: This specifies the native VLAN characteristics
of the Layer2 trunk interface for classifying
untagged traffic.
    """
    return self.__native_vlan
      
  def _set_native_vlan(self, v, load=False):
    """
    Setter method for native_vlan, mapped from YANG variable /port_profile/vlan_profile/switchport/trunk/native_vlan (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_native_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_native_vlan() directly.

    YANG Description: This specifies the native VLAN characteristics
of the Layer2 trunk interface for classifying
untagged traffic.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4090']}), is_leaf=True, yang_name="native-vlan", rest_name="native-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the native VLAN to classify\nuntagged traffic.', u'callpoint': u'native_vlan_on_port_profile_conf'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """native_vlan must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4090']}), is_leaf=True, yang_name="native-vlan", rest_name="native-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the native VLAN to classify\nuntagged traffic.', u'callpoint': u'native_vlan_on_port_profile_conf'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='uint32', is_config=True)""",
        })

    self.__native_vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_native_vlan(self):
    self.__native_vlan = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..4090']}), is_leaf=True, yang_name="native-vlan", rest_name="native-vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the native VLAN to classify\nuntagged traffic.', u'callpoint': u'native_vlan_on_port_profile_conf'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='uint32', is_config=True)

  allowed = __builtin__.property(_get_allowed, _set_allowed)
  trunk_vlan_classification = __builtin__.property(_get_trunk_vlan_classification, _set_trunk_vlan_classification)
  native_vlan_classification = __builtin__.property(_get_native_vlan_classification, _set_native_vlan_classification)
  native_vlan = __builtin__.property(_get_native_vlan, _set_native_vlan)


  _pyangbind_elements = {'allowed': allowed, 'trunk_vlan_classification': trunk_vlan_classification, 'native_vlan_classification': native_vlan_classification, 'native_vlan': native_vlan, }


