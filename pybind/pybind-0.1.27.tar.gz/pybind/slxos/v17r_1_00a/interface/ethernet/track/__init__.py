
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import interface
import remove_
class track(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/ethernet/track. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Track interface
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__track_enable','__min_link','__interface','__remove_',)

  _yang_name = 'track'
  _rest_name = 'track'

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
    self.__interface = YANGDynClass(base=YANGListType("track_interface_type track_interface_name",interface.interface, yang_name="interface", rest_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='track-interface-type track-interface-name', extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-list-no': None, u'cli-suppress-mode': None, u'info': u'Interface or Port-channel to be tracked', u'callpoint': u'track_interface_call_point'}}), is_container='list', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-list-no': None, u'cli-suppress-mode': None, u'info': u'Interface or Port-channel to be tracked', u'callpoint': u'track_interface_call_point'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)
    self.__track_enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="track_enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable tracking interface', u'alt-name': u'enable', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    self.__remove_ = YANGDynClass(base=remove_.remove_, is_container='container', presence=False, yang_name="remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Remove Link State Tracking configuration from this interface', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    self.__min_link = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..24']}), is_leaf=True, yang_name="min-link", rest_name="min-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Min link', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='uint32', is_config=True)

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
      return [u'interface', u'ethernet', u'track']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ethernet', u'track']

  def _get_track_enable(self):
    """
    Getter method for track_enable, mapped from YANG variable /interface/ethernet/track/track_enable (empty)

    YANG Description: Enable tracking interface
    """
    return self.__track_enable
      
  def _set_track_enable(self, v, load=False):
    """
    Setter method for track_enable, mapped from YANG variable /interface/ethernet/track/track_enable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_track_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_track_enable() directly.

    YANG Description: Enable tracking interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="track_enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable tracking interface', u'alt-name': u'enable', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """track_enable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="track_enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable tracking interface', u'alt-name': u'enable', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)""",
        })

    self.__track_enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_track_enable(self):
    self.__track_enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="track_enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable tracking interface', u'alt-name': u'enable', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)


  def _get_min_link(self):
    """
    Getter method for min_link, mapped from YANG variable /interface/ethernet/track/min_link (uint32)

    YANG Description: Min link
    """
    return self.__min_link
      
  def _set_min_link(self, v, load=False):
    """
    Setter method for min_link, mapped from YANG variable /interface/ethernet/track/min_link (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_min_link is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_min_link() directly.

    YANG Description: Min link
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..24']}), is_leaf=True, yang_name="min-link", rest_name="min-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Min link', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """min_link must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..24']}), is_leaf=True, yang_name="min-link", rest_name="min-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Min link', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='uint32', is_config=True)""",
        })

    self.__min_link = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_min_link(self):
    self.__min_link = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..24']}), is_leaf=True, yang_name="min-link", rest_name="min-link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Min link', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='uint32', is_config=True)


  def _get_interface(self):
    """
    Getter method for interface, mapped from YANG variable /interface/ethernet/track/interface (list)

    YANG Description: Interface or Port-channel to be tracked
    """
    return self.__interface
      
  def _set_interface(self, v, load=False):
    """
    Setter method for interface, mapped from YANG variable /interface/ethernet/track/interface (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_interface() directly.

    YANG Description: Interface or Port-channel to be tracked
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("track_interface_type track_interface_name",interface.interface, yang_name="interface", rest_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='track-interface-type track-interface-name', extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-list-no': None, u'cli-suppress-mode': None, u'info': u'Interface or Port-channel to be tracked', u'callpoint': u'track_interface_call_point'}}), is_container='list', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-list-no': None, u'cli-suppress-mode': None, u'info': u'Interface or Port-channel to be tracked', u'callpoint': u'track_interface_call_point'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """interface must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("track_interface_type track_interface_name",interface.interface, yang_name="interface", rest_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='track-interface-type track-interface-name', extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-list-no': None, u'cli-suppress-mode': None, u'info': u'Interface or Port-channel to be tracked', u'callpoint': u'track_interface_call_point'}}), is_container='list', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-list-no': None, u'cli-suppress-mode': None, u'info': u'Interface or Port-channel to be tracked', u'callpoint': u'track_interface_call_point'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)""",
        })

    self.__interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_interface(self):
    self.__interface = YANGDynClass(base=YANGListType("track_interface_type track_interface_name",interface.interface, yang_name="interface", rest_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='track-interface-type track-interface-name', extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-list-no': None, u'cli-suppress-mode': None, u'info': u'Interface or Port-channel to be tracked', u'callpoint': u'track_interface_call_point'}}), is_container='list', yang_name="interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-suppress-list-no': None, u'cli-suppress-mode': None, u'info': u'Interface or Port-channel to be tracked', u'callpoint': u'track_interface_call_point'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='list', is_config=True)


  def _get_remove_(self):
    """
    Getter method for remove_, mapped from YANG variable /interface/ethernet/track/remove (container)

    YANG Description: Remove Link State Tracking configuration from this interface
    """
    return self.__remove_
      
  def _set_remove_(self, v, load=False):
    """
    Setter method for remove_, mapped from YANG variable /interface/ethernet/track/remove (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_remove_ is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_remove_() directly.

    YANG Description: Remove Link State Tracking configuration from this interface
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=remove_.remove_, is_container='container', presence=False, yang_name="remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Remove Link State Tracking configuration from this interface', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """remove_ must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=remove_.remove_, is_container='container', presence=False, yang_name="remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Remove Link State Tracking configuration from this interface', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)""",
        })

    self.__remove_ = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_remove_(self):
    self.__remove_ = YANGDynClass(base=remove_.remove_, is_container='container', presence=False, yang_name="remove", rest_name="remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Remove Link State Tracking configuration from this interface', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='container', is_config=True)

  track_enable = __builtin__.property(_get_track_enable, _set_track_enable)
  min_link = __builtin__.property(_get_min_link, _set_min_link)
  interface = __builtin__.property(_get_interface, _set_interface)
  remove_ = __builtin__.property(_get_remove_, _set_remove_)


  _pyangbind_elements = {'track_enable': track_enable, 'min_link': min_link, 'interface': interface, 'remove_': remove_, }


