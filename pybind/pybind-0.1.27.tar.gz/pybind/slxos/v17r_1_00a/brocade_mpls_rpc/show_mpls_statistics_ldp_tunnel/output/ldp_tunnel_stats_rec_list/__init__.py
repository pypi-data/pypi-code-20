
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ldp_tunnel_stats_rec_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-statistics-ldp-tunnel/output/ldp-tunnel-stats-rec-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ldp_tunnel_stats_vif','__ldp_tunnel_stats_total_packets','__ldp_tunnel_stats_total_bytes','__ldp_tunnel_stats_rate_pps','__ldp_tunnel_stats_rate_bps',)

  _yang_name = 'ldp-tunnel-stats-rec-list'
  _rest_name = 'ldp-tunnel-stats-rec-list'

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
    self.__ldp_tunnel_stats_rate_pps = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-tunnel-stats-rate-pps", rest_name="ldp-tunnel-stats-rate-pps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)
    self.__ldp_tunnel_stats_total_packets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-tunnel-stats-total-packets", rest_name="ldp-tunnel-stats-total-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)
    self.__ldp_tunnel_stats_rate_bps = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-tunnel-stats-rate-bps", rest_name="ldp-tunnel-stats-rate-bps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)
    self.__ldp_tunnel_stats_total_bytes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-tunnel-stats-total-bytes", rest_name="ldp-tunnel-stats-total-bytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)
    self.__ldp_tunnel_stats_vif = YANGDynClass(base=unicode, is_leaf=True, yang_name="ldp-tunnel-stats-vif", rest_name="ldp-tunnel-stats-vif", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-statistics-ldp-tunnel', u'output', u'ldp-tunnel-stats-rec-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-statistics-ldp-tunnel', u'output', u'ldp-tunnel-stats-rec-list']

  def _get_ldp_tunnel_stats_vif(self):
    """
    Getter method for ldp_tunnel_stats_vif, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_ldp_tunnel/output/ldp_tunnel_stats_rec_list/ldp_tunnel_stats_vif (string)

    YANG Description: Tunnel interface index
    """
    return self.__ldp_tunnel_stats_vif
      
  def _set_ldp_tunnel_stats_vif(self, v, load=False):
    """
    Setter method for ldp_tunnel_stats_vif, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_ldp_tunnel/output/ldp_tunnel_stats_rec_list/ldp_tunnel_stats_vif (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_tunnel_stats_vif is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_tunnel_stats_vif() directly.

    YANG Description: Tunnel interface index
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="ldp-tunnel-stats-vif", rest_name="ldp-tunnel-stats-vif", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_tunnel_stats_vif must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="ldp-tunnel-stats-vif", rest_name="ldp-tunnel-stats-vif", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__ldp_tunnel_stats_vif = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_tunnel_stats_vif(self):
    self.__ldp_tunnel_stats_vif = YANGDynClass(base=unicode, is_leaf=True, yang_name="ldp-tunnel-stats-vif", rest_name="ldp-tunnel-stats-vif", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_ldp_tunnel_stats_total_packets(self):
    """
    Getter method for ldp_tunnel_stats_total_packets, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_ldp_tunnel/output/ldp_tunnel_stats_rec_list/ldp_tunnel_stats_total_packets (uint64)

    YANG Description: Total Packets
    """
    return self.__ldp_tunnel_stats_total_packets
      
  def _set_ldp_tunnel_stats_total_packets(self, v, load=False):
    """
    Setter method for ldp_tunnel_stats_total_packets, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_ldp_tunnel/output/ldp_tunnel_stats_rec_list/ldp_tunnel_stats_total_packets (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_tunnel_stats_total_packets is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_tunnel_stats_total_packets() directly.

    YANG Description: Total Packets
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-tunnel-stats-total-packets", rest_name="ldp-tunnel-stats-total-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_tunnel_stats_total_packets must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-tunnel-stats-total-packets", rest_name="ldp-tunnel-stats-total-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)""",
        })

    self.__ldp_tunnel_stats_total_packets = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_tunnel_stats_total_packets(self):
    self.__ldp_tunnel_stats_total_packets = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-tunnel-stats-total-packets", rest_name="ldp-tunnel-stats-total-packets", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)


  def _get_ldp_tunnel_stats_total_bytes(self):
    """
    Getter method for ldp_tunnel_stats_total_bytes, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_ldp_tunnel/output/ldp_tunnel_stats_rec_list/ldp_tunnel_stats_total_bytes (uint64)

    YANG Description: Total Bytes
    """
    return self.__ldp_tunnel_stats_total_bytes
      
  def _set_ldp_tunnel_stats_total_bytes(self, v, load=False):
    """
    Setter method for ldp_tunnel_stats_total_bytes, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_ldp_tunnel/output/ldp_tunnel_stats_rec_list/ldp_tunnel_stats_total_bytes (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_tunnel_stats_total_bytes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_tunnel_stats_total_bytes() directly.

    YANG Description: Total Bytes
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-tunnel-stats-total-bytes", rest_name="ldp-tunnel-stats-total-bytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_tunnel_stats_total_bytes must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-tunnel-stats-total-bytes", rest_name="ldp-tunnel-stats-total-bytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)""",
        })

    self.__ldp_tunnel_stats_total_bytes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_tunnel_stats_total_bytes(self):
    self.__ldp_tunnel_stats_total_bytes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-tunnel-stats-total-bytes", rest_name="ldp-tunnel-stats-total-bytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)


  def _get_ldp_tunnel_stats_rate_pps(self):
    """
    Getter method for ldp_tunnel_stats_rate_pps, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_ldp_tunnel/output/ldp_tunnel_stats_rec_list/ldp_tunnel_stats_rate_pps (uint64)

    YANG Description: Rate in pps
    """
    return self.__ldp_tunnel_stats_rate_pps
      
  def _set_ldp_tunnel_stats_rate_pps(self, v, load=False):
    """
    Setter method for ldp_tunnel_stats_rate_pps, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_ldp_tunnel/output/ldp_tunnel_stats_rec_list/ldp_tunnel_stats_rate_pps (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_tunnel_stats_rate_pps is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_tunnel_stats_rate_pps() directly.

    YANG Description: Rate in pps
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-tunnel-stats-rate-pps", rest_name="ldp-tunnel-stats-rate-pps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_tunnel_stats_rate_pps must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-tunnel-stats-rate-pps", rest_name="ldp-tunnel-stats-rate-pps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)""",
        })

    self.__ldp_tunnel_stats_rate_pps = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_tunnel_stats_rate_pps(self):
    self.__ldp_tunnel_stats_rate_pps = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-tunnel-stats-rate-pps", rest_name="ldp-tunnel-stats-rate-pps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)


  def _get_ldp_tunnel_stats_rate_bps(self):
    """
    Getter method for ldp_tunnel_stats_rate_bps, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_ldp_tunnel/output/ldp_tunnel_stats_rec_list/ldp_tunnel_stats_rate_bps (uint64)

    YANG Description: Rate in bps
    """
    return self.__ldp_tunnel_stats_rate_bps
      
  def _set_ldp_tunnel_stats_rate_bps(self, v, load=False):
    """
    Setter method for ldp_tunnel_stats_rate_bps, mapped from YANG variable /brocade_mpls_rpc/show_mpls_statistics_ldp_tunnel/output/ldp_tunnel_stats_rec_list/ldp_tunnel_stats_rate_bps (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ldp_tunnel_stats_rate_bps is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ldp_tunnel_stats_rate_bps() directly.

    YANG Description: Rate in bps
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-tunnel-stats-rate-bps", rest_name="ldp-tunnel-stats-rate-bps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ldp_tunnel_stats_rate_bps must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-tunnel-stats-rate-bps", rest_name="ldp-tunnel-stats-rate-bps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)""",
        })

    self.__ldp_tunnel_stats_rate_bps = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ldp_tunnel_stats_rate_bps(self):
    self.__ldp_tunnel_stats_rate_bps = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="ldp-tunnel-stats-rate-bps", rest_name="ldp-tunnel-stats-rate-bps", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint64', is_config=True)

  ldp_tunnel_stats_vif = __builtin__.property(_get_ldp_tunnel_stats_vif, _set_ldp_tunnel_stats_vif)
  ldp_tunnel_stats_total_packets = __builtin__.property(_get_ldp_tunnel_stats_total_packets, _set_ldp_tunnel_stats_total_packets)
  ldp_tunnel_stats_total_bytes = __builtin__.property(_get_ldp_tunnel_stats_total_bytes, _set_ldp_tunnel_stats_total_bytes)
  ldp_tunnel_stats_rate_pps = __builtin__.property(_get_ldp_tunnel_stats_rate_pps, _set_ldp_tunnel_stats_rate_pps)
  ldp_tunnel_stats_rate_bps = __builtin__.property(_get_ldp_tunnel_stats_rate_bps, _set_ldp_tunnel_stats_rate_bps)


  _pyangbind_elements = {'ldp_tunnel_stats_vif': ldp_tunnel_stats_vif, 'ldp_tunnel_stats_total_packets': ldp_tunnel_stats_total_packets, 'ldp_tunnel_stats_total_bytes': ldp_tunnel_stats_total_bytes, 'ldp_tunnel_stats_rate_pps': ldp_tunnel_stats_rate_pps, 'ldp_tunnel_stats_rate_bps': ldp_tunnel_stats_rate_bps, }


