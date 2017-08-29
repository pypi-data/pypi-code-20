
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class mpls_rsvp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-rsvp/output/mpls-rsvp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__rsvp_protocol_status','__rsvp_refresh_interval','__rsvp_refresh_multiple','__rsvp_transport_address','__rsvp_message_id_epoch',)

  _yang_name = 'mpls-rsvp'
  _rest_name = 'mpls-rsvp'

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
    self.__rsvp_refresh_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rsvp-refresh-interval", rest_name="rsvp-refresh-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__rsvp_message_id_epoch = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="rsvp-message-id-epoch", rest_name="rsvp-message-id-epoch", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__rsvp_refresh_multiple = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rsvp-refresh-multiple", rest_name="rsvp-refresh-multiple", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__rsvp_transport_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="rsvp-transport-address", rest_name="rsvp-transport-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    self.__rsvp_protocol_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="rsvp-protocol-status", rest_name="rsvp-protocol-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-rsvp', u'output', u'mpls-rsvp']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-rsvp', u'output', u'mpls-rsvp']

  def _get_rsvp_protocol_status(self):
    """
    Getter method for rsvp_protocol_status, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp/output/mpls_rsvp/rsvp_protocol_status (boolean)

    YANG Description: Status of RSVP protocol
    """
    return self.__rsvp_protocol_status
      
  def _set_rsvp_protocol_status(self, v, load=False):
    """
    Setter method for rsvp_protocol_status, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp/output/mpls_rsvp/rsvp_protocol_status (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rsvp_protocol_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rsvp_protocol_status() directly.

    YANG Description: Status of RSVP protocol
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="rsvp-protocol-status", rest_name="rsvp-protocol-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rsvp_protocol_status must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="rsvp-protocol-status", rest_name="rsvp-protocol-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)""",
        })

    self.__rsvp_protocol_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rsvp_protocol_status(self):
    self.__rsvp_protocol_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="rsvp-protocol-status", rest_name="rsvp-protocol-status", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='boolean', is_config=True)


  def _get_rsvp_refresh_interval(self):
    """
    Getter method for rsvp_refresh_interval, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp/output/mpls_rsvp/rsvp_refresh_interval (uint32)

    YANG Description: RSVP Refresh Interval (R)
    """
    return self.__rsvp_refresh_interval
      
  def _set_rsvp_refresh_interval(self, v, load=False):
    """
    Setter method for rsvp_refresh_interval, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp/output/mpls_rsvp/rsvp_refresh_interval (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rsvp_refresh_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rsvp_refresh_interval() directly.

    YANG Description: RSVP Refresh Interval (R)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rsvp-refresh-interval", rest_name="rsvp-refresh-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rsvp_refresh_interval must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rsvp-refresh-interval", rest_name="rsvp-refresh-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__rsvp_refresh_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rsvp_refresh_interval(self):
    self.__rsvp_refresh_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rsvp-refresh-interval", rest_name="rsvp-refresh-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_rsvp_refresh_multiple(self):
    """
    Getter method for rsvp_refresh_multiple, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp/output/mpls_rsvp/rsvp_refresh_multiple (uint32)

    YANG Description: RSVP Refresh Multiple (K)
    """
    return self.__rsvp_refresh_multiple
      
  def _set_rsvp_refresh_multiple(self, v, load=False):
    """
    Setter method for rsvp_refresh_multiple, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp/output/mpls_rsvp/rsvp_refresh_multiple (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rsvp_refresh_multiple is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rsvp_refresh_multiple() directly.

    YANG Description: RSVP Refresh Multiple (K)
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rsvp-refresh-multiple", rest_name="rsvp-refresh-multiple", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rsvp_refresh_multiple must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rsvp-refresh-multiple", rest_name="rsvp-refresh-multiple", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__rsvp_refresh_multiple = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rsvp_refresh_multiple(self):
    self.__rsvp_refresh_multiple = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="rsvp-refresh-multiple", rest_name="rsvp-refresh-multiple", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_rsvp_transport_address(self):
    """
    Getter method for rsvp_transport_address, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp/output/mpls_rsvp/rsvp_transport_address (inet:ipv4-address)

    YANG Description: RSVP Transport Address
    """
    return self.__rsvp_transport_address
      
  def _set_rsvp_transport_address(self, v, load=False):
    """
    Setter method for rsvp_transport_address, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp/output/mpls_rsvp/rsvp_transport_address (inet:ipv4-address)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rsvp_transport_address is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rsvp_transport_address() directly.

    YANG Description: RSVP Transport Address
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="rsvp-transport-address", rest_name="rsvp-transport-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rsvp_transport_address must be of a type compatible with inet:ipv4-address""",
          'defined-type': "inet:ipv4-address",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="rsvp-transport-address", rest_name="rsvp-transport-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)""",
        })

    self.__rsvp_transport_address = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rsvp_transport_address(self):
    self.__rsvp_transport_address = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}), is_leaf=True, yang_name="rsvp-transport-address", rest_name="rsvp-transport-address", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='inet:ipv4-address', is_config=True)


  def _get_rsvp_message_id_epoch(self):
    """
    Getter method for rsvp_message_id_epoch, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp/output/mpls_rsvp/rsvp_message_id_epoch (uint32)

    YANG Description: MsgId Epoch
    """
    return self.__rsvp_message_id_epoch
      
  def _set_rsvp_message_id_epoch(self, v, load=False):
    """
    Setter method for rsvp_message_id_epoch, mapped from YANG variable /brocade_mpls_rpc/show_mpls_rsvp/output/mpls_rsvp/rsvp_message_id_epoch (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rsvp_message_id_epoch is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rsvp_message_id_epoch() directly.

    YANG Description: MsgId Epoch
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="rsvp-message-id-epoch", rest_name="rsvp-message-id-epoch", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rsvp_message_id_epoch must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="rsvp-message-id-epoch", rest_name="rsvp-message-id-epoch", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__rsvp_message_id_epoch = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rsvp_message_id_epoch(self):
    self.__rsvp_message_id_epoch = YANGDynClass(base=TypedListType(allowed_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)), is_leaf=False, yang_name="rsvp-message-id-epoch", rest_name="rsvp-message-id-epoch", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

  rsvp_protocol_status = __builtin__.property(_get_rsvp_protocol_status, _set_rsvp_protocol_status)
  rsvp_refresh_interval = __builtin__.property(_get_rsvp_refresh_interval, _set_rsvp_refresh_interval)
  rsvp_refresh_multiple = __builtin__.property(_get_rsvp_refresh_multiple, _set_rsvp_refresh_multiple)
  rsvp_transport_address = __builtin__.property(_get_rsvp_transport_address, _set_rsvp_transport_address)
  rsvp_message_id_epoch = __builtin__.property(_get_rsvp_message_id_epoch, _set_rsvp_message_id_epoch)


  _pyangbind_elements = {'rsvp_protocol_status': rsvp_protocol_status, 'rsvp_refresh_interval': rsvp_refresh_interval, 'rsvp_refresh_multiple': rsvp_refresh_multiple, 'rsvp_transport_address': rsvp_transport_address, 'rsvp_message_id_epoch': rsvp_message_id_epoch, }


