
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class vlan(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /protocol/spanning-tree/pvst/vlan. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__id','__priority','__forward_delay','__max_age','__hello_time',)

  _yang_name = 'vlan'
  _rest_name = 'vlan'

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
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..61440']}), is_leaf=True, yang_name="priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Bridge priority in increments of 4096', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)
    self.__max_age = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'6..40']}), is_leaf=True, yang_name="max-age", rest_name="max-age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the max age for the spanning tree', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)
    self.__hello_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..10']}), is_leaf=True, yang_name="hello-time", rest_name="hello-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the hello interval for the spanning tree', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)
    self.__id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="id", rest_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'cli-suppress-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)
    self.__forward_delay = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'4..30']}), is_leaf=True, yang_name="forward-delay", rest_name="forward-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the forward delay for the spanning tree', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)

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
      return [u'protocol', u'spanning-tree', u'pvst', u'vlan']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'protocol', u'spanning-tree', u'pvst', u'vlan']

  def _get_id(self):
    """
    Getter method for id, mapped from YANG variable /protocol/spanning_tree/pvst/vlan/id (uint32)
    """
    return self.__id
      
  def _set_id(self, v, load=False):
    """
    Setter method for id, mapped from YANG variable /protocol/spanning_tree/pvst/vlan/id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_id() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="id", rest_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'cli-suppress-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="id", rest_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'cli-suppress-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)""",
        })

    self.__id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_id(self):
    self.__id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}), is_leaf=True, yang_name="id", rest_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-suppress-range': None, u'cli-suppress-no': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)


  def _get_priority(self):
    """
    Getter method for priority, mapped from YANG variable /protocol/spanning_tree/pvst/vlan/priority (uint32)
    """
    return self.__priority
      
  def _set_priority(self, v, load=False):
    """
    Setter method for priority, mapped from YANG variable /protocol/spanning_tree/pvst/vlan/priority (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_priority() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..61440']}), is_leaf=True, yang_name="priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Bridge priority in increments of 4096', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """priority must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..61440']}), is_leaf=True, yang_name="priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Bridge priority in increments of 4096', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)""",
        })

    self.__priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_priority(self):
    self.__priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..61440']}), is_leaf=True, yang_name="priority", rest_name="priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Bridge priority in increments of 4096', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)


  def _get_forward_delay(self):
    """
    Getter method for forward_delay, mapped from YANG variable /protocol/spanning_tree/pvst/vlan/forward_delay (uint32)
    """
    return self.__forward_delay
      
  def _set_forward_delay(self, v, load=False):
    """
    Setter method for forward_delay, mapped from YANG variable /protocol/spanning_tree/pvst/vlan/forward_delay (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_forward_delay is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_forward_delay() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'4..30']}), is_leaf=True, yang_name="forward-delay", rest_name="forward-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the forward delay for the spanning tree', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """forward_delay must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'4..30']}), is_leaf=True, yang_name="forward-delay", rest_name="forward-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the forward delay for the spanning tree', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)""",
        })

    self.__forward_delay = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_forward_delay(self):
    self.__forward_delay = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'4..30']}), is_leaf=True, yang_name="forward-delay", rest_name="forward-delay", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the forward delay for the spanning tree', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)


  def _get_max_age(self):
    """
    Getter method for max_age, mapped from YANG variable /protocol/spanning_tree/pvst/vlan/max_age (uint32)
    """
    return self.__max_age
      
  def _set_max_age(self, v, load=False):
    """
    Setter method for max_age, mapped from YANG variable /protocol/spanning_tree/pvst/vlan/max_age (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_max_age is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_max_age() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'6..40']}), is_leaf=True, yang_name="max-age", rest_name="max-age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the max age for the spanning tree', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """max_age must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'6..40']}), is_leaf=True, yang_name="max-age", rest_name="max-age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the max age for the spanning tree', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)""",
        })

    self.__max_age = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_max_age(self):
    self.__max_age = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'6..40']}), is_leaf=True, yang_name="max-age", rest_name="max-age", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the max age for the spanning tree', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)


  def _get_hello_time(self):
    """
    Getter method for hello_time, mapped from YANG variable /protocol/spanning_tree/pvst/vlan/hello_time (uint32)
    """
    return self.__hello_time
      
  def _set_hello_time(self, v, load=False):
    """
    Setter method for hello_time, mapped from YANG variable /protocol/spanning_tree/pvst/vlan/hello_time (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hello_time is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hello_time() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..10']}), is_leaf=True, yang_name="hello-time", rest_name="hello-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the hello interval for the spanning tree', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hello_time must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..10']}), is_leaf=True, yang_name="hello-time", rest_name="hello-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the hello interval for the spanning tree', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)""",
        })

    self.__hello_time = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hello_time(self):
    self.__hello_time = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..10']}), is_leaf=True, yang_name="hello-time", rest_name="hello-time", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the hello interval for the spanning tree', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='uint32', is_config=True)

  id = __builtin__.property(_get_id, _set_id)
  priority = __builtin__.property(_get_priority, _set_priority)
  forward_delay = __builtin__.property(_get_forward_delay, _set_forward_delay)
  max_age = __builtin__.property(_get_max_age, _set_max_age)
  hello_time = __builtin__.property(_get_hello_time, _set_hello_time)


  _pyangbind_elements = {'id': id, 'priority': priority, 'forward_delay': forward_delay, 'max_age': max_age, 'hello_time': hello_time, }


