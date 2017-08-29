
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class edgeport(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/tengigabitethernet/spanning-tree/edgeport. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__edgeportbasic','__bpdu_guard','__bpdu_filter',)

  _yang_name = 'edgeport'
  _rest_name = 'edgeport'

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
    self.__edgeportbasic = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="edgeportbasic", rest_name="edgeportbasic", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Edgeport', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='empty', is_config=True)
    self.__bpdu_filter = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bpdu-filter", rest_name="bpdu-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the portfast bpdu-filter for the port'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='empty', is_config=True)
    self.__bpdu_guard = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bpdu-guard", rest_name="bpdu-guard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Guard the port against reception of BPDUs'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='empty', is_config=True)

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
      return [u'interface', u'tengigabitethernet', u'spanning-tree', u'edgeport']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'TenGigabitEthernet', u'spanning-tree', u'edgeport']

  def _get_edgeportbasic(self):
    """
    Getter method for edgeportbasic, mapped from YANG variable /interface/tengigabitethernet/spanning_tree/edgeport/edgeportbasic (empty)
    """
    return self.__edgeportbasic
      
  def _set_edgeportbasic(self, v, load=False):
    """
    Setter method for edgeportbasic, mapped from YANG variable /interface/tengigabitethernet/spanning_tree/edgeport/edgeportbasic (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_edgeportbasic is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_edgeportbasic() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="edgeportbasic", rest_name="edgeportbasic", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Edgeport', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """edgeportbasic must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="edgeportbasic", rest_name="edgeportbasic", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Edgeport', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='empty', is_config=True)""",
        })

    self.__edgeportbasic = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_edgeportbasic(self):
    self.__edgeportbasic = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="edgeportbasic", rest_name="edgeportbasic", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Edgeport', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='empty', is_config=True)


  def _get_bpdu_guard(self):
    """
    Getter method for bpdu_guard, mapped from YANG variable /interface/tengigabitethernet/spanning_tree/edgeport/bpdu_guard (empty)
    """
    return self.__bpdu_guard
      
  def _set_bpdu_guard(self, v, load=False):
    """
    Setter method for bpdu_guard, mapped from YANG variable /interface/tengigabitethernet/spanning_tree/edgeport/bpdu_guard (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bpdu_guard is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bpdu_guard() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="bpdu-guard", rest_name="bpdu-guard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Guard the port against reception of BPDUs'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bpdu_guard must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bpdu-guard", rest_name="bpdu-guard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Guard the port against reception of BPDUs'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='empty', is_config=True)""",
        })

    self.__bpdu_guard = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bpdu_guard(self):
    self.__bpdu_guard = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bpdu-guard", rest_name="bpdu-guard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Guard the port against reception of BPDUs'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='empty', is_config=True)


  def _get_bpdu_filter(self):
    """
    Getter method for bpdu_filter, mapped from YANG variable /interface/tengigabitethernet/spanning_tree/edgeport/bpdu_filter (empty)
    """
    return self.__bpdu_filter
      
  def _set_bpdu_filter(self, v, load=False):
    """
    Setter method for bpdu_filter, mapped from YANG variable /interface/tengigabitethernet/spanning_tree/edgeport/bpdu_filter (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bpdu_filter is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bpdu_filter() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="bpdu-filter", rest_name="bpdu-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the portfast bpdu-filter for the port'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bpdu_filter must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bpdu-filter", rest_name="bpdu-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the portfast bpdu-filter for the port'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='empty', is_config=True)""",
        })

    self.__bpdu_filter = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bpdu_filter(self):
    self.__bpdu_filter = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="bpdu-filter", rest_name="bpdu-filter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the portfast bpdu-filter for the port'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='empty', is_config=True)

  edgeportbasic = __builtin__.property(_get_edgeportbasic, _set_edgeportbasic)
  bpdu_guard = __builtin__.property(_get_bpdu_guard, _set_bpdu_guard)
  bpdu_filter = __builtin__.property(_get_bpdu_filter, _set_bpdu_filter)


  _pyangbind_elements = {'edgeportbasic': edgeportbasic, 'bpdu_guard': bpdu_guard, 'bpdu_filter': bpdu_filter, }


