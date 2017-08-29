
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class rules(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-maps-ext - based on the path /brocade_maps_ext_rpc/maps-get-default-rules/output/rules. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__rbridgeid','__rulename','__groupname','__monitor','__op','__value','__action','__timebase','__policyname',)

  _yang_name = 'rules'
  _rest_name = 'rules'

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
    self.__policyname = YANGDynClass(base=unicode, is_leaf=True, yang_name="policyname", rest_name="policyname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)
    self.__timebase = YANGDynClass(base=unicode, is_leaf=True, yang_name="timebase", rest_name="timebase", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)
    self.__monitor = YANGDynClass(base=unicode, is_leaf=True, yang_name="monitor", rest_name="monitor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)
    self.__value = YANGDynClass(base=unicode, is_leaf=True, yang_name="value", rest_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)
    self.__groupname = YANGDynClass(base=unicode, is_leaf=True, yang_name="groupname", rest_name="groupname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)
    self.__rulename = YANGDynClass(base=unicode, is_leaf=True, yang_name="rulename", rest_name="rulename", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)
    self.__action = YANGDynClass(base=unicode, is_leaf=True, yang_name="action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)
    self.__rbridgeid = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..239']}), is_leaf=True, yang_name="rbridgeid", rest_name="rbridgeid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='common-def:rbridge-id-type', is_config=True)
    self.__op = YANGDynClass(base=unicode, is_leaf=True, yang_name="op", rest_name="op", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)

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
      return [u'brocade_maps_ext_rpc', u'maps-get-default-rules', u'output', u'rules']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'maps-get-default-rules', u'output', u'rules']

  def _get_rbridgeid(self):
    """
    Getter method for rbridgeid, mapped from YANG variable /brocade_maps_ext_rpc/maps_get_default_rules/output/rules/rbridgeid (common-def:rbridge-id-type)
    """
    return self.__rbridgeid
      
  def _set_rbridgeid(self, v, load=False):
    """
    Setter method for rbridgeid, mapped from YANG variable /brocade_maps_ext_rpc/maps_get_default_rules/output/rules/rbridgeid (common-def:rbridge-id-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rbridgeid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rbridgeid() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..239']}), is_leaf=True, yang_name="rbridgeid", rest_name="rbridgeid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='common-def:rbridge-id-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rbridgeid must be of a type compatible with common-def:rbridge-id-type""",
          'defined-type': "common-def:rbridge-id-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..239']}), is_leaf=True, yang_name="rbridgeid", rest_name="rbridgeid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='common-def:rbridge-id-type', is_config=True)""",
        })

    self.__rbridgeid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rbridgeid(self):
    self.__rbridgeid = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..239']}), is_leaf=True, yang_name="rbridgeid", rest_name="rbridgeid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='common-def:rbridge-id-type', is_config=True)


  def _get_rulename(self):
    """
    Getter method for rulename, mapped from YANG variable /brocade_maps_ext_rpc/maps_get_default_rules/output/rules/rulename (string)

    YANG Description: MAPS Rule name
    """
    return self.__rulename
      
  def _set_rulename(self, v, load=False):
    """
    Setter method for rulename, mapped from YANG variable /brocade_maps_ext_rpc/maps_get_default_rules/output/rules/rulename (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rulename is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rulename() directly.

    YANG Description: MAPS Rule name
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="rulename", rest_name="rulename", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rulename must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="rulename", rest_name="rulename", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)""",
        })

    self.__rulename = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rulename(self):
    self.__rulename = YANGDynClass(base=unicode, is_leaf=True, yang_name="rulename", rest_name="rulename", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)


  def _get_groupname(self):
    """
    Getter method for groupname, mapped from YANG variable /brocade_maps_ext_rpc/maps_get_default_rules/output/rules/groupname (string)

    YANG Description: MAPS Group name
    """
    return self.__groupname
      
  def _set_groupname(self, v, load=False):
    """
    Setter method for groupname, mapped from YANG variable /brocade_maps_ext_rpc/maps_get_default_rules/output/rules/groupname (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_groupname is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_groupname() directly.

    YANG Description: MAPS Group name
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="groupname", rest_name="groupname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """groupname must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="groupname", rest_name="groupname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)""",
        })

    self.__groupname = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_groupname(self):
    self.__groupname = YANGDynClass(base=unicode, is_leaf=True, yang_name="groupname", rest_name="groupname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)


  def _get_monitor(self):
    """
    Getter method for monitor, mapped from YANG variable /brocade_maps_ext_rpc/maps_get_default_rules/output/rules/monitor (string)

    YANG Description: MAPS Monitor name
    """
    return self.__monitor
      
  def _set_monitor(self, v, load=False):
    """
    Setter method for monitor, mapped from YANG variable /brocade_maps_ext_rpc/maps_get_default_rules/output/rules/monitor (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_monitor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_monitor() directly.

    YANG Description: MAPS Monitor name
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="monitor", rest_name="monitor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """monitor must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="monitor", rest_name="monitor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)""",
        })

    self.__monitor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_monitor(self):
    self.__monitor = YANGDynClass(base=unicode, is_leaf=True, yang_name="monitor", rest_name="monitor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)


  def _get_op(self):
    """
    Getter method for op, mapped from YANG variable /brocade_maps_ext_rpc/maps_get_default_rules/output/rules/op (string)

    YANG Description: MAPS operator
    """
    return self.__op
      
  def _set_op(self, v, load=False):
    """
    Setter method for op, mapped from YANG variable /brocade_maps_ext_rpc/maps_get_default_rules/output/rules/op (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_op is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_op() directly.

    YANG Description: MAPS operator
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="op", rest_name="op", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """op must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="op", rest_name="op", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)""",
        })

    self.__op = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_op(self):
    self.__op = YANGDynClass(base=unicode, is_leaf=True, yang_name="op", rest_name="op", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)


  def _get_value(self):
    """
    Getter method for value, mapped from YANG variable /brocade_maps_ext_rpc/maps_get_default_rules/output/rules/value (string)

    YANG Description: MAPS threshold value
    """
    return self.__value
      
  def _set_value(self, v, load=False):
    """
    Setter method for value, mapped from YANG variable /brocade_maps_ext_rpc/maps_get_default_rules/output/rules/value (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_value() directly.

    YANG Description: MAPS threshold value
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="value", rest_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """value must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="value", rest_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)""",
        })

    self.__value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_value(self):
    self.__value = YANGDynClass(base=unicode, is_leaf=True, yang_name="value", rest_name="value", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)


  def _get_action(self):
    """
    Getter method for action, mapped from YANG variable /brocade_maps_ext_rpc/maps_get_default_rules/output/rules/action (string)

    YANG Description: MAPS action value
    """
    return self.__action
      
  def _set_action(self, v, load=False):
    """
    Setter method for action, mapped from YANG variable /brocade_maps_ext_rpc/maps_get_default_rules/output/rules/action (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_action is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_action() directly.

    YANG Description: MAPS action value
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """action must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)""",
        })

    self.__action = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_action(self):
    self.__action = YANGDynClass(base=unicode, is_leaf=True, yang_name="action", rest_name="action", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)


  def _get_timebase(self):
    """
    Getter method for timebase, mapped from YANG variable /brocade_maps_ext_rpc/maps_get_default_rules/output/rules/timebase (string)

    YANG Description: MAPS timebase value
    """
    return self.__timebase
      
  def _set_timebase(self, v, load=False):
    """
    Setter method for timebase, mapped from YANG variable /brocade_maps_ext_rpc/maps_get_default_rules/output/rules/timebase (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_timebase is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_timebase() directly.

    YANG Description: MAPS timebase value
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="timebase", rest_name="timebase", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """timebase must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="timebase", rest_name="timebase", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)""",
        })

    self.__timebase = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_timebase(self):
    self.__timebase = YANGDynClass(base=unicode, is_leaf=True, yang_name="timebase", rest_name="timebase", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)


  def _get_policyname(self):
    """
    Getter method for policyname, mapped from YANG variable /brocade_maps_ext_rpc/maps_get_default_rules/output/rules/policyname (string)

    YANG Description: MAPS policy associated with rule
    """
    return self.__policyname
      
  def _set_policyname(self, v, load=False):
    """
    Setter method for policyname, mapped from YANG variable /brocade_maps_ext_rpc/maps_get_default_rules/output/rules/policyname (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_policyname is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_policyname() directly.

    YANG Description: MAPS policy associated with rule
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="policyname", rest_name="policyname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """policyname must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="policyname", rest_name="policyname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)""",
        })

    self.__policyname = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_policyname(self):
    self.__policyname = YANGDynClass(base=unicode, is_leaf=True, yang_name="policyname", rest_name="policyname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-maps-ext', defining_module='brocade-maps-ext', yang_type='string', is_config=True)

  rbridgeid = __builtin__.property(_get_rbridgeid, _set_rbridgeid)
  rulename = __builtin__.property(_get_rulename, _set_rulename)
  groupname = __builtin__.property(_get_groupname, _set_groupname)
  monitor = __builtin__.property(_get_monitor, _set_monitor)
  op = __builtin__.property(_get_op, _set_op)
  value = __builtin__.property(_get_value, _set_value)
  action = __builtin__.property(_get_action, _set_action)
  timebase = __builtin__.property(_get_timebase, _set_timebase)
  policyname = __builtin__.property(_get_policyname, _set_policyname)


  _pyangbind_elements = {'rbridgeid': rbridgeid, 'rulename': rulename, 'groupname': groupname, 'monitor': monitor, 'op': op, 'value': value, 'action': action, 'timebase': timebase, 'policyname': policyname, }


