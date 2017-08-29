
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class link_interval_properties(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/interface/ve/ipv6/interface-ospfv3-conf/link-interval-properties. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__hello_interval','__dead_interval','__hello_jitter','__retransmit_interval','__transmit_delay',)

  _yang_name = 'link-interval-properties'
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
    self.__transmit_delay = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..3600']}), is_leaf=True, yang_name="transmit-delay", rest_name="transmit-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Link state transmit delay'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)
    self.__retransmit_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3600']}), is_leaf=True, yang_name="retransmit-interval", rest_name="retransmit-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Time between retransmitting lost link state advertisements.'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)
    self.__dead_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..65535']}), is_leaf=True, yang_name="dead-interval", rest_name="dead-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Interval after which a neighbor is declared dead'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)
    self.__hello_jitter = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..50']}), is_leaf=True, yang_name="hello-jitter", rest_name="hello-jitter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Allowed jitter between HELLO packets'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='uint32', is_config=True)
    self.__hello_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="hello-interval", rest_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Time between HELLO packets'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)

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
      return [u'rbridge-id', u'interface', u've', u'ipv6', u'interface-ospfv3-conf', u'link-interval-properties']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'interface', u'Ve', u'ipv6', u'ospf']

  def _get_hello_interval(self):
    """
    Getter method for hello_interval, mapped from YANG variable /rbridge_id/interface/ve/ipv6/interface_ospfv3_conf/link_interval_properties/hello_interval (common-def:time-interval-sec)

    YANG Description: Time interval in seconds between HELLO packets
    """
    return self.__hello_interval
      
  def _set_hello_interval(self, v, load=False):
    """
    Setter method for hello_interval, mapped from YANG variable /rbridge_id/interface/ve/ipv6/interface_ospfv3_conf/link_interval_properties/hello_interval (common-def:time-interval-sec)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hello_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hello_interval() directly.

    YANG Description: Time interval in seconds between HELLO packets
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="hello-interval", rest_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Time between HELLO packets'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hello_interval must be of a type compatible with common-def:time-interval-sec""",
          'defined-type': "common-def:time-interval-sec",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="hello-interval", rest_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Time between HELLO packets'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)""",
        })

    self.__hello_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hello_interval(self):
    self.__hello_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..65535']}), is_leaf=True, yang_name="hello-interval", rest_name="hello-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Time between HELLO packets'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)


  def _get_dead_interval(self):
    """
    Getter method for dead_interval, mapped from YANG variable /rbridge_id/interface/ve/ipv6/interface_ospfv3_conf/link_interval_properties/dead_interval (common-def:time-interval-sec)

    YANG Description: Indicates the number of seconds that a neighbor router waits for a hello packetfrom the device before declaring the router down.
    """
    return self.__dead_interval
      
  def _set_dead_interval(self, v, load=False):
    """
    Setter method for dead_interval, mapped from YANG variable /rbridge_id/interface/ve/ipv6/interface_ospfv3_conf/link_interval_properties/dead_interval (common-def:time-interval-sec)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_dead_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_dead_interval() directly.

    YANG Description: Indicates the number of seconds that a neighbor router waits for a hello packetfrom the device before declaring the router down.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..65535']}), is_leaf=True, yang_name="dead-interval", rest_name="dead-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Interval after which a neighbor is declared dead'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """dead_interval must be of a type compatible with common-def:time-interval-sec""",
          'defined-type': "common-def:time-interval-sec",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..65535']}), is_leaf=True, yang_name="dead-interval", rest_name="dead-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Interval after which a neighbor is declared dead'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)""",
        })

    self.__dead_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_dead_interval(self):
    self.__dead_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..65535']}), is_leaf=True, yang_name="dead-interval", rest_name="dead-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Interval after which a neighbor is declared dead'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)


  def _get_hello_jitter(self):
    """
    Getter method for hello_jitter, mapped from YANG variable /rbridge_id/interface/ve/ipv6/interface_ospfv3_conf/link_interval_properties/hello_jitter (uint32)

    YANG Description: Allowed jitter between HELLO packets
    """
    return self.__hello_jitter
      
  def _set_hello_jitter(self, v, load=False):
    """
    Setter method for hello_jitter, mapped from YANG variable /rbridge_id/interface/ve/ipv6/interface_ospfv3_conf/link_interval_properties/hello_jitter (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hello_jitter is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hello_jitter() directly.

    YANG Description: Allowed jitter between HELLO packets
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..50']}), is_leaf=True, yang_name="hello-jitter", rest_name="hello-jitter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Allowed jitter between HELLO packets'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hello_jitter must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..50']}), is_leaf=True, yang_name="hello-jitter", rest_name="hello-jitter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Allowed jitter between HELLO packets'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='uint32', is_config=True)""",
        })

    self.__hello_jitter = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hello_jitter(self):
    self.__hello_jitter = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..50']}), is_leaf=True, yang_name="hello-jitter", rest_name="hello-jitter", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Allowed jitter between HELLO packets'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='uint32', is_config=True)


  def _get_retransmit_interval(self):
    """
    Getter method for retransmit_interval, mapped from YANG variable /rbridge_id/interface/ve/ipv6/interface_ospfv3_conf/link_interval_properties/retransmit_interval (common-def:time-interval-sec)

    YANG Description: The time between retransmissions of LSAs to adjacent routers for an interface.The value can be from 1-3600 seconds. The default is 5 seconds.
    """
    return self.__retransmit_interval
      
  def _set_retransmit_interval(self, v, load=False):
    """
    Setter method for retransmit_interval, mapped from YANG variable /rbridge_id/interface/ve/ipv6/interface_ospfv3_conf/link_interval_properties/retransmit_interval (common-def:time-interval-sec)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_retransmit_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_retransmit_interval() directly.

    YANG Description: The time between retransmissions of LSAs to adjacent routers for an interface.The value can be from 1-3600 seconds. The default is 5 seconds.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3600']}), is_leaf=True, yang_name="retransmit-interval", rest_name="retransmit-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Time between retransmitting lost link state advertisements.'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """retransmit_interval must be of a type compatible with common-def:time-interval-sec""",
          'defined-type': "common-def:time-interval-sec",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3600']}), is_leaf=True, yang_name="retransmit-interval", rest_name="retransmit-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Time between retransmitting lost link state advertisements.'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)""",
        })

    self.__retransmit_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_retransmit_interval(self):
    self.__retransmit_interval = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..3600']}), is_leaf=True, yang_name="retransmit-interval", rest_name="retransmit-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Time between retransmitting lost link state advertisements.'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)


  def _get_transmit_delay(self):
    """
    Getter method for transmit_delay, mapped from YANG variable /rbridge_id/interface/ve/ipv6/interface_ospfv3_conf/link_interval_properties/transmit_delay (common-def:time-interval-sec)

    YANG Description: The time it takes to transmit Link State Update packets on this interface.The range is 0-3600 seconds. The default is 1 second.
    """
    return self.__transmit_delay
      
  def _set_transmit_delay(self, v, load=False):
    """
    Setter method for transmit_delay, mapped from YANG variable /rbridge_id/interface/ve/ipv6/interface_ospfv3_conf/link_interval_properties/transmit_delay (common-def:time-interval-sec)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_transmit_delay is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_transmit_delay() directly.

    YANG Description: The time it takes to transmit Link State Update packets on this interface.The range is 0-3600 seconds. The default is 1 second.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..3600']}), is_leaf=True, yang_name="transmit-delay", rest_name="transmit-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Link state transmit delay'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """transmit_delay must be of a type compatible with common-def:time-interval-sec""",
          'defined-type': "common-def:time-interval-sec",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..3600']}), is_leaf=True, yang_name="transmit-delay", rest_name="transmit-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Link state transmit delay'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)""",
        })

    self.__transmit_delay = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_transmit_delay(self):
    self.__transmit_delay = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..3600']}), is_leaf=True, yang_name="transmit-delay", rest_name="transmit-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Link state transmit delay'}}, namespace='urn:brocade.com:mgmt:brocade-ospfv3', defining_module='brocade-ospfv3', yang_type='common-def:time-interval-sec', is_config=True)

  hello_interval = __builtin__.property(_get_hello_interval, _set_hello_interval)
  dead_interval = __builtin__.property(_get_dead_interval, _set_dead_interval)
  hello_jitter = __builtin__.property(_get_hello_jitter, _set_hello_jitter)
  retransmit_interval = __builtin__.property(_get_retransmit_interval, _set_retransmit_interval)
  transmit_delay = __builtin__.property(_get_transmit_delay, _set_transmit_delay)


  _pyangbind_elements = {'hello_interval': hello_interval, 'dead_interval': dead_interval, 'hello_jitter': hello_jitter, 'retransmit_interval': retransmit_interval, 'transmit_delay': transmit_delay, }


