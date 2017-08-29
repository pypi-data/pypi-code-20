
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import redundancy
import reload
class brocade_ha(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ha - based on the path /brocade_ha_rpc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This management module is an instrumentation to ha
level commands
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__redundancy','__reload',)

  _yang_name = 'brocade-ha'
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
    self.__reload = YANGDynClass(base=reload.reload, is_leaf=True, yang_name="reload", rest_name="reload", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'reload switch', u'hidden': u'rpccmd', u'actionpoint': u'reloadha'}}, namespace='urn:brocade.com:mgmt:brocade-ha', defining_module='brocade-ha', yang_type='rpc', is_config=True)
    self.__redundancy = YANGDynClass(base=redundancy.redundancy, is_leaf=True, yang_name="redundancy", rest_name="redundancy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Show high availability redundancy state', u'hidden': u'rpccmd', u'actionpoint': u'showha'}}, namespace='urn:brocade.com:mgmt:brocade-ha', defining_module='brocade-ha', yang_type='rpc', is_config=True)

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
      return [u'brocade_ha_rpc']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return []

  def _get_redundancy(self):
    """
    Getter method for redundancy, mapped from YANG variable /brocade_ha_rpc/redundancy (rpc)
    """
    return self.__redundancy
      
  def _set_redundancy(self, v, load=False):
    """
    Setter method for redundancy, mapped from YANG variable /brocade_ha_rpc/redundancy (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_redundancy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_redundancy() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=redundancy.redundancy, is_leaf=True, yang_name="redundancy", rest_name="redundancy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Show high availability redundancy state', u'hidden': u'rpccmd', u'actionpoint': u'showha'}}, namespace='urn:brocade.com:mgmt:brocade-ha', defining_module='brocade-ha', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """redundancy must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=redundancy.redundancy, is_leaf=True, yang_name="redundancy", rest_name="redundancy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Show high availability redundancy state', u'hidden': u'rpccmd', u'actionpoint': u'showha'}}, namespace='urn:brocade.com:mgmt:brocade-ha', defining_module='brocade-ha', yang_type='rpc', is_config=True)""",
        })

    self.__redundancy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_redundancy(self):
    self.__redundancy = YANGDynClass(base=redundancy.redundancy, is_leaf=True, yang_name="redundancy", rest_name="redundancy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'Show high availability redundancy state', u'hidden': u'rpccmd', u'actionpoint': u'showha'}}, namespace='urn:brocade.com:mgmt:brocade-ha', defining_module='brocade-ha', yang_type='rpc', is_config=True)


  def _get_reload(self):
    """
    Getter method for reload, mapped from YANG variable /brocade_ha_rpc/reload (rpc)
    """
    return self.__reload
      
  def _set_reload(self, v, load=False):
    """
    Setter method for reload, mapped from YANG variable /brocade_ha_rpc/reload (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reload is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reload() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=reload.reload, is_leaf=True, yang_name="reload", rest_name="reload", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'reload switch', u'hidden': u'rpccmd', u'actionpoint': u'reloadha'}}, namespace='urn:brocade.com:mgmt:brocade-ha', defining_module='brocade-ha', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reload must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=reload.reload, is_leaf=True, yang_name="reload", rest_name="reload", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'reload switch', u'hidden': u'rpccmd', u'actionpoint': u'reloadha'}}, namespace='urn:brocade.com:mgmt:brocade-ha', defining_module='brocade-ha', yang_type='rpc', is_config=True)""",
        })

    self.__reload = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reload(self):
    self.__reload = YANGDynClass(base=reload.reload, is_leaf=True, yang_name="reload", rest_name="reload", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'info': u'reload switch', u'hidden': u'rpccmd', u'actionpoint': u'reloadha'}}, namespace='urn:brocade.com:mgmt:brocade-ha', defining_module='brocade-ha', yang_type='rpc', is_config=True)

  redundancy = __builtin__.property(_get_redundancy, _set_redundancy)
  reload = __builtin__.property(_get_reload, _set_reload)


  _pyangbind_elements = {'redundancy': redundancy, 'reload': reload, }


