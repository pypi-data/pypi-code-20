
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class unnumbered(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/gigabitethernet/ip/ip-config/unnumbered. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ip_donor_interface_type','__ip_donor_interface_name',)

  _yang_name = 'unnumbered'
  _rest_name = 'unnumbered'

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
    self.__ip_donor_interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u've': {'value': 5}, u'loopback': {'value': 9}, u'fortygigabitethernet': {'value': 2}, u'gigabitethernet': {'value': 0}, u'tengigabitethernet': {'value': 1}, u'hundredgigabitethernet': {'value': 10}},), is_leaf=True, yang_name="ip-donor-interface-type", rest_name="ip-donor-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The type of donor interface.', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='ip-unnumbered-donor-interface-type_t', is_config=True)
    self.__ip_donor_interface_name = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}),], is_leaf=True, yang_name="ip-donor-interface-name", rest_name="ip-donor-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'The name of donor interface.'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='ip-unnumbered-donor-interface-name_t', is_config=True)

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
      return [u'interface', u'gigabitethernet', u'ip', u'ip-config', u'unnumbered']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'GigabitEthernet', u'ip', u'unnumbered']

  def _get_ip_donor_interface_type(self):
    """
    Getter method for ip_donor_interface_type, mapped from YANG variable /interface/gigabitethernet/ip/ip_config/unnumbered/ip_donor_interface_type (ip-unnumbered-donor-interface-type_t)
    """
    return self.__ip_donor_interface_type
      
  def _set_ip_donor_interface_type(self, v, load=False):
    """
    Setter method for ip_donor_interface_type, mapped from YANG variable /interface/gigabitethernet/ip/ip_config/unnumbered/ip_donor_interface_type (ip-unnumbered-donor-interface-type_t)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip_donor_interface_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip_donor_interface_type() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u've': {'value': 5}, u'loopback': {'value': 9}, u'fortygigabitethernet': {'value': 2}, u'gigabitethernet': {'value': 0}, u'tengigabitethernet': {'value': 1}, u'hundredgigabitethernet': {'value': 10}},), is_leaf=True, yang_name="ip-donor-interface-type", rest_name="ip-donor-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The type of donor interface.', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='ip-unnumbered-donor-interface-type_t', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip_donor_interface_type must be of a type compatible with ip-unnumbered-donor-interface-type_t""",
          'defined-type': "brocade-ip-config:ip-unnumbered-donor-interface-type_t",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u've': {'value': 5}, u'loopback': {'value': 9}, u'fortygigabitethernet': {'value': 2}, u'gigabitethernet': {'value': 0}, u'tengigabitethernet': {'value': 1}, u'hundredgigabitethernet': {'value': 10}},), is_leaf=True, yang_name="ip-donor-interface-type", rest_name="ip-donor-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The type of donor interface.', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='ip-unnumbered-donor-interface-type_t', is_config=True)""",
        })

    self.__ip_donor_interface_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip_donor_interface_type(self):
    self.__ip_donor_interface_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u've': {'value': 5}, u'loopback': {'value': 9}, u'fortygigabitethernet': {'value': 2}, u'gigabitethernet': {'value': 0}, u'tengigabitethernet': {'value': 1}, u'hundredgigabitethernet': {'value': 10}},), is_leaf=True, yang_name="ip-donor-interface-type", rest_name="ip-donor-interface-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The type of donor interface.', u'cli-drop-node-name': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='ip-unnumbered-donor-interface-type_t', is_config=True)


  def _get_ip_donor_interface_name(self):
    """
    Getter method for ip_donor_interface_name, mapped from YANG variable /interface/gigabitethernet/ip/ip_config/unnumbered/ip_donor_interface_name (ip-unnumbered-donor-interface-name_t)
    """
    return self.__ip_donor_interface_name
      
  def _set_ip_donor_interface_name(self, v, load=False):
    """
    Setter method for ip_donor_interface_name, mapped from YANG variable /interface/gigabitethernet/ip/ip_config/unnumbered/ip_donor_interface_name (ip-unnumbered-donor-interface-name_t)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ip_donor_interface_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ip_donor_interface_name() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}),], is_leaf=True, yang_name="ip-donor-interface-name", rest_name="ip-donor-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'The name of donor interface.'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='ip-unnumbered-donor-interface-name_t', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ip_donor_interface_name must be of a type compatible with ip-unnumbered-donor-interface-name_t""",
          'defined-type': "brocade-ip-config:ip-unnumbered-donor-interface-name_t",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}),], is_leaf=True, yang_name="ip-donor-interface-name", rest_name="ip-donor-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'The name of donor interface.'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='ip-unnumbered-donor-interface-name_t', is_config=True)""",
        })

    self.__ip_donor_interface_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ip_donor_interface_name(self):
    self.__ip_donor_interface_name = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-3][0-9])/)?(([0-9]|[1][0-6]))/([1-9]|[1-9][0-9]|[1-9][0-9][0-9])(:[1-4])?)', 'length': [u'3..16']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..8191']}),RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..255']}),], is_leaf=True, yang_name="ip-donor-interface-name", rest_name="ip-donor-interface-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-drop-node-name': None, u'info': u'The name of donor interface.'}}, namespace='urn:brocade.com:mgmt:brocade-ip-config', defining_module='brocade-ip-config', yang_type='ip-unnumbered-donor-interface-name_t', is_config=True)

  ip_donor_interface_type = __builtin__.property(_get_ip_donor_interface_type, _set_ip_donor_interface_type)
  ip_donor_interface_name = __builtin__.property(_get_ip_donor_interface_name, _set_ip_donor_interface_name)


  _pyangbind_elements = {'ip_donor_interface_type': ip_donor_interface_type, 'ip_donor_interface_name': ip_donor_interface_name, }


