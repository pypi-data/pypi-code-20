
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import external_lsa
import summary_lsa
import link
import on_startup
class router_lsa(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/ospf/max-metric/router-lsa. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__all_vrfs','__all_lsas','__external_lsa','__summary_lsa','__link','__on_startup',)

  _yang_name = 'router-lsa'
  _rest_name = 'router-lsa'

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
    self.__external_lsa = YANGDynClass(base=external_lsa.external_lsa, is_container='container', presence=True, yang_name="external-lsa", rest_name="external-lsa", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Replace Metric in External LSA with max metric value'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    self.__summary_lsa = YANGDynClass(base=summary_lsa.summary_lsa, is_container='container', presence=True, yang_name="summary-lsa", rest_name="summary-lsa", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Replace Metric in Summary LSA with max metric value'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    self.__all_lsas = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="all-lsas", rest_name="all-lsas", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Replace Metric in all External and Summary\nLSAs with default max metric value'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    self.__link = YANGDynClass(base=link.link, is_container='container', presence=False, yang_name="link", rest_name="link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Router LSA link type', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    self.__all_vrfs = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="all-vrfs", rest_name="all-vrfs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Apply this to all the current OSPF instances'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    self.__on_startup = YANGDynClass(base=on_startup.on_startup, is_container='container', presence=False, yang_name="on-startup", rest_name="on-startup", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Apply this on OSPF startup'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)

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
      return [u'routing-system', u'router', u'ospf', u'max-metric', u'router-lsa']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'ospf', u'max-metric', u'router-lsa']

  def _get_all_vrfs(self):
    """
    Getter method for all_vrfs, mapped from YANG variable /routing_system/router/ospf/max_metric/router_lsa/all_vrfs (empty)
    """
    return self.__all_vrfs
      
  def _set_all_vrfs(self, v, load=False):
    """
    Setter method for all_vrfs, mapped from YANG variable /routing_system/router/ospf/max_metric/router_lsa/all_vrfs (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_all_vrfs is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_all_vrfs() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="all-vrfs", rest_name="all-vrfs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Apply this to all the current OSPF instances'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """all_vrfs must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="all-vrfs", rest_name="all-vrfs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Apply this to all the current OSPF instances'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)""",
        })

    self.__all_vrfs = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_all_vrfs(self):
    self.__all_vrfs = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="all-vrfs", rest_name="all-vrfs", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Apply this to all the current OSPF instances'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)


  def _get_all_lsas(self):
    """
    Getter method for all_lsas, mapped from YANG variable /routing_system/router/ospf/max_metric/router_lsa/all_lsas (empty)
    """
    return self.__all_lsas
      
  def _set_all_lsas(self, v, load=False):
    """
    Setter method for all_lsas, mapped from YANG variable /routing_system/router/ospf/max_metric/router_lsa/all_lsas (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_all_lsas is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_all_lsas() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="all-lsas", rest_name="all-lsas", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Replace Metric in all External and Summary\nLSAs with default max metric value'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """all_lsas must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="all-lsas", rest_name="all-lsas", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Replace Metric in all External and Summary\nLSAs with default max metric value'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)""",
        })

    self.__all_lsas = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_all_lsas(self):
    self.__all_lsas = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="all-lsas", rest_name="all-lsas", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Replace Metric in all External and Summary\nLSAs with default max metric value'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='empty', is_config=True)


  def _get_external_lsa(self):
    """
    Getter method for external_lsa, mapped from YANG variable /routing_system/router/ospf/max_metric/router_lsa/external_lsa (container)
    """
    return self.__external_lsa
      
  def _set_external_lsa(self, v, load=False):
    """
    Setter method for external_lsa, mapped from YANG variable /routing_system/router/ospf/max_metric/router_lsa/external_lsa (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_external_lsa is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_external_lsa() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=external_lsa.external_lsa, is_container='container', presence=True, yang_name="external-lsa", rest_name="external-lsa", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Replace Metric in External LSA with max metric value'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """external_lsa must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=external_lsa.external_lsa, is_container='container', presence=True, yang_name="external-lsa", rest_name="external-lsa", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Replace Metric in External LSA with max metric value'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)""",
        })

    self.__external_lsa = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_external_lsa(self):
    self.__external_lsa = YANGDynClass(base=external_lsa.external_lsa, is_container='container', presence=True, yang_name="external-lsa", rest_name="external-lsa", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Replace Metric in External LSA with max metric value'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)


  def _get_summary_lsa(self):
    """
    Getter method for summary_lsa, mapped from YANG variable /routing_system/router/ospf/max_metric/router_lsa/summary_lsa (container)
    """
    return self.__summary_lsa
      
  def _set_summary_lsa(self, v, load=False):
    """
    Setter method for summary_lsa, mapped from YANG variable /routing_system/router/ospf/max_metric/router_lsa/summary_lsa (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_summary_lsa is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_summary_lsa() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=summary_lsa.summary_lsa, is_container='container', presence=True, yang_name="summary-lsa", rest_name="summary-lsa", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Replace Metric in Summary LSA with max metric value'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """summary_lsa must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=summary_lsa.summary_lsa, is_container='container', presence=True, yang_name="summary-lsa", rest_name="summary-lsa", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Replace Metric in Summary LSA with max metric value'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)""",
        })

    self.__summary_lsa = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_summary_lsa(self):
    self.__summary_lsa = YANGDynClass(base=summary_lsa.summary_lsa, is_container='container', presence=True, yang_name="summary-lsa", rest_name="summary-lsa", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Replace Metric in Summary LSA with max metric value'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)


  def _get_link(self):
    """
    Getter method for link, mapped from YANG variable /routing_system/router/ospf/max_metric/router_lsa/link (container)
    """
    return self.__link
      
  def _set_link(self, v, load=False):
    """
    Setter method for link, mapped from YANG variable /routing_system/router/ospf/max_metric/router_lsa/link (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=link.link, is_container='container', presence=False, yang_name="link", rest_name="link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Router LSA link type', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=link.link, is_container='container', presence=False, yang_name="link", rest_name="link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Router LSA link type', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)""",
        })

    self.__link = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link(self):
    self.__link = YANGDynClass(base=link.link, is_container='container', presence=False, yang_name="link", rest_name="link", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Router LSA link type', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)


  def _get_on_startup(self):
    """
    Getter method for on_startup, mapped from YANG variable /routing_system/router/ospf/max_metric/router_lsa/on_startup (container)
    """
    return self.__on_startup
      
  def _set_on_startup(self, v, load=False):
    """
    Setter method for on_startup, mapped from YANG variable /routing_system/router/ospf/max_metric/router_lsa/on_startup (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_on_startup is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_on_startup() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=on_startup.on_startup, is_container='container', presence=False, yang_name="on-startup", rest_name="on-startup", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Apply this on OSPF startup'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """on_startup must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=on_startup.on_startup, is_container='container', presence=False, yang_name="on-startup", rest_name="on-startup", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Apply this on OSPF startup'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)""",
        })

    self.__on_startup = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_on_startup(self):
    self.__on_startup = YANGDynClass(base=on_startup.on_startup, is_container='container', presence=False, yang_name="on-startup", rest_name="on-startup", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Apply this on OSPF startup'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)

  all_vrfs = __builtin__.property(_get_all_vrfs, _set_all_vrfs)
  all_lsas = __builtin__.property(_get_all_lsas, _set_all_lsas)
  external_lsa = __builtin__.property(_get_external_lsa, _set_external_lsa)
  summary_lsa = __builtin__.property(_get_summary_lsa, _set_summary_lsa)
  link = __builtin__.property(_get_link, _set_link)
  on_startup = __builtin__.property(_get_on_startup, _set_on_startup)


  _pyangbind_elements = {'all_vrfs': all_vrfs, 'all_lsas': all_lsas, 'external_lsa': external_lsa, 'summary_lsa': summary_lsa, 'link': link, 'on_startup': on_startup, }


