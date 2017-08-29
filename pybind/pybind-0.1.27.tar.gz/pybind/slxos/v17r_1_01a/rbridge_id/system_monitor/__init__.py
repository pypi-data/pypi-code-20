
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import fan
import power
import temp
import cid_card
import compact_flash
import MM
import LineCard
import SFM
class system_monitor(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/system-monitor. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__fan','__power','__temp','__cid_card','__compact_flash','__MM','__LineCard','__SFM',)

  _yang_name = 'system-monitor'
  _rest_name = 'system-monitor'

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
    self.__power = YANGDynClass(base=power.power, is_container='container', presence=False, yang_name="power", rest_name="power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold and alert setting for\ncomponent:POWER SUPPLY', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)
    self.__temp = YANGDynClass(base=temp.temp, is_container='container', presence=False, yang_name="temp", rest_name="temp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold for component:TEMPERATURE SENSOR', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)
    self.__MM = YANGDynClass(base=MM.MM, is_container='container', presence=False, yang_name="MM", rest_name="MM", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold setting for \n component:MM', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)
    self.__LineCard = YANGDynClass(base=LineCard.LineCard, is_container='container', presence=False, yang_name="LineCard", rest_name="LineCard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold and alert setting for \n component:LineCard', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)
    self.__cid_card = YANGDynClass(base=cid_card.cid_card, is_container='container', presence=False, yang_name="cid-card", rest_name="cid-card", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold and alert setting for\ncomponent:CID-CARD', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)
    self.__SFM = YANGDynClass(base=SFM.SFM, is_container='container', presence=False, yang_name="SFM", rest_name="SFM", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold setting for \n component:SFM', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)
    self.__fan = YANGDynClass(base=fan.fan, is_container='container', presence=False, yang_name="fan", rest_name="fan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold and alert setting for \n component:FAN', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)
    self.__compact_flash = YANGDynClass(base=compact_flash.compact_flash, is_container='container', presence=False, yang_name="compact-flash", rest_name="compact-flash", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold for component:COMPACT-FLASH', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)

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
      return [u'rbridge-id', u'system-monitor']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'system-monitor']

  def _get_fan(self):
    """
    Getter method for fan, mapped from YANG variable /rbridge_id/system_monitor/fan (container)
    """
    return self.__fan
      
  def _set_fan(self, v, load=False):
    """
    Setter method for fan, mapped from YANG variable /rbridge_id/system_monitor/fan (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fan() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=fan.fan, is_container='container', presence=False, yang_name="fan", rest_name="fan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold and alert setting for \n component:FAN', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fan must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=fan.fan, is_container='container', presence=False, yang_name="fan", rest_name="fan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold and alert setting for \n component:FAN', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)""",
        })

    self.__fan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fan(self):
    self.__fan = YANGDynClass(base=fan.fan, is_container='container', presence=False, yang_name="fan", rest_name="fan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold and alert setting for \n component:FAN', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)


  def _get_power(self):
    """
    Getter method for power, mapped from YANG variable /rbridge_id/system_monitor/power (container)
    """
    return self.__power
      
  def _set_power(self, v, load=False):
    """
    Setter method for power, mapped from YANG variable /rbridge_id/system_monitor/power (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_power is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_power() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=power.power, is_container='container', presence=False, yang_name="power", rest_name="power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold and alert setting for\ncomponent:POWER SUPPLY', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """power must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=power.power, is_container='container', presence=False, yang_name="power", rest_name="power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold and alert setting for\ncomponent:POWER SUPPLY', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)""",
        })

    self.__power = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_power(self):
    self.__power = YANGDynClass(base=power.power, is_container='container', presence=False, yang_name="power", rest_name="power", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold and alert setting for\ncomponent:POWER SUPPLY', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)


  def _get_temp(self):
    """
    Getter method for temp, mapped from YANG variable /rbridge_id/system_monitor/temp (container)
    """
    return self.__temp
      
  def _set_temp(self, v, load=False):
    """
    Setter method for temp, mapped from YANG variable /rbridge_id/system_monitor/temp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_temp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_temp() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=temp.temp, is_container='container', presence=False, yang_name="temp", rest_name="temp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold for component:TEMPERATURE SENSOR', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """temp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=temp.temp, is_container='container', presence=False, yang_name="temp", rest_name="temp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold for component:TEMPERATURE SENSOR', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)""",
        })

    self.__temp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_temp(self):
    self.__temp = YANGDynClass(base=temp.temp, is_container='container', presence=False, yang_name="temp", rest_name="temp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold for component:TEMPERATURE SENSOR', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)


  def _get_cid_card(self):
    """
    Getter method for cid_card, mapped from YANG variable /rbridge_id/system_monitor/cid_card (container)
    """
    return self.__cid_card
      
  def _set_cid_card(self, v, load=False):
    """
    Setter method for cid_card, mapped from YANG variable /rbridge_id/system_monitor/cid_card (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cid_card is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cid_card() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=cid_card.cid_card, is_container='container', presence=False, yang_name="cid-card", rest_name="cid-card", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold and alert setting for\ncomponent:CID-CARD', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cid_card must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=cid_card.cid_card, is_container='container', presence=False, yang_name="cid-card", rest_name="cid-card", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold and alert setting for\ncomponent:CID-CARD', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)""",
        })

    self.__cid_card = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cid_card(self):
    self.__cid_card = YANGDynClass(base=cid_card.cid_card, is_container='container', presence=False, yang_name="cid-card", rest_name="cid-card", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold and alert setting for\ncomponent:CID-CARD', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)


  def _get_compact_flash(self):
    """
    Getter method for compact_flash, mapped from YANG variable /rbridge_id/system_monitor/compact_flash (container)
    """
    return self.__compact_flash
      
  def _set_compact_flash(self, v, load=False):
    """
    Setter method for compact_flash, mapped from YANG variable /rbridge_id/system_monitor/compact_flash (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_compact_flash is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_compact_flash() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=compact_flash.compact_flash, is_container='container', presence=False, yang_name="compact-flash", rest_name="compact-flash", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold for component:COMPACT-FLASH', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """compact_flash must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=compact_flash.compact_flash, is_container='container', presence=False, yang_name="compact-flash", rest_name="compact-flash", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold for component:COMPACT-FLASH', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)""",
        })

    self.__compact_flash = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_compact_flash(self):
    self.__compact_flash = YANGDynClass(base=compact_flash.compact_flash, is_container='container', presence=False, yang_name="compact-flash", rest_name="compact-flash", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold for component:COMPACT-FLASH', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)


  def _get_MM(self):
    """
    Getter method for MM, mapped from YANG variable /rbridge_id/system_monitor/MM (container)
    """
    return self.__MM
      
  def _set_MM(self, v, load=False):
    """
    Setter method for MM, mapped from YANG variable /rbridge_id/system_monitor/MM (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_MM is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_MM() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=MM.MM, is_container='container', presence=False, yang_name="MM", rest_name="MM", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold setting for \n component:MM', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """MM must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=MM.MM, is_container='container', presence=False, yang_name="MM", rest_name="MM", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold setting for \n component:MM', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)""",
        })

    self.__MM = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_MM(self):
    self.__MM = YANGDynClass(base=MM.MM, is_container='container', presence=False, yang_name="MM", rest_name="MM", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold setting for \n component:MM', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)


  def _get_LineCard(self):
    """
    Getter method for LineCard, mapped from YANG variable /rbridge_id/system_monitor/LineCard (container)
    """
    return self.__LineCard
      
  def _set_LineCard(self, v, load=False):
    """
    Setter method for LineCard, mapped from YANG variable /rbridge_id/system_monitor/LineCard (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_LineCard is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_LineCard() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=LineCard.LineCard, is_container='container', presence=False, yang_name="LineCard", rest_name="LineCard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold and alert setting for \n component:LineCard', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """LineCard must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=LineCard.LineCard, is_container='container', presence=False, yang_name="LineCard", rest_name="LineCard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold and alert setting for \n component:LineCard', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)""",
        })

    self.__LineCard = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_LineCard(self):
    self.__LineCard = YANGDynClass(base=LineCard.LineCard, is_container='container', presence=False, yang_name="LineCard", rest_name="LineCard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold and alert setting for \n component:LineCard', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)


  def _get_SFM(self):
    """
    Getter method for SFM, mapped from YANG variable /rbridge_id/system_monitor/SFM (container)
    """
    return self.__SFM
      
  def _set_SFM(self, v, load=False):
    """
    Setter method for SFM, mapped from YANG variable /rbridge_id/system_monitor/SFM (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_SFM is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_SFM() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=SFM.SFM, is_container='container', presence=False, yang_name="SFM", rest_name="SFM", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold setting for \n component:SFM', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """SFM must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=SFM.SFM, is_container='container', presence=False, yang_name="SFM", rest_name="SFM", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold setting for \n component:SFM', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)""",
        })

    self.__SFM = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_SFM(self):
    self.__SFM = YANGDynClass(base=SFM.SFM, is_container='container', presence=False, yang_name="SFM", rest_name="SFM", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure threshold setting for \n component:SFM', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-system-monitor', defining_module='brocade-system-monitor', yang_type='container', is_config=True)

  fan = __builtin__.property(_get_fan, _set_fan)
  power = __builtin__.property(_get_power, _set_power)
  temp = __builtin__.property(_get_temp, _set_temp)
  cid_card = __builtin__.property(_get_cid_card, _set_cid_card)
  compact_flash = __builtin__.property(_get_compact_flash, _set_compact_flash)
  MM = __builtin__.property(_get_MM, _set_MM)
  LineCard = __builtin__.property(_get_LineCard, _set_LineCard)
  SFM = __builtin__.property(_get_SFM, _set_SFM)


  _pyangbind_elements = {'fan': fan, 'power': power, 'temp': temp, 'cid_card': cid_card, 'compact_flash': compact_flash, 'MM': MM, 'LineCard': LineCard, 'SFM': SFM, }


