
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class trap(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/tengigabitethernet/snmp/trap. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: SNMP Trap configuration
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__link_snmp_trap_status',)

  _yang_name = 'trap'
  _rest_name = 'trap'

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
    self.__link_snmp_trap_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="link-snmp-trap-status", rest_name="link-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable/disable SNMP traps', u'cli-run-template': u' snmp trap $($(link-snmp-trap-status)==true?:$(link-snmp-trap-status))\n', u'alt-name': u'link-status', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)

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
      return [u'interface', u'tengigabitethernet', u'snmp', u'trap']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'TenGigabitEthernet', u'snmp', u'trap']

  def _get_link_snmp_trap_status(self):
    """
    Getter method for link_snmp_trap_status, mapped from YANG variable /interface/tengigabitethernet/snmp/trap/link_snmp_trap_status (empty)

    YANG Description: Flag to enable/disable SNMP Traps
    """
    return self.__link_snmp_trap_status
      
  def _set_link_snmp_trap_status(self, v, load=False):
    """
    Setter method for link_snmp_trap_status, mapped from YANG variable /interface/tengigabitethernet/snmp/trap/link_snmp_trap_status (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_link_snmp_trap_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_link_snmp_trap_status() directly.

    YANG Description: Flag to enable/disable SNMP Traps
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="link-snmp-trap-status", rest_name="link-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable/disable SNMP traps', u'cli-run-template': u' snmp trap $($(link-snmp-trap-status)==true?:$(link-snmp-trap-status))\n', u'alt-name': u'link-status', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """link_snmp_trap_status must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="link-snmp-trap-status", rest_name="link-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable/disable SNMP traps', u'cli-run-template': u' snmp trap $($(link-snmp-trap-status)==true?:$(link-snmp-trap-status))\n', u'alt-name': u'link-status', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)""",
        })

    self.__link_snmp_trap_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_link_snmp_trap_status(self):
    self.__link_snmp_trap_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="link-snmp-trap-status", rest_name="link-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable/disable SNMP traps', u'cli-run-template': u' snmp trap $($(link-snmp-trap-status)==true?:$(link-snmp-trap-status))\n', u'alt-name': u'link-status', u'cli-show-no': None}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='empty', is_config=True)

  link_snmp_trap_status = __builtin__.property(_get_link_snmp_trap_status, _set_link_snmp_trap_status)


  _pyangbind_elements = {'link_snmp_trap_status': link_snmp_trap_status, }


