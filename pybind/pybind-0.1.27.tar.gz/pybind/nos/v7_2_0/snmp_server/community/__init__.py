
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class community(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-snmp - based on the path /snmp-server/community. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__community','__groupname','__ipv4_acl','__ipv6_acl',)

  _yang_name = 'community'
  _rest_name = 'community'

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
    self.__ipv4_acl = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0 .. 63']}), default=unicode(""), is_leaf=True, yang_name="ipv4-acl", rest_name="ipv4-acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'standard IPv4 Access list name (or) ID associated with community strings.'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='std-ip-acl-policy-name', is_config=True)
    self.__groupname = YANGDynClass(base=unicode, default=unicode(""), is_leaf=True, yang_name="groupname", rest_name="groupname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Groupname associated with community string'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)
    self.__ipv6_acl = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0 .. 63']}), default=unicode(""), is_leaf=True, yang_name="ipv6-acl", rest_name="ipv6-acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'standard IPv6 Access list name (or) ID associated with community strings.'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='std-ip-acl-policy-name', is_config=True)
    self.__community = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'2 .. 64']}), is_leaf=True, yang_name="community", rest_name="community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)

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
      return [u'snmp-server', u'community']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'snmp-server', u'community']

  def _get_community(self):
    """
    Getter method for community, mapped from YANG variable /snmp_server/community/community (string)
    """
    return self.__community
      
  def _set_community(self, v, load=False):
    """
    Setter method for community, mapped from YANG variable /snmp_server/community/community (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_community is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_community() directly.
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'2 .. 64']}), is_leaf=True, yang_name="community", rest_name="community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """community must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'2 .. 64']}), is_leaf=True, yang_name="community", rest_name="community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)""",
        })

    self.__community = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_community(self):
    self.__community = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'2 .. 64']}), is_leaf=True, yang_name="community", rest_name="community", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)


  def _get_groupname(self):
    """
    Getter method for groupname, mapped from YANG variable /snmp_server/community/groupname (string)
    """
    return self.__groupname
      
  def _set_groupname(self, v, load=False):
    """
    Setter method for groupname, mapped from YANG variable /snmp_server/community/groupname (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_groupname is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_groupname() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, default=unicode(""), is_leaf=True, yang_name="groupname", rest_name="groupname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Groupname associated with community string'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """groupname must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, default=unicode(""), is_leaf=True, yang_name="groupname", rest_name="groupname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Groupname associated with community string'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)""",
        })

    self.__groupname = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_groupname(self):
    self.__groupname = YANGDynClass(base=unicode, default=unicode(""), is_leaf=True, yang_name="groupname", rest_name="groupname", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Groupname associated with community string'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='string', is_config=True)


  def _get_ipv4_acl(self):
    """
    Getter method for ipv4_acl, mapped from YANG variable /snmp_server/community/ipv4_acl (std-ip-acl-policy-name)
    """
    return self.__ipv4_acl
      
  def _set_ipv4_acl(self, v, load=False):
    """
    Setter method for ipv4_acl, mapped from YANG variable /snmp_server/community/ipv4_acl (std-ip-acl-policy-name)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv4_acl is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv4_acl() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0 .. 63']}), default=unicode(""), is_leaf=True, yang_name="ipv4-acl", rest_name="ipv4-acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'standard IPv4 Access list name (or) ID associated with community strings.'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='std-ip-acl-policy-name', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv4_acl must be of a type compatible with std-ip-acl-policy-name""",
          'defined-type': "brocade-snmp:std-ip-acl-policy-name",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0 .. 63']}), default=unicode(""), is_leaf=True, yang_name="ipv4-acl", rest_name="ipv4-acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'standard IPv4 Access list name (or) ID associated with community strings.'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='std-ip-acl-policy-name', is_config=True)""",
        })

    self.__ipv4_acl = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv4_acl(self):
    self.__ipv4_acl = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0 .. 63']}), default=unicode(""), is_leaf=True, yang_name="ipv4-acl", rest_name="ipv4-acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'standard IPv4 Access list name (or) ID associated with community strings.'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='std-ip-acl-policy-name', is_config=True)


  def _get_ipv6_acl(self):
    """
    Getter method for ipv6_acl, mapped from YANG variable /snmp_server/community/ipv6_acl (std-ip-acl-policy-name)
    """
    return self.__ipv6_acl
      
  def _set_ipv6_acl(self, v, load=False):
    """
    Setter method for ipv6_acl, mapped from YANG variable /snmp_server/community/ipv6_acl (std-ip-acl-policy-name)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6_acl is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6_acl() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0 .. 63']}), default=unicode(""), is_leaf=True, yang_name="ipv6-acl", rest_name="ipv6-acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'standard IPv6 Access list name (or) ID associated with community strings.'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='std-ip-acl-policy-name', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6_acl must be of a type compatible with std-ip-acl-policy-name""",
          'defined-type': "brocade-snmp:std-ip-acl-policy-name",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0 .. 63']}), default=unicode(""), is_leaf=True, yang_name="ipv6-acl", rest_name="ipv6-acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'standard IPv6 Access list name (or) ID associated with community strings.'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='std-ip-acl-policy-name', is_config=True)""",
        })

    self.__ipv6_acl = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6_acl(self):
    self.__ipv6_acl = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'0 .. 63']}), default=unicode(""), is_leaf=True, yang_name="ipv6-acl", rest_name="ipv6-acl", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'standard IPv6 Access list name (or) ID associated with community strings.'}}, namespace='urn:brocade.com:mgmt:brocade-snmp', defining_module='brocade-snmp', yang_type='std-ip-acl-policy-name', is_config=True)

  community = __builtin__.property(_get_community, _set_community)
  groupname = __builtin__.property(_get_groupname, _set_groupname)
  ipv4_acl = __builtin__.property(_get_ipv4_acl, _set_ipv4_acl)
  ipv6_acl = __builtin__.property(_get_ipv6_acl, _set_ipv6_acl)


  _pyangbind_elements = {'community': community, 'groupname': groupname, 'ipv4_acl': ipv4_acl, 'ipv6_acl': ipv6_acl, }


