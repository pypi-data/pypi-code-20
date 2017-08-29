
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class apply_exp_traffic_class_map_name(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-mpls - based on the path /qos-mpls/map-apply/apply-exp-traffic-class-map-name. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__map_name_cmd1','__all_zero_map_cmd1','__default_map_cmd1','__All_cmd1',)

  _yang_name = 'apply-exp-traffic-class-map-name'
  _rest_name = 'exp-traffic-class'

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
    self.__default_map_cmd1 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="default-map-cmd1", rest_name="default-map", parent=self, choice=(u'apply-exp-traffic-class', u'ca-default-map-cmd1'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Map EXP value to internal traffic-class and drop-prec based on default map', u'alt-name': u'default-map', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-apply-qos-mpls', defining_module='brocade-apply-qos-mpls', yang_type='empty', is_config=True)
    self.__all_zero_map_cmd1 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="all-zero-map-cmd1", rest_name="all-zero-map", parent=self, choice=(u'apply-exp-traffic-class', u'ca-all-zero-map-cmd1'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Map EXP value to internal traffic-class 0 and drop-prec 0', u'alt-name': u'all-zero-map', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-apply-qos-mpls', defining_module='brocade-apply-qos-mpls', yang_type='empty', is_config=True)
    self.__All_cmd1 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="All-cmd1", rest_name="All", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Apply globally on all interface', u'alt-name': u'All'}}, namespace='urn:brocade.com:mgmt:brocade-apply-qos-mpls', defining_module='brocade-apply-qos-mpls', yang_type='empty', is_config=True)
    self.__map_name_cmd1 = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="map-name-cmd1", rest_name="map-name-cmd1", parent=self, choice=(u'apply-exp-traffic-class', u'ca-map-name-cmd1'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'<MAP NAME>;;Name for the MAP(Max 64)', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-apply-qos-mpls', defining_module='brocade-apply-qos-mpls', yang_type='map-name-type', is_config=True)

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
      return [u'qos-mpls', u'map-apply', u'apply-exp-traffic-class-map-name']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'qos-mpls', u'map-apply', u'exp-traffic-class']

  def _get_map_name_cmd1(self):
    """
    Getter method for map_name_cmd1, mapped from YANG variable /qos_mpls/map_apply/apply_exp_traffic_class_map_name/map_name_cmd1 (map-name-type)
    """
    return self.__map_name_cmd1
      
  def _set_map_name_cmd1(self, v, load=False):
    """
    Setter method for map_name_cmd1, mapped from YANG variable /qos_mpls/map_apply/apply_exp_traffic_class_map_name/map_name_cmd1 (map-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_map_name_cmd1 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_map_name_cmd1() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="map-name-cmd1", rest_name="map-name-cmd1", parent=self, choice=(u'apply-exp-traffic-class', u'ca-map-name-cmd1'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'<MAP NAME>;;Name for the MAP(Max 64)', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-apply-qos-mpls', defining_module='brocade-apply-qos-mpls', yang_type='map-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """map_name_cmd1 must be of a type compatible with map-name-type""",
          'defined-type': "brocade-apply-qos-mpls:map-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="map-name-cmd1", rest_name="map-name-cmd1", parent=self, choice=(u'apply-exp-traffic-class', u'ca-map-name-cmd1'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'<MAP NAME>;;Name for the MAP(Max 64)', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-apply-qos-mpls', defining_module='brocade-apply-qos-mpls', yang_type='map-name-type', is_config=True)""",
        })

    self.__map_name_cmd1 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_map_name_cmd1(self):
    self.__map_name_cmd1 = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9_]{0,63})'}), is_leaf=True, yang_name="map-name-cmd1", rest_name="map-name-cmd1", parent=self, choice=(u'apply-exp-traffic-class', u'ca-map-name-cmd1'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'<MAP NAME>;;Name for the MAP(Max 64)', u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-apply-qos-mpls', defining_module='brocade-apply-qos-mpls', yang_type='map-name-type', is_config=True)


  def _get_all_zero_map_cmd1(self):
    """
    Getter method for all_zero_map_cmd1, mapped from YANG variable /qos_mpls/map_apply/apply_exp_traffic_class_map_name/all_zero_map_cmd1 (empty)
    """
    return self.__all_zero_map_cmd1
      
  def _set_all_zero_map_cmd1(self, v, load=False):
    """
    Setter method for all_zero_map_cmd1, mapped from YANG variable /qos_mpls/map_apply/apply_exp_traffic_class_map_name/all_zero_map_cmd1 (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_all_zero_map_cmd1 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_all_zero_map_cmd1() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="all-zero-map-cmd1", rest_name="all-zero-map", parent=self, choice=(u'apply-exp-traffic-class', u'ca-all-zero-map-cmd1'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Map EXP value to internal traffic-class 0 and drop-prec 0', u'alt-name': u'all-zero-map', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-apply-qos-mpls', defining_module='brocade-apply-qos-mpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """all_zero_map_cmd1 must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="all-zero-map-cmd1", rest_name="all-zero-map", parent=self, choice=(u'apply-exp-traffic-class', u'ca-all-zero-map-cmd1'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Map EXP value to internal traffic-class 0 and drop-prec 0', u'alt-name': u'all-zero-map', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-apply-qos-mpls', defining_module='brocade-apply-qos-mpls', yang_type='empty', is_config=True)""",
        })

    self.__all_zero_map_cmd1 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_all_zero_map_cmd1(self):
    self.__all_zero_map_cmd1 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="all-zero-map-cmd1", rest_name="all-zero-map", parent=self, choice=(u'apply-exp-traffic-class', u'ca-all-zero-map-cmd1'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Map EXP value to internal traffic-class 0 and drop-prec 0', u'alt-name': u'all-zero-map', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-apply-qos-mpls', defining_module='brocade-apply-qos-mpls', yang_type='empty', is_config=True)


  def _get_default_map_cmd1(self):
    """
    Getter method for default_map_cmd1, mapped from YANG variable /qos_mpls/map_apply/apply_exp_traffic_class_map_name/default_map_cmd1 (empty)
    """
    return self.__default_map_cmd1
      
  def _set_default_map_cmd1(self, v, load=False):
    """
    Setter method for default_map_cmd1, mapped from YANG variable /qos_mpls/map_apply/apply_exp_traffic_class_map_name/default_map_cmd1 (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_default_map_cmd1 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_default_map_cmd1() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="default-map-cmd1", rest_name="default-map", parent=self, choice=(u'apply-exp-traffic-class', u'ca-default-map-cmd1'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Map EXP value to internal traffic-class and drop-prec based on default map', u'alt-name': u'default-map', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-apply-qos-mpls', defining_module='brocade-apply-qos-mpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """default_map_cmd1 must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="default-map-cmd1", rest_name="default-map", parent=self, choice=(u'apply-exp-traffic-class', u'ca-default-map-cmd1'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Map EXP value to internal traffic-class and drop-prec based on default map', u'alt-name': u'default-map', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-apply-qos-mpls', defining_module='brocade-apply-qos-mpls', yang_type='empty', is_config=True)""",
        })

    self.__default_map_cmd1 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_default_map_cmd1(self):
    self.__default_map_cmd1 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="default-map-cmd1", rest_name="default-map", parent=self, choice=(u'apply-exp-traffic-class', u'ca-default-map-cmd1'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Map EXP value to internal traffic-class and drop-prec based on default map', u'alt-name': u'default-map', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-apply-qos-mpls', defining_module='brocade-apply-qos-mpls', yang_type='empty', is_config=True)


  def _get_All_cmd1(self):
    """
    Getter method for All_cmd1, mapped from YANG variable /qos_mpls/map_apply/apply_exp_traffic_class_map_name/All_cmd1 (empty)
    """
    return self.__All_cmd1
      
  def _set_All_cmd1(self, v, load=False):
    """
    Setter method for All_cmd1, mapped from YANG variable /qos_mpls/map_apply/apply_exp_traffic_class_map_name/All_cmd1 (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_All_cmd1 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_All_cmd1() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="All-cmd1", rest_name="All", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Apply globally on all interface', u'alt-name': u'All'}}, namespace='urn:brocade.com:mgmt:brocade-apply-qos-mpls', defining_module='brocade-apply-qos-mpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """All_cmd1 must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="All-cmd1", rest_name="All", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Apply globally on all interface', u'alt-name': u'All'}}, namespace='urn:brocade.com:mgmt:brocade-apply-qos-mpls', defining_module='brocade-apply-qos-mpls', yang_type='empty', is_config=True)""",
        })

    self.__All_cmd1 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_All_cmd1(self):
    self.__All_cmd1 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="All-cmd1", rest_name="All", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Apply globally on all interface', u'alt-name': u'All'}}, namespace='urn:brocade.com:mgmt:brocade-apply-qos-mpls', defining_module='brocade-apply-qos-mpls', yang_type='empty', is_config=True)

  map_name_cmd1 = __builtin__.property(_get_map_name_cmd1, _set_map_name_cmd1)
  all_zero_map_cmd1 = __builtin__.property(_get_all_zero_map_cmd1, _set_all_zero_map_cmd1)
  default_map_cmd1 = __builtin__.property(_get_default_map_cmd1, _set_default_map_cmd1)
  All_cmd1 = __builtin__.property(_get_All_cmd1, _set_All_cmd1)

  __choices__ = {u'apply-exp-traffic-class': {u'ca-default-map-cmd1': [u'default_map_cmd1'], u'ca-map-name-cmd1': [u'map_name_cmd1'], u'ca-all-zero-map-cmd1': [u'all_zero_map_cmd1']}}
  _pyangbind_elements = {'map_name_cmd1': map_name_cmd1, 'all_zero_map_cmd1': all_zero_map_cmd1, 'default_map_cmd1': default_map_cmd1, 'All_cmd1': All_cmd1, }


