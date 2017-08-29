
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class line_speed(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/management/line-speed. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The line-speed characteristics for this management 
interface.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__actual','__configured',)

  _yang_name = 'line-speed'
  _rest_name = 'line-speed'

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
    self.__configured = YANGDynClass(base=unicode, is_leaf=True, yang_name="configured", rest_name="configured", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The configured line-speed for this management \ninterface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='string', is_config=False)
    self.__actual = YANGDynClass(base=unicode, is_leaf=True, yang_name="actual", rest_name="actual", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The actual line-speed for this management \ninterface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='string', is_config=False)

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
      return [u'interface', u'management', u'line-speed']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Management', u'line-speed']

  def _get_actual(self):
    """
    Getter method for actual, mapped from YANG variable /interface/management/line_speed/actual (string)

    YANG Description: The actual line-speed for this management 
interface.
    """
    return self.__actual
      
  def _set_actual(self, v, load=False):
    """
    Setter method for actual, mapped from YANG variable /interface/management/line_speed/actual (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_actual is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_actual() directly.

    YANG Description: The actual line-speed for this management 
interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="actual", rest_name="actual", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The actual line-speed for this management \ninterface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """actual must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="actual", rest_name="actual", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The actual line-speed for this management \ninterface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='string', is_config=False)""",
        })

    self.__actual = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_actual(self):
    self.__actual = YANGDynClass(base=unicode, is_leaf=True, yang_name="actual", rest_name="actual", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The actual line-speed for this management \ninterface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='string', is_config=False)


  def _get_configured(self):
    """
    Getter method for configured, mapped from YANG variable /interface/management/line_speed/configured (string)

    YANG Description: The configured line-speed for this management 
interface.
    """
    return self.__configured
      
  def _set_configured(self, v, load=False):
    """
    Setter method for configured, mapped from YANG variable /interface/management/line_speed/configured (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_configured is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_configured() directly.

    YANG Description: The configured line-speed for this management 
interface.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="configured", rest_name="configured", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The configured line-speed for this management \ninterface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """configured must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="configured", rest_name="configured", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The configured line-speed for this management \ninterface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='string', is_config=False)""",
        })

    self.__configured = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_configured(self):
    self.__configured = YANGDynClass(base=unicode, is_leaf=True, yang_name="configured", rest_name="configured", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The configured line-speed for this management \ninterface.'}}, namespace='urn:brocade.com:mgmt:brocade-interface', defining_module='brocade-interface', yang_type='string', is_config=False)

  actual = __builtin__.property(_get_actual)
  configured = __builtin__.property(_get_configured)


  _pyangbind_elements = {'actual': actual, 'configured': configured, }


