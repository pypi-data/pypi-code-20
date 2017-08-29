
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class relay(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-maps - based on the path /maps/relay. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__hostip','__domainname',)

  _yang_name = 'relay'
  _rest_name = 'relay'

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
    self.__domainname = YANGDynClass(base=unicode, is_leaf=True, yang_name="domainname", rest_name="domainname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Domain name server'}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='string', is_config=True)
    self.__hostip = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..253']}),], is_leaf=True, yang_name="hostip", rest_name="hostip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'<IP:Address> IP address of Relay Host'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='inet:host', is_config=True)

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
      return [u'maps', u'relay']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'maps', u'relay']

  def _get_hostip(self):
    """
    Getter method for hostip, mapped from YANG variable /maps/relay/hostip (inet:host)
    """
    return self.__hostip
      
  def _set_hostip(self, v, load=False):
    """
    Setter method for hostip, mapped from YANG variable /maps/relay/hostip (inet:host)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hostip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hostip() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..253']}),], is_leaf=True, yang_name="hostip", rest_name="hostip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'<IP:Address> IP address of Relay Host'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='inet:host', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hostip must be of a type compatible with inet:host""",
          'defined-type': "inet:host",
          'generated-type': """YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..253']}),], is_leaf=True, yang_name="hostip", rest_name="hostip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'<IP:Address> IP address of Relay Host'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='inet:host', is_config=True)""",
        })

    self.__hostip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hostip(self):
    self.__hostip = YANGDynClass(base=[RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'}),RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.', 'length': [u'1..253']}),], is_leaf=True, yang_name="hostip", rest_name="hostip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'<IP:Address> IP address of Relay Host'}}, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='inet:host', is_config=True)


  def _get_domainname(self):
    """
    Getter method for domainname, mapped from YANG variable /maps/relay/domainname (string)
    """
    return self.__domainname
      
  def _set_domainname(self, v, load=False):
    """
    Setter method for domainname, mapped from YANG variable /maps/relay/domainname (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_domainname is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_domainname() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="domainname", rest_name="domainname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Domain name server'}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """domainname must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="domainname", rest_name="domainname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Domain name server'}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='string', is_config=True)""",
        })

    self.__domainname = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_domainname(self):
    self.__domainname = YANGDynClass(base=unicode, is_leaf=True, yang_name="domainname", rest_name="domainname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Domain name server'}}, namespace='urn:brocade.com:mgmt:brocade-maps', defining_module='brocade-maps', yang_type='string', is_config=True)

  hostip = __builtin__.property(_get_hostip, _set_hostip)
  domainname = __builtin__.property(_get_domainname, _set_domainname)


  _pyangbind_elements = {'hostip': hostip, 'domainname': domainname, }


