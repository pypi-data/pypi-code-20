
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
  from YANG module brocade-rbridge - based on the path /rbridge-id/route-map/content/match/community. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Community Access List Name.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__community_access_list_name',)

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
    self.__community_access_list_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="community-access-list-name", rest_name="community-access-list-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-completion-actionpoint': u'ip-community-std-action-point', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='match-community-list-name-t', is_config=True)

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
      return [u'rbridge-id', u'route-map', u'content', u'match', u'community']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'route-map', u'match', u'community']

  def _get_community_access_list_name(self):
    """
    Getter method for community_access_list_name, mapped from YANG variable /rbridge_id/route_map/content/match/community/community_access_list_name (match-community-list-name-t)
    """
    return self.__community_access_list_name
      
  def _set_community_access_list_name(self, v, load=False):
    """
    Setter method for community_access_list_name, mapped from YANG variable /rbridge_id/route_map/content/match/community/community_access_list_name (match-community-list-name-t)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_community_access_list_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_community_access_list_name() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="community-access-list-name", rest_name="community-access-list-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-completion-actionpoint': u'ip-community-std-action-point', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='match-community-list-name-t', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """community_access_list_name must be of a type compatible with match-community-list-name-t""",
          'defined-type': "brocade-ip-policy:match-community-list-name-t",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="community-access-list-name", rest_name="community-access-list-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-completion-actionpoint': u'ip-community-std-action-point', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='match-community-list-name-t', is_config=True)""",
        })

    self.__community_access_list_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_community_access_list_name(self):
    self.__community_access_list_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="community-access-list-name", rest_name="community-access-list-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-completion-actionpoint': u'ip-community-std-action-point', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-ip-policy', defining_module='brocade-ip-policy', yang_type='match-community-list-name-t', is_config=True)

  community_access_list_name = __builtin__.property(_get_community_access_list_name, _set_community_access_list_name)


  _pyangbind_elements = {'community_access_list_name': community_access_list_name, }


