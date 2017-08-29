
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import prefix_flags
class preferred(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/gigabitethernet/ipv6/ipv6-nd-ra/ipv6-intf-cmds/nd/prefix/lifetime/preferred. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__preferred_lifetime','__preferred_infinite','__prefix_flags',)

  _yang_name = 'preferred'
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
    self.__prefix_flags = YANGDynClass(base=prefix_flags.prefix_flags, is_container='container', presence=False, yang_name="prefix-flags", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='container', is_config=True)
    self.__preferred_infinite = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="preferred-infinite", rest_name="infinite", parent=self, choice=(u'ch-preferred-type', u'ca-preferred-infinite'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Infinite preferred lifetime', u'alt-name': u'infinite'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)
    self.__preferred_lifetime = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..4294967295']}), is_leaf=True, yang_name="preferred-lifetime", rest_name="preferred-lifetime", parent=self, choice=(u'ch-preferred-type', u'ca-preferred-lifetime'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configures preferred lifetime', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='common-def:time-interval-sec', is_config=True)

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
      return [u'interface', u'gigabitethernet', u'ipv6', u'ipv6-nd-ra', u'ipv6-intf-cmds', u'nd', u'prefix', u'lifetime', u'preferred']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'GigabitEthernet', u'ipv6', u'nd', u'prefix']

  def _get_preferred_lifetime(self):
    """
    Getter method for preferred_lifetime, mapped from YANG variable /interface/gigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/prefix/lifetime/preferred/preferred_lifetime (common-def:time-interval-sec)
    """
    return self.__preferred_lifetime
      
  def _set_preferred_lifetime(self, v, load=False):
    """
    Setter method for preferred_lifetime, mapped from YANG variable /interface/gigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/prefix/lifetime/preferred/preferred_lifetime (common-def:time-interval-sec)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_preferred_lifetime is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_preferred_lifetime() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..4294967295']}), is_leaf=True, yang_name="preferred-lifetime", rest_name="preferred-lifetime", parent=self, choice=(u'ch-preferred-type', u'ca-preferred-lifetime'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configures preferred lifetime', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='common-def:time-interval-sec', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """preferred_lifetime must be of a type compatible with common-def:time-interval-sec""",
          'defined-type': "common-def:time-interval-sec",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..4294967295']}), is_leaf=True, yang_name="preferred-lifetime", rest_name="preferred-lifetime", parent=self, choice=(u'ch-preferred-type', u'ca-preferred-lifetime'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configures preferred lifetime', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='common-def:time-interval-sec', is_config=True)""",
        })

    self.__preferred_lifetime = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_preferred_lifetime(self):
    self.__preferred_lifetime = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..4294967295']}), is_leaf=True, yang_name="preferred-lifetime", rest_name="preferred-lifetime", parent=self, choice=(u'ch-preferred-type', u'ca-preferred-lifetime'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configures preferred lifetime', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='common-def:time-interval-sec', is_config=True)


  def _get_preferred_infinite(self):
    """
    Getter method for preferred_infinite, mapped from YANG variable /interface/gigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/prefix/lifetime/preferred/preferred_infinite (empty)
    """
    return self.__preferred_infinite
      
  def _set_preferred_infinite(self, v, load=False):
    """
    Setter method for preferred_infinite, mapped from YANG variable /interface/gigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/prefix/lifetime/preferred/preferred_infinite (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_preferred_infinite is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_preferred_infinite() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="preferred-infinite", rest_name="infinite", parent=self, choice=(u'ch-preferred-type', u'ca-preferred-infinite'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Infinite preferred lifetime', u'alt-name': u'infinite'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """preferred_infinite must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="preferred-infinite", rest_name="infinite", parent=self, choice=(u'ch-preferred-type', u'ca-preferred-infinite'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Infinite preferred lifetime', u'alt-name': u'infinite'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)""",
        })

    self.__preferred_infinite = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_preferred_infinite(self):
    self.__preferred_infinite = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="preferred-infinite", rest_name="infinite", parent=self, choice=(u'ch-preferred-type', u'ca-preferred-infinite'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Infinite preferred lifetime', u'alt-name': u'infinite'}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='empty', is_config=True)


  def _get_prefix_flags(self):
    """
    Getter method for prefix_flags, mapped from YANG variable /interface/gigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/prefix/lifetime/preferred/prefix_flags (container)
    """
    return self.__prefix_flags
      
  def _set_prefix_flags(self, v, load=False):
    """
    Setter method for prefix_flags, mapped from YANG variable /interface/gigabitethernet/ipv6/ipv6_nd_ra/ipv6_intf_cmds/nd/prefix/lifetime/preferred/prefix_flags (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefix_flags is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefix_flags() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=prefix_flags.prefix_flags, is_container='container', presence=False, yang_name="prefix-flags", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefix_flags must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=prefix_flags.prefix_flags, is_container='container', presence=False, yang_name="prefix-flags", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='container', is_config=True)""",
        })

    self.__prefix_flags = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefix_flags(self):
    self.__prefix_flags = YANGDynClass(base=prefix_flags.prefix_flags, is_container='container', presence=False, yang_name="prefix-flags", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-compact-syntax': None, u'cli-drop-node-name': None, u'cli-sequence-commands': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-ipv6-nd-ra', defining_module='brocade-ipv6-nd-ra', yang_type='container', is_config=True)

  preferred_lifetime = __builtin__.property(_get_preferred_lifetime, _set_preferred_lifetime)
  preferred_infinite = __builtin__.property(_get_preferred_infinite, _set_preferred_infinite)
  prefix_flags = __builtin__.property(_get_prefix_flags, _set_prefix_flags)

  __choices__ = {u'ch-preferred-type': {u'ca-preferred-infinite': [u'preferred_infinite'], u'ca-preferred-lifetime': [u'preferred_lifetime']}}
  _pyangbind_elements = {'preferred_lifetime': preferred_lifetime, 'preferred_infinite': preferred_infinite, 'prefix_flags': prefix_flags, }


