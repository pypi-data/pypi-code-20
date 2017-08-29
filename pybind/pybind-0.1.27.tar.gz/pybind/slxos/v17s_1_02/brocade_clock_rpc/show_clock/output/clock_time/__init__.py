
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class clock_time(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-clock - based on the path /brocade_clock_rpc/show-clock/output/clock-time. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__current_time','__timezone',)

  _yang_name = 'clock-time'
  _rest_name = 'clock-time'

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
    self.__current_time = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'}), is_leaf=True, yang_name="current-time", rest_name="current-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-clock', defining_module='brocade-clock', yang_type='ietfyang:date-and-time', is_config=True)
    self.__timezone = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'3 .. 100']}), is_leaf=True, yang_name="timezone", rest_name="timezone", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-clock', defining_module='brocade-clock', yang_type='string', is_config=True)

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
      return [u'brocade_clock_rpc', u'show-clock', u'output', u'clock-time']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-clock', u'output', u'clock-time']

  def _get_current_time(self):
    """
    Getter method for current_time, mapped from YANG variable /brocade_clock_rpc/show_clock/output/clock_time/current_time (ietfyang:date-and-time)

    YANG Description: switch date and time
    """
    return self.__current_time
      
  def _set_current_time(self, v, load=False):
    """
    Setter method for current_time, mapped from YANG variable /brocade_clock_rpc/show_clock/output/clock_time/current_time (ietfyang:date-and-time)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_current_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_current_time() directly.

    YANG Description: switch date and time
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'}), is_leaf=True, yang_name="current-time", rest_name="current-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-clock', defining_module='brocade-clock', yang_type='ietfyang:date-and-time', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """current_time must be of a type compatible with ietfyang:date-and-time""",
          'defined-type': "ietfyang:date-and-time",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'}), is_leaf=True, yang_name="current-time", rest_name="current-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-clock', defining_module='brocade-clock', yang_type='ietfyang:date-and-time', is_config=True)""",
        })

    self.__current_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_current_time(self):
    self.__current_time = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'}), is_leaf=True, yang_name="current-time", rest_name="current-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-clock', defining_module='brocade-clock', yang_type='ietfyang:date-and-time', is_config=True)


  def _get_timezone(self):
    """
    Getter method for timezone, mapped from YANG variable /brocade_clock_rpc/show_clock/output/clock_time/timezone (string)

    YANG Description: region/city or region/state/city
    """
    return self.__timezone
      
  def _set_timezone(self, v, load=False):
    """
    Setter method for timezone, mapped from YANG variable /brocade_clock_rpc/show_clock/output/clock_time/timezone (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_timezone is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_timezone() directly.

    YANG Description: region/city or region/state/city
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'3 .. 100']}), is_leaf=True, yang_name="timezone", rest_name="timezone", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-clock', defining_module='brocade-clock', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """timezone must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'3 .. 100']}), is_leaf=True, yang_name="timezone", rest_name="timezone", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-clock', defining_module='brocade-clock', yang_type='string', is_config=True)""",
        })

    self.__timezone = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_timezone(self):
    self.__timezone = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'3 .. 100']}), is_leaf=True, yang_name="timezone", rest_name="timezone", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-clock', defining_module='brocade-clock', yang_type='string', is_config=True)

  current_time = __builtin__.property(_get_current_time, _set_current_time)
  timezone = __builtin__.property(_get_timezone, _set_timezone)


  _pyangbind_elements = {'current_time': current_time, 'timezone': timezone, }


