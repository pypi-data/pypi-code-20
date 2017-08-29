
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class link(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/ospf/max-metric/router-lsa/link. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__all','__ptp','__stub','__transit',)

  _yang_name = 'link'
  _rest_name = 'link'

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
    self.__stub = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="stub", rest_name="stub", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise maximum metric in Router LSA for stub links'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    self.__all = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise maximum metric in Router LSA for ptp,stub and transit links'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    self.__transit = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="transit", rest_name="transit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise maximum metric in Router LSA for transit links'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    self.__ptp = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ptp", rest_name="ptp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise maximum metric in Router LSA for ptp links'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)

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
      return [u'rbridge-id', u'router', u'ospf', u'max-metric', u'router-lsa', u'link']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'ospf', u'max-metric', u'router-lsa', u'link']

  def _get_all(self):
    """
    Getter method for all, mapped from YANG variable /rbridge_id/router/ospf/max_metric/router_lsa/link/all (empty)
    """
    return self.__all
      
  def _set_all(self, v, load=False):
    """
    Setter method for all, mapped from YANG variable /rbridge_id/router/ospf/max_metric/router_lsa/link/all (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_all is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_all() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise maximum metric in Router LSA for ptp,stub and transit links'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """all must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise maximum metric in Router LSA for ptp,stub and transit links'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)""",
        })

    self.__all = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_all(self):
    self.__all = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise maximum metric in Router LSA for ptp,stub and transit links'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)


  def _get_ptp(self):
    """
    Getter method for ptp, mapped from YANG variable /rbridge_id/router/ospf/max_metric/router_lsa/link/ptp (empty)
    """
    return self.__ptp
      
  def _set_ptp(self, v, load=False):
    """
    Setter method for ptp, mapped from YANG variable /rbridge_id/router/ospf/max_metric/router_lsa/link/ptp (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ptp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ptp() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ptp", rest_name="ptp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise maximum metric in Router LSA for ptp links'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ptp must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ptp", rest_name="ptp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise maximum metric in Router LSA for ptp links'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)""",
        })

    self.__ptp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ptp(self):
    self.__ptp = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ptp", rest_name="ptp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise maximum metric in Router LSA for ptp links'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)


  def _get_stub(self):
    """
    Getter method for stub, mapped from YANG variable /rbridge_id/router/ospf/max_metric/router_lsa/link/stub (empty)
    """
    return self.__stub
      
  def _set_stub(self, v, load=False):
    """
    Setter method for stub, mapped from YANG variable /rbridge_id/router/ospf/max_metric/router_lsa/link/stub (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_stub is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_stub() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="stub", rest_name="stub", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise maximum metric in Router LSA for stub links'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """stub must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="stub", rest_name="stub", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise maximum metric in Router LSA for stub links'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)""",
        })

    self.__stub = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_stub(self):
    self.__stub = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="stub", rest_name="stub", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise maximum metric in Router LSA for stub links'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)


  def _get_transit(self):
    """
    Getter method for transit, mapped from YANG variable /rbridge_id/router/ospf/max_metric/router_lsa/link/transit (empty)
    """
    return self.__transit
      
  def _set_transit(self, v, load=False):
    """
    Setter method for transit, mapped from YANG variable /rbridge_id/router/ospf/max_metric/router_lsa/link/transit (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_transit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_transit() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="transit", rest_name="transit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise maximum metric in Router LSA for transit links'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """transit must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="transit", rest_name="transit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise maximum metric in Router LSA for transit links'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)""",
        })

    self.__transit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_transit(self):
    self.__transit = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="transit", rest_name="transit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Advertise maximum metric in Router LSA for transit links'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)

  all = __builtin__.property(_get_all, _set_all)
  ptp = __builtin__.property(_get_ptp, _set_ptp)
  stub = __builtin__.property(_get_stub, _set_stub)
  transit = __builtin__.property(_get_transit, _set_transit)


  _pyangbind_elements = {'all': all, 'ptp': ptp, 'stub': stub, 'transit': transit, }


