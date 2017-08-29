
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class monitor(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-tunnels - based on the path /overlay-gateway/monitor. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__session','__direction','__remote_endpoint','__vlan_leaf','__vlan_add_remove','__vlan_range',)

  _yang_name = 'monitor'
  _rest_name = 'monitor'

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
    self.__vlan_add_remove = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'add': {'value': 1}, u'remove': {'value': 2}},), is_leaf=True, yang_name="vlan-add-remove", rest_name="vlan-add-remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='enumeration', is_config=True)
    self.__direction = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'both': {'value': 3}, u'rx': {'value': 2}, u'tx': {'value': 1}},), is_leaf=True, yang_name="direction", rest_name="direction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify flow direction', u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='direction-type', is_config=True)
    self.__remote_endpoint = YANGDynClass(base=[RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'any': {'value': 1}},),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="remote-endpoint", rest_name="remote-endpoint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Tunnel destination end point address', u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='union', is_config=True)
    self.__vlan_leaf = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'vlan': {'value': 1}},), is_leaf=True, yang_name="vlan-leaf", rest_name="vlan-leaf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Target VLAN IDs', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='enumeration', is_config=True)
    self.__session = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}), is_leaf=True, yang_name="session", rest_name="session", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Session number', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='span:session-type', is_config=True)
    self.__vlan_range = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9]+(-[0-9]+)?(,[0-9]+(-[0-9]+)?)*'}), is_leaf=True, yang_name="vlan-range", rest_name="vlan-range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='vfab-range-type', is_config=True)

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
      return [u'overlay-gateway', u'monitor']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'overlay-gateway', u'monitor']

  def _get_session(self):
    """
    Getter method for session, mapped from YANG variable /overlay_gateway/monitor/session (span:session-type)
    """
    return self.__session
      
  def _set_session(self, v, load=False):
    """
    Setter method for session, mapped from YANG variable /overlay_gateway/monitor/session (span:session-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_session is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_session() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}), is_leaf=True, yang_name="session", rest_name="session", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Session number', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='span:session-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """session must be of a type compatible with span:session-type""",
          'defined-type': "span:session-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}), is_leaf=True, yang_name="session", rest_name="session", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Session number', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='span:session-type', is_config=True)""",
        })

    self.__session = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_session(self):
    self.__session = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..512']}), is_leaf=True, yang_name="session", rest_name="session", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Session number', u'cli-expose-key-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='span:session-type', is_config=True)


  def _get_direction(self):
    """
    Getter method for direction, mapped from YANG variable /overlay_gateway/monitor/direction (direction-type)
    """
    return self.__direction
      
  def _set_direction(self, v, load=False):
    """
    Setter method for direction, mapped from YANG variable /overlay_gateway/monitor/direction (direction-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_direction is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_direction() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'both': {'value': 3}, u'rx': {'value': 2}, u'tx': {'value': 1}},), is_leaf=True, yang_name="direction", rest_name="direction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify flow direction', u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='direction-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """direction must be of a type compatible with direction-type""",
          'defined-type': "brocade-tunnels:direction-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'both': {'value': 3}, u'rx': {'value': 2}, u'tx': {'value': 1}},), is_leaf=True, yang_name="direction", rest_name="direction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify flow direction', u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='direction-type', is_config=True)""",
        })

    self.__direction = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_direction(self):
    self.__direction = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'both': {'value': 3}, u'rx': {'value': 2}, u'tx': {'value': 1}},), is_leaf=True, yang_name="direction", rest_name="direction", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Specify flow direction', u'cli-full-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='direction-type', is_config=True)


  def _get_remote_endpoint(self):
    """
    Getter method for remote_endpoint, mapped from YANG variable /overlay_gateway/monitor/remote_endpoint (union)
    """
    return self.__remote_endpoint
      
  def _set_remote_endpoint(self, v, load=False):
    """
    Setter method for remote_endpoint, mapped from YANG variable /overlay_gateway/monitor/remote_endpoint (union)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_remote_endpoint is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_remote_endpoint() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'any': {'value': 1}},),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="remote-endpoint", rest_name="remote-endpoint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Tunnel destination end point address', u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='union', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """remote_endpoint must be of a type compatible with union""",
          'defined-type': "brocade-tunnels:union",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'any': {'value': 1}},),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="remote-endpoint", rest_name="remote-endpoint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Tunnel destination end point address', u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='union', is_config=True)""",
        })

    self.__remote_endpoint = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_remote_endpoint(self):
    self.__remote_endpoint = YANGDynClass(base=[RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'any': {'value': 1}},),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),], is_leaf=True, yang_name="remote-endpoint", rest_name="remote-endpoint", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Tunnel destination end point address', u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='union', is_config=True)


  def _get_vlan_leaf(self):
    """
    Getter method for vlan_leaf, mapped from YANG variable /overlay_gateway/monitor/vlan_leaf (enumeration)
    """
    return self.__vlan_leaf
      
  def _set_vlan_leaf(self, v, load=False):
    """
    Setter method for vlan_leaf, mapped from YANG variable /overlay_gateway/monitor/vlan_leaf (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_leaf is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_leaf() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'vlan': {'value': 1}},), is_leaf=True, yang_name="vlan-leaf", rest_name="vlan-leaf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Target VLAN IDs', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_leaf must be of a type compatible with enumeration""",
          'defined-type': "brocade-tunnels:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'vlan': {'value': 1}},), is_leaf=True, yang_name="vlan-leaf", rest_name="vlan-leaf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Target VLAN IDs', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='enumeration', is_config=True)""",
        })

    self.__vlan_leaf = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_leaf(self):
    self.__vlan_leaf = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'vlan': {'value': 1}},), is_leaf=True, yang_name="vlan-leaf", rest_name="vlan-leaf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Target VLAN IDs', u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='enumeration', is_config=True)


  def _get_vlan_add_remove(self):
    """
    Getter method for vlan_add_remove, mapped from YANG variable /overlay_gateway/monitor/vlan_add_remove (enumeration)
    """
    return self.__vlan_add_remove
      
  def _set_vlan_add_remove(self, v, load=False):
    """
    Setter method for vlan_add_remove, mapped from YANG variable /overlay_gateway/monitor/vlan_add_remove (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_add_remove is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_add_remove() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'add': {'value': 1}, u'remove': {'value': 2}},), is_leaf=True, yang_name="vlan-add-remove", rest_name="vlan-add-remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_add_remove must be of a type compatible with enumeration""",
          'defined-type': "brocade-tunnels:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'add': {'value': 1}, u'remove': {'value': 2}},), is_leaf=True, yang_name="vlan-add-remove", rest_name="vlan-add-remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='enumeration', is_config=True)""",
        })

    self.__vlan_add_remove = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_add_remove(self):
    self.__vlan_add_remove = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'add': {'value': 1}, u'remove': {'value': 2}},), is_leaf=True, yang_name="vlan-add-remove", rest_name="vlan-add-remove", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='enumeration', is_config=True)


  def _get_vlan_range(self):
    """
    Getter method for vlan_range, mapped from YANG variable /overlay_gateway/monitor/vlan_range (vfab-range-type)
    """
    return self.__vlan_range
      
  def _set_vlan_range(self, v, load=False):
    """
    Setter method for vlan_range, mapped from YANG variable /overlay_gateway/monitor/vlan_range (vfab-range-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vlan_range is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vlan_range() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9]+(-[0-9]+)?(,[0-9]+(-[0-9]+)?)*'}), is_leaf=True, yang_name="vlan-range", rest_name="vlan-range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='vfab-range-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vlan_range must be of a type compatible with vfab-range-type""",
          'defined-type': "brocade-tunnels:vfab-range-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9]+(-[0-9]+)?(,[0-9]+(-[0-9]+)?)*'}), is_leaf=True, yang_name="vlan-range", rest_name="vlan-range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='vfab-range-type', is_config=True)""",
        })

    self.__vlan_range = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vlan_range(self):
    self.__vlan_range = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[0-9]+(-[0-9]+)?(,[0-9]+(-[0-9]+)?)*'}), is_leaf=True, yang_name="vlan-range", rest_name="vlan-range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-tunnels', defining_module='brocade-tunnels', yang_type='vfab-range-type', is_config=True)

  session = __builtin__.property(_get_session, _set_session)
  direction = __builtin__.property(_get_direction, _set_direction)
  remote_endpoint = __builtin__.property(_get_remote_endpoint, _set_remote_endpoint)
  vlan_leaf = __builtin__.property(_get_vlan_leaf, _set_vlan_leaf)
  vlan_add_remove = __builtin__.property(_get_vlan_add_remove, _set_vlan_add_remove)
  vlan_range = __builtin__.property(_get_vlan_range, _set_vlan_range)


  _pyangbind_elements = {'session': session, 'direction': direction, 'remote_endpoint': remote_endpoint, 'vlan_leaf': vlan_leaf, 'vlan_add_remove': vlan_add_remove, 'vlan_range': vlan_range, }


