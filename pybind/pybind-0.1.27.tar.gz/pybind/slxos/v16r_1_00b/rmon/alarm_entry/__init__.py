
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class alarm_entry(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rmon - based on the path /rmon/alarm-entry. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__alarm_index','__snmp_oid','__alarm_interval','__alarm_sample','__alarm_rising_threshold','__alarm_rising_event_index','__alarm_falling_threshold','__alarm_falling_event_index','__alarm_owner',)

  _yang_name = 'alarm-entry'
  _rest_name = 'alarm'

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
    self.__alarm_sample = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'delta': {'value': 2}, u'absolute': {'value': 1}},), is_leaf=True, yang_name="alarm-sample", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'alt-name': u'type', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='alarm-sample-type', is_config=True)
    self.__alarm_index = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="alarm-index", rest_name="alarm-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='alarm-index-type', is_config=True)
    self.__alarm_rising_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 4294967295']}), is_leaf=True, yang_name="alarm-rising-threshold", rest_name="rising-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Alarm rising threshold', u'alt-name': u'rising-threshold', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='uint32', is_config=True)
    self.__alarm_falling_event_index = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="alarm-falling-event-index", rest_name="event", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event for falling alarm', u'alt-name': u'event'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='alarm-falling-event-index-type', is_config=True)
    self.__alarm_rising_event_index = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="alarm-rising-event-index", rest_name="event", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event for rising alarm', u'alt-name': u'event'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='alarm-rising-event-index-type', is_config=True)
    self.__alarm_falling_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 4294967295']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="alarm-falling-threshold", rest_name="falling-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Alarm falling threshold', u'alt-name': u'falling-threshold', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='uint32', is_config=True)
    self.__alarm_owner = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,14})', 'length': [u'1 .. 15']}), is_leaf=True, yang_name="alarm-owner", rest_name="owner", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Owner identity', u'alt-name': u'owner'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='owner-string', is_config=True)
    self.__snmp_oid = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'min .. 35']}), is_leaf=True, yang_name="snmp-oid", rest_name="snmp-oid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='snmp-oid-type', is_config=True)
    self.__alarm_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 2147483648']}), is_leaf=True, yang_name="alarm-interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Alarm sample interval', u'alt-name': u'interval', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='uint32', is_config=True)

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
      return [u'rmon', u'alarm-entry']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rmon', u'alarm']

  def _get_alarm_index(self):
    """
    Getter method for alarm_index, mapped from YANG variable /rmon/alarm_entry/alarm_index (alarm-index-type)
    """
    return self.__alarm_index
      
  def _set_alarm_index(self, v, load=False):
    """
    Setter method for alarm_index, mapped from YANG variable /rmon/alarm_entry/alarm_index (alarm-index-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_alarm_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_alarm_index() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="alarm-index", rest_name="alarm-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='alarm-index-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """alarm_index must be of a type compatible with alarm-index-type""",
          'defined-type': "brocade-rmon:alarm-index-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="alarm-index", rest_name="alarm-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='alarm-index-type', is_config=True)""",
        })

    self.__alarm_index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_alarm_index(self):
    self.__alarm_index = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="alarm-index", rest_name="alarm-index", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='alarm-index-type', is_config=True)


  def _get_snmp_oid(self):
    """
    Getter method for snmp_oid, mapped from YANG variable /rmon/alarm_entry/snmp_oid (snmp-oid-type)
    """
    return self.__snmp_oid
      
  def _set_snmp_oid(self, v, load=False):
    """
    Setter method for snmp_oid, mapped from YANG variable /rmon/alarm_entry/snmp_oid (snmp-oid-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_snmp_oid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_snmp_oid() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'min .. 35']}), is_leaf=True, yang_name="snmp-oid", rest_name="snmp-oid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='snmp-oid-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """snmp_oid must be of a type compatible with snmp-oid-type""",
          'defined-type': "brocade-rmon:snmp-oid-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'min .. 35']}), is_leaf=True, yang_name="snmp-oid", rest_name="snmp-oid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='snmp-oid-type', is_config=True)""",
        })

    self.__snmp_oid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_snmp_oid(self):
    self.__snmp_oid = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'min .. 35']}), is_leaf=True, yang_name="snmp-oid", rest_name="snmp-oid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='snmp-oid-type', is_config=True)


  def _get_alarm_interval(self):
    """
    Getter method for alarm_interval, mapped from YANG variable /rmon/alarm_entry/alarm_interval (uint32)
    """
    return self.__alarm_interval
      
  def _set_alarm_interval(self, v, load=False):
    """
    Setter method for alarm_interval, mapped from YANG variable /rmon/alarm_entry/alarm_interval (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_alarm_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_alarm_interval() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 2147483648']}), is_leaf=True, yang_name="alarm-interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Alarm sample interval', u'alt-name': u'interval', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """alarm_interval must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 2147483648']}), is_leaf=True, yang_name="alarm-interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Alarm sample interval', u'alt-name': u'interval', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='uint32', is_config=True)""",
        })

    self.__alarm_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_alarm_interval(self):
    self.__alarm_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 2147483648']}), is_leaf=True, yang_name="alarm-interval", rest_name="interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Alarm sample interval', u'alt-name': u'interval', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='uint32', is_config=True)


  def _get_alarm_sample(self):
    """
    Getter method for alarm_sample, mapped from YANG variable /rmon/alarm_entry/alarm_sample (alarm-sample-type)
    """
    return self.__alarm_sample
      
  def _set_alarm_sample(self, v, load=False):
    """
    Setter method for alarm_sample, mapped from YANG variable /rmon/alarm_entry/alarm_sample (alarm-sample-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_alarm_sample is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_alarm_sample() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'delta': {'value': 2}, u'absolute': {'value': 1}},), is_leaf=True, yang_name="alarm-sample", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'alt-name': u'type', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='alarm-sample-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """alarm_sample must be of a type compatible with alarm-sample-type""",
          'defined-type': "brocade-rmon:alarm-sample-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'delta': {'value': 2}, u'absolute': {'value': 1}},), is_leaf=True, yang_name="alarm-sample", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'alt-name': u'type', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='alarm-sample-type', is_config=True)""",
        })

    self.__alarm_sample = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_alarm_sample(self):
    self.__alarm_sample = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'delta': {'value': 2}, u'absolute': {'value': 1}},), is_leaf=True, yang_name="alarm-sample", rest_name="type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'alt-name': u'type', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='alarm-sample-type', is_config=True)


  def _get_alarm_rising_threshold(self):
    """
    Getter method for alarm_rising_threshold, mapped from YANG variable /rmon/alarm_entry/alarm_rising_threshold (uint32)
    """
    return self.__alarm_rising_threshold
      
  def _set_alarm_rising_threshold(self, v, load=False):
    """
    Setter method for alarm_rising_threshold, mapped from YANG variable /rmon/alarm_entry/alarm_rising_threshold (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_alarm_rising_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_alarm_rising_threshold() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 4294967295']}), is_leaf=True, yang_name="alarm-rising-threshold", rest_name="rising-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Alarm rising threshold', u'alt-name': u'rising-threshold', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """alarm_rising_threshold must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 4294967295']}), is_leaf=True, yang_name="alarm-rising-threshold", rest_name="rising-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Alarm rising threshold', u'alt-name': u'rising-threshold', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='uint32', is_config=True)""",
        })

    self.__alarm_rising_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_alarm_rising_threshold(self):
    self.__alarm_rising_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 4294967295']}), is_leaf=True, yang_name="alarm-rising-threshold", rest_name="rising-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Alarm rising threshold', u'alt-name': u'rising-threshold', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='uint32', is_config=True)


  def _get_alarm_rising_event_index(self):
    """
    Getter method for alarm_rising_event_index, mapped from YANG variable /rmon/alarm_entry/alarm_rising_event_index (alarm-rising-event-index-type)
    """
    return self.__alarm_rising_event_index
      
  def _set_alarm_rising_event_index(self, v, load=False):
    """
    Setter method for alarm_rising_event_index, mapped from YANG variable /rmon/alarm_entry/alarm_rising_event_index (alarm-rising-event-index-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_alarm_rising_event_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_alarm_rising_event_index() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="alarm-rising-event-index", rest_name="event", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event for rising alarm', u'alt-name': u'event'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='alarm-rising-event-index-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """alarm_rising_event_index must be of a type compatible with alarm-rising-event-index-type""",
          'defined-type': "brocade-rmon:alarm-rising-event-index-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="alarm-rising-event-index", rest_name="event", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event for rising alarm', u'alt-name': u'event'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='alarm-rising-event-index-type', is_config=True)""",
        })

    self.__alarm_rising_event_index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_alarm_rising_event_index(self):
    self.__alarm_rising_event_index = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="alarm-rising-event-index", rest_name="event", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event for rising alarm', u'alt-name': u'event'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='alarm-rising-event-index-type', is_config=True)


  def _get_alarm_falling_threshold(self):
    """
    Getter method for alarm_falling_threshold, mapped from YANG variable /rmon/alarm_entry/alarm_falling_threshold (uint32)
    """
    return self.__alarm_falling_threshold
      
  def _set_alarm_falling_threshold(self, v, load=False):
    """
    Setter method for alarm_falling_threshold, mapped from YANG variable /rmon/alarm_entry/alarm_falling_threshold (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_alarm_falling_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_alarm_falling_threshold() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 4294967295']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="alarm-falling-threshold", rest_name="falling-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Alarm falling threshold', u'alt-name': u'falling-threshold', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """alarm_falling_threshold must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 4294967295']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="alarm-falling-threshold", rest_name="falling-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Alarm falling threshold', u'alt-name': u'falling-threshold', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='uint32', is_config=True)""",
        })

    self.__alarm_falling_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_alarm_falling_threshold(self):
    self.__alarm_falling_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 4294967295']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="alarm-falling-threshold", rest_name="falling-threshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Alarm falling threshold', u'alt-name': u'falling-threshold', u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='uint32', is_config=True)


  def _get_alarm_falling_event_index(self):
    """
    Getter method for alarm_falling_event_index, mapped from YANG variable /rmon/alarm_entry/alarm_falling_event_index (alarm-falling-event-index-type)
    """
    return self.__alarm_falling_event_index
      
  def _set_alarm_falling_event_index(self, v, load=False):
    """
    Setter method for alarm_falling_event_index, mapped from YANG variable /rmon/alarm_entry/alarm_falling_event_index (alarm-falling-event-index-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_alarm_falling_event_index is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_alarm_falling_event_index() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="alarm-falling-event-index", rest_name="event", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event for falling alarm', u'alt-name': u'event'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='alarm-falling-event-index-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """alarm_falling_event_index must be of a type compatible with alarm-falling-event-index-type""",
          'defined-type': "brocade-rmon:alarm-falling-event-index-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="alarm-falling-event-index", rest_name="event", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event for falling alarm', u'alt-name': u'event'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='alarm-falling-event-index-type', is_config=True)""",
        })

    self.__alarm_falling_event_index = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_alarm_falling_event_index(self):
    self.__alarm_falling_event_index = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), is_leaf=True, yang_name="alarm-falling-event-index", rest_name="event", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Event for falling alarm', u'alt-name': u'event'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='alarm-falling-event-index-type', is_config=True)


  def _get_alarm_owner(self):
    """
    Getter method for alarm_owner, mapped from YANG variable /rmon/alarm_entry/alarm_owner (owner-string)
    """
    return self.__alarm_owner
      
  def _set_alarm_owner(self, v, load=False):
    """
    Setter method for alarm_owner, mapped from YANG variable /rmon/alarm_entry/alarm_owner (owner-string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_alarm_owner is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_alarm_owner() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,14})', 'length': [u'1 .. 15']}), is_leaf=True, yang_name="alarm-owner", rest_name="owner", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Owner identity', u'alt-name': u'owner'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='owner-string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """alarm_owner must be of a type compatible with owner-string""",
          'defined-type': "brocade-rmon:owner-string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,14})', 'length': [u'1 .. 15']}), is_leaf=True, yang_name="alarm-owner", rest_name="owner", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Owner identity', u'alt-name': u'owner'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='owner-string', is_config=True)""",
        })

    self.__alarm_owner = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_alarm_owner(self):
    self.__alarm_owner = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[a-zA-Z]{1}([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,14})', 'length': [u'1 .. 15']}), is_leaf=True, yang_name="alarm-owner", rest_name="owner", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Owner identity', u'alt-name': u'owner'}}, namespace='urn:brocade.com:mgmt:brocade-rmon', defining_module='brocade-rmon', yang_type='owner-string', is_config=True)

  alarm_index = __builtin__.property(_get_alarm_index, _set_alarm_index)
  snmp_oid = __builtin__.property(_get_snmp_oid, _set_snmp_oid)
  alarm_interval = __builtin__.property(_get_alarm_interval, _set_alarm_interval)
  alarm_sample = __builtin__.property(_get_alarm_sample, _set_alarm_sample)
  alarm_rising_threshold = __builtin__.property(_get_alarm_rising_threshold, _set_alarm_rising_threshold)
  alarm_rising_event_index = __builtin__.property(_get_alarm_rising_event_index, _set_alarm_rising_event_index)
  alarm_falling_threshold = __builtin__.property(_get_alarm_falling_threshold, _set_alarm_falling_threshold)
  alarm_falling_event_index = __builtin__.property(_get_alarm_falling_event_index, _set_alarm_falling_event_index)
  alarm_owner = __builtin__.property(_get_alarm_owner, _set_alarm_owner)


  _pyangbind_elements = {'alarm_index': alarm_index, 'snmp_oid': snmp_oid, 'alarm_interval': alarm_interval, 'alarm_sample': alarm_sample, 'alarm_rising_threshold': alarm_rising_threshold, 'alarm_rising_event_index': alarm_rising_event_index, 'alarm_falling_threshold': alarm_falling_threshold, 'alarm_falling_event_index': alarm_falling_event_index, 'alarm_owner': alarm_owner, }


