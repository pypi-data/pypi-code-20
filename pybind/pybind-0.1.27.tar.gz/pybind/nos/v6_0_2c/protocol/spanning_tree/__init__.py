
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import stp
import rstp
import pvst
import rpvst
import mstp
class spanning_tree(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /protocol/spanning-tree. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__stp','__rstp','__pvst','__rpvst','__mstp',)

  _yang_name = 'spanning-tree'
  _rest_name = 'spanning-tree'

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
    self.__rpvst = YANGDynClass(base=rpvst.rpvst, is_container='container', presence=True, yang_name="rpvst", rest_name="rpvst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'rpvst-config', u'info': u'Rapid PVST spanning tree', u'display-when': u'not ((/protocol/spanning-tree/stp) or (/protocol/spanning-tree/rstp) or (/protocol/spanning-tree/mstp) or (/protocol/spanning-tree/pvst))'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)
    self.__pvst = YANGDynClass(base=pvst.pvst, is_container='container', presence=True, yang_name="pvst", rest_name="pvst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'pvst-config', u'info': u'PVST spanning-tree', u'display-when': u'not ((/protocol/spanning-tree/stp) or (/protocol/spanning-tree/rstp) or (/protocol/spanning-tree/mstp) or (/protocol/spanning-tree/rpvst))'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)
    self.__stp = YANGDynClass(base=stp.stp, is_container='container', presence=True, yang_name="stp", rest_name="stp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'stp-config', u'info': u'STP spanning-tree', u'display-when': u'not ((/protocol/spanning-tree/rstp) or (/protocol/spanning-tree/mstp) or (/protocol/spanning-tree/pvst) or (/protocol/spanning-tree/rpvst))'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)
    self.__rstp = YANGDynClass(base=rstp.rstp, is_container='container', presence=True, yang_name="rstp", rest_name="rstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'rstp-config', u'info': u'Rapid spanning tree', u'display-when': u'not ((/protocol/spanning-tree/stp) or (/protocol/spanning-tree/mstp) or (/protocol/spanning-tree/pvst) or (/protocol/spanning-tree/rpvst))'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)
    self.__mstp = YANGDynClass(base=mstp.mstp, is_container='container', presence=True, yang_name="mstp", rest_name="mstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'mstp-config', u'info': u'Multiple spanning tree', u'display-when': u'not ((/protocol/spanning-tree/stp) or (/protocol/spanning-tree/rstp) or (/protocol/spanning-tree/rpvst) or (/protocol/spanning-tree/pvst))'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)

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
      return [u'protocol', u'spanning-tree']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'protocol', u'spanning-tree']

  def _get_stp(self):
    """
    Getter method for stp, mapped from YANG variable /protocol/spanning_tree/stp (container)
    """
    return self.__stp
      
  def _set_stp(self, v, load=False):
    """
    Setter method for stp, mapped from YANG variable /protocol/spanning_tree/stp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_stp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_stp() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=stp.stp, is_container='container', presence=True, yang_name="stp", rest_name="stp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'stp-config', u'info': u'STP spanning-tree', u'display-when': u'not ((/protocol/spanning-tree/rstp) or (/protocol/spanning-tree/mstp) or (/protocol/spanning-tree/pvst) or (/protocol/spanning-tree/rpvst))'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """stp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=stp.stp, is_container='container', presence=True, yang_name="stp", rest_name="stp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'stp-config', u'info': u'STP spanning-tree', u'display-when': u'not ((/protocol/spanning-tree/rstp) or (/protocol/spanning-tree/mstp) or (/protocol/spanning-tree/pvst) or (/protocol/spanning-tree/rpvst))'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)""",
        })

    self.__stp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_stp(self):
    self.__stp = YANGDynClass(base=stp.stp, is_container='container', presence=True, yang_name="stp", rest_name="stp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'stp-config', u'info': u'STP spanning-tree', u'display-when': u'not ((/protocol/spanning-tree/rstp) or (/protocol/spanning-tree/mstp) or (/protocol/spanning-tree/pvst) or (/protocol/spanning-tree/rpvst))'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)


  def _get_rstp(self):
    """
    Getter method for rstp, mapped from YANG variable /protocol/spanning_tree/rstp (container)
    """
    return self.__rstp
      
  def _set_rstp(self, v, load=False):
    """
    Setter method for rstp, mapped from YANG variable /protocol/spanning_tree/rstp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rstp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rstp() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=rstp.rstp, is_container='container', presence=True, yang_name="rstp", rest_name="rstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'rstp-config', u'info': u'Rapid spanning tree', u'display-when': u'not ((/protocol/spanning-tree/stp) or (/protocol/spanning-tree/mstp) or (/protocol/spanning-tree/pvst) or (/protocol/spanning-tree/rpvst))'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rstp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=rstp.rstp, is_container='container', presence=True, yang_name="rstp", rest_name="rstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'rstp-config', u'info': u'Rapid spanning tree', u'display-when': u'not ((/protocol/spanning-tree/stp) or (/protocol/spanning-tree/mstp) or (/protocol/spanning-tree/pvst) or (/protocol/spanning-tree/rpvst))'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)""",
        })

    self.__rstp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rstp(self):
    self.__rstp = YANGDynClass(base=rstp.rstp, is_container='container', presence=True, yang_name="rstp", rest_name="rstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'rstp-config', u'info': u'Rapid spanning tree', u'display-when': u'not ((/protocol/spanning-tree/stp) or (/protocol/spanning-tree/mstp) or (/protocol/spanning-tree/pvst) or (/protocol/spanning-tree/rpvst))'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)


  def _get_pvst(self):
    """
    Getter method for pvst, mapped from YANG variable /protocol/spanning_tree/pvst (container)
    """
    return self.__pvst
      
  def _set_pvst(self, v, load=False):
    """
    Setter method for pvst, mapped from YANG variable /protocol/spanning_tree/pvst (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pvst is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pvst() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=pvst.pvst, is_container='container', presence=True, yang_name="pvst", rest_name="pvst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'pvst-config', u'info': u'PVST spanning-tree', u'display-when': u'not ((/protocol/spanning-tree/stp) or (/protocol/spanning-tree/rstp) or (/protocol/spanning-tree/mstp) or (/protocol/spanning-tree/rpvst))'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pvst must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=pvst.pvst, is_container='container', presence=True, yang_name="pvst", rest_name="pvst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'pvst-config', u'info': u'PVST spanning-tree', u'display-when': u'not ((/protocol/spanning-tree/stp) or (/protocol/spanning-tree/rstp) or (/protocol/spanning-tree/mstp) or (/protocol/spanning-tree/rpvst))'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)""",
        })

    self.__pvst = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pvst(self):
    self.__pvst = YANGDynClass(base=pvst.pvst, is_container='container', presence=True, yang_name="pvst", rest_name="pvst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'pvst-config', u'info': u'PVST spanning-tree', u'display-when': u'not ((/protocol/spanning-tree/stp) or (/protocol/spanning-tree/rstp) or (/protocol/spanning-tree/mstp) or (/protocol/spanning-tree/rpvst))'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)


  def _get_rpvst(self):
    """
    Getter method for rpvst, mapped from YANG variable /protocol/spanning_tree/rpvst (container)
    """
    return self.__rpvst
      
  def _set_rpvst(self, v, load=False):
    """
    Setter method for rpvst, mapped from YANG variable /protocol/spanning_tree/rpvst (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rpvst is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rpvst() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=rpvst.rpvst, is_container='container', presence=True, yang_name="rpvst", rest_name="rpvst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'rpvst-config', u'info': u'Rapid PVST spanning tree', u'display-when': u'not ((/protocol/spanning-tree/stp) or (/protocol/spanning-tree/rstp) or (/protocol/spanning-tree/mstp) or (/protocol/spanning-tree/pvst))'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rpvst must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=rpvst.rpvst, is_container='container', presence=True, yang_name="rpvst", rest_name="rpvst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'rpvst-config', u'info': u'Rapid PVST spanning tree', u'display-when': u'not ((/protocol/spanning-tree/stp) or (/protocol/spanning-tree/rstp) or (/protocol/spanning-tree/mstp) or (/protocol/spanning-tree/pvst))'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)""",
        })

    self.__rpvst = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rpvst(self):
    self.__rpvst = YANGDynClass(base=rpvst.rpvst, is_container='container', presence=True, yang_name="rpvst", rest_name="rpvst", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'rpvst-config', u'info': u'Rapid PVST spanning tree', u'display-when': u'not ((/protocol/spanning-tree/stp) or (/protocol/spanning-tree/rstp) or (/protocol/spanning-tree/mstp) or (/protocol/spanning-tree/pvst))'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)


  def _get_mstp(self):
    """
    Getter method for mstp, mapped from YANG variable /protocol/spanning_tree/mstp (container)
    """
    return self.__mstp
      
  def _set_mstp(self, v, load=False):
    """
    Setter method for mstp, mapped from YANG variable /protocol/spanning_tree/mstp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mstp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mstp() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=mstp.mstp, is_container='container', presence=True, yang_name="mstp", rest_name="mstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'mstp-config', u'info': u'Multiple spanning tree', u'display-when': u'not ((/protocol/spanning-tree/stp) or (/protocol/spanning-tree/rstp) or (/protocol/spanning-tree/rpvst) or (/protocol/spanning-tree/pvst))'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mstp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=mstp.mstp, is_container='container', presence=True, yang_name="mstp", rest_name="mstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'mstp-config', u'info': u'Multiple spanning tree', u'display-when': u'not ((/protocol/spanning-tree/stp) or (/protocol/spanning-tree/rstp) or (/protocol/spanning-tree/rpvst) or (/protocol/spanning-tree/pvst))'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)""",
        })

    self.__mstp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mstp(self):
    self.__mstp = YANGDynClass(base=mstp.mstp, is_container='container', presence=True, yang_name="mstp", rest_name="mstp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-add-mode': None, u'callpoint': u'mstp-config', u'info': u'Multiple spanning tree', u'display-when': u'not ((/protocol/spanning-tree/stp) or (/protocol/spanning-tree/rstp) or (/protocol/spanning-tree/rpvst) or (/protocol/spanning-tree/pvst))'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)

  stp = __builtin__.property(_get_stp, _set_stp)
  rstp = __builtin__.property(_get_rstp, _set_rstp)
  pvst = __builtin__.property(_get_pvst, _set_pvst)
  rpvst = __builtin__.property(_get_rpvst, _set_rpvst)
  mstp = __builtin__.property(_get_mstp, _set_mstp)


  _pyangbind_elements = {'stp': stp, 'rstp': rstp, 'pvst': pvst, 'rpvst': rpvst, 'mstp': mstp, }


