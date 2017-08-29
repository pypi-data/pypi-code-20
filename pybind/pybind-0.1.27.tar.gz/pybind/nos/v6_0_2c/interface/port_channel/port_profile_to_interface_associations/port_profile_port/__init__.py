
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import port_to_port_profile_domain_association
import port_to_port_profile_associations
class port_profile_port(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/port-channel/port-profile-to-interface-associations/port-profile-port. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__port_to_port_profile_domain_association','__port_to_port_profile_associations',)

  _yang_name = 'port-profile-port'
  _rest_name = 'port-profile-port'

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
    self.__port_to_port_profile_associations = YANGDynClass(base=YANGListType("port_to_port_profile_association",port_to_port_profile_associations.port_to_port_profile_associations, yang_name="port-to-port-profile-associations", rest_name="profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='port-to-port-profile-association', extensions={u'tailf-common': {u'info': u'Associate a list of port-profiles with an interface.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'114', u'cli-suppress-list-no': None, u'callpoint': u'po-to-port-profile-associations-callpoint', u'cli-full-command': None, u'hidden': u'full', u'alt-name': u'profile'}}), is_container='list', yang_name="port-to-port-profile-associations", rest_name="profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Associate a list of port-profiles with an interface.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'114', u'cli-suppress-list-no': None, u'callpoint': u'po-to-port-profile-associations-callpoint', u'cli-full-command': None, u'hidden': u'full', u'alt-name': u'profile'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='list', is_config=True)
    self.__port_to_port_profile_domain_association = YANGDynClass(base=port_to_port_profile_domain_association.port_to_port_profile_domain_association, is_container='container', presence=False, yang_name="port-to-port-profile-domain-association", rest_name="domain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Associate a port-profile-domain with an interface.', u'alt-name': u'domain', u'sort-priority': u'114', u'callpoint': u'po-to-port-profile-domain-association-callpoint'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)

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
      return [u'interface', u'port-channel', u'port-profile-to-interface-associations', u'port-profile-port']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Port-channel', u'port-profile-port']

  def _get_port_to_port_profile_domain_association(self):
    """
    Getter method for port_to_port_profile_domain_association, mapped from YANG variable /interface/port_channel/port_profile_to_interface_associations/port_profile_port/port_to_port_profile_domain_association (container)

    YANG Description: Associate a port-profile-domain with an interface.
    """
    return self.__port_to_port_profile_domain_association
      
  def _set_port_to_port_profile_domain_association(self, v, load=False):
    """
    Setter method for port_to_port_profile_domain_association, mapped from YANG variable /interface/port_channel/port_profile_to_interface_associations/port_profile_port/port_to_port_profile_domain_association (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_to_port_profile_domain_association is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_to_port_profile_domain_association() directly.

    YANG Description: Associate a port-profile-domain with an interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=port_to_port_profile_domain_association.port_to_port_profile_domain_association, is_container='container', presence=False, yang_name="port-to-port-profile-domain-association", rest_name="domain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Associate a port-profile-domain with an interface.', u'alt-name': u'domain', u'sort-priority': u'114', u'callpoint': u'po-to-port-profile-domain-association-callpoint'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_to_port_profile_domain_association must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=port_to_port_profile_domain_association.port_to_port_profile_domain_association, is_container='container', presence=False, yang_name="port-to-port-profile-domain-association", rest_name="domain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Associate a port-profile-domain with an interface.', u'alt-name': u'domain', u'sort-priority': u'114', u'callpoint': u'po-to-port-profile-domain-association-callpoint'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)""",
        })

    self.__port_to_port_profile_domain_association = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_to_port_profile_domain_association(self):
    self.__port_to_port_profile_domain_association = YANGDynClass(base=port_to_port_profile_domain_association.port_to_port_profile_domain_association, is_container='container', presence=False, yang_name="port-to-port-profile-domain-association", rest_name="domain", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Associate a port-profile-domain with an interface.', u'alt-name': u'domain', u'sort-priority': u'114', u'callpoint': u'po-to-port-profile-domain-association-callpoint'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)


  def _get_port_to_port_profile_associations(self):
    """
    Getter method for port_to_port_profile_associations, mapped from YANG variable /interface/port_channel/port_profile_to_interface_associations/port_profile_port/port_to_port_profile_associations (list)

    YANG Description: The list of automatic port profiles. Each row
provides the name of the port profile associated 
with an interface.
    """
    return self.__port_to_port_profile_associations
      
  def _set_port_to_port_profile_associations(self, v, load=False):
    """
    Setter method for port_to_port_profile_associations, mapped from YANG variable /interface/port_channel/port_profile_to_interface_associations/port_profile_port/port_to_port_profile_associations (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_to_port_profile_associations is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_to_port_profile_associations() directly.

    YANG Description: The list of automatic port profiles. Each row
provides the name of the port profile associated 
with an interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("port_to_port_profile_association",port_to_port_profile_associations.port_to_port_profile_associations, yang_name="port-to-port-profile-associations", rest_name="profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='port-to-port-profile-association', extensions={u'tailf-common': {u'info': u'Associate a list of port-profiles with an interface.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'114', u'cli-suppress-list-no': None, u'callpoint': u'po-to-port-profile-associations-callpoint', u'cli-full-command': None, u'hidden': u'full', u'alt-name': u'profile'}}), is_container='list', yang_name="port-to-port-profile-associations", rest_name="profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Associate a list of port-profiles with an interface.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'114', u'cli-suppress-list-no': None, u'callpoint': u'po-to-port-profile-associations-callpoint', u'cli-full-command': None, u'hidden': u'full', u'alt-name': u'profile'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_to_port_profile_associations must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("port_to_port_profile_association",port_to_port_profile_associations.port_to_port_profile_associations, yang_name="port-to-port-profile-associations", rest_name="profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='port-to-port-profile-association', extensions={u'tailf-common': {u'info': u'Associate a list of port-profiles with an interface.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'114', u'cli-suppress-list-no': None, u'callpoint': u'po-to-port-profile-associations-callpoint', u'cli-full-command': None, u'hidden': u'full', u'alt-name': u'profile'}}), is_container='list', yang_name="port-to-port-profile-associations", rest_name="profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Associate a list of port-profiles with an interface.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'114', u'cli-suppress-list-no': None, u'callpoint': u'po-to-port-profile-associations-callpoint', u'cli-full-command': None, u'hidden': u'full', u'alt-name': u'profile'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='list', is_config=True)""",
        })

    self.__port_to_port_profile_associations = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_to_port_profile_associations(self):
    self.__port_to_port_profile_associations = YANGDynClass(base=YANGListType("port_to_port_profile_association",port_to_port_profile_associations.port_to_port_profile_associations, yang_name="port-to-port-profile-associations", rest_name="profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='port-to-port-profile-association', extensions={u'tailf-common': {u'info': u'Associate a list of port-profiles with an interface.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'114', u'cli-suppress-list-no': None, u'callpoint': u'po-to-port-profile-associations-callpoint', u'cli-full-command': None, u'hidden': u'full', u'alt-name': u'profile'}}), is_container='list', yang_name="port-to-port-profile-associations", rest_name="profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Associate a list of port-profiles with an interface.', u'cli-no-key-completion': None, u'cli-suppress-mode': None, u'sort-priority': u'114', u'cli-suppress-list-no': None, u'callpoint': u'po-to-port-profile-associations-callpoint', u'cli-full-command': None, u'hidden': u'full', u'alt-name': u'profile'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='list', is_config=True)

  port_to_port_profile_domain_association = __builtin__.property(_get_port_to_port_profile_domain_association, _set_port_to_port_profile_domain_association)
  port_to_port_profile_associations = __builtin__.property(_get_port_to_port_profile_associations, _set_port_to_port_profile_associations)


  _pyangbind_elements = {'port_to_port_profile_domain_association': port_to_port_profile_domain_association, 'port_to_port_profile_associations': port_to_port_profile_associations, }


