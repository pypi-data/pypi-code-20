
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class spf6_interval(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/isis/router-isis-cmds-holder/address-family/ipv6/af-ipv6-unicast/af-ipv6-attributes/spf6-interval. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__spf6_interval_level','__spf6_interval_max_hold_time','__spf6_interval_initial_delay','__spf6_interval_hold_time',)

  _yang_name = 'spf6-interval'
  _rest_name = 'spf-interval'

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
    self.__spf6_interval_initial_delay = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..120000']}), is_leaf=True, yang_name="spf6-interval-initial-delay", rest_name="spf6-interval-initial-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)
    self.__spf6_interval_max_hold_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..120']}), is_leaf=True, yang_name="spf6-interval-max-hold-time", rest_name="spf6-interval-max-hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)
    self.__spf6_interval_hold_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..120000']}), is_leaf=True, yang_name="spf6-interval-hold-time", rest_name="spf6-interval-hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)
    self.__spf6_interval_level = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'level-2': {'value': 2}, u'level-1': {'value': 1}},), is_leaf=True, yang_name="spf6-interval-level", rest_name="spf6-interval-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='enumeration', is_config=True)

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
      return [u'routing-system', u'router', u'isis', u'router-isis-cmds-holder', u'address-family', u'ipv6', u'af-ipv6-unicast', u'af-ipv6-attributes', u'spf6-interval']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'isis', u'address-family', u'ipv6', u'unicast', u'spf-interval']

  def _get_spf6_interval_level(self):
    """
    Getter method for spf6_interval_level, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv6/af_ipv6_unicast/af_ipv6_attributes/spf6_interval/spf6_interval_level (enumeration)
    """
    return self.__spf6_interval_level
      
  def _set_spf6_interval_level(self, v, load=False):
    """
    Setter method for spf6_interval_level, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv6/af_ipv6_unicast/af_ipv6_attributes/spf6_interval/spf6_interval_level (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_spf6_interval_level is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_spf6_interval_level() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'level-2': {'value': 2}, u'level-1': {'value': 1}},), is_leaf=True, yang_name="spf6-interval-level", rest_name="spf6-interval-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """spf6_interval_level must be of a type compatible with enumeration""",
          'defined-type': "brocade-isis:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'level-2': {'value': 2}, u'level-1': {'value': 1}},), is_leaf=True, yang_name="spf6-interval-level", rest_name="spf6-interval-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='enumeration', is_config=True)""",
        })

    self.__spf6_interval_level = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_spf6_interval_level(self):
    self.__spf6_interval_level = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'level-2': {'value': 2}, u'level-1': {'value': 1}},), is_leaf=True, yang_name="spf6-interval-level", rest_name="spf6-interval-level", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-incomplete-command': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='enumeration', is_config=True)


  def _get_spf6_interval_max_hold_time(self):
    """
    Getter method for spf6_interval_max_hold_time, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv6/af_ipv6_unicast/af_ipv6_attributes/spf6_interval/spf6_interval_max_hold_time (uint32)
    """
    return self.__spf6_interval_max_hold_time
      
  def _set_spf6_interval_max_hold_time(self, v, load=False):
    """
    Setter method for spf6_interval_max_hold_time, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv6/af_ipv6_unicast/af_ipv6_attributes/spf6_interval/spf6_interval_max_hold_time (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_spf6_interval_max_hold_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_spf6_interval_max_hold_time() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..120']}), is_leaf=True, yang_name="spf6-interval-max-hold-time", rest_name="spf6-interval-max-hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """spf6_interval_max_hold_time must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..120']}), is_leaf=True, yang_name="spf6-interval-max-hold-time", rest_name="spf6-interval-max-hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)""",
        })

    self.__spf6_interval_max_hold_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_spf6_interval_max_hold_time(self):
    self.__spf6_interval_max_hold_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..120']}), is_leaf=True, yang_name="spf6-interval-max-hold-time", rest_name="spf6-interval-max-hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)


  def _get_spf6_interval_initial_delay(self):
    """
    Getter method for spf6_interval_initial_delay, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv6/af_ipv6_unicast/af_ipv6_attributes/spf6_interval/spf6_interval_initial_delay (uint32)
    """
    return self.__spf6_interval_initial_delay
      
  def _set_spf6_interval_initial_delay(self, v, load=False):
    """
    Setter method for spf6_interval_initial_delay, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv6/af_ipv6_unicast/af_ipv6_attributes/spf6_interval/spf6_interval_initial_delay (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_spf6_interval_initial_delay is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_spf6_interval_initial_delay() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..120000']}), is_leaf=True, yang_name="spf6-interval-initial-delay", rest_name="spf6-interval-initial-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """spf6_interval_initial_delay must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..120000']}), is_leaf=True, yang_name="spf6-interval-initial-delay", rest_name="spf6-interval-initial-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)""",
        })

    self.__spf6_interval_initial_delay = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_spf6_interval_initial_delay(self):
    self.__spf6_interval_initial_delay = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..120000']}), is_leaf=True, yang_name="spf6-interval-initial-delay", rest_name="spf6-interval-initial-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)


  def _get_spf6_interval_hold_time(self):
    """
    Getter method for spf6_interval_hold_time, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv6/af_ipv6_unicast/af_ipv6_attributes/spf6_interval/spf6_interval_hold_time (uint32)
    """
    return self.__spf6_interval_hold_time
      
  def _set_spf6_interval_hold_time(self, v, load=False):
    """
    Setter method for spf6_interval_hold_time, mapped from YANG variable /routing_system/router/isis/router_isis_cmds_holder/address_family/ipv6/af_ipv6_unicast/af_ipv6_attributes/spf6_interval/spf6_interval_hold_time (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_spf6_interval_hold_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_spf6_interval_hold_time() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..120000']}), is_leaf=True, yang_name="spf6-interval-hold-time", rest_name="spf6-interval-hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """spf6_interval_hold_time must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..120000']}), is_leaf=True, yang_name="spf6-interval-hold-time", rest_name="spf6-interval-hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)""",
        })

    self.__spf6_interval_hold_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_spf6_interval_hold_time(self):
    self.__spf6_interval_hold_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..120000']}), is_leaf=True, yang_name="spf6-interval-hold-time", rest_name="spf6-interval-hold-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-isis', defining_module='brocade-isis', yang_type='uint32', is_config=True)

  spf6_interval_level = __builtin__.property(_get_spf6_interval_level, _set_spf6_interval_level)
  spf6_interval_max_hold_time = __builtin__.property(_get_spf6_interval_max_hold_time, _set_spf6_interval_max_hold_time)
  spf6_interval_initial_delay = __builtin__.property(_get_spf6_interval_initial_delay, _set_spf6_interval_initial_delay)
  spf6_interval_hold_time = __builtin__.property(_get_spf6_interval_hold_time, _set_spf6_interval_hold_time)


  _pyangbind_elements = {'spf6_interval_level': spf6_interval_level, 'spf6_interval_max_hold_time': spf6_interval_max_hold_time, 'spf6_interval_initial_delay': spf6_interval_initial_delay, 'spf6_interval_hold_time': spf6_interval_hold_time, }


