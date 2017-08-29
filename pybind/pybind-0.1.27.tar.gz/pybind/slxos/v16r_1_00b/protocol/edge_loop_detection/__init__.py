
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import mac_refresh_time_config
class edge_loop_detection(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /protocol/edge-loop-detection. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__pdu_rx_limit','__hello_interval','__shutdown_time','__mac_refresh_time_config',)

  _yang_name = 'edge-loop-detection'
  _rest_name = 'edge-loop-detection'

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
    self.__mac_refresh_time_config = YANGDynClass(base=mac_refresh_time_config.mac_refresh_time_config, is_container='container', presence=False, yang_name="mac-refresh-time-config", rest_name="mac-refresh", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Refresh-time for MAC', u'cli-sequence-commands': None, u'alt-name': u'mac-refresh', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='container', is_config=True)
    self.__hello_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..5000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="hello-interval", rest_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sets hello-interval-limit'}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='uint32', is_config=True)
    self.__pdu_rx_limit = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..5']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="pdu-rx-limit", rest_name="pdu-rx-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sets bpdu-rx-limit'}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='uint32', is_config=True)
    self.__shutdown_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..1440']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="shutdown-time", rest_name="shutdown-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sets shutdown-time-limit'}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='uint32', is_config=True)

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
      return [u'protocol', u'edge-loop-detection']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'protocol', u'edge-loop-detection']

  def _get_pdu_rx_limit(self):
    """
    Getter method for pdu_rx_limit, mapped from YANG variable /protocol/edge_loop_detection/pdu_rx_limit (uint32)
    """
    return self.__pdu_rx_limit
      
  def _set_pdu_rx_limit(self, v, load=False):
    """
    Setter method for pdu_rx_limit, mapped from YANG variable /protocol/edge_loop_detection/pdu_rx_limit (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pdu_rx_limit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pdu_rx_limit() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..5']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="pdu-rx-limit", rest_name="pdu-rx-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sets bpdu-rx-limit'}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pdu_rx_limit must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..5']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="pdu-rx-limit", rest_name="pdu-rx-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sets bpdu-rx-limit'}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='uint32', is_config=True)""",
        })

    self.__pdu_rx_limit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pdu_rx_limit(self):
    self.__pdu_rx_limit = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..5']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1), is_leaf=True, yang_name="pdu-rx-limit", rest_name="pdu-rx-limit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sets bpdu-rx-limit'}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='uint32', is_config=True)


  def _get_hello_interval(self):
    """
    Getter method for hello_interval, mapped from YANG variable /protocol/edge_loop_detection/hello_interval (uint32)
    """
    return self.__hello_interval
      
  def _set_hello_interval(self, v, load=False):
    """
    Setter method for hello_interval, mapped from YANG variable /protocol/edge_loop_detection/hello_interval (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hello_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hello_interval() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..5000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="hello-interval", rest_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sets hello-interval-limit'}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hello_interval must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..5000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="hello-interval", rest_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sets hello-interval-limit'}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='uint32', is_config=True)""",
        })

    self.__hello_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hello_interval(self):
    self.__hello_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'100..5000']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(1000), is_leaf=True, yang_name="hello-interval", rest_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sets hello-interval-limit'}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='uint32', is_config=True)


  def _get_shutdown_time(self):
    """
    Getter method for shutdown_time, mapped from YANG variable /protocol/edge_loop_detection/shutdown_time (uint32)
    """
    return self.__shutdown_time
      
  def _set_shutdown_time(self, v, load=False):
    """
    Setter method for shutdown_time, mapped from YANG variable /protocol/edge_loop_detection/shutdown_time (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_shutdown_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_shutdown_time() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..1440']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="shutdown-time", rest_name="shutdown-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sets shutdown-time-limit'}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """shutdown_time must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..1440']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="shutdown-time", rest_name="shutdown-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sets shutdown-time-limit'}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='uint32', is_config=True)""",
        })

    self.__shutdown_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_shutdown_time(self):
    self.__shutdown_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..1440']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(0), is_leaf=True, yang_name="shutdown-time", rest_name="shutdown-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Sets shutdown-time-limit'}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='uint32', is_config=True)


  def _get_mac_refresh_time_config(self):
    """
    Getter method for mac_refresh_time_config, mapped from YANG variable /protocol/edge_loop_detection/mac_refresh_time_config (container)
    """
    return self.__mac_refresh_time_config
      
  def _set_mac_refresh_time_config(self, v, load=False):
    """
    Setter method for mac_refresh_time_config, mapped from YANG variable /protocol/edge_loop_detection/mac_refresh_time_config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mac_refresh_time_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mac_refresh_time_config() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=mac_refresh_time_config.mac_refresh_time_config, is_container='container', presence=False, yang_name="mac-refresh-time-config", rest_name="mac-refresh", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Refresh-time for MAC', u'cli-sequence-commands': None, u'alt-name': u'mac-refresh', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mac_refresh_time_config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=mac_refresh_time_config.mac_refresh_time_config, is_container='container', presence=False, yang_name="mac-refresh-time-config", rest_name="mac-refresh", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Refresh-time for MAC', u'cli-sequence-commands': None, u'alt-name': u'mac-refresh', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='container', is_config=True)""",
        })

    self.__mac_refresh_time_config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mac_refresh_time_config(self):
    self.__mac_refresh_time_config = YANGDynClass(base=mac_refresh_time_config.mac_refresh_time_config, is_container='container', presence=False, yang_name="mac-refresh-time-config", rest_name="mac-refresh", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Refresh-time for MAC', u'cli-sequence-commands': None, u'alt-name': u'mac-refresh', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='container', is_config=True)

  pdu_rx_limit = __builtin__.property(_get_pdu_rx_limit, _set_pdu_rx_limit)
  hello_interval = __builtin__.property(_get_hello_interval, _set_hello_interval)
  shutdown_time = __builtin__.property(_get_shutdown_time, _set_shutdown_time)
  mac_refresh_time_config = __builtin__.property(_get_mac_refresh_time_config, _set_mac_refresh_time_config)


  _pyangbind_elements = {'pdu_rx_limit': pdu_rx_limit, 'hello_interval': hello_interval, 'shutdown_time': shutdown_time, 'mac_refresh_time_config': mac_refresh_time_config, }


