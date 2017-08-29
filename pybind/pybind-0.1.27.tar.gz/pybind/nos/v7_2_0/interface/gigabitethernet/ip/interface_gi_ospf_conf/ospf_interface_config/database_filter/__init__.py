
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class database_filter(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/gigabitethernet/ip/interface-gi-ospf-conf/ospf-interface-config/database-filter. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__all_out','__all_external','__all_summary_external',)

  _yang_name = 'database-filter'
  _rest_name = 'database-filter'

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
    self.__all_external = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'allow-default-out': {'value': 1}, u'allow-default-and-type4-out': {'value': 2}, u'out': {'value': 3}},), is_leaf=True, yang_name="all-external", rest_name="all-external", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Filter all external LSAs'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='database-filter-options', is_config=True)
    self.__all_summary_external = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'allow-default-out': {'value': 1}, u'allow-default-and-type4-out': {'value': 2}, u'out': {'value': 3}},), is_leaf=True, yang_name="all-summary-external", rest_name="all-summary-external", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Filter all summary external LSAs'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='database-filter-options', is_config=True)
    self.__all_out = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="all-out", rest_name="all-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'filter all LSAs'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)

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
      return [u'interface', u'gigabitethernet', u'ip', u'interface-gi-ospf-conf', u'ospf-interface-config', u'database-filter']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'GigabitEthernet', u'ip', u'ospf', u'database-filter']

  def _get_all_out(self):
    """
    Getter method for all_out, mapped from YANG variable /interface/gigabitethernet/ip/interface_gi_ospf_conf/ospf_interface_config/database_filter/all_out (empty)
    """
    return self.__all_out
      
  def _set_all_out(self, v, load=False):
    """
    Setter method for all_out, mapped from YANG variable /interface/gigabitethernet/ip/interface_gi_ospf_conf/ospf_interface_config/database_filter/all_out (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_all_out is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_all_out() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="all-out", rest_name="all-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'filter all LSAs'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """all_out must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="all-out", rest_name="all-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'filter all LSAs'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)""",
        })

    self.__all_out = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_all_out(self):
    self.__all_out = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="all-out", rest_name="all-out", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'filter all LSAs'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)


  def _get_all_external(self):
    """
    Getter method for all_external, mapped from YANG variable /interface/gigabitethernet/ip/interface_gi_ospf_conf/ospf_interface_config/database_filter/all_external (database-filter-options)
    """
    return self.__all_external
      
  def _set_all_external(self, v, load=False):
    """
    Setter method for all_external, mapped from YANG variable /interface/gigabitethernet/ip/interface_gi_ospf_conf/ospf_interface_config/database_filter/all_external (database-filter-options)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_all_external is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_all_external() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'allow-default-out': {'value': 1}, u'allow-default-and-type4-out': {'value': 2}, u'out': {'value': 3}},), is_leaf=True, yang_name="all-external", rest_name="all-external", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Filter all external LSAs'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='database-filter-options', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """all_external must be of a type compatible with database-filter-options""",
          'defined-type': "brocade-ospf:database-filter-options",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'allow-default-out': {'value': 1}, u'allow-default-and-type4-out': {'value': 2}, u'out': {'value': 3}},), is_leaf=True, yang_name="all-external", rest_name="all-external", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Filter all external LSAs'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='database-filter-options', is_config=True)""",
        })

    self.__all_external = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_all_external(self):
    self.__all_external = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'allow-default-out': {'value': 1}, u'allow-default-and-type4-out': {'value': 2}, u'out': {'value': 3}},), is_leaf=True, yang_name="all-external", rest_name="all-external", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Filter all external LSAs'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='database-filter-options', is_config=True)


  def _get_all_summary_external(self):
    """
    Getter method for all_summary_external, mapped from YANG variable /interface/gigabitethernet/ip/interface_gi_ospf_conf/ospf_interface_config/database_filter/all_summary_external (database-filter-options)
    """
    return self.__all_summary_external
      
  def _set_all_summary_external(self, v, load=False):
    """
    Setter method for all_summary_external, mapped from YANG variable /interface/gigabitethernet/ip/interface_gi_ospf_conf/ospf_interface_config/database_filter/all_summary_external (database-filter-options)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_all_summary_external is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_all_summary_external() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'allow-default-out': {'value': 1}, u'allow-default-and-type4-out': {'value': 2}, u'out': {'value': 3}},), is_leaf=True, yang_name="all-summary-external", rest_name="all-summary-external", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Filter all summary external LSAs'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='database-filter-options', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """all_summary_external must be of a type compatible with database-filter-options""",
          'defined-type': "brocade-ospf:database-filter-options",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'allow-default-out': {'value': 1}, u'allow-default-and-type4-out': {'value': 2}, u'out': {'value': 3}},), is_leaf=True, yang_name="all-summary-external", rest_name="all-summary-external", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Filter all summary external LSAs'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='database-filter-options', is_config=True)""",
        })

    self.__all_summary_external = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_all_summary_external(self):
    self.__all_summary_external = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'allow-default-out': {'value': 1}, u'allow-default-and-type4-out': {'value': 2}, u'out': {'value': 3}},), is_leaf=True, yang_name="all-summary-external", rest_name="all-summary-external", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Filter all summary external LSAs'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='database-filter-options', is_config=True)

  all_out = __builtin__.property(_get_all_out, _set_all_out)
  all_external = __builtin__.property(_get_all_external, _set_all_external)
  all_summary_external = __builtin__.property(_get_all_summary_external, _set_all_summary_external)


  _pyangbind_elements = {'all_out': all_out, 'all_external': all_external, 'all_summary_external': all_summary_external, }


