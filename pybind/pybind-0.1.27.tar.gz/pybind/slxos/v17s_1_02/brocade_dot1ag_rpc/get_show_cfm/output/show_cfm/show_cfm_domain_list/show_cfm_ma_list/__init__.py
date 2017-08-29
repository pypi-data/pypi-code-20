
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import show_cfm_ma_list_
class show_cfm_ma_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-dot1ag - based on the path /brocade_dot1ag_rpc/get-show-cfm/output/show-cfm/show-cfm-domain-list/show-cfm-ma-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__show_cfm_ma_name','__show_cfm_ma_idx','__show_cfm_ccm_interval','__show_cfm_vid','__show_cfm_priority','__show_cfm_eth_ais_tx','__show_cfm_eth_ais_rx','__show_cfm_eth_ais_int','__show_cfm_ma_list',)

  _yang_name = 'show-cfm-ma-list'
  _rest_name = 'show-cfm-ma-list'

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
    self.__show_cfm_ccm_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-ccm-interval", rest_name="show-cfm-ccm-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)
    self.__show_cfm_ma_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="show-cfm-ma-name", rest_name="show-cfm-ma-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='string', is_config=True)
    self.__show_cfm_ma_idx = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-ma-idx", rest_name="show-cfm-ma-idx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)
    self.__show_cfm_eth_ais_int = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-eth-ais-int", rest_name="show-cfm-eth-ais-int", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)
    self.__show_cfm_eth_ais_tx = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-eth-ais-tx", rest_name="show-cfm-eth-ais-tx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)
    self.__show_cfm_priority = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-priority", rest_name="show-cfm-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)
    self.__show_cfm_vid = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-vid", rest_name="show-cfm-vid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)
    self.__show_cfm_eth_ais_rx = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-eth-ais-rx", rest_name="show-cfm-eth-ais-rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)
    self.__show_cfm_ma_list = YANGDynClass(base=YANGListType(False,show_cfm_ma_list_.show_cfm_ma_list, yang_name="show-cfm-ma-list", rest_name="show-cfm-ma-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="show-cfm-ma-list", rest_name="show-cfm-ma-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='list', is_config=True)

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
      return [u'brocade_dot1ag_rpc', u'get-show-cfm', u'output', u'show-cfm', u'show-cfm-domain-list', u'show-cfm-ma-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-show-cfm', u'output', u'show-cfm', u'show-cfm-domain-list', u'show-cfm-ma-list']

  def _get_show_cfm_ma_name(self):
    """
    Getter method for show_cfm_ma_name, mapped from YANG variable /brocade_dot1ag_rpc/get_show_cfm/output/show_cfm/show_cfm_domain_list/show_cfm_ma_list/show_cfm_ma_name (string)
    """
    return self.__show_cfm_ma_name
      
  def _set_show_cfm_ma_name(self, v, load=False):
    """
    Setter method for show_cfm_ma_name, mapped from YANG variable /brocade_dot1ag_rpc/get_show_cfm/output/show_cfm/show_cfm_domain_list/show_cfm_ma_list/show_cfm_ma_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_cfm_ma_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_cfm_ma_name() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="show-cfm-ma-name", rest_name="show-cfm-ma-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_cfm_ma_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="show-cfm-ma-name", rest_name="show-cfm-ma-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='string', is_config=True)""",
        })

    self.__show_cfm_ma_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_cfm_ma_name(self):
    self.__show_cfm_ma_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="show-cfm-ma-name", rest_name="show-cfm-ma-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='string', is_config=True)


  def _get_show_cfm_ma_idx(self):
    """
    Getter method for show_cfm_ma_idx, mapped from YANG variable /brocade_dot1ag_rpc/get_show_cfm/output/show_cfm/show_cfm_domain_list/show_cfm_ma_list/show_cfm_ma_idx (uint32)
    """
    return self.__show_cfm_ma_idx
      
  def _set_show_cfm_ma_idx(self, v, load=False):
    """
    Setter method for show_cfm_ma_idx, mapped from YANG variable /brocade_dot1ag_rpc/get_show_cfm/output/show_cfm/show_cfm_domain_list/show_cfm_ma_list/show_cfm_ma_idx (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_cfm_ma_idx is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_cfm_ma_idx() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-ma-idx", rest_name="show-cfm-ma-idx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_cfm_ma_idx must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-ma-idx", rest_name="show-cfm-ma-idx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)""",
        })

    self.__show_cfm_ma_idx = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_cfm_ma_idx(self):
    self.__show_cfm_ma_idx = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-ma-idx", rest_name="show-cfm-ma-idx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)


  def _get_show_cfm_ccm_interval(self):
    """
    Getter method for show_cfm_ccm_interval, mapped from YANG variable /brocade_dot1ag_rpc/get_show_cfm/output/show_cfm/show_cfm_domain_list/show_cfm_ma_list/show_cfm_ccm_interval (uint32)
    """
    return self.__show_cfm_ccm_interval
      
  def _set_show_cfm_ccm_interval(self, v, load=False):
    """
    Setter method for show_cfm_ccm_interval, mapped from YANG variable /brocade_dot1ag_rpc/get_show_cfm/output/show_cfm/show_cfm_domain_list/show_cfm_ma_list/show_cfm_ccm_interval (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_cfm_ccm_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_cfm_ccm_interval() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-ccm-interval", rest_name="show-cfm-ccm-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_cfm_ccm_interval must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-ccm-interval", rest_name="show-cfm-ccm-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)""",
        })

    self.__show_cfm_ccm_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_cfm_ccm_interval(self):
    self.__show_cfm_ccm_interval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-ccm-interval", rest_name="show-cfm-ccm-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)


  def _get_show_cfm_vid(self):
    """
    Getter method for show_cfm_vid, mapped from YANG variable /brocade_dot1ag_rpc/get_show_cfm/output/show_cfm/show_cfm_domain_list/show_cfm_ma_list/show_cfm_vid (uint32)
    """
    return self.__show_cfm_vid
      
  def _set_show_cfm_vid(self, v, load=False):
    """
    Setter method for show_cfm_vid, mapped from YANG variable /brocade_dot1ag_rpc/get_show_cfm/output/show_cfm/show_cfm_domain_list/show_cfm_ma_list/show_cfm_vid (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_cfm_vid is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_cfm_vid() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-vid", rest_name="show-cfm-vid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_cfm_vid must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-vid", rest_name="show-cfm-vid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)""",
        })

    self.__show_cfm_vid = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_cfm_vid(self):
    self.__show_cfm_vid = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-vid", rest_name="show-cfm-vid", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)


  def _get_show_cfm_priority(self):
    """
    Getter method for show_cfm_priority, mapped from YANG variable /brocade_dot1ag_rpc/get_show_cfm/output/show_cfm/show_cfm_domain_list/show_cfm_ma_list/show_cfm_priority (uint32)
    """
    return self.__show_cfm_priority
      
  def _set_show_cfm_priority(self, v, load=False):
    """
    Setter method for show_cfm_priority, mapped from YANG variable /brocade_dot1ag_rpc/get_show_cfm/output/show_cfm/show_cfm_domain_list/show_cfm_ma_list/show_cfm_priority (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_cfm_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_cfm_priority() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-priority", rest_name="show-cfm-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_cfm_priority must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-priority", rest_name="show-cfm-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)""",
        })

    self.__show_cfm_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_cfm_priority(self):
    self.__show_cfm_priority = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-priority", rest_name="show-cfm-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)


  def _get_show_cfm_eth_ais_tx(self):
    """
    Getter method for show_cfm_eth_ais_tx, mapped from YANG variable /brocade_dot1ag_rpc/get_show_cfm/output/show_cfm/show_cfm_domain_list/show_cfm_ma_list/show_cfm_eth_ais_tx (uint32)
    """
    return self.__show_cfm_eth_ais_tx
      
  def _set_show_cfm_eth_ais_tx(self, v, load=False):
    """
    Setter method for show_cfm_eth_ais_tx, mapped from YANG variable /brocade_dot1ag_rpc/get_show_cfm/output/show_cfm/show_cfm_domain_list/show_cfm_ma_list/show_cfm_eth_ais_tx (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_cfm_eth_ais_tx is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_cfm_eth_ais_tx() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-eth-ais-tx", rest_name="show-cfm-eth-ais-tx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_cfm_eth_ais_tx must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-eth-ais-tx", rest_name="show-cfm-eth-ais-tx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)""",
        })

    self.__show_cfm_eth_ais_tx = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_cfm_eth_ais_tx(self):
    self.__show_cfm_eth_ais_tx = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-eth-ais-tx", rest_name="show-cfm-eth-ais-tx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)


  def _get_show_cfm_eth_ais_rx(self):
    """
    Getter method for show_cfm_eth_ais_rx, mapped from YANG variable /brocade_dot1ag_rpc/get_show_cfm/output/show_cfm/show_cfm_domain_list/show_cfm_ma_list/show_cfm_eth_ais_rx (uint32)
    """
    return self.__show_cfm_eth_ais_rx
      
  def _set_show_cfm_eth_ais_rx(self, v, load=False):
    """
    Setter method for show_cfm_eth_ais_rx, mapped from YANG variable /brocade_dot1ag_rpc/get_show_cfm/output/show_cfm/show_cfm_domain_list/show_cfm_ma_list/show_cfm_eth_ais_rx (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_cfm_eth_ais_rx is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_cfm_eth_ais_rx() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-eth-ais-rx", rest_name="show-cfm-eth-ais-rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_cfm_eth_ais_rx must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-eth-ais-rx", rest_name="show-cfm-eth-ais-rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)""",
        })

    self.__show_cfm_eth_ais_rx = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_cfm_eth_ais_rx(self):
    self.__show_cfm_eth_ais_rx = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-eth-ais-rx", rest_name="show-cfm-eth-ais-rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)


  def _get_show_cfm_eth_ais_int(self):
    """
    Getter method for show_cfm_eth_ais_int, mapped from YANG variable /brocade_dot1ag_rpc/get_show_cfm/output/show_cfm/show_cfm_domain_list/show_cfm_ma_list/show_cfm_eth_ais_int (uint32)
    """
    return self.__show_cfm_eth_ais_int
      
  def _set_show_cfm_eth_ais_int(self, v, load=False):
    """
    Setter method for show_cfm_eth_ais_int, mapped from YANG variable /brocade_dot1ag_rpc/get_show_cfm/output/show_cfm/show_cfm_domain_list/show_cfm_ma_list/show_cfm_eth_ais_int (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_cfm_eth_ais_int is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_cfm_eth_ais_int() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-eth-ais-int", rest_name="show-cfm-eth-ais-int", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_cfm_eth_ais_int must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-eth-ais-int", rest_name="show-cfm-eth-ais-int", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)""",
        })

    self.__show_cfm_eth_ais_int = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_cfm_eth_ais_int(self):
    self.__show_cfm_eth_ais_int = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="show-cfm-eth-ais-int", rest_name="show-cfm-eth-ais-int", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='uint32', is_config=True)


  def _get_show_cfm_ma_list(self):
    """
    Getter method for show_cfm_ma_list, mapped from YANG variable /brocade_dot1ag_rpc/get_show_cfm/output/show_cfm/show_cfm_domain_list/show_cfm_ma_list/show_cfm_ma_list (list)
    """
    return self.__show_cfm_ma_list
      
  def _set_show_cfm_ma_list(self, v, load=False):
    """
    Setter method for show_cfm_ma_list, mapped from YANG variable /brocade_dot1ag_rpc/get_show_cfm/output/show_cfm/show_cfm_domain_list/show_cfm_ma_list/show_cfm_ma_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_cfm_ma_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_cfm_ma_list() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType(False,show_cfm_ma_list_.show_cfm_ma_list, yang_name="show-cfm-ma-list", rest_name="show-cfm-ma-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="show-cfm-ma-list", rest_name="show-cfm-ma-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_cfm_ma_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType(False,show_cfm_ma_list_.show_cfm_ma_list, yang_name="show-cfm-ma-list", rest_name="show-cfm-ma-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="show-cfm-ma-list", rest_name="show-cfm-ma-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='list', is_config=True)""",
        })

    self.__show_cfm_ma_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_cfm_ma_list(self):
    self.__show_cfm_ma_list = YANGDynClass(base=YANGListType(False,show_cfm_ma_list_.show_cfm_ma_list, yang_name="show-cfm-ma-list", rest_name="show-cfm-ma-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="show-cfm-ma-list", rest_name="show-cfm-ma-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='list', is_config=True)

  show_cfm_ma_name = __builtin__.property(_get_show_cfm_ma_name, _set_show_cfm_ma_name)
  show_cfm_ma_idx = __builtin__.property(_get_show_cfm_ma_idx, _set_show_cfm_ma_idx)
  show_cfm_ccm_interval = __builtin__.property(_get_show_cfm_ccm_interval, _set_show_cfm_ccm_interval)
  show_cfm_vid = __builtin__.property(_get_show_cfm_vid, _set_show_cfm_vid)
  show_cfm_priority = __builtin__.property(_get_show_cfm_priority, _set_show_cfm_priority)
  show_cfm_eth_ais_tx = __builtin__.property(_get_show_cfm_eth_ais_tx, _set_show_cfm_eth_ais_tx)
  show_cfm_eth_ais_rx = __builtin__.property(_get_show_cfm_eth_ais_rx, _set_show_cfm_eth_ais_rx)
  show_cfm_eth_ais_int = __builtin__.property(_get_show_cfm_eth_ais_int, _set_show_cfm_eth_ais_int)
  show_cfm_ma_list = __builtin__.property(_get_show_cfm_ma_list, _set_show_cfm_ma_list)


  _pyangbind_elements = {'show_cfm_ma_name': show_cfm_ma_name, 'show_cfm_ma_idx': show_cfm_ma_idx, 'show_cfm_ccm_interval': show_cfm_ccm_interval, 'show_cfm_vid': show_cfm_vid, 'show_cfm_priority': show_cfm_priority, 'show_cfm_eth_ais_tx': show_cfm_eth_ais_tx, 'show_cfm_eth_ais_rx': show_cfm_eth_ais_rx, 'show_cfm_eth_ais_int': show_cfm_eth_ais_int, 'show_cfm_ma_list': show_cfm_ma_list, }


