
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import bfd_ipv6_interval_attributes
class bfd_ipv6_link_local_static_route(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/ipv6/route/static/bfd/bfd-ipv6-link-local-static-route. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__bfd_ipv6_link_local_dest','__bfd_ipv6_link_local_src','__bfd_interface_type','__bfd_interface_name','__bfd_ipv6_interval_attributes',)

  _yang_name = 'bfd-ipv6-link-local-static-route'
  _rest_name = 'bfd-ipv6-link-local-static-route'

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
    self.__bfd_ipv6_interval_attributes = YANGDynClass(base=bfd_ipv6_interval_attributes.bfd_ipv6_interval_attributes, is_container='container', presence=False, yang_name="bfd-ipv6-interval-attributes", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='container', is_config=True)
    self.__bfd_interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'port-channel': {'value': 8}, u've': {'value': 4}, u'fortygigabitethernet': {'value': 6}, u'gigabitethernet': {'value': 2}, u'tengigabitethernet': {'value': 1}, u'hundredgigabitethernet': {'value': 7}, u'null': {'value': 5}},), is_leaf=True, yang_name="bfd-interface-type", rest_name="bfd-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Outgoing interface type'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='enumeration', is_config=True)
    self.__bfd_ipv6_link_local_dest = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="bfd-ipv6-link-local-dest", rest_name="bfd-ipv6-link-local-dest", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D ;; Destination IPv6 address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-address', is_config=True)
    self.__bfd_ipv6_link_local_src = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="bfd-ipv6-link-local-src", rest_name="bfd-ipv6-link-local-src", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D ;; Source IPv6 address', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-address', is_config=True)
    self.__bfd_interface_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..16']}), is_leaf=True, yang_name="bfd-interface-name", rest_name="bfd-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='string', is_config=True)

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
      return [u'rbridge-id', u'ipv6', u'route', u'static', u'bfd', u'bfd-ipv6-link-local-static-route']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'ipv6', u'route', u'static', u'bfd', u'bfd-ipv6-link-local-static-route']

  def _get_bfd_ipv6_link_local_dest(self):
    """
    Getter method for bfd_ipv6_link_local_dest, mapped from YANG variable /rbridge_id/ipv6/route/static/bfd/bfd_ipv6_link_local_static_route/bfd_ipv6_link_local_dest (inet:ipv6-address)
    """
    return self.__bfd_ipv6_link_local_dest
      
  def _set_bfd_ipv6_link_local_dest(self, v, load=False):
    """
    Setter method for bfd_ipv6_link_local_dest, mapped from YANG variable /rbridge_id/ipv6/route/static/bfd/bfd_ipv6_link_local_static_route/bfd_ipv6_link_local_dest (inet:ipv6-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bfd_ipv6_link_local_dest is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bfd_ipv6_link_local_dest() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="bfd-ipv6-link-local-dest", rest_name="bfd-ipv6-link-local-dest", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D ;; Destination IPv6 address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bfd_ipv6_link_local_dest must be of a type compatible with inet:ipv6-address""",
          'defined-type': "inet:ipv6-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="bfd-ipv6-link-local-dest", rest_name="bfd-ipv6-link-local-dest", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D ;; Destination IPv6 address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-address', is_config=True)""",
        })

    self.__bfd_ipv6_link_local_dest = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bfd_ipv6_link_local_dest(self):
    self.__bfd_ipv6_link_local_dest = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="bfd-ipv6-link-local-dest", rest_name="bfd-ipv6-link-local-dest", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D ;; Destination IPv6 address'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-address', is_config=True)


  def _get_bfd_ipv6_link_local_src(self):
    """
    Getter method for bfd_ipv6_link_local_src, mapped from YANG variable /rbridge_id/ipv6/route/static/bfd/bfd_ipv6_link_local_static_route/bfd_ipv6_link_local_src (inet:ipv6-address)
    """
    return self.__bfd_ipv6_link_local_src
      
  def _set_bfd_ipv6_link_local_src(self, v, load=False):
    """
    Setter method for bfd_ipv6_link_local_src, mapped from YANG variable /rbridge_id/ipv6/route/static/bfd/bfd_ipv6_link_local_static_route/bfd_ipv6_link_local_src (inet:ipv6-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bfd_ipv6_link_local_src is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bfd_ipv6_link_local_src() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="bfd-ipv6-link-local-src", rest_name="bfd-ipv6-link-local-src", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D ;; Source IPv6 address', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bfd_ipv6_link_local_src must be of a type compatible with inet:ipv6-address""",
          'defined-type': "inet:ipv6-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="bfd-ipv6-link-local-src", rest_name="bfd-ipv6-link-local-src", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D ;; Source IPv6 address', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-address', is_config=True)""",
        })

    self.__bfd_ipv6_link_local_src = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bfd_ipv6_link_local_src(self):
    self.__bfd_ipv6_link_local_src = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="bfd-ipv6-link-local-src", rest_name="bfd-ipv6-link-local-src", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'A:B::C:D ;; Source IPv6 address', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='inet:ipv6-address', is_config=True)


  def _get_bfd_interface_type(self):
    """
    Getter method for bfd_interface_type, mapped from YANG variable /rbridge_id/ipv6/route/static/bfd/bfd_ipv6_link_local_static_route/bfd_interface_type (enumeration)
    """
    return self.__bfd_interface_type
      
  def _set_bfd_interface_type(self, v, load=False):
    """
    Setter method for bfd_interface_type, mapped from YANG variable /rbridge_id/ipv6/route/static/bfd/bfd_ipv6_link_local_static_route/bfd_interface_type (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bfd_interface_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bfd_interface_type() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'port-channel': {'value': 8}, u've': {'value': 4}, u'fortygigabitethernet': {'value': 6}, u'gigabitethernet': {'value': 2}, u'tengigabitethernet': {'value': 1}, u'hundredgigabitethernet': {'value': 7}, u'null': {'value': 5}},), is_leaf=True, yang_name="bfd-interface-type", rest_name="bfd-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Outgoing interface type'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bfd_interface_type must be of a type compatible with enumeration""",
          'defined-type': "brocade-ipv6-rtm:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'port-channel': {'value': 8}, u've': {'value': 4}, u'fortygigabitethernet': {'value': 6}, u'gigabitethernet': {'value': 2}, u'tengigabitethernet': {'value': 1}, u'hundredgigabitethernet': {'value': 7}, u'null': {'value': 5}},), is_leaf=True, yang_name="bfd-interface-type", rest_name="bfd-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Outgoing interface type'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='enumeration', is_config=True)""",
        })

    self.__bfd_interface_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bfd_interface_type(self):
    self.__bfd_interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'port-channel': {'value': 8}, u've': {'value': 4}, u'fortygigabitethernet': {'value': 6}, u'gigabitethernet': {'value': 2}, u'tengigabitethernet': {'value': 1}, u'hundredgigabitethernet': {'value': 7}, u'null': {'value': 5}},), is_leaf=True, yang_name="bfd-interface-type", rest_name="bfd-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Outgoing interface type'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='enumeration', is_config=True)


  def _get_bfd_interface_name(self):
    """
    Getter method for bfd_interface_name, mapped from YANG variable /rbridge_id/ipv6/route/static/bfd/bfd_ipv6_link_local_static_route/bfd_interface_name (string)
    """
    return self.__bfd_interface_name
      
  def _set_bfd_interface_name(self, v, load=False):
    """
    Setter method for bfd_interface_name, mapped from YANG variable /rbridge_id/ipv6/route/static/bfd/bfd_ipv6_link_local_static_route/bfd_interface_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bfd_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bfd_interface_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..16']}), is_leaf=True, yang_name="bfd-interface-name", rest_name="bfd-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bfd_interface_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..16']}), is_leaf=True, yang_name="bfd-interface-name", rest_name="bfd-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='string', is_config=True)""",
        })

    self.__bfd_interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bfd_interface_name(self):
    self.__bfd_interface_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..16']}), is_leaf=True, yang_name="bfd-interface-name", rest_name="bfd-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='string', is_config=True)


  def _get_bfd_ipv6_interval_attributes(self):
    """
    Getter method for bfd_ipv6_interval_attributes, mapped from YANG variable /rbridge_id/ipv6/route/static/bfd/bfd_ipv6_link_local_static_route/bfd_ipv6_interval_attributes (container)
    """
    return self.__bfd_ipv6_interval_attributes
      
  def _set_bfd_ipv6_interval_attributes(self, v, load=False):
    """
    Setter method for bfd_ipv6_interval_attributes, mapped from YANG variable /rbridge_id/ipv6/route/static/bfd/bfd_ipv6_link_local_static_route/bfd_ipv6_interval_attributes (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bfd_ipv6_interval_attributes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bfd_ipv6_interval_attributes() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=bfd_ipv6_interval_attributes.bfd_ipv6_interval_attributes, is_container='container', presence=False, yang_name="bfd-ipv6-interval-attributes", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bfd_ipv6_interval_attributes must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=bfd_ipv6_interval_attributes.bfd_ipv6_interval_attributes, is_container='container', presence=False, yang_name="bfd-ipv6-interval-attributes", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='container', is_config=True)""",
        })

    self.__bfd_ipv6_interval_attributes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bfd_ipv6_interval_attributes(self):
    self.__bfd_ipv6_interval_attributes = YANGDynClass(base=bfd_ipv6_interval_attributes.bfd_ipv6_interval_attributes, is_container='container', presence=False, yang_name="bfd-ipv6-interval-attributes", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-rtm', defining_module='brocade-ipv6-rtm', yang_type='container', is_config=True)

  bfd_ipv6_link_local_dest = __builtin__.property(_get_bfd_ipv6_link_local_dest, _set_bfd_ipv6_link_local_dest)
  bfd_ipv6_link_local_src = __builtin__.property(_get_bfd_ipv6_link_local_src, _set_bfd_ipv6_link_local_src)
  bfd_interface_type = __builtin__.property(_get_bfd_interface_type, _set_bfd_interface_type)
  bfd_interface_name = __builtin__.property(_get_bfd_interface_name, _set_bfd_interface_name)
  bfd_ipv6_interval_attributes = __builtin__.property(_get_bfd_ipv6_interval_attributes, _set_bfd_ipv6_interval_attributes)


  _pyangbind_elements = {'bfd_ipv6_link_local_dest': bfd_ipv6_link_local_dest, 'bfd_ipv6_link_local_src': bfd_ipv6_link_local_src, 'bfd_interface_type': bfd_interface_type, 'bfd_interface_name': bfd_interface_name, 'bfd_ipv6_interval_attributes': bfd_ipv6_interval_attributes, }


