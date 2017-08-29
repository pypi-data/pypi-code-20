
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class group(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-vlan - based on the path /vlan/classifier/group. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__groupid','__oper','__rule_name','__ruleid',)

  _yang_name = 'group'
  _rest_name = 'group'

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
    self.__oper = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'add': {'value': 1}, u'delete': {'value': 2}},), is_leaf=True, yang_name="oper", rest_name="oper", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Add/Delete Rule.', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='rule-opp-type', is_config=True)
    self.__rule_name = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'rule': {'value': 0}},), is_leaf=True, yang_name="rule-name", rest_name="rule-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='rule-name-type', is_config=True)
    self.__groupid = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16']}), is_leaf=True, yang_name="groupid", rest_name="groupid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='uint32', is_config=True)
    self.__ruleid = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..256']}), is_leaf=True, yang_name="ruleid", rest_name="ruleid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='uint32', is_config=True)

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
      return [u'vlan', u'classifier', u'group']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'vlan', u'classifier', u'group']

  def _get_groupid(self):
    """
    Getter method for groupid, mapped from YANG variable /vlan/classifier/group/groupid (uint32)
    """
    return self.__groupid
      
  def _set_groupid(self, v, load=False):
    """
    Setter method for groupid, mapped from YANG variable /vlan/classifier/group/groupid (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_groupid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_groupid() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16']}), is_leaf=True, yang_name="groupid", rest_name="groupid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """groupid must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16']}), is_leaf=True, yang_name="groupid", rest_name="groupid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='uint32', is_config=True)""",
        })

    self.__groupid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_groupid(self):
    self.__groupid = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..16']}), is_leaf=True, yang_name="groupid", rest_name="groupid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='uint32', is_config=True)


  def _get_oper(self):
    """
    Getter method for oper, mapped from YANG variable /vlan/classifier/group/oper (rule-opp-type)
    """
    return self.__oper
      
  def _set_oper(self, v, load=False):
    """
    Setter method for oper, mapped from YANG variable /vlan/classifier/group/oper (rule-opp-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_oper is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_oper() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'add': {'value': 1}, u'delete': {'value': 2}},), is_leaf=True, yang_name="oper", rest_name="oper", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Add/Delete Rule.', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='rule-opp-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """oper must be of a type compatible with rule-opp-type""",
          'defined-type': "brocade-vlan:rule-opp-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'add': {'value': 1}, u'delete': {'value': 2}},), is_leaf=True, yang_name="oper", rest_name="oper", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Add/Delete Rule.', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='rule-opp-type', is_config=True)""",
        })

    self.__oper = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_oper(self):
    self.__oper = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'add': {'value': 1}, u'delete': {'value': 2}},), is_leaf=True, yang_name="oper", rest_name="oper", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Add/Delete Rule.', u'cli-drop-node-name': None}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='rule-opp-type', is_config=True)


  def _get_rule_name(self):
    """
    Getter method for rule_name, mapped from YANG variable /vlan/classifier/group/rule_name (rule-name-type)
    """
    return self.__rule_name
      
  def _set_rule_name(self, v, load=False):
    """
    Setter method for rule_name, mapped from YANG variable /vlan/classifier/group/rule_name (rule-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rule_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rule_name() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'rule': {'value': 0}},), is_leaf=True, yang_name="rule-name", rest_name="rule-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='rule-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rule_name must be of a type compatible with rule-name-type""",
          'defined-type': "brocade-vlan:rule-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'rule': {'value': 0}},), is_leaf=True, yang_name="rule-name", rest_name="rule-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='rule-name-type', is_config=True)""",
        })

    self.__rule_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rule_name(self):
    self.__rule_name = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'rule': {'value': 0}},), is_leaf=True, yang_name="rule-name", rest_name="rule-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='rule-name-type', is_config=True)


  def _get_ruleid(self):
    """
    Getter method for ruleid, mapped from YANG variable /vlan/classifier/group/ruleid (uint32)
    """
    return self.__ruleid
      
  def _set_ruleid(self, v, load=False):
    """
    Setter method for ruleid, mapped from YANG variable /vlan/classifier/group/ruleid (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ruleid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ruleid() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..256']}), is_leaf=True, yang_name="ruleid", rest_name="ruleid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ruleid must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..256']}), is_leaf=True, yang_name="ruleid", rest_name="ruleid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='uint32', is_config=True)""",
        })

    self.__ruleid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ruleid(self):
    self.__ruleid = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..256']}), is_leaf=True, yang_name="ruleid", rest_name="ruleid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-vlan', defining_module='brocade-vlan', yang_type='uint32', is_config=True)

  groupid = __builtin__.property(_get_groupid, _set_groupid)
  oper = __builtin__.property(_get_oper, _set_oper)
  rule_name = __builtin__.property(_get_rule_name, _set_rule_name)
  ruleid = __builtin__.property(_get_ruleid, _set_ruleid)


  _pyangbind_elements = {'groupid': groupid, 'oper': oper, 'rule_name': rule_name, 'ruleid': ruleid, }


