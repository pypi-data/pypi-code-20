
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class fabric_isl(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/hundredgigabitethernet/fabric/fabric-isl. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configure the Fabric Protocol ISL parameters
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__fabric_isl_enable',)

  _yang_name = 'fabric-isl'
  _rest_name = 'isl'

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
    self.__fabric_isl_enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fabric-isl-enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure fabric isl status ', u'cli-show-no': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)

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
      return [u'interface', u'hundredgigabitethernet', u'fabric', u'fabric-isl']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'HundredGigabitEthernet', u'fabric', u'isl']

  def _get_fabric_isl_enable(self):
    """
    Getter method for fabric_isl_enable, mapped from YANG variable /interface/hundredgigabitethernet/fabric/fabric_isl/fabric_isl_enable (empty)

    YANG Description: Configure the Fabric Protocol ISL status
    """
    return self.__fabric_isl_enable
      
  def _set_fabric_isl_enable(self, v, load=False):
    """
    Setter method for fabric_isl_enable, mapped from YANG variable /interface/hundredgigabitethernet/fabric/fabric_isl/fabric_isl_enable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fabric_isl_enable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fabric_isl_enable() directly.

    YANG Description: Configure the Fabric Protocol ISL status
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="fabric-isl-enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure fabric isl status ', u'cli-show-no': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fabric_isl_enable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fabric-isl-enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure fabric isl status ', u'cli-show-no': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)""",
        })

    self.__fabric_isl_enable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fabric_isl_enable(self):
    self.__fabric_isl_enable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="fabric-isl-enable", rest_name="enable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure fabric isl status ', u'cli-show-no': None, u'alt-name': u'enable'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe', defining_module='brocade-fcoe', yang_type='empty', is_config=True)

  fabric_isl_enable = __builtin__.property(_get_fabric_isl_enable, _set_fabric_isl_enable)


  _pyangbind_elements = {'fabric_isl_enable': fabric_isl_enable, }


