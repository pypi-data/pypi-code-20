
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class metric_type(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/route-map/content/set/metric-type. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Type of metric for destination routing protocol
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__external','__internal','__type_1','__type_2',)

  _yang_name = 'metric-type'
  _rest_name = 'metric-type'

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
    self.__type_2 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="type-2", rest_name="type-2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'OSPF external type 2 metric', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)
    self.__type_1 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="type-1", rest_name="type-1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'OSPF external type 1 metric', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)
    self.__internal = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="internal", rest_name="internal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IGP internal metric to BGP MED', u'cli-full-command': None, u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)
    self.__external = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="external", rest_name="external", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IS-IS external metric', u'cli-full-command': None, u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)

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
      return [u'routing-system', u'route-map', u'content', u'set', u'metric-type']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'route-map', u'set', u'metric-type']

  def _get_external(self):
    """
    Getter method for external, mapped from YANG variable /routing_system/route_map/content/set/metric_type/external (empty)

    YANG Description: IS-IS external metric
    """
    return self.__external
      
  def _set_external(self, v, load=False):
    """
    Setter method for external, mapped from YANG variable /routing_system/route_map/content/set/metric_type/external (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_external is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_external() directly.

    YANG Description: IS-IS external metric
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="external", rest_name="external", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IS-IS external metric', u'cli-full-command': None, u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """external must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="external", rest_name="external", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IS-IS external metric', u'cli-full-command': None, u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)""",
        })

    self.__external = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_external(self):
    self.__external = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="external", rest_name="external", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IS-IS external metric', u'cli-full-command': None, u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)


  def _get_internal(self):
    """
    Getter method for internal, mapped from YANG variable /routing_system/route_map/content/set/metric_type/internal (empty)

    YANG Description: IGP internal metric to BGP MED
    """
    return self.__internal
      
  def _set_internal(self, v, load=False):
    """
    Setter method for internal, mapped from YANG variable /routing_system/route_map/content/set/metric_type/internal (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_internal is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_internal() directly.

    YANG Description: IGP internal metric to BGP MED
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="internal", rest_name="internal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IGP internal metric to BGP MED', u'cli-full-command': None, u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """internal must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="internal", rest_name="internal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IGP internal metric to BGP MED', u'cli-full-command': None, u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)""",
        })

    self.__internal = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_internal(self):
    self.__internal = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="internal", rest_name="internal", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'IGP internal metric to BGP MED', u'cli-full-command': None, u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)


  def _get_type_1(self):
    """
    Getter method for type_1, mapped from YANG variable /routing_system/route_map/content/set/metric_type/type_1 (empty)

    YANG Description: OSPF external type 1 metric
    """
    return self.__type_1
      
  def _set_type_1(self, v, load=False):
    """
    Setter method for type_1, mapped from YANG variable /routing_system/route_map/content/set/metric_type/type_1 (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type_1 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type_1() directly.

    YANG Description: OSPF external type 1 metric
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="type-1", rest_name="type-1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'OSPF external type 1 metric', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type_1 must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="type-1", rest_name="type-1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'OSPF external type 1 metric', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)""",
        })

    self.__type_1 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type_1(self):
    self.__type_1 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="type-1", rest_name="type-1", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'OSPF external type 1 metric', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)


  def _get_type_2(self):
    """
    Getter method for type_2, mapped from YANG variable /routing_system/route_map/content/set/metric_type/type_2 (empty)

    YANG Description: OSPF external type 2 metric
    """
    return self.__type_2
      
  def _set_type_2(self, v, load=False):
    """
    Setter method for type_2, mapped from YANG variable /routing_system/route_map/content/set/metric_type/type_2 (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_type_2 is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_type_2() directly.

    YANG Description: OSPF external type 2 metric
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="type-2", rest_name="type-2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'OSPF external type 2 metric', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """type_2 must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="type-2", rest_name="type-2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'OSPF external type 2 metric', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)""",
        })

    self.__type_2 = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_type_2(self):
    self.__type_2 = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="type-2", rest_name="type-2", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'OSPF external type 2 metric', u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='empty', is_config=True)

  external = __builtin__.property(_get_external, _set_external)
  internal = __builtin__.property(_get_internal, _set_internal)
  type_1 = __builtin__.property(_get_type_1, _set_type_1)
  type_2 = __builtin__.property(_get_type_2, _set_type_2)


  _pyangbind_elements = {'external': external, 'internal': internal, 'type_1': type_1, 'type_2': type_2, }


