
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class flowcontrolglobal(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-port-profile - based on the path /port-profile/qos-profile/qos/flowcontrol/flowcontrolglobal. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__tx','__rx',)

  _yang_name = 'flowcontrolglobal'
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
    self.__rx = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'on': {'value': 1}, u'off': {'value': 0}},), is_leaf=True, yang_name="rx", rest_name="rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Pause reception', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='enumeration', is_config=True)
    self.__tx = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'on': {'value': 1}, u'off': {'value': 0}},), is_leaf=True, yang_name="tx", rest_name="tx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Pause generation', u'cli-suppress-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='enumeration', is_config=True)

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
      return [u'port-profile', u'qos-profile', u'qos', u'flowcontrol', u'flowcontrolglobal']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'port-profile', u'qos-profile', u'qos', u'flowcontrol']

  def _get_tx(self):
    """
    Getter method for tx, mapped from YANG variable /port_profile/qos_profile/qos/flowcontrol/flowcontrolglobal/tx (enumeration)

    YANG Description: This specifies if the pause generation is 
enabled or disabled.
    """
    return self.__tx
      
  def _set_tx(self, v, load=False):
    """
    Setter method for tx, mapped from YANG variable /port_profile/qos_profile/qos/flowcontrol/flowcontrolglobal/tx (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tx is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tx() directly.

    YANG Description: This specifies if the pause generation is 
enabled or disabled.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'on': {'value': 1}, u'off': {'value': 0}},), is_leaf=True, yang_name="tx", rest_name="tx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Pause generation', u'cli-suppress-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tx must be of a type compatible with enumeration""",
          'defined-type': "brocade-port-profile:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'on': {'value': 1}, u'off': {'value': 0}},), is_leaf=True, yang_name="tx", rest_name="tx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Pause generation', u'cli-suppress-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='enumeration', is_config=True)""",
        })

    self.__tx = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tx(self):
    self.__tx = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'on': {'value': 1}, u'off': {'value': 0}},), is_leaf=True, yang_name="tx", rest_name="tx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Pause generation', u'cli-suppress-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='enumeration', is_config=True)


  def _get_rx(self):
    """
    Getter method for rx, mapped from YANG variable /port_profile/qos_profile/qos/flowcontrol/flowcontrolglobal/rx (enumeration)

    YANG Description: This specifies if the Pause reception is
enabled or disabled.
    """
    return self.__rx
      
  def _set_rx(self, v, load=False):
    """
    Setter method for rx, mapped from YANG variable /port_profile/qos_profile/qos/flowcontrol/flowcontrolglobal/rx (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rx is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rx() directly.

    YANG Description: This specifies if the Pause reception is
enabled or disabled.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'on': {'value': 1}, u'off': {'value': 0}},), is_leaf=True, yang_name="rx", rest_name="rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Pause reception', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rx must be of a type compatible with enumeration""",
          'defined-type': "brocade-port-profile:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'on': {'value': 1}, u'off': {'value': 0}},), is_leaf=True, yang_name="rx", rest_name="rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Pause reception', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='enumeration', is_config=True)""",
        })

    self.__rx = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rx(self):
    self.__rx = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'on': {'value': 1}, u'off': {'value': 0}},), is_leaf=True, yang_name="rx", rest_name="rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure Pause reception', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='enumeration', is_config=True)

  tx = __builtin__.property(_get_tx, _set_tx)
  rx = __builtin__.property(_get_rx, _set_rx)


  _pyangbind_elements = {'tx': tx, 'rx': rx, }


