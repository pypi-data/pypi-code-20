
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import group_bucket_list
class group_id(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-openflow-operational - based on the path /openflow-state/group-id. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__group_id','__transaction_id','__group_type','__packet_count','__byte_count','__flow_count','__num_of_bkts','__group_bucket_list',)

  _yang_name = 'group-id'
  _rest_name = 'group-id'

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
    self.__byte_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="byte-count", rest_name="byte-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__packet_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="packet-count", rest_name="packet-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__transaction_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="transaction-id", rest_name="transaction-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    self.__flow_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="flow-count", rest_name="flow-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__num_of_bkts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-of-bkts", rest_name="num-of-bkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__group_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="group-id", rest_name="group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    self.__group_bucket_list = YANGDynClass(base=YANGListType("bucket_id",group_bucket_list.group_bucket_list, yang_name="group-bucket-list", rest_name="group-bucket-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bucket-id', extensions={u'tailf-common': {u'callpoint': u'openflow-group-bucket-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="group-bucket-list", rest_name="group-bucket-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-group-bucket-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)
    self.__group_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-group-type-select': {'value': 2}, u'dcm-group-type-invalid': {'value': 0}, u'dcm-group-type-fast-failover': {'value': 4}, u'dcm-group-type-indirect': {'value': 3}, u'dcm-group-type-all': {'value': 1}},), is_leaf=True, yang_name="group-type", rest_name="group-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='group-type', is_config=False)

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
      return [u'openflow-state', u'group-id']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'openflow-state', u'group-id']

  def _get_group_id(self):
    """
    Getter method for group_id, mapped from YANG variable /openflow_state/group_id/group_id (uint32)

    YANG Description: Group id
    """
    return self.__group_id
      
  def _set_group_id(self, v, load=False):
    """
    Setter method for group_id, mapped from YANG variable /openflow_state/group_id/group_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_group_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_group_id() directly.

    YANG Description: Group id
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="group-id", rest_name="group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """group_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="group-id", rest_name="group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__group_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_group_id(self):
    self.__group_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="group-id", rest_name="group-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_transaction_id(self):
    """
    Getter method for transaction_id, mapped from YANG variable /openflow_state/group_id/transaction_id (string)

    YANG Description: Transaction id
    """
    return self.__transaction_id
      
  def _set_transaction_id(self, v, load=False):
    """
    Setter method for transaction_id, mapped from YANG variable /openflow_state/group_id/transaction_id (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_transaction_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_transaction_id() directly.

    YANG Description: Transaction id
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="transaction-id", rest_name="transaction-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """transaction_id must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="transaction-id", rest_name="transaction-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)""",
        })

    self.__transaction_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_transaction_id(self):
    self.__transaction_id = YANGDynClass(base=unicode, is_leaf=True, yang_name="transaction-id", rest_name="transaction-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='string', is_config=False)


  def _get_group_type(self):
    """
    Getter method for group_type, mapped from YANG variable /openflow_state/group_id/group_type (group-type)

    YANG Description: Group type
    """
    return self.__group_type
      
  def _set_group_type(self, v, load=False):
    """
    Setter method for group_type, mapped from YANG variable /openflow_state/group_id/group_type (group-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_group_type is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_group_type() directly.

    YANG Description: Group type
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-group-type-select': {'value': 2}, u'dcm-group-type-invalid': {'value': 0}, u'dcm-group-type-fast-failover': {'value': 4}, u'dcm-group-type-indirect': {'value': 3}, u'dcm-group-type-all': {'value': 1}},), is_leaf=True, yang_name="group-type", rest_name="group-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='group-type', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """group_type must be of a type compatible with group-type""",
          'defined-type': "brocade-openflow-operational:group-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-group-type-select': {'value': 2}, u'dcm-group-type-invalid': {'value': 0}, u'dcm-group-type-fast-failover': {'value': 4}, u'dcm-group-type-indirect': {'value': 3}, u'dcm-group-type-all': {'value': 1}},), is_leaf=True, yang_name="group-type", rest_name="group-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='group-type', is_config=False)""",
        })

    self.__group_type = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_group_type(self):
    self.__group_type = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'dcm-group-type-select': {'value': 2}, u'dcm-group-type-invalid': {'value': 0}, u'dcm-group-type-fast-failover': {'value': 4}, u'dcm-group-type-indirect': {'value': 3}, u'dcm-group-type-all': {'value': 1}},), is_leaf=True, yang_name="group-type", rest_name="group-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='group-type', is_config=False)


  def _get_packet_count(self):
    """
    Getter method for packet_count, mapped from YANG variable /openflow_state/group_id/packet_count (uint32)

    YANG Description: Packet Count
    """
    return self.__packet_count
      
  def _set_packet_count(self, v, load=False):
    """
    Setter method for packet_count, mapped from YANG variable /openflow_state/group_id/packet_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_packet_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_packet_count() directly.

    YANG Description: Packet Count
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="packet-count", rest_name="packet-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """packet_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="packet-count", rest_name="packet-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__packet_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_packet_count(self):
    self.__packet_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="packet-count", rest_name="packet-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_byte_count(self):
    """
    Getter method for byte_count, mapped from YANG variable /openflow_state/group_id/byte_count (uint32)

    YANG Description: Byte   Count
    """
    return self.__byte_count
      
  def _set_byte_count(self, v, load=False):
    """
    Setter method for byte_count, mapped from YANG variable /openflow_state/group_id/byte_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_byte_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_byte_count() directly.

    YANG Description: Byte   Count
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="byte-count", rest_name="byte-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """byte_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="byte-count", rest_name="byte-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__byte_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_byte_count(self):
    self.__byte_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="byte-count", rest_name="byte-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_flow_count(self):
    """
    Getter method for flow_count, mapped from YANG variable /openflow_state/group_id/flow_count (uint32)

    YANG Description: Flow   Count
    """
    return self.__flow_count
      
  def _set_flow_count(self, v, load=False):
    """
    Setter method for flow_count, mapped from YANG variable /openflow_state/group_id/flow_count (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_flow_count is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_flow_count() directly.

    YANG Description: Flow   Count
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="flow-count", rest_name="flow-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """flow_count must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="flow-count", rest_name="flow-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__flow_count = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_flow_count(self):
    self.__flow_count = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="flow-count", rest_name="flow-count", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_num_of_bkts(self):
    """
    Getter method for num_of_bkts, mapped from YANG variable /openflow_state/group_id/num_of_bkts (uint32)

    YANG Description: Number of buckets
    """
    return self.__num_of_bkts
      
  def _set_num_of_bkts(self, v, load=False):
    """
    Setter method for num_of_bkts, mapped from YANG variable /openflow_state/group_id/num_of_bkts (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_num_of_bkts is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_num_of_bkts() directly.

    YANG Description: Number of buckets
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-of-bkts", rest_name="num-of-bkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """num_of_bkts must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-of-bkts", rest_name="num-of-bkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)""",
        })

    self.__num_of_bkts = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_num_of_bkts(self):
    self.__num_of_bkts = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-of-bkts", rest_name="num-of-bkts", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='uint32', is_config=False)


  def _get_group_bucket_list(self):
    """
    Getter method for group_bucket_list, mapped from YANG variable /openflow_state/group_id/group_bucket_list (list)

    YANG Description: Group Bucket Info
    """
    return self.__group_bucket_list
      
  def _set_group_bucket_list(self, v, load=False):
    """
    Setter method for group_bucket_list, mapped from YANG variable /openflow_state/group_id/group_bucket_list (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_group_bucket_list is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_group_bucket_list() directly.

    YANG Description: Group Bucket Info
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("bucket_id",group_bucket_list.group_bucket_list, yang_name="group-bucket-list", rest_name="group-bucket-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bucket-id', extensions={u'tailf-common': {u'callpoint': u'openflow-group-bucket-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="group-bucket-list", rest_name="group-bucket-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-group-bucket-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """group_bucket_list must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("bucket_id",group_bucket_list.group_bucket_list, yang_name="group-bucket-list", rest_name="group-bucket-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bucket-id', extensions={u'tailf-common': {u'callpoint': u'openflow-group-bucket-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="group-bucket-list", rest_name="group-bucket-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-group-bucket-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)""",
        })

    self.__group_bucket_list = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_group_bucket_list(self):
    self.__group_bucket_list = YANGDynClass(base=YANGListType("bucket_id",group_bucket_list.group_bucket_list, yang_name="group-bucket-list", rest_name="group-bucket-list", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='bucket-id', extensions={u'tailf-common': {u'callpoint': u'openflow-group-bucket-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="group-bucket-list", rest_name="group-bucket-list", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'openflow-group-bucket-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-openflow-operational', defining_module='brocade-openflow-operational', yang_type='list', is_config=False)

  group_id = __builtin__.property(_get_group_id)
  transaction_id = __builtin__.property(_get_transaction_id)
  group_type = __builtin__.property(_get_group_type)
  packet_count = __builtin__.property(_get_packet_count)
  byte_count = __builtin__.property(_get_byte_count)
  flow_count = __builtin__.property(_get_flow_count)
  num_of_bkts = __builtin__.property(_get_num_of_bkts)
  group_bucket_list = __builtin__.property(_get_group_bucket_list)


  _pyangbind_elements = {'group_id': group_id, 'transaction_id': transaction_id, 'group_type': group_type, 'packet_count': packet_count, 'byte_count': byte_count, 'flow_count': flow_count, 'num_of_bkts': num_of_bkts, 'group_bucket_list': group_bucket_list, }


