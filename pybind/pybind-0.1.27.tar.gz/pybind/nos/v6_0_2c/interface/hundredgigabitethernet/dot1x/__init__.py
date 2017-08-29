
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import timeout
class dot1x(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/hundredgigabitethernet/dot1x. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This provides grouping of all the dot1x configuration
elements.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__authentication','__port_control','__protocol_version','__quiet_period','__reauthMax','__reauthentication','__timeout',)

  _yang_name = 'dot1x'
  _rest_name = 'dot1x'

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
    self.__reauthMax = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2), is_leaf=True, yang_name="reauthMax", rest_name="reauthMax", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Number of reauthentication attempts before becoming\nunauthorized'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='uint32', is_config=True)
    self.__port_control = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'auto': {'value': 1}, u'force-unauthorized': {'value': 3}, u'force-authorized': {'value': 2}},), is_leaf=True, yang_name="port-control", rest_name="port-control", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Port control commands'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='enumeration', is_config=True)
    self.__quiet_period = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(60), is_leaf=True, yang_name="quiet-period", rest_name="quiet-period", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Quiet period in the HELD state'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='uint32', is_config=True)
    self.__authentication = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="authentication", rest_name="authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable dot1x on a port'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='empty', is_config=True)
    self.__timeout = YANGDynClass(base=timeout.timeout, is_container='container', presence=False, yang_name="timeout", rest_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set a timeout parameter', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='container', is_config=True)
    self.__reauthentication = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="reauthentication", rest_name="reauthentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable reauthentication on a port'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='empty', is_config=True)
    self.__protocol_version = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 2']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2), is_leaf=True, yang_name="protocol-version", rest_name="protocol-version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the protocol version'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='uint32', is_config=True)

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
      return [u'interface', u'hundredgigabitethernet', u'dot1x']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'HundredGigabitEthernet', u'dot1x']

  def _get_authentication(self):
    """
    Getter method for authentication, mapped from YANG variable /interface/hundredgigabitethernet/dot1x/authentication (empty)

    YANG Description: This specifies if the dot1x is enabled on the port 
or not.
                    
The presence of this leaf indicates that the dot1x 
is enabled on the port.
    """
    return self.__authentication
      
  def _set_authentication(self, v, load=False):
    """
    Setter method for authentication, mapped from YANG variable /interface/hundredgigabitethernet/dot1x/authentication (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_authentication is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_authentication() directly.

    YANG Description: This specifies if the dot1x is enabled on the port 
or not.
                    
The presence of this leaf indicates that the dot1x 
is enabled on the port.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="authentication", rest_name="authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable dot1x on a port'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """authentication must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="authentication", rest_name="authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable dot1x on a port'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='empty', is_config=True)""",
        })

    self.__authentication = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_authentication(self):
    self.__authentication = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="authentication", rest_name="authentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable dot1x on a port'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='empty', is_config=True)


  def _get_port_control(self):
    """
    Getter method for port_control, mapped from YANG variable /interface/hundredgigabitethernet/dot1x/port_control (enumeration)

    YANG Description: This leaf specifies the port state.
'auto' enables 802.1x authentication. The port 
moves to authorized state only after successful 
authentication. 'force-authorized' disables 802.1x
and port moves to authorized state without any 
authentication. 'force-unauthorized' causes the
port to remain in the unauthorized state,
ignoring all attempts by the client to 
authenticate.
    """
    return self.__port_control
      
  def _set_port_control(self, v, load=False):
    """
    Setter method for port_control, mapped from YANG variable /interface/hundredgigabitethernet/dot1x/port_control (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port_control is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port_control() directly.

    YANG Description: This leaf specifies the port state.
'auto' enables 802.1x authentication. The port 
moves to authorized state only after successful 
authentication. 'force-authorized' disables 802.1x
and port moves to authorized state without any 
authentication. 'force-unauthorized' causes the
port to remain in the unauthorized state,
ignoring all attempts by the client to 
authenticate.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'auto': {'value': 1}, u'force-unauthorized': {'value': 3}, u'force-authorized': {'value': 2}},), is_leaf=True, yang_name="port-control", rest_name="port-control", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Port control commands'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port_control must be of a type compatible with enumeration""",
          'defined-type': "brocade-dot1x:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'auto': {'value': 1}, u'force-unauthorized': {'value': 3}, u'force-authorized': {'value': 2}},), is_leaf=True, yang_name="port-control", rest_name="port-control", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Port control commands'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='enumeration', is_config=True)""",
        })

    self.__port_control = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port_control(self):
    self.__port_control = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'auto': {'value': 1}, u'force-unauthorized': {'value': 3}, u'force-authorized': {'value': 2}},), is_leaf=True, yang_name="port-control", rest_name="port-control", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Port control commands'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='enumeration', is_config=True)


  def _get_protocol_version(self):
    """
    Getter method for protocol_version, mapped from YANG variable /interface/hundredgigabitethernet/dot1x/protocol_version (uint32)

    YANG Description: This specifies the Extensible Authentication
Protocol version.
    """
    return self.__protocol_version
      
  def _set_protocol_version(self, v, load=False):
    """
    Setter method for protocol_version, mapped from YANG variable /interface/hundredgigabitethernet/dot1x/protocol_version (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_protocol_version is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_protocol_version() directly.

    YANG Description: This specifies the Extensible Authentication
Protocol version.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 2']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2), is_leaf=True, yang_name="protocol-version", rest_name="protocol-version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the protocol version'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """protocol_version must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 2']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2), is_leaf=True, yang_name="protocol-version", rest_name="protocol-version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the protocol version'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='uint32', is_config=True)""",
        })

    self.__protocol_version = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_protocol_version(self):
    self.__protocol_version = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 2']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2), is_leaf=True, yang_name="protocol-version", rest_name="protocol-version", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set the protocol version'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='uint32', is_config=True)


  def _get_quiet_period(self):
    """
    Getter method for quiet_period, mapped from YANG variable /interface/hundredgigabitethernet/dot1x/quiet_period (uint32)

    YANG Description: This specifies the quiet period in HELD state.
When the switch cannot authenticate the client
it stays idle for this period of time and tries
again. 
    """
    return self.__quiet_period
      
  def _set_quiet_period(self, v, load=False):
    """
    Setter method for quiet_period, mapped from YANG variable /interface/hundredgigabitethernet/dot1x/quiet_period (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_quiet_period is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_quiet_period() directly.

    YANG Description: This specifies the quiet period in HELD state.
When the switch cannot authenticate the client
it stays idle for this period of time and tries
again. 
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(60), is_leaf=True, yang_name="quiet-period", rest_name="quiet-period", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Quiet period in the HELD state'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """quiet_period must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(60), is_leaf=True, yang_name="quiet-period", rest_name="quiet-period", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Quiet period in the HELD state'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='uint32', is_config=True)""",
        })

    self.__quiet_period = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_quiet_period(self):
    self.__quiet_period = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 65535']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(60), is_leaf=True, yang_name="quiet-period", rest_name="quiet-period", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Quiet period in the HELD state'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='uint32', is_config=True)


  def _get_reauthMax(self):
    """
    Getter method for reauthMax, mapped from YANG variable /interface/hundredgigabitethernet/dot1x/reauthMax (uint32)

    YANG Description: This specifies the number of reauthentication 
attempts before becoming unauthorized.
    """
    return self.__reauthMax
      
  def _set_reauthMax(self, v, load=False):
    """
    Setter method for reauthMax, mapped from YANG variable /interface/hundredgigabitethernet/dot1x/reauthMax (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reauthMax is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reauthMax() directly.

    YANG Description: This specifies the number of reauthentication 
attempts before becoming unauthorized.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2), is_leaf=True, yang_name="reauthMax", rest_name="reauthMax", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Number of reauthentication attempts before becoming\nunauthorized'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reauthMax must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2), is_leaf=True, yang_name="reauthMax", rest_name="reauthMax", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Number of reauthentication attempts before becoming\nunauthorized'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='uint32', is_config=True)""",
        })

    self.__reauthMax = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reauthMax(self):
    self.__reauthMax = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'1 .. 10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(2), is_leaf=True, yang_name="reauthMax", rest_name="reauthMax", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Number of reauthentication attempts before becoming\nunauthorized'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='uint32', is_config=True)


  def _get_reauthentication(self):
    """
    Getter method for reauthentication, mapped from YANG variable /interface/hundredgigabitethernet/dot1x/reauthentication (empty)

    YANG Description: This specifies if the re-authentication should be 
done on a port.
                    
The presence of this leaf indicates that the 
re-authentication should be done.
    """
    return self.__reauthentication
      
  def _set_reauthentication(self, v, load=False):
    """
    Setter method for reauthentication, mapped from YANG variable /interface/hundredgigabitethernet/dot1x/reauthentication (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_reauthentication is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_reauthentication() directly.

    YANG Description: This specifies if the re-authentication should be 
done on a port.
                    
The presence of this leaf indicates that the 
re-authentication should be done.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="reauthentication", rest_name="reauthentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable reauthentication on a port'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """reauthentication must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="reauthentication", rest_name="reauthentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable reauthentication on a port'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='empty', is_config=True)""",
        })

    self.__reauthentication = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_reauthentication(self):
    self.__reauthentication = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="reauthentication", rest_name="reauthentication", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Enable reauthentication on a port'}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='empty', is_config=True)


  def _get_timeout(self):
    """
    Getter method for timeout, mapped from YANG variable /interface/hundredgigabitethernet/dot1x/timeout (container)

    YANG Description: This provides the grouping of all the timeout
configuration elements.
    """
    return self.__timeout
      
  def _set_timeout(self, v, load=False):
    """
    Setter method for timeout, mapped from YANG variable /interface/hundredgigabitethernet/dot1x/timeout (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_timeout is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_timeout() directly.

    YANG Description: This provides the grouping of all the timeout
configuration elements.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=timeout.timeout, is_container='container', presence=False, yang_name="timeout", rest_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set a timeout parameter', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """timeout must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=timeout.timeout, is_container='container', presence=False, yang_name="timeout", rest_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set a timeout parameter', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='container', is_config=True)""",
        })

    self.__timeout = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_timeout(self):
    self.__timeout = YANGDynClass(base=timeout.timeout, is_container='container', presence=False, yang_name="timeout", rest_name="timeout", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Set a timeout parameter', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-dot1x', defining_module='brocade-dot1x', yang_type='container', is_config=True)

  authentication = __builtin__.property(_get_authentication, _set_authentication)
  port_control = __builtin__.property(_get_port_control, _set_port_control)
  protocol_version = __builtin__.property(_get_protocol_version, _set_protocol_version)
  quiet_period = __builtin__.property(_get_quiet_period, _set_quiet_period)
  reauthMax = __builtin__.property(_get_reauthMax, _set_reauthMax)
  reauthentication = __builtin__.property(_get_reauthentication, _set_reauthentication)
  timeout = __builtin__.property(_get_timeout, _set_timeout)


  _pyangbind_elements = {'authentication': authentication, 'port_control': port_control, 'protocol_version': protocol_version, 'quiet_period': quiet_period, 'reauthMax': reauthMax, 'reauthentication': reauthentication, 'timeout': timeout, }


