
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class credentials(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-vswitch - based on the path /vcenter/credentials. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__url','__username','__password','__vrf_name',)

  _yang_name = 'credentials'
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
    self.__url = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[h][t][t][p]([s]{0,1})[:][/][/]([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_:\\[\\]\\|]{1,57})', 'length': [u'1 .. 64']}), is_leaf=True, yang_name="url", rest_name="url", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'URL', u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='vcenter-url', is_config=True)
    self.__username = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 255']}), is_leaf=True, yang_name="username", rest_name="username", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'User name', u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)
    self.__password = YANGDynClass(base=unicode, is_leaf=True, yang_name="password", rest_name="password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Password', u'suppress-echo': u'true', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)
    self.__vrf_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 255']}), is_leaf=True, yang_name="vrf-name", rest_name="use-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'VRF name of the vCenter server', u'alt-name': u'use-vrf'}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)

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
      return [u'vcenter', u'credentials']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'vcenter']

  def _get_url(self):
    """
    Getter method for url, mapped from YANG variable /vcenter/credentials/url (vcenter-url)

    YANG Description: URL
    """
    return self.__url
      
  def _set_url(self, v, load=False):
    """
    Setter method for url, mapped from YANG variable /vcenter/credentials/url (vcenter-url)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_url is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_url() directly.

    YANG Description: URL
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[h][t][t][p]([s]{0,1})[:][/][/]([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_:\\[\\]\\|]{1,57})', 'length': [u'1 .. 64']}), is_leaf=True, yang_name="url", rest_name="url", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'URL', u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='vcenter-url', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """url must be of a type compatible with vcenter-url""",
          'defined-type': "brocade-vswitch:vcenter-url",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[h][t][t][p]([s]{0,1})[:][/][/]([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_:\\[\\]\\|]{1,57})', 'length': [u'1 .. 64']}), is_leaf=True, yang_name="url", rest_name="url", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'URL', u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='vcenter-url', is_config=True)""",
        })

    self.__url = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_url(self):
    self.__url = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[h][t][t][p]([s]{0,1})[:][/][/]([-a-zA-Z0-9\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_:\\[\\]\\|]{1,57})', 'length': [u'1 .. 64']}), is_leaf=True, yang_name="url", rest_name="url", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'URL', u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='vcenter-url', is_config=True)


  def _get_username(self):
    """
    Getter method for username, mapped from YANG variable /vcenter/credentials/username (string)

    YANG Description: User name
    """
    return self.__username
      
  def _set_username(self, v, load=False):
    """
    Setter method for username, mapped from YANG variable /vcenter/credentials/username (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_username is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_username() directly.

    YANG Description: User name
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 255']}), is_leaf=True, yang_name="username", rest_name="username", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'User name', u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """username must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 255']}), is_leaf=True, yang_name="username", rest_name="username", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'User name', u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)""",
        })

    self.__username = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_username(self):
    self.__username = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 255']}), is_leaf=True, yang_name="username", rest_name="username", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'User name', u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)


  def _get_password(self):
    """
    Getter method for password, mapped from YANG variable /vcenter/credentials/password (string)

    YANG Description: Password
    """
    return self.__password
      
  def _set_password(self, v, load=False):
    """
    Setter method for password, mapped from YANG variable /vcenter/credentials/password (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_password is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_password() directly.

    YANG Description: Password
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="password", rest_name="password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Password', u'suppress-echo': u'true', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """password must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="password", rest_name="password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Password', u'suppress-echo': u'true', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)""",
        })

    self.__password = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_password(self):
    self.__password = YANGDynClass(base=unicode, is_leaf=True, yang_name="password", rest_name="password", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Password', u'suppress-echo': u'true', u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)


  def _get_vrf_name(self):
    """
    Getter method for vrf_name, mapped from YANG variable /vcenter/credentials/vrf_name (string)

    YANG Description: Name of the VRF that the vCenter server is within
    """
    return self.__vrf_name
      
  def _set_vrf_name(self, v, load=False):
    """
    Setter method for vrf_name, mapped from YANG variable /vcenter/credentials/vrf_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vrf_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vrf_name() directly.

    YANG Description: Name of the VRF that the vCenter server is within
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 255']}), is_leaf=True, yang_name="vrf-name", rest_name="use-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'VRF name of the vCenter server', u'alt-name': u'use-vrf'}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vrf_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 255']}), is_leaf=True, yang_name="vrf-name", rest_name="use-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'VRF name of the vCenter server', u'alt-name': u'use-vrf'}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)""",
        })

    self.__vrf_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vrf_name(self):
    self.__vrf_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 255']}), is_leaf=True, yang_name="vrf-name", rest_name="use-vrf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'VRF name of the vCenter server', u'alt-name': u'use-vrf'}}, namespace='urn:brocade.com:mgmt:brocade-vswitch', defining_module='brocade-vswitch', yang_type='string', is_config=True)

  url = __builtin__.property(_get_url, _set_url)
  username = __builtin__.property(_get_username, _set_username)
  password = __builtin__.property(_get_password, _set_password)
  vrf_name = __builtin__.property(_get_vrf_name, _set_vrf_name)


  _pyangbind_elements = {'url': url, 'username': username, 'password': password, 'vrf_name': vrf_name, }


