
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import client_state_info
class show_cluster_mctd_client(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mct-operational - based on the path /mctd-client-state-state/show-cluster-mctd-client. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: MCT cluster client states
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__cluster_id','__num_clients','__client_state_info',)

  _yang_name = 'show-cluster-mctd-client'
  _rest_name = 'show-cluster-mctd-client'

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
    self.__client_state_info = YANGDynClass(base=YANGListType("client_id",client_state_info.client_state_info, yang_name="client-state-info", rest_name="client-state-info", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='client-id', extensions={u'tailf-common': {u'callpoint': u'mct-client-state-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="client-state-info", rest_name="client-state-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mct-client-state-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='list', is_config=False)
    self.__cluster_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cluster-id", rest_name="cluster-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)
    self.__num_clients = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-clients", rest_name="num-clients", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)

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
      return [u'mctd-client-state-state', u'show-cluster-mctd-client']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'mctd-client-state-state', u'show-cluster-mctd-client']

  def _get_cluster_id(self):
    """
    Getter method for cluster_id, mapped from YANG variable /mctd_client_state_state/show_cluster_mctd_client/cluster_id (uint32)

    YANG Description: Cluster ID
    """
    return self.__cluster_id
      
  def _set_cluster_id(self, v, load=False):
    """
    Setter method for cluster_id, mapped from YANG variable /mctd_client_state_state/show_cluster_mctd_client/cluster_id (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cluster_id is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cluster_id() directly.

    YANG Description: Cluster ID
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cluster-id", rest_name="cluster-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cluster_id must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cluster-id", rest_name="cluster-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)""",
        })

    self.__cluster_id = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cluster_id(self):
    self.__cluster_id = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="cluster-id", rest_name="cluster-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)


  def _get_num_clients(self):
    """
    Getter method for num_clients, mapped from YANG variable /mctd_client_state_state/show_cluster_mctd_client/num_clients (uint32)

    YANG Description: No. of Clients
    """
    return self.__num_clients
      
  def _set_num_clients(self, v, load=False):
    """
    Setter method for num_clients, mapped from YANG variable /mctd_client_state_state/show_cluster_mctd_client/num_clients (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_num_clients is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_num_clients() directly.

    YANG Description: No. of Clients
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-clients", rest_name="num-clients", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """num_clients must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-clients", rest_name="num-clients", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)""",
        })

    self.__num_clients = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_num_clients(self):
    self.__num_clients = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="num-clients", rest_name="num-clients", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='uint32', is_config=False)


  def _get_client_state_info(self):
    """
    Getter method for client_state_info, mapped from YANG variable /mctd_client_state_state/show_cluster_mctd_client/client_state_info (list)

    YANG Description: cluster client state
    """
    return self.__client_state_info
      
  def _set_client_state_info(self, v, load=False):
    """
    Setter method for client_state_info, mapped from YANG variable /mctd_client_state_state/show_cluster_mctd_client/client_state_info (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_client_state_info is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_client_state_info() directly.

    YANG Description: cluster client state
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("client_id",client_state_info.client_state_info, yang_name="client-state-info", rest_name="client-state-info", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='client-id', extensions={u'tailf-common': {u'callpoint': u'mct-client-state-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="client-state-info", rest_name="client-state-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mct-client-state-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='list', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """client_state_info must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("client_id",client_state_info.client_state_info, yang_name="client-state-info", rest_name="client-state-info", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='client-id', extensions={u'tailf-common': {u'callpoint': u'mct-client-state-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="client-state-info", rest_name="client-state-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mct-client-state-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='list', is_config=False)""",
        })

    self.__client_state_info = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_client_state_info(self):
    self.__client_state_info = YANGDynClass(base=YANGListType("client_id",client_state_info.client_state_info, yang_name="client-state-info", rest_name="client-state-info", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='client-id', extensions={u'tailf-common': {u'callpoint': u'mct-client-state-info', u'cli-suppress-show-path': None}}), is_container='list', yang_name="client-state-info", rest_name="client-state-info", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'callpoint': u'mct-client-state-info', u'cli-suppress-show-path': None}}, namespace='urn:brocade.com:mgmt:brocade-mct-operational', defining_module='brocade-mct-operational', yang_type='list', is_config=False)

  cluster_id = __builtin__.property(_get_cluster_id)
  num_clients = __builtin__.property(_get_num_clients)
  client_state_info = __builtin__.property(_get_client_state_info)


  _pyangbind_elements = {'cluster_id': cluster_id, 'num_clients': num_clients, 'client_state_info': client_state_info, }


