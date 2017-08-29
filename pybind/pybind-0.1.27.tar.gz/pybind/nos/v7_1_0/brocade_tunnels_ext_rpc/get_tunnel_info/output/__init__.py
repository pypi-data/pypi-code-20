
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import tunnel
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-tunnels-ext - based on the path /brocade_tunnels_ext_rpc/get-tunnel-info/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__tunnel','__next_page_cursor',)

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
    self.__tunnel = YANGDynClass(base=YANGListType(False,tunnel.tunnel, yang_name="tunnel", rest_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="tunnel", rest_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='list', is_config=True)
    self.__next_page_cursor = YANGDynClass(base=unicode, is_leaf=True, yang_name="next-page-cursor", rest_name="next-page-cursor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='string', is_config=True)

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
      return [u'brocade_tunnels_ext_rpc', u'get-tunnel-info', u'output']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-tunnel-info', u'output']

  def _get_tunnel(self):
    """
    Getter method for tunnel, mapped from YANG variable /brocade_tunnels_ext_rpc/get_tunnel_info/output/tunnel (list)
    """
    return self.__tunnel
      
  def _set_tunnel(self, v, load=False):
    """
    Setter method for tunnel, mapped from YANG variable /brocade_tunnels_ext_rpc/get_tunnel_info/output/tunnel (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tunnel is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tunnel() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType(False,tunnel.tunnel, yang_name="tunnel", rest_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="tunnel", rest_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tunnel must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType(False,tunnel.tunnel, yang_name="tunnel", rest_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="tunnel", rest_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='list', is_config=True)""",
        })

    self.__tunnel = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tunnel(self):
    self.__tunnel = YANGDynClass(base=YANGListType(False,tunnel.tunnel, yang_name="tunnel", rest_name="tunnel", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="tunnel", rest_name="tunnel", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='list', is_config=True)


  def _get_next_page_cursor(self):
    """
    Getter method for next_page_cursor, mapped from YANG variable /brocade_tunnels_ext_rpc/get_tunnel_info/output/next_page_cursor (string)

    YANG Description: Opaque data identifying the next page. Client must
pass this value as 'page-cursor' parameter in
following RPC to retrieve next page tunnel data.
Value will not be present if no more tunnel records
exist (current page is the last page).
    """
    return self.__next_page_cursor
      
  def _set_next_page_cursor(self, v, load=False):
    """
    Setter method for next_page_cursor, mapped from YANG variable /brocade_tunnels_ext_rpc/get_tunnel_info/output/next_page_cursor (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_next_page_cursor is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_next_page_cursor() directly.

    YANG Description: Opaque data identifying the next page. Client must
pass this value as 'page-cursor' parameter in
following RPC to retrieve next page tunnel data.
Value will not be present if no more tunnel records
exist (current page is the last page).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="next-page-cursor", rest_name="next-page-cursor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """next_page_cursor must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="next-page-cursor", rest_name="next-page-cursor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='string', is_config=True)""",
        })

    self.__next_page_cursor = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_next_page_cursor(self):
    self.__next_page_cursor = YANGDynClass(base=unicode, is_leaf=True, yang_name="next-page-cursor", rest_name="next-page-cursor", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-tunnels-ext', defining_module='brocade-tunnels-ext', yang_type='string', is_config=True)

  tunnel = __builtin__.property(_get_tunnel, _set_tunnel)
  next_page_cursor = __builtin__.property(_get_next_page_cursor, _set_next_page_cursor)


  _pyangbind_elements = {'tunnel': tunnel, 'next_page_cursor': next_page_cursor, }


