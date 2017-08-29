
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class extcommunity(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-ip-policy - based on the path /hide-routemap-holder/route-map/content/match/extcommunity. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Match BGP/VPN extended community list
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__extcommunity_num',)

  _yang_name = 'extcommunity'
  _rest_name = 'extcommunity'

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
    self.__extcommunity_num = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((0|[1-9][0-9]{0,1})(\\s+(0|[1-9][0-9]{0,1}))*)'}), is_leaf=True, yang_name="extcommunity-num", rest_name="extcommunity-num", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Extcommunity numbers', u'cli-drop-node-name': None, u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='extcommunitylist-expr', is_config=True)

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
      return [u'hide-routemap-holder', u'route-map', u'content', u'match', u'extcommunity']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'route-map', u'match', u'extcommunity']

  def _get_extcommunity_num(self):
    """
    Getter method for extcommunity_num, mapped from YANG variable /hide_routemap_holder/route_map/content/match/extcommunity/extcommunity_num (extcommunitylist-expr)
    """
    return self.__extcommunity_num
      
  def _set_extcommunity_num(self, v, load=False):
    """
    Setter method for extcommunity_num, mapped from YANG variable /hide_routemap_holder/route_map/content/match/extcommunity/extcommunity_num (extcommunitylist-expr)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_extcommunity_num is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_extcommunity_num() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((0|[1-9][0-9]{0,1})(\\s+(0|[1-9][0-9]{0,1}))*)'}), is_leaf=True, yang_name="extcommunity-num", rest_name="extcommunity-num", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Extcommunity numbers', u'cli-drop-node-name': None, u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='extcommunitylist-expr', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """extcommunity_num must be of a type compatible with extcommunitylist-expr""",
          'defined-type': "brocade-ip-policy:extcommunitylist-expr",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((0|[1-9][0-9]{0,1})(\\s+(0|[1-9][0-9]{0,1}))*)'}), is_leaf=True, yang_name="extcommunity-num", rest_name="extcommunity-num", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Extcommunity numbers', u'cli-drop-node-name': None, u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='extcommunitylist-expr', is_config=True)""",
        })

    self.__extcommunity_num = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_extcommunity_num(self):
    self.__extcommunity_num = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'((0|[1-9][0-9]{0,1})(\\s+(0|[1-9][0-9]{0,1}))*)'}), is_leaf=True, yang_name="extcommunity-num", rest_name="extcommunity-num", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Extcommunity numbers', u'cli-drop-node-name': None, u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='extcommunitylist-expr', is_config=True)

  extcommunity_num = __builtin__.property(_get_extcommunity_num, _set_extcommunity_num)


  _pyangbind_elements = {'extcommunity_num': extcommunity_num, }


