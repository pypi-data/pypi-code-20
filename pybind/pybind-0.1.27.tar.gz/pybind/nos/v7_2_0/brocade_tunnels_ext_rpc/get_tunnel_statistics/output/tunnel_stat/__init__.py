
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class tunnel_stat(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-tunnels-ext - based on the path /brocade_tunnels_ext_rpc/get-tunnel-statistics/output/tunnel-stat. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__id','__tx_frames','__tx_bytes','__rx_frames','__rx_bytes',)

  _yang_name = 'tunnel-stat'
  _rest_name = 'tunnel-stat'

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
    self.__tx_frames = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="tx-frames", rest_name="tx-frames", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='uint64', is_config=True)
    self.__tx_bytes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="tx-bytes", rest_name="tx-bytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='uint64', is_config=True)
    self.__rx_bytes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="rx-bytes", rest_name="rx-bytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='uint64', is_config=True)
    self.__id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..100000']}), is_leaf=True, yang_name="id", rest_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='tnl:tunnel-id-type', is_config=True)
    self.__rx_frames = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="rx-frames", rest_name="rx-frames", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='uint64', is_config=True)

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
      return [u'brocade_tunnels_ext_rpc', u'get-tunnel-statistics', u'output', u'tunnel-stat']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-tunnel-statistics', u'output', u'tunnel-stat']

  def _get_id(self):
    """
    Getter method for id, mapped from YANG variable /brocade_tunnels_ext_rpc/get_tunnel_statistics/output/tunnel_stat/id (tnl:tunnel-id-type)

    YANG Description: Tunnel id.
    """
    return self.__id
      
  def _set_id(self, v, load=False):
    """
    Setter method for id, mapped from YANG variable /brocade_tunnels_ext_rpc/get_tunnel_statistics/output/tunnel_stat/id (tnl:tunnel-id-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_id() directly.

    YANG Description: Tunnel id.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..100000']}), is_leaf=True, yang_name="id", rest_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='tnl:tunnel-id-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """id must be of a type compatible with tnl:tunnel-id-type""",
          'defined-type': "tnl:tunnel-id-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..100000']}), is_leaf=True, yang_name="id", rest_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='tnl:tunnel-id-type', is_config=True)""",
        })

    self.__id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_id(self):
    self.__id = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1..100000']}), is_leaf=True, yang_name="id", rest_name="id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='tnl:tunnel-id-type', is_config=True)


  def _get_tx_frames(self):
    """
    Getter method for tx_frames, mapped from YANG variable /brocade_tunnels_ext_rpc/get_tunnel_statistics/output/tunnel_stat/tx_frames (uint64)

    YANG Description: Number of frames transmitted.
    """
    return self.__tx_frames
      
  def _set_tx_frames(self, v, load=False):
    """
    Setter method for tx_frames, mapped from YANG variable /brocade_tunnels_ext_rpc/get_tunnel_statistics/output/tunnel_stat/tx_frames (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tx_frames is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tx_frames() directly.

    YANG Description: Number of frames transmitted.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="tx-frames", rest_name="tx-frames", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='uint64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tx_frames must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="tx-frames", rest_name="tx-frames", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='uint64', is_config=True)""",
        })

    self.__tx_frames = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tx_frames(self):
    self.__tx_frames = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="tx-frames", rest_name="tx-frames", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='uint64', is_config=True)


  def _get_tx_bytes(self):
    """
    Getter method for tx_bytes, mapped from YANG variable /brocade_tunnels_ext_rpc/get_tunnel_statistics/output/tunnel_stat/tx_bytes (uint64)

    YANG Description: Number of bytes transmitted.
    """
    return self.__tx_bytes
      
  def _set_tx_bytes(self, v, load=False):
    """
    Setter method for tx_bytes, mapped from YANG variable /brocade_tunnels_ext_rpc/get_tunnel_statistics/output/tunnel_stat/tx_bytes (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tx_bytes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tx_bytes() directly.

    YANG Description: Number of bytes transmitted.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="tx-bytes", rest_name="tx-bytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='uint64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tx_bytes must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="tx-bytes", rest_name="tx-bytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='uint64', is_config=True)""",
        })

    self.__tx_bytes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tx_bytes(self):
    self.__tx_bytes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="tx-bytes", rest_name="tx-bytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='uint64', is_config=True)


  def _get_rx_frames(self):
    """
    Getter method for rx_frames, mapped from YANG variable /brocade_tunnels_ext_rpc/get_tunnel_statistics/output/tunnel_stat/rx_frames (uint64)

    YANG Description: Number of frames received.
    """
    return self.__rx_frames
      
  def _set_rx_frames(self, v, load=False):
    """
    Setter method for rx_frames, mapped from YANG variable /brocade_tunnels_ext_rpc/get_tunnel_statistics/output/tunnel_stat/rx_frames (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rx_frames is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rx_frames() directly.

    YANG Description: Number of frames received.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="rx-frames", rest_name="rx-frames", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='uint64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rx_frames must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="rx-frames", rest_name="rx-frames", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='uint64', is_config=True)""",
        })

    self.__rx_frames = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rx_frames(self):
    self.__rx_frames = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="rx-frames", rest_name="rx-frames", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='uint64', is_config=True)


  def _get_rx_bytes(self):
    """
    Getter method for rx_bytes, mapped from YANG variable /brocade_tunnels_ext_rpc/get_tunnel_statistics/output/tunnel_stat/rx_bytes (uint64)

    YANG Description: Number of bytes received. Value will not be
present if the hardware does not support rx byte
counter.
    """
    return self.__rx_bytes
      
  def _set_rx_bytes(self, v, load=False):
    """
    Setter method for rx_bytes, mapped from YANG variable /brocade_tunnels_ext_rpc/get_tunnel_statistics/output/tunnel_stat/rx_bytes (uint64)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rx_bytes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rx_bytes() directly.

    YANG Description: Number of bytes received. Value will not be
present if the hardware does not support rx byte
counter.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="rx-bytes", rest_name="rx-bytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='uint64', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rx_bytes must be of a type compatible with uint64""",
          'defined-type': "uint64",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="rx-bytes", rest_name="rx-bytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='uint64', is_config=True)""",
        })

    self.__rx_bytes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rx_bytes(self):
    self.__rx_bytes = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range':  ['0..18446744073709551615']}, int_size=64), is_leaf=True, yang_name="rx-bytes", rest_name="rx-bytes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='uint64', is_config=True)

  id = __builtin__.property(_get_id, _set_id)
  tx_frames = __builtin__.property(_get_tx_frames, _set_tx_frames)
  tx_bytes = __builtin__.property(_get_tx_bytes, _set_tx_bytes)
  rx_frames = __builtin__.property(_get_rx_frames, _set_rx_frames)
  rx_bytes = __builtin__.property(_get_rx_bytes, _set_rx_bytes)


  _pyangbind_elements = {'id': id, 'tx_frames': tx_frames, 'tx_bytes': tx_bytes, 'rx_frames': rx_frames, 'rx_bytes': rx_bytes, }


