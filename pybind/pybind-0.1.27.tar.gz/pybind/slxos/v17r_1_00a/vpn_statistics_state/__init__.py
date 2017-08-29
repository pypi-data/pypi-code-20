
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import vpn_vrf_statistics
class vpn_statistics_state(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-nsm-operational - based on the path /vpn-statistics-state. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: 
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__vpn_vrf_statistics',)

  _yang_name = 'vpn-statistics-state'
  _rest_name = 'vpn-statistics-state'

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
    self.__vpn_vrf_statistics = YANGDynClass(base=YANGListType("vrf_name",vpn_vrf_statistics.vpn_vrf_statistics, yang_name="vpn-vrf-statistics", rest_name="vpn-vrf-statistics", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vrf-name', extensions={u'tailf-common': {u'callpoint': u'nsm-vpn-vrf-statistics', u'cli-suppress-show-path': None}}), is_container='list', yang_name="vpn-vrf-statistics", rest_name="vpn-vrf-statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-vpn-vrf-statistics', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)

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
      return [u'vpn-statistics-state']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'vpn-statistics-state']

  def _get_vpn_vrf_statistics(self):
    """
    Getter method for vpn_vrf_statistics, mapped from YANG variable /vpn_statistics_state/vpn_vrf_statistics (list)
    """
    return self.__vpn_vrf_statistics
      
  def _set_vpn_vrf_statistics(self, v, load=False):
    """
    Setter method for vpn_vrf_statistics, mapped from YANG variable /vpn_statistics_state/vpn_vrf_statistics (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vpn_vrf_statistics is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vpn_vrf_statistics() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("vrf_name",vpn_vrf_statistics.vpn_vrf_statistics, yang_name="vpn-vrf-statistics", rest_name="vpn-vrf-statistics", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vrf-name', extensions={u'tailf-common': {u'callpoint': u'nsm-vpn-vrf-statistics', u'cli-suppress-show-path': None}}), is_container='list', yang_name="vpn-vrf-statistics", rest_name="vpn-vrf-statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-vpn-vrf-statistics', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vpn_vrf_statistics must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("vrf_name",vpn_vrf_statistics.vpn_vrf_statistics, yang_name="vpn-vrf-statistics", rest_name="vpn-vrf-statistics", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vrf-name', extensions={u'tailf-common': {u'callpoint': u'nsm-vpn-vrf-statistics', u'cli-suppress-show-path': None}}), is_container='list', yang_name="vpn-vrf-statistics", rest_name="vpn-vrf-statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-vpn-vrf-statistics', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)""",
        })

    self.__vpn_vrf_statistics = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vpn_vrf_statistics(self):
    self.__vpn_vrf_statistics = YANGDynClass(base=YANGListType("vrf_name",vpn_vrf_statistics.vpn_vrf_statistics, yang_name="vpn-vrf-statistics", rest_name="vpn-vrf-statistics", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='vrf-name', extensions={u'tailf-common': {u'callpoint': u'nsm-vpn-vrf-statistics', u'cli-suppress-show-path': None}}), is_container='list', yang_name="vpn-vrf-statistics", rest_name="vpn-vrf-statistics", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'nsm-vpn-vrf-statistics', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-nsm-operational', defining_module='brocade-nsm-operational', yang_type='list', is_config=False)

  vpn_vrf_statistics = __builtin__.property(_get_vpn_vrf_statistics)


  _pyangbind_elements = {'vpn_vrf_statistics': vpn_vrf_statistics, }


