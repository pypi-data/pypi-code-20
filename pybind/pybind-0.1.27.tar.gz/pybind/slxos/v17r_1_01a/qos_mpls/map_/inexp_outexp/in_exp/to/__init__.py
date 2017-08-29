
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class to(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos-mpls - based on the path /qos-mpls/map/inexp-outexp/in-exp/to. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__out_exp',)

  _yang_name = 'to'
  _rest_name = 'to'

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
    self.__out_exp = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="out-exp", rest_name="out-exp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'out-exp value 0-7', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='int32', is_config=True)

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
      return [u'qos-mpls', u'map', u'inexp-outexp', u'in-exp', u'to']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'qos-mpls', u'map', u'inexp-outexp', u'in-exp', u'to']

  def _get_out_exp(self):
    """
    Getter method for out_exp, mapped from YANG variable /qos_mpls/map/inexp_outexp/in_exp/to/out_exp (int32)
    """
    return self.__out_exp
      
  def _set_out_exp(self, v, load=False):
    """
    Setter method for out_exp, mapped from YANG variable /qos_mpls/map/inexp_outexp/in_exp/to/out_exp (int32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_out_exp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_out_exp() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="out-exp", rest_name="out-exp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'out-exp value 0-7', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='int32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """out_exp must be of a type compatible with int32""",
          'defined-type': "int32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="out-exp", rest_name="out-exp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'out-exp value 0-7', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='int32', is_config=True)""",
        })

    self.__out_exp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_out_exp(self):
    self.__out_exp = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['-2147483648..2147483647']}, int_size=32), restriction_dict={'range': [u'0 .. 7']}), is_leaf=True, yang_name="out-exp", rest_name="out-exp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'out-exp value 0-7', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos-mpls', defining_module='brocade-qos-mpls', yang_type='int32', is_config=True)

  out_exp = __builtin__.property(_get_out_exp, _set_out_exp)


  _pyangbind_elements = {'out_exp': out_exp, }


