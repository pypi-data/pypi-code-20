
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class max_threshold(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /protocol/cfm/y1731/action-profile-name/event/max-threshold. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__max_threshold_actions',)

  _yang_name = 'max-threshold'
  _rest_name = 'max-threshold'

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
    self.__max_threshold_actions = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'interface-down': {'value': 0}, u'all': {'value': 15}, u'event-handler': {'value': 1}},), default=unicode("interface-down"), is_leaf=True, yang_name="max-threshold-actions", rest_name="actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure action(s) for max-threshold event', u'alt-name': u'actions'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='action-profile-bitmap', is_config=True)

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
      return [u'protocol', u'cfm', u'y1731', u'action-profile-name', u'event', u'max-threshold']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'protocol', u'cfm', u'y1731', u'action-profile', u'event', u'max-threshold']

  def _get_max_threshold_actions(self):
    """
    Getter method for max_threshold_actions, mapped from YANG variable /protocol/cfm/y1731/action_profile_name/event/max_threshold/max_threshold_actions (action-profile-bitmap)
    """
    return self.__max_threshold_actions
      
  def _set_max_threshold_actions(self, v, load=False):
    """
    Setter method for max_threshold_actions, mapped from YANG variable /protocol/cfm/y1731/action_profile_name/event/max_threshold/max_threshold_actions (action-profile-bitmap)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_threshold_actions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_threshold_actions() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'interface-down': {'value': 0}, u'all': {'value': 15}, u'event-handler': {'value': 1}},), default=unicode("interface-down"), is_leaf=True, yang_name="max-threshold-actions", rest_name="actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure action(s) for max-threshold event', u'alt-name': u'actions'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='action-profile-bitmap', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_threshold_actions must be of a type compatible with action-profile-bitmap""",
          'defined-type': "brocade-dot1ag:action-profile-bitmap",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'interface-down': {'value': 0}, u'all': {'value': 15}, u'event-handler': {'value': 1}},), default=unicode("interface-down"), is_leaf=True, yang_name="max-threshold-actions", rest_name="actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure action(s) for max-threshold event', u'alt-name': u'actions'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='action-profile-bitmap', is_config=True)""",
        })

    self.__max_threshold_actions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_threshold_actions(self):
    self.__max_threshold_actions = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'interface-down': {'value': 0}, u'all': {'value': 15}, u'event-handler': {'value': 1}},), default=unicode("interface-down"), is_leaf=True, yang_name="max-threshold-actions", rest_name="actions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure action(s) for max-threshold event', u'alt-name': u'actions'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='action-profile-bitmap', is_config=True)

  max_threshold_actions = __builtin__.property(_get_max_threshold_actions, _set_max_threshold_actions)


  _pyangbind_elements = {'max_threshold_actions': max_threshold_actions, }


