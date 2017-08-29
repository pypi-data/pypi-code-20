
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ldp_session_summary(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls-operational - based on the path /mpls-state/ldp/ldp-session-summary. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: 
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__num_link_sessions','__num_operational_link_sessions','__num_targeted_sessions','__num_operational_targeted_sessions',)

  _yang_name = 'ldp-session-summary'
  _rest_name = 'ldp-session-summary'

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
    self.__num_targeted_sessions = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-targeted-sessions", rest_name="num-targeted-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__num_operational_targeted_sessions = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-operational-targeted-sessions", rest_name="num-operational-targeted-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__num_link_sessions = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-link-sessions", rest_name="num-link-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    self.__num_operational_link_sessions = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-operational-link-sessions", rest_name="num-operational-link-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)

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
      return [u'mpls-state', u'ldp', u'ldp-session-summary']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mpls-state', u'ldp', u'ldp-session-summary']

  def _get_num_link_sessions(self):
    """
    Getter method for num_link_sessions, mapped from YANG variable /mpls_state/ldp/ldp_session_summary/num_link_sessions (uint32)

    YANG Description: mpls_num_link_sessions
    """
    return self.__num_link_sessions
      
  def _set_num_link_sessions(self, v, load=False):
    """
    Setter method for num_link_sessions, mapped from YANG variable /mpls_state/ldp/ldp_session_summary/num_link_sessions (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_num_link_sessions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_num_link_sessions() directly.

    YANG Description: mpls_num_link_sessions
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-link-sessions", rest_name="num-link-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """num_link_sessions must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-link-sessions", rest_name="num-link-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__num_link_sessions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_num_link_sessions(self):
    self.__num_link_sessions = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-link-sessions", rest_name="num-link-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_num_operational_link_sessions(self):
    """
    Getter method for num_operational_link_sessions, mapped from YANG variable /mpls_state/ldp/ldp_session_summary/num_operational_link_sessions (uint32)

    YANG Description: mpls_num_operational_link_sessions
    """
    return self.__num_operational_link_sessions
      
  def _set_num_operational_link_sessions(self, v, load=False):
    """
    Setter method for num_operational_link_sessions, mapped from YANG variable /mpls_state/ldp/ldp_session_summary/num_operational_link_sessions (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_num_operational_link_sessions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_num_operational_link_sessions() directly.

    YANG Description: mpls_num_operational_link_sessions
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-operational-link-sessions", rest_name="num-operational-link-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """num_operational_link_sessions must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-operational-link-sessions", rest_name="num-operational-link-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__num_operational_link_sessions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_num_operational_link_sessions(self):
    self.__num_operational_link_sessions = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-operational-link-sessions", rest_name="num-operational-link-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_num_targeted_sessions(self):
    """
    Getter method for num_targeted_sessions, mapped from YANG variable /mpls_state/ldp/ldp_session_summary/num_targeted_sessions (uint32)

    YANG Description: mpls_num_targeted_sessions
    """
    return self.__num_targeted_sessions
      
  def _set_num_targeted_sessions(self, v, load=False):
    """
    Setter method for num_targeted_sessions, mapped from YANG variable /mpls_state/ldp/ldp_session_summary/num_targeted_sessions (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_num_targeted_sessions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_num_targeted_sessions() directly.

    YANG Description: mpls_num_targeted_sessions
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-targeted-sessions", rest_name="num-targeted-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """num_targeted_sessions must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-targeted-sessions", rest_name="num-targeted-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__num_targeted_sessions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_num_targeted_sessions(self):
    self.__num_targeted_sessions = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-targeted-sessions", rest_name="num-targeted-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)


  def _get_num_operational_targeted_sessions(self):
    """
    Getter method for num_operational_targeted_sessions, mapped from YANG variable /mpls_state/ldp/ldp_session_summary/num_operational_targeted_sessions (uint32)

    YANG Description: mpls_num_operational_targeted_sessions
    """
    return self.__num_operational_targeted_sessions
      
  def _set_num_operational_targeted_sessions(self, v, load=False):
    """
    Setter method for num_operational_targeted_sessions, mapped from YANG variable /mpls_state/ldp/ldp_session_summary/num_operational_targeted_sessions (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_num_operational_targeted_sessions is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_num_operational_targeted_sessions() directly.

    YANG Description: mpls_num_operational_targeted_sessions
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-operational-targeted-sessions", rest_name="num-operational-targeted-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """num_operational_targeted_sessions must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-operational-targeted-sessions", rest_name="num-operational-targeted-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)""",
        })

    self.__num_operational_targeted_sessions = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_num_operational_targeted_sessions(self):
    self.__num_operational_targeted_sessions = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-operational-targeted-sessions", rest_name="num-operational-targeted-sessions", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mpls-operational', defining_module='brocade-mpls-operational', yang_type='uint32', is_config=False)

  num_link_sessions = __builtin__.property(_get_num_link_sessions)
  num_operational_link_sessions = __builtin__.property(_get_num_operational_link_sessions)
  num_targeted_sessions = __builtin__.property(_get_num_targeted_sessions)
  num_operational_targeted_sessions = __builtin__.property(_get_num_operational_targeted_sessions)


  _pyangbind_elements = {'num_link_sessions': num_link_sessions, 'num_operational_link_sessions': num_operational_link_sessions, 'num_targeted_sessions': num_targeted_sessions, 'num_operational_targeted_sessions': num_operational_targeted_sessions, }


