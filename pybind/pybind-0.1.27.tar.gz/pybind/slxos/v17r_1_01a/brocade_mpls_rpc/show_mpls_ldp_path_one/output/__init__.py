
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ldp_upstr_session_list
import ldp_downstr_session_list
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-ldp-path-one/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ldp_destination_route','__ldp_upstr_session_list','__ldp_downstr_session_list',)

  _yang_name = 'output'
  _rest_name = 'output'

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
    self.__ldp_downstr_session_list = YANGDynClass(base=YANGListType("ldp_downstr_session_ip",ldp_downstr_session_list.ldp_downstr_session_list, yang_name="ldp-downstr-session-list", rest_name="ldp-downstr-session-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ldp-downstr-session-ip', extensions=None), is_container='list', yang_name="ldp-downstr-session-list", rest_name="ldp-downstr-session-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)
    self.__ldp_upstr_session_list = YANGDynClass(base=YANGListType("ldp_upstr_session",ldp_upstr_session_list.ldp_upstr_session_list, yang_name="ldp-upstr-session-list", rest_name="ldp-upstr-session-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ldp-upstr-session', extensions=None), is_container='list', yang_name="ldp-upstr-session-list", rest_name="ldp-upstr-session-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)
    self.__ldp_destination_route = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="ldp-destination-route", rest_name="ldp-destination-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-prefix', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-ldp-path-one', u'output']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-ldp-path-one', u'output']

  def _get_ldp_destination_route(self):
    """
    Getter method for ldp_destination_route, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_path_one/output/ldp_destination_route (inet:ipv4-prefix)

    YANG Description: Destination route
    """
    return self.__ldp_destination_route
      
  def _set_ldp_destination_route(self, v, load=False):
    """
    Setter method for ldp_destination_route, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_path_one/output/ldp_destination_route (inet:ipv4-prefix)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_destination_route is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_destination_route() directly.

    YANG Description: Destination route
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="ldp-destination-route", rest_name="ldp-destination-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-prefix', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_destination_route must be of a type compatible with inet:ipv4-prefix""",
          'defined-type': "inet:ipv4-prefix",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="ldp-destination-route", rest_name="ldp-destination-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-prefix', is_config=True)""",
        })

    self.__ldp_destination_route = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_destination_route(self):
    self.__ldp_destination_route = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'}), is_leaf=True, yang_name="ldp-destination-route", rest_name="ldp-destination-route", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-prefix', is_config=True)


  def _get_ldp_upstr_session_list(self):
    """
    Getter method for ldp_upstr_session_list, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_path_one/output/ldp_upstr_session_list (list)
    """
    return self.__ldp_upstr_session_list
      
  def _set_ldp_upstr_session_list(self, v, load=False):
    """
    Setter method for ldp_upstr_session_list, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_path_one/output/ldp_upstr_session_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_upstr_session_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_upstr_session_list() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("ldp_upstr_session",ldp_upstr_session_list.ldp_upstr_session_list, yang_name="ldp-upstr-session-list", rest_name="ldp-upstr-session-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ldp-upstr-session', extensions=None), is_container='list', yang_name="ldp-upstr-session-list", rest_name="ldp-upstr-session-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_upstr_session_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ldp_upstr_session",ldp_upstr_session_list.ldp_upstr_session_list, yang_name="ldp-upstr-session-list", rest_name="ldp-upstr-session-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ldp-upstr-session', extensions=None), is_container='list', yang_name="ldp-upstr-session-list", rest_name="ldp-upstr-session-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)""",
        })

    self.__ldp_upstr_session_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_upstr_session_list(self):
    self.__ldp_upstr_session_list = YANGDynClass(base=YANGListType("ldp_upstr_session",ldp_upstr_session_list.ldp_upstr_session_list, yang_name="ldp-upstr-session-list", rest_name="ldp-upstr-session-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ldp-upstr-session', extensions=None), is_container='list', yang_name="ldp-upstr-session-list", rest_name="ldp-upstr-session-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)


  def _get_ldp_downstr_session_list(self):
    """
    Getter method for ldp_downstr_session_list, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_path_one/output/ldp_downstr_session_list (list)
    """
    return self.__ldp_downstr_session_list
      
  def _set_ldp_downstr_session_list(self, v, load=False):
    """
    Setter method for ldp_downstr_session_list, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_path_one/output/ldp_downstr_session_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_downstr_session_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_downstr_session_list() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("ldp_downstr_session_ip",ldp_downstr_session_list.ldp_downstr_session_list, yang_name="ldp-downstr-session-list", rest_name="ldp-downstr-session-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ldp-downstr-session-ip', extensions=None), is_container='list', yang_name="ldp-downstr-session-list", rest_name="ldp-downstr-session-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_downstr_session_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("ldp_downstr_session_ip",ldp_downstr_session_list.ldp_downstr_session_list, yang_name="ldp-downstr-session-list", rest_name="ldp-downstr-session-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ldp-downstr-session-ip', extensions=None), is_container='list', yang_name="ldp-downstr-session-list", rest_name="ldp-downstr-session-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)""",
        })

    self.__ldp_downstr_session_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_downstr_session_list(self):
    self.__ldp_downstr_session_list = YANGDynClass(base=YANGListType("ldp_downstr_session_ip",ldp_downstr_session_list.ldp_downstr_session_list, yang_name="ldp-downstr-session-list", rest_name="ldp-downstr-session-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='ldp-downstr-session-ip', extensions=None), is_container='list', yang_name="ldp-downstr-session-list", rest_name="ldp-downstr-session-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)

  ldp_destination_route = __builtin__.property(_get_ldp_destination_route, _set_ldp_destination_route)
  ldp_upstr_session_list = __builtin__.property(_get_ldp_upstr_session_list, _set_ldp_upstr_session_list)
  ldp_downstr_session_list = __builtin__.property(_get_ldp_downstr_session_list, _set_ldp_downstr_session_list)


  _pyangbind_elements = {'ldp_destination_route': ldp_destination_route, 'ldp_upstr_session_list': ldp_upstr_session_list, 'ldp_downstr_session_list': ldp_downstr_session_list, }


