
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import fe_access_check
import link_crc_monitoring
import sfm_walk
class sysmon(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-sysmon - based on the path /sysmon. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__fe_access_check','__link_crc_monitoring','__sfm_walk',)

  _yang_name = 'sysmon'
  _rest_name = 'sysmon'

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
    self.__sfm_walk = YANGDynClass(base=sfm_walk.sfm_walk, is_container='container', presence=False, yang_name="sfm-walk", rest_name="sfm-walk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'SFM Walk', u'callpoint': u'sfmWalk', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='container', is_config=True)
    self.__fe_access_check = YANGDynClass(base=fe_access_check.fe_access_check, is_container='container', presence=False, yang_name="fe-access-check", rest_name="fe-access-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Fe Access Check', u'callpoint': u'feAccessCheck', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='container', is_config=True)
    self.__link_crc_monitoring = YANGDynClass(base=link_crc_monitoring.link_crc_monitoring, is_container='container', presence=False, yang_name="link-crc-monitoring", rest_name="link-crc-monitoring", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Link CRC Monitoring', u'callpoint': u'linkCrcMonitoring', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='container', is_config=True)

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
      return [u'sysmon']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'sysmon']

  def _get_fe_access_check(self):
    """
    Getter method for fe_access_check, mapped from YANG variable /sysmon/fe_access_check (container)
    """
    return self.__fe_access_check
      
  def _set_fe_access_check(self, v, load=False):
    """
    Setter method for fe_access_check, mapped from YANG variable /sysmon/fe_access_check (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fe_access_check is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fe_access_check() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=fe_access_check.fe_access_check, is_container='container', presence=False, yang_name="fe-access-check", rest_name="fe-access-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Fe Access Check', u'callpoint': u'feAccessCheck', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fe_access_check must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=fe_access_check.fe_access_check, is_container='container', presence=False, yang_name="fe-access-check", rest_name="fe-access-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Fe Access Check', u'callpoint': u'feAccessCheck', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='container', is_config=True)""",
        })

    self.__fe_access_check = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fe_access_check(self):
    self.__fe_access_check = YANGDynClass(base=fe_access_check.fe_access_check, is_container='container', presence=False, yang_name="fe-access-check", rest_name="fe-access-check", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Fe Access Check', u'callpoint': u'feAccessCheck', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='container', is_config=True)


  def _get_link_crc_monitoring(self):
    """
    Getter method for link_crc_monitoring, mapped from YANG variable /sysmon/link_crc_monitoring (container)
    """
    return self.__link_crc_monitoring
      
  def _set_link_crc_monitoring(self, v, load=False):
    """
    Setter method for link_crc_monitoring, mapped from YANG variable /sysmon/link_crc_monitoring (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link_crc_monitoring is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link_crc_monitoring() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=link_crc_monitoring.link_crc_monitoring, is_container='container', presence=False, yang_name="link-crc-monitoring", rest_name="link-crc-monitoring", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Link CRC Monitoring', u'callpoint': u'linkCrcMonitoring', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link_crc_monitoring must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=link_crc_monitoring.link_crc_monitoring, is_container='container', presence=False, yang_name="link-crc-monitoring", rest_name="link-crc-monitoring", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Link CRC Monitoring', u'callpoint': u'linkCrcMonitoring', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='container', is_config=True)""",
        })

    self.__link_crc_monitoring = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link_crc_monitoring(self):
    self.__link_crc_monitoring = YANGDynClass(base=link_crc_monitoring.link_crc_monitoring, is_container='container', presence=False, yang_name="link-crc-monitoring", rest_name="link-crc-monitoring", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Link CRC Monitoring', u'callpoint': u'linkCrcMonitoring', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='container', is_config=True)


  def _get_sfm_walk(self):
    """
    Getter method for sfm_walk, mapped from YANG variable /sysmon/sfm_walk (container)
    """
    return self.__sfm_walk
      
  def _set_sfm_walk(self, v, load=False):
    """
    Setter method for sfm_walk, mapped from YANG variable /sysmon/sfm_walk (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_sfm_walk is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_sfm_walk() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=sfm_walk.sfm_walk, is_container='container', presence=False, yang_name="sfm-walk", rest_name="sfm-walk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'SFM Walk', u'callpoint': u'sfmWalk', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """sfm_walk must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=sfm_walk.sfm_walk, is_container='container', presence=False, yang_name="sfm-walk", rest_name="sfm-walk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'SFM Walk', u'callpoint': u'sfmWalk', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='container', is_config=True)""",
        })

    self.__sfm_walk = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_sfm_walk(self):
    self.__sfm_walk = YANGDynClass(base=sfm_walk.sfm_walk, is_container='container', presence=False, yang_name="sfm-walk", rest_name="sfm-walk", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'SFM Walk', u'callpoint': u'sfmWalk', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-sysmon', defining_module='brocade-sysmon', yang_type='container', is_config=True)

  fe_access_check = __builtin__.property(_get_fe_access_check, _set_fe_access_check)
  link_crc_monitoring = __builtin__.property(_get_link_crc_monitoring, _set_link_crc_monitoring)
  sfm_walk = __builtin__.property(_get_sfm_walk, _set_sfm_walk)


  _pyangbind_elements = {'fe_access_check': fe_access_check, 'link_crc_monitoring': link_crc_monitoring, 'sfm_walk': sfm_walk, }


