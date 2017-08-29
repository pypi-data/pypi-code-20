
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import switchport
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface-ext - based on the path /brocade_interface_ext_rpc/get-interface-switchport/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__switchport',)

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
    self.__switchport = YANGDynClass(base=YANGListType("interface_type interface_name",switchport.switchport, yang_name="switchport", rest_name="switchport", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-type interface-name', extensions=None), is_container='list', yang_name="switchport", rest_name="switchport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='list', is_config=True)

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
      return [u'brocade_interface_ext_rpc', u'get-interface-switchport', u'output']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-interface-switchport', u'output']

  def _get_switchport(self):
    """
    Getter method for switchport, mapped from YANG variable /brocade_interface_ext_rpc/get_interface_switchport/output/switchport (list)

    YANG Description: This is a list of all the switch-ports in the 
managed device. Each row represents an L2 port 
along with the operational characteristics.
    """
    return self.__switchport
      
  def _set_switchport(self, v, load=False):
    """
    Setter method for switchport, mapped from YANG variable /brocade_interface_ext_rpc/get_interface_switchport/output/switchport (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_switchport is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_switchport() directly.

    YANG Description: This is a list of all the switch-ports in the 
managed device. Each row represents an L2 port 
along with the operational characteristics.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("interface_type interface_name",switchport.switchport, yang_name="switchport", rest_name="switchport", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-type interface-name', extensions=None), is_container='list', yang_name="switchport", rest_name="switchport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """switchport must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("interface_type interface_name",switchport.switchport, yang_name="switchport", rest_name="switchport", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-type interface-name', extensions=None), is_container='list', yang_name="switchport", rest_name="switchport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='list', is_config=True)""",
        })

    self.__switchport = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_switchport(self):
    self.__switchport = YANGDynClass(base=YANGListType("interface_type interface_name",switchport.switchport, yang_name="switchport", rest_name="switchport", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='interface-type interface-name', extensions=None), is_container='list', yang_name="switchport", rest_name="switchport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-interface-ext', defining_module='brocade-interface-ext', yang_type='list', is_config=True)

  switchport = __builtin__.property(_get_switchport, _set_switchport)


  _pyangbind_elements = {'switchport': switchport, }


