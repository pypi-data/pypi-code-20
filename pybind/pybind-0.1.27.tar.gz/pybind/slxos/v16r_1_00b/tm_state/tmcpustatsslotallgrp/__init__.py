
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class tmcpustatsslotallgrp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-sysdiag-operational - based on the path /tm-state/tmcpustatsslotallgrp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: TM voq stats for CPU port per slot for all CPU group
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__slot_id','__enquepkt','__enqueubytes','__discardpkt','__discardbytes','__currdepth','__maxdepth',)

  _yang_name = 'tmcpustatsslotallgrp'
  _rest_name = 'tmcpustatsslotallgrp'

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
    self.__discardpkt = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="discardpkt", rest_name="discardpkt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    self.__enqueubytes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="enqueubytes", rest_name="enqueubytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    self.__discardbytes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="discardbytes", rest_name="discardbytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    self.__slot_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="slot-id", rest_name="slot-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)
    self.__maxdepth = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="maxdepth", rest_name="maxdepth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    self.__enquepkt = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="enquepkt", rest_name="enquepkt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    self.__currdepth = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="currdepth", rest_name="currdepth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)

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
      return [u'tm-state', u'tmcpustatsslotallgrp']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'tm-state', u'tmcpustatsslotallgrp']

  def _get_slot_id(self):
    """
    Getter method for slot_id, mapped from YANG variable /tm_state/tmcpustatsslotallgrp/slot_id (uint16)

    YANG Description: slot_id
    """
    return self.__slot_id
      
  def _set_slot_id(self, v, load=False):
    """
    Setter method for slot_id, mapped from YANG variable /tm_state/tmcpustatsslotallgrp/slot_id (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_slot_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_slot_id() directly.

    YANG Description: slot_id
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="slot-id", rest_name="slot-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """slot_id must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="slot-id", rest_name="slot-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)""",
        })

    self.__slot_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_slot_id(self):
    self.__slot_id = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="slot-id", rest_name="slot-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint16', is_config=False)


  def _get_enquepkt(self):
    """
    Getter method for enquepkt, mapped from YANG variable /tm_state/tmcpustatsslotallgrp/enquepkt (uint64)

    YANG Description: enque_pkts
    """
    return self.__enquepkt
      
  def _set_enquepkt(self, v, load=False):
    """
    Setter method for enquepkt, mapped from YANG variable /tm_state/tmcpustatsslotallgrp/enquepkt (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enquepkt is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enquepkt() directly.

    YANG Description: enque_pkts
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="enquepkt", rest_name="enquepkt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enquepkt must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="enquepkt", rest_name="enquepkt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)""",
        })

    self.__enquepkt = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enquepkt(self):
    self.__enquepkt = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="enquepkt", rest_name="enquepkt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)


  def _get_enqueubytes(self):
    """
    Getter method for enqueubytes, mapped from YANG variable /tm_state/tmcpustatsslotallgrp/enqueubytes (uint64)

    YANG Description: enque_bytes
    """
    return self.__enqueubytes
      
  def _set_enqueubytes(self, v, load=False):
    """
    Setter method for enqueubytes, mapped from YANG variable /tm_state/tmcpustatsslotallgrp/enqueubytes (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_enqueubytes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_enqueubytes() directly.

    YANG Description: enque_bytes
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="enqueubytes", rest_name="enqueubytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """enqueubytes must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="enqueubytes", rest_name="enqueubytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)""",
        })

    self.__enqueubytes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_enqueubytes(self):
    self.__enqueubytes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="enqueubytes", rest_name="enqueubytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)


  def _get_discardpkt(self):
    """
    Getter method for discardpkt, mapped from YANG variable /tm_state/tmcpustatsslotallgrp/discardpkt (uint64)

    YANG Description: discard_pkts
    """
    return self.__discardpkt
      
  def _set_discardpkt(self, v, load=False):
    """
    Setter method for discardpkt, mapped from YANG variable /tm_state/tmcpustatsslotallgrp/discardpkt (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_discardpkt is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_discardpkt() directly.

    YANG Description: discard_pkts
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="discardpkt", rest_name="discardpkt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """discardpkt must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="discardpkt", rest_name="discardpkt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)""",
        })

    self.__discardpkt = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_discardpkt(self):
    self.__discardpkt = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="discardpkt", rest_name="discardpkt", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)


  def _get_discardbytes(self):
    """
    Getter method for discardbytes, mapped from YANG variable /tm_state/tmcpustatsslotallgrp/discardbytes (uint64)

    YANG Description: discard_bytes
    """
    return self.__discardbytes
      
  def _set_discardbytes(self, v, load=False):
    """
    Setter method for discardbytes, mapped from YANG variable /tm_state/tmcpustatsslotallgrp/discardbytes (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_discardbytes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_discardbytes() directly.

    YANG Description: discard_bytes
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="discardbytes", rest_name="discardbytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """discardbytes must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="discardbytes", rest_name="discardbytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)""",
        })

    self.__discardbytes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_discardbytes(self):
    self.__discardbytes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="discardbytes", rest_name="discardbytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)


  def _get_currdepth(self):
    """
    Getter method for currdepth, mapped from YANG variable /tm_state/tmcpustatsslotallgrp/currdepth (uint64)

    YANG Description: current_queue_depth
    """
    return self.__currdepth
      
  def _set_currdepth(self, v, load=False):
    """
    Setter method for currdepth, mapped from YANG variable /tm_state/tmcpustatsslotallgrp/currdepth (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_currdepth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_currdepth() directly.

    YANG Description: current_queue_depth
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="currdepth", rest_name="currdepth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """currdepth must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="currdepth", rest_name="currdepth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)""",
        })

    self.__currdepth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_currdepth(self):
    self.__currdepth = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="currdepth", rest_name="currdepth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)


  def _get_maxdepth(self):
    """
    Getter method for maxdepth, mapped from YANG variable /tm_state/tmcpustatsslotallgrp/maxdepth (uint64)

    YANG Description: max_queue_depth
    """
    return self.__maxdepth
      
  def _set_maxdepth(self, v, load=False):
    """
    Setter method for maxdepth, mapped from YANG variable /tm_state/tmcpustatsslotallgrp/maxdepth (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_maxdepth is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_maxdepth() directly.

    YANG Description: max_queue_depth
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="maxdepth", rest_name="maxdepth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """maxdepth must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="maxdepth", rest_name="maxdepth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)""",
        })

    self.__maxdepth = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_maxdepth(self):
    self.__maxdepth = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="maxdepth", rest_name="maxdepth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-sysdiag-operational', defining_module='brocade-sysdiag-operational', yang_type='uint64', is_config=False)

  slot_id = __builtin__.property(_get_slot_id)
  enquepkt = __builtin__.property(_get_enquepkt)
  enqueubytes = __builtin__.property(_get_enqueubytes)
  discardpkt = __builtin__.property(_get_discardpkt)
  discardbytes = __builtin__.property(_get_discardbytes)
  currdepth = __builtin__.property(_get_currdepth)
  maxdepth = __builtin__.property(_get_maxdepth)


  _pyangbind_elements = {'slot_id': slot_id, 'enquepkt': enquepkt, 'enqueubytes': enqueubytes, 'discardpkt': discardpkt, 'discardbytes': discardbytes, 'currdepth': currdepth, 'maxdepth': maxdepth, }


