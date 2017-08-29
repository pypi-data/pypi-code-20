
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class input(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-ldp-peer-det/input. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ldp_peer_brief','__ldp_peer_detail','__ldp_peer_ip','__ldp_peer_ip_lblspid',)

  _yang_name = 'input'
  _rest_name = 'input'

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
    self.__ldp_peer_brief = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ldp-peer-brief", rest_name="ldp-peer-brief", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    self.__ldp_peer_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-peer-ip", rest_name="ldp-peer-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    self.__ldp_peer_ip_lblspid = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-peer-ip-lblspid", rest_name="ldp-peer-ip-lblspid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__ldp_peer_detail = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ldp-peer-detail", rest_name="ldp-peer-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-ldp-peer-det', u'input']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-ldp-peer-det', u'input']

  def _get_ldp_peer_brief(self):
    """
    Getter method for ldp_peer_brief, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_peer_det/input/ldp_peer_brief (boolean)

    YANG Description: Brief information
    """
    return self.__ldp_peer_brief
      
  def _set_ldp_peer_brief(self, v, load=False):
    """
    Setter method for ldp_peer_brief, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_peer_det/input/ldp_peer_brief (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_peer_brief is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_peer_brief() directly.

    YANG Description: Brief information
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ldp-peer-brief", rest_name="ldp-peer-brief", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_peer_brief must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ldp-peer-brief", rest_name="ldp-peer-brief", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__ldp_peer_brief = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_peer_brief(self):
    self.__ldp_peer_brief = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ldp-peer-brief", rest_name="ldp-peer-brief", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_ldp_peer_detail(self):
    """
    Getter method for ldp_peer_detail, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_peer_det/input/ldp_peer_detail (boolean)

    YANG Description: Detailed information
    """
    return self.__ldp_peer_detail
      
  def _set_ldp_peer_detail(self, v, load=False):
    """
    Setter method for ldp_peer_detail, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_peer_det/input/ldp_peer_detail (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_peer_detail is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_peer_detail() directly.

    YANG Description: Detailed information
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ldp-peer-detail", rest_name="ldp-peer-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_peer_detail must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ldp-peer-detail", rest_name="ldp-peer-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__ldp_peer_detail = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_peer_detail(self):
    self.__ldp_peer_detail = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ldp-peer-detail", rest_name="ldp-peer-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_ldp_peer_ip(self):
    """
    Getter method for ldp_peer_ip, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_peer_det/input/ldp_peer_ip (inet:ipv4-address)

    YANG Description: Peer IP Address
    """
    return self.__ldp_peer_ip
      
  def _set_ldp_peer_ip(self, v, load=False):
    """
    Setter method for ldp_peer_ip, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_peer_det/input/ldp_peer_ip (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_peer_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_peer_ip() directly.

    YANG Description: Peer IP Address
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-peer-ip", rest_name="ldp-peer-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_peer_ip must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-peer-ip", rest_name="ldp-peer-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__ldp_peer_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_peer_ip(self):
    self.__ldp_peer_ip = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="ldp-peer-ip", rest_name="ldp-peer-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)


  def _get_ldp_peer_ip_lblspid(self):
    """
    Getter method for ldp_peer_ip_lblspid, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_peer_det/input/ldp_peer_ip_lblspid (uint32)

    YANG Description: Peer label space id
    """
    return self.__ldp_peer_ip_lblspid
      
  def _set_ldp_peer_ip_lblspid(self, v, load=False):
    """
    Setter method for ldp_peer_ip_lblspid, mapped from YANG variable /brocade_mpls_rpc/show_mpls_ldp_peer_det/input/ldp_peer_ip_lblspid (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_peer_ip_lblspid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_peer_ip_lblspid() directly.

    YANG Description: Peer label space id
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-peer-ip-lblspid", rest_name="ldp-peer-ip-lblspid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_peer_ip_lblspid must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-peer-ip-lblspid", rest_name="ldp-peer-ip-lblspid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__ldp_peer_ip_lblspid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_peer_ip_lblspid(self):
    self.__ldp_peer_ip_lblspid = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="ldp-peer-ip-lblspid", rest_name="ldp-peer-ip-lblspid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

  ldp_peer_brief = __builtin__.property(_get_ldp_peer_brief, _set_ldp_peer_brief)
  ldp_peer_detail = __builtin__.property(_get_ldp_peer_detail, _set_ldp_peer_detail)
  ldp_peer_ip = __builtin__.property(_get_ldp_peer_ip, _set_ldp_peer_ip)
  ldp_peer_ip_lblspid = __builtin__.property(_get_ldp_peer_ip_lblspid, _set_ldp_peer_ip_lblspid)


  _pyangbind_elements = {'ldp_peer_brief': ldp_peer_brief, 'ldp_peer_detail': ldp_peer_detail, 'ldp_peer_ip': ldp_peer_ip, 'ldp_peer_ip_lblspid': ldp_peer_ip_lblspid, }


