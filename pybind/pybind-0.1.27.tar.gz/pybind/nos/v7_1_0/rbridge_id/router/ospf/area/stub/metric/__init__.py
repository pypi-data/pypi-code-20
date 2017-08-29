
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class metric(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/ospf/area/stub/metric. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__stub_value','__no_summary',)

  _yang_name = 'metric'
  _rest_name = ''

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
    self.__stub_value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="stub-value", rest_name="stub-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u"Stub's advertised external route metric.", u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='big-metric', is_config=True)
    self.__no_summary = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="no-summary", rest_name="no-summary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Do not send summary LSA into stub area'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)

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
      return [u'rbridge-id', u'router', u'ospf', u'area', u'stub', u'metric']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'ospf', u'area', u'stub']

  def _get_stub_value(self):
    """
    Getter method for stub_value, mapped from YANG variable /rbridge_id/router/ospf/area/stub/metric/stub_value (big-metric)
    """
    return self.__stub_value
      
  def _set_stub_value(self, v, load=False):
    """
    Setter method for stub_value, mapped from YANG variable /rbridge_id/router/ospf/area/stub/metric/stub_value (big-metric)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_stub_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_stub_value() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="stub-value", rest_name="stub-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u"Stub's advertised external route metric.", u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='big-metric', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """stub_value must be of a type compatible with big-metric""",
          'defined-type': "brocade-ospf:big-metric",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="stub-value", rest_name="stub-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u"Stub's advertised external route metric.", u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='big-metric', is_config=True)""",
        })

    self.__stub_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_stub_value(self):
    self.__stub_value = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="stub-value", rest_name="stub-value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u"Stub's advertised external route metric.", u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='big-metric', is_config=True)


  def _get_no_summary(self):
    """
    Getter method for no_summary, mapped from YANG variable /rbridge_id/router/ospf/area/stub/metric/no_summary (empty)
    """
    return self.__no_summary
      
  def _set_no_summary(self, v, load=False):
    """
    Setter method for no_summary, mapped from YANG variable /rbridge_id/router/ospf/area/stub/metric/no_summary (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_no_summary is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_no_summary() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="no-summary", rest_name="no-summary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Do not send summary LSA into stub area'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """no_summary must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="no-summary", rest_name="no-summary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Do not send summary LSA into stub area'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)""",
        })

    self.__no_summary = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_no_summary(self):
    self.__no_summary = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="no-summary", rest_name="no-summary", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Do not send summary LSA into stub area'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)

  stub_value = __builtin__.property(_get_stub_value, _set_stub_value)
  no_summary = __builtin__.property(_get_no_summary, _set_no_summary)


  _pyangbind_elements = {'stub_value': stub_value, 'no_summary': no_summary, }


