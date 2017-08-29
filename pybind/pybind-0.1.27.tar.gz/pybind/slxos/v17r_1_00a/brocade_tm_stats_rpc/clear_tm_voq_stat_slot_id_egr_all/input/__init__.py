
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class input(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-tm-stats - based on the path /brocade_tm_stats_rpc/clear-tm-voq-stat-slot-id-egr-all/input. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__slot_id','__clear_tm_voq_slot_egress_port_all',)

  _yang_name = 'input'
  _rest_name = 'input'

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
    self.__slot_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="slot-id", rest_name="clear-slot-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'clear all voq statistics for selected slot', u'alt-name': u'clear-slot-id'}}, namespace='urn:brocade.com:mgmt:brocade-tm-stats', defining_module='brocade-tm-stats', yang_type='common-def:lc-number-type', is_config=True)
    self.__clear_tm_voq_slot_egress_port_all = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="clear-tm-voq-slot-egress-port-all", rest_name="clear-slot-id-egr-all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'clear all voq statistics for selected slot', u'alt-name': u'clear-slot-id-egr-all'}}, namespace='urn:brocade.com:mgmt:brocade-tm-stats', defining_module='brocade-tm-stats', yang_type='boolean', is_config=True)

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
      return [u'brocade_tm_stats_rpc', u'clear-tm-voq-stat-slot-id-egr-all', u'input']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'clear-tm-voq-stat-slot-id-egr-all', u'input']

  def _get_slot_id(self):
    """
    Getter method for slot_id, mapped from YANG variable /brocade_tm_stats_rpc/clear_tm_voq_stat_slot_id_egr_all/input/slot_id (common-def:lc-number-type)
    """
    return self.__slot_id
      
  def _set_slot_id(self, v, load=False):
    """
    Setter method for slot_id, mapped from YANG variable /brocade_tm_stats_rpc/clear_tm_voq_stat_slot_id_egr_all/input/slot_id (common-def:lc-number-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_slot_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_slot_id() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="slot-id", rest_name="clear-slot-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'clear all voq statistics for selected slot', u'alt-name': u'clear-slot-id'}}, namespace='urn:brocade.com:mgmt:brocade-tm-stats', defining_module='brocade-tm-stats', yang_type='common-def:lc-number-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """slot_id must be of a type compatible with common-def:lc-number-type""",
          'defined-type': "common-def:lc-number-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="slot-id", rest_name="clear-slot-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'clear all voq statistics for selected slot', u'alt-name': u'clear-slot-id'}}, namespace='urn:brocade.com:mgmt:brocade-tm-stats', defining_module='brocade-tm-stats', yang_type='common-def:lc-number-type', is_config=True)""",
        })

    self.__slot_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_slot_id(self):
    self.__slot_id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), restriction_dict={'range': [u'0..65535']}), is_leaf=True, yang_name="slot-id", rest_name="clear-slot-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'clear all voq statistics for selected slot', u'alt-name': u'clear-slot-id'}}, namespace='urn:brocade.com:mgmt:brocade-tm-stats', defining_module='brocade-tm-stats', yang_type='common-def:lc-number-type', is_config=True)


  def _get_clear_tm_voq_slot_egress_port_all(self):
    """
    Getter method for clear_tm_voq_slot_egress_port_all, mapped from YANG variable /brocade_tm_stats_rpc/clear_tm_voq_stat_slot_id_egr_all/input/clear_tm_voq_slot_egress_port_all (boolean)
    """
    return self.__clear_tm_voq_slot_egress_port_all
      
  def _set_clear_tm_voq_slot_egress_port_all(self, v, load=False):
    """
    Setter method for clear_tm_voq_slot_egress_port_all, mapped from YANG variable /brocade_tm_stats_rpc/clear_tm_voq_stat_slot_id_egr_all/input/clear_tm_voq_slot_egress_port_all (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_clear_tm_voq_slot_egress_port_all is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_clear_tm_voq_slot_egress_port_all() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="clear-tm-voq-slot-egress-port-all", rest_name="clear-slot-id-egr-all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'clear all voq statistics for selected slot', u'alt-name': u'clear-slot-id-egr-all'}}, namespace='urn:brocade.com:mgmt:brocade-tm-stats', defining_module='brocade-tm-stats', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """clear_tm_voq_slot_egress_port_all must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="clear-tm-voq-slot-egress-port-all", rest_name="clear-slot-id-egr-all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'clear all voq statistics for selected slot', u'alt-name': u'clear-slot-id-egr-all'}}, namespace='urn:brocade.com:mgmt:brocade-tm-stats', defining_module='brocade-tm-stats', yang_type='boolean', is_config=True)""",
        })

    self.__clear_tm_voq_slot_egress_port_all = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_clear_tm_voq_slot_egress_port_all(self):
    self.__clear_tm_voq_slot_egress_port_all = YANGDynClass(base=YANGBool, default=YANGBool("true"), is_leaf=True, yang_name="clear-tm-voq-slot-egress-port-all", rest_name="clear-slot-id-egr-all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'clear all voq statistics for selected slot', u'alt-name': u'clear-slot-id-egr-all'}}, namespace='urn:brocade.com:mgmt:brocade-tm-stats', defining_module='brocade-tm-stats', yang_type='boolean', is_config=True)

  slot_id = __builtin__.property(_get_slot_id, _set_slot_id)
  clear_tm_voq_slot_egress_port_all = __builtin__.property(_get_clear_tm_voq_slot_egress_port_all, _set_clear_tm_voq_slot_egress_port_all)


  _pyangbind_elements = {'slot_id': slot_id, 'clear_tm_voq_slot_egress_port_all': clear_tm_voq_slot_egress_port_all, }


