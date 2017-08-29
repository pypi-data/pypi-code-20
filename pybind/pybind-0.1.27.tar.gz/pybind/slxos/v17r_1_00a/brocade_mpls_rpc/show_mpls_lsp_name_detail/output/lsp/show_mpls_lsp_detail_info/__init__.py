
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import show_mpls_lsp_basic_info
import show_mpls_lsp_common_info
import show_mpls_lsp_instances_info
import show_mpls_lsp_forwarding_info
import show_mpls_lsp_sec_path_info
import show_mpls_lsp_frr_info
import show_mpls_lsp_backup_info
class show_mpls_lsp_detail_info(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/show-mpls-lsp-name-detail/output/lsp/show-mpls-lsp-detail-info. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__show_mpls_lsp_basic_info','__show_mpls_lsp_common_info','__show_mpls_lsp_instances_info','__show_mpls_lsp_forwarding_info','__show_mpls_lsp_sec_path_info','__show_mpls_lsp_frr_info','__show_mpls_lsp_backup_info',)

  _yang_name = 'show-mpls-lsp-detail-info'
  _rest_name = ''

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
    self.__show_mpls_lsp_common_info = YANGDynClass(base=show_mpls_lsp_common_info.show_mpls_lsp_common_info, is_container='container', presence=False, yang_name="show-mpls-lsp-common-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    self.__show_mpls_lsp_basic_info = YANGDynClass(base=show_mpls_lsp_basic_info.show_mpls_lsp_basic_info, is_container='container', presence=False, yang_name="show-mpls-lsp-basic-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    self.__show_mpls_lsp_instances_info = YANGDynClass(base=show_mpls_lsp_instances_info.show_mpls_lsp_instances_info, is_container='container', presence=False, yang_name="show-mpls-lsp-instances-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    self.__show_mpls_lsp_backup_info = YANGDynClass(base=show_mpls_lsp_backup_info.show_mpls_lsp_backup_info, is_container='container', presence=False, yang_name="show-mpls-lsp-backup-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    self.__show_mpls_lsp_frr_info = YANGDynClass(base=show_mpls_lsp_frr_info.show_mpls_lsp_frr_info, is_container='container', presence=False, yang_name="show-mpls-lsp-frr-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    self.__show_mpls_lsp_forwarding_info = YANGDynClass(base=show_mpls_lsp_forwarding_info.show_mpls_lsp_forwarding_info, is_container='container', presence=False, yang_name="show-mpls-lsp-forwarding-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    self.__show_mpls_lsp_sec_path_info = YANGDynClass(base=show_mpls_lsp_sec_path_info.show_mpls_lsp_sec_path_info, is_container='container', presence=False, yang_name="show-mpls-lsp-sec-path-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)

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
      return [u'brocade_mpls_rpc', u'show-mpls-lsp-name-detail', u'output', u'lsp', u'show-mpls-lsp-detail-info']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-mpls-lsp-name-detail', u'output', u'lsp']

  def _get_show_mpls_lsp_basic_info(self):
    """
    Getter method for show_mpls_lsp_basic_info, mapped from YANG variable /brocade_mpls_rpc/show_mpls_lsp_name_detail/output/lsp/show_mpls_lsp_detail_info/show_mpls_lsp_basic_info (container)
    """
    return self.__show_mpls_lsp_basic_info
      
  def _set_show_mpls_lsp_basic_info(self, v, load=False):
    """
    Setter method for show_mpls_lsp_basic_info, mapped from YANG variable /brocade_mpls_rpc/show_mpls_lsp_name_detail/output/lsp/show_mpls_lsp_detail_info/show_mpls_lsp_basic_info (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_mpls_lsp_basic_info is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_mpls_lsp_basic_info() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=show_mpls_lsp_basic_info.show_mpls_lsp_basic_info, is_container='container', presence=False, yang_name="show-mpls-lsp-basic-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_mpls_lsp_basic_info must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=show_mpls_lsp_basic_info.show_mpls_lsp_basic_info, is_container='container', presence=False, yang_name="show-mpls-lsp-basic-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__show_mpls_lsp_basic_info = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_mpls_lsp_basic_info(self):
    self.__show_mpls_lsp_basic_info = YANGDynClass(base=show_mpls_lsp_basic_info.show_mpls_lsp_basic_info, is_container='container', presence=False, yang_name="show-mpls-lsp-basic-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)


  def _get_show_mpls_lsp_common_info(self):
    """
    Getter method for show_mpls_lsp_common_info, mapped from YANG variable /brocade_mpls_rpc/show_mpls_lsp_name_detail/output/lsp/show_mpls_lsp_detail_info/show_mpls_lsp_common_info (container)
    """
    return self.__show_mpls_lsp_common_info
      
  def _set_show_mpls_lsp_common_info(self, v, load=False):
    """
    Setter method for show_mpls_lsp_common_info, mapped from YANG variable /brocade_mpls_rpc/show_mpls_lsp_name_detail/output/lsp/show_mpls_lsp_detail_info/show_mpls_lsp_common_info (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_mpls_lsp_common_info is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_mpls_lsp_common_info() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=show_mpls_lsp_common_info.show_mpls_lsp_common_info, is_container='container', presence=False, yang_name="show-mpls-lsp-common-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_mpls_lsp_common_info must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=show_mpls_lsp_common_info.show_mpls_lsp_common_info, is_container='container', presence=False, yang_name="show-mpls-lsp-common-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__show_mpls_lsp_common_info = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_mpls_lsp_common_info(self):
    self.__show_mpls_lsp_common_info = YANGDynClass(base=show_mpls_lsp_common_info.show_mpls_lsp_common_info, is_container='container', presence=False, yang_name="show-mpls-lsp-common-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)


  def _get_show_mpls_lsp_instances_info(self):
    """
    Getter method for show_mpls_lsp_instances_info, mapped from YANG variable /brocade_mpls_rpc/show_mpls_lsp_name_detail/output/lsp/show_mpls_lsp_detail_info/show_mpls_lsp_instances_info (container)
    """
    return self.__show_mpls_lsp_instances_info
      
  def _set_show_mpls_lsp_instances_info(self, v, load=False):
    """
    Setter method for show_mpls_lsp_instances_info, mapped from YANG variable /brocade_mpls_rpc/show_mpls_lsp_name_detail/output/lsp/show_mpls_lsp_detail_info/show_mpls_lsp_instances_info (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_mpls_lsp_instances_info is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_mpls_lsp_instances_info() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=show_mpls_lsp_instances_info.show_mpls_lsp_instances_info, is_container='container', presence=False, yang_name="show-mpls-lsp-instances-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_mpls_lsp_instances_info must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=show_mpls_lsp_instances_info.show_mpls_lsp_instances_info, is_container='container', presence=False, yang_name="show-mpls-lsp-instances-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__show_mpls_lsp_instances_info = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_mpls_lsp_instances_info(self):
    self.__show_mpls_lsp_instances_info = YANGDynClass(base=show_mpls_lsp_instances_info.show_mpls_lsp_instances_info, is_container='container', presence=False, yang_name="show-mpls-lsp-instances-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)


  def _get_show_mpls_lsp_forwarding_info(self):
    """
    Getter method for show_mpls_lsp_forwarding_info, mapped from YANG variable /brocade_mpls_rpc/show_mpls_lsp_name_detail/output/lsp/show_mpls_lsp_detail_info/show_mpls_lsp_forwarding_info (container)
    """
    return self.__show_mpls_lsp_forwarding_info
      
  def _set_show_mpls_lsp_forwarding_info(self, v, load=False):
    """
    Setter method for show_mpls_lsp_forwarding_info, mapped from YANG variable /brocade_mpls_rpc/show_mpls_lsp_name_detail/output/lsp/show_mpls_lsp_detail_info/show_mpls_lsp_forwarding_info (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_mpls_lsp_forwarding_info is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_mpls_lsp_forwarding_info() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=show_mpls_lsp_forwarding_info.show_mpls_lsp_forwarding_info, is_container='container', presence=False, yang_name="show-mpls-lsp-forwarding-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_mpls_lsp_forwarding_info must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=show_mpls_lsp_forwarding_info.show_mpls_lsp_forwarding_info, is_container='container', presence=False, yang_name="show-mpls-lsp-forwarding-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__show_mpls_lsp_forwarding_info = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_mpls_lsp_forwarding_info(self):
    self.__show_mpls_lsp_forwarding_info = YANGDynClass(base=show_mpls_lsp_forwarding_info.show_mpls_lsp_forwarding_info, is_container='container', presence=False, yang_name="show-mpls-lsp-forwarding-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)


  def _get_show_mpls_lsp_sec_path_info(self):
    """
    Getter method for show_mpls_lsp_sec_path_info, mapped from YANG variable /brocade_mpls_rpc/show_mpls_lsp_name_detail/output/lsp/show_mpls_lsp_detail_info/show_mpls_lsp_sec_path_info (container)
    """
    return self.__show_mpls_lsp_sec_path_info
      
  def _set_show_mpls_lsp_sec_path_info(self, v, load=False):
    """
    Setter method for show_mpls_lsp_sec_path_info, mapped from YANG variable /brocade_mpls_rpc/show_mpls_lsp_name_detail/output/lsp/show_mpls_lsp_detail_info/show_mpls_lsp_sec_path_info (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_mpls_lsp_sec_path_info is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_mpls_lsp_sec_path_info() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=show_mpls_lsp_sec_path_info.show_mpls_lsp_sec_path_info, is_container='container', presence=False, yang_name="show-mpls-lsp-sec-path-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_mpls_lsp_sec_path_info must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=show_mpls_lsp_sec_path_info.show_mpls_lsp_sec_path_info, is_container='container', presence=False, yang_name="show-mpls-lsp-sec-path-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__show_mpls_lsp_sec_path_info = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_mpls_lsp_sec_path_info(self):
    self.__show_mpls_lsp_sec_path_info = YANGDynClass(base=show_mpls_lsp_sec_path_info.show_mpls_lsp_sec_path_info, is_container='container', presence=False, yang_name="show-mpls-lsp-sec-path-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)


  def _get_show_mpls_lsp_frr_info(self):
    """
    Getter method for show_mpls_lsp_frr_info, mapped from YANG variable /brocade_mpls_rpc/show_mpls_lsp_name_detail/output/lsp/show_mpls_lsp_detail_info/show_mpls_lsp_frr_info (container)
    """
    return self.__show_mpls_lsp_frr_info
      
  def _set_show_mpls_lsp_frr_info(self, v, load=False):
    """
    Setter method for show_mpls_lsp_frr_info, mapped from YANG variable /brocade_mpls_rpc/show_mpls_lsp_name_detail/output/lsp/show_mpls_lsp_detail_info/show_mpls_lsp_frr_info (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_mpls_lsp_frr_info is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_mpls_lsp_frr_info() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=show_mpls_lsp_frr_info.show_mpls_lsp_frr_info, is_container='container', presence=False, yang_name="show-mpls-lsp-frr-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_mpls_lsp_frr_info must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=show_mpls_lsp_frr_info.show_mpls_lsp_frr_info, is_container='container', presence=False, yang_name="show-mpls-lsp-frr-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__show_mpls_lsp_frr_info = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_mpls_lsp_frr_info(self):
    self.__show_mpls_lsp_frr_info = YANGDynClass(base=show_mpls_lsp_frr_info.show_mpls_lsp_frr_info, is_container='container', presence=False, yang_name="show-mpls-lsp-frr-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)


  def _get_show_mpls_lsp_backup_info(self):
    """
    Getter method for show_mpls_lsp_backup_info, mapped from YANG variable /brocade_mpls_rpc/show_mpls_lsp_name_detail/output/lsp/show_mpls_lsp_detail_info/show_mpls_lsp_backup_info (container)
    """
    return self.__show_mpls_lsp_backup_info
      
  def _set_show_mpls_lsp_backup_info(self, v, load=False):
    """
    Setter method for show_mpls_lsp_backup_info, mapped from YANG variable /brocade_mpls_rpc/show_mpls_lsp_name_detail/output/lsp/show_mpls_lsp_detail_info/show_mpls_lsp_backup_info (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_show_mpls_lsp_backup_info is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_show_mpls_lsp_backup_info() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=show_mpls_lsp_backup_info.show_mpls_lsp_backup_info, is_container='container', presence=False, yang_name="show-mpls-lsp-backup-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """show_mpls_lsp_backup_info must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=show_mpls_lsp_backup_info.show_mpls_lsp_backup_info, is_container='container', presence=False, yang_name="show-mpls-lsp-backup-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__show_mpls_lsp_backup_info = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_show_mpls_lsp_backup_info(self):
    self.__show_mpls_lsp_backup_info = YANGDynClass(base=show_mpls_lsp_backup_info.show_mpls_lsp_backup_info, is_container='container', presence=False, yang_name="show-mpls-lsp-backup-info", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)

  show_mpls_lsp_basic_info = __builtin__.property(_get_show_mpls_lsp_basic_info, _set_show_mpls_lsp_basic_info)
  show_mpls_lsp_common_info = __builtin__.property(_get_show_mpls_lsp_common_info, _set_show_mpls_lsp_common_info)
  show_mpls_lsp_instances_info = __builtin__.property(_get_show_mpls_lsp_instances_info, _set_show_mpls_lsp_instances_info)
  show_mpls_lsp_forwarding_info = __builtin__.property(_get_show_mpls_lsp_forwarding_info, _set_show_mpls_lsp_forwarding_info)
  show_mpls_lsp_sec_path_info = __builtin__.property(_get_show_mpls_lsp_sec_path_info, _set_show_mpls_lsp_sec_path_info)
  show_mpls_lsp_frr_info = __builtin__.property(_get_show_mpls_lsp_frr_info, _set_show_mpls_lsp_frr_info)
  show_mpls_lsp_backup_info = __builtin__.property(_get_show_mpls_lsp_backup_info, _set_show_mpls_lsp_backup_info)


  _pyangbind_elements = {'show_mpls_lsp_basic_info': show_mpls_lsp_basic_info, 'show_mpls_lsp_common_info': show_mpls_lsp_common_info, 'show_mpls_lsp_instances_info': show_mpls_lsp_instances_info, 'show_mpls_lsp_forwarding_info': show_mpls_lsp_forwarding_info, 'show_mpls_lsp_sec_path_info': show_mpls_lsp_sec_path_info, 'show_mpls_lsp_frr_info': show_mpls_lsp_frr_info, 'show_mpls_lsp_backup_info': show_mpls_lsp_backup_info, }


