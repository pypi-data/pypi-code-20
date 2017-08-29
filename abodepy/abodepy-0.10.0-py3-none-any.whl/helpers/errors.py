"""Errors for AbodePy."""
USERNAME = (0, "Username must be a non-empty string")

PASSWORD = (1, "Password must be a non-empty string")

REQUEST = (2, "Request failed")

SET_STATUS_DEV_ID = (
    3, "Device status/level response ID does not match request ID")

SET_STATUS_STATE = (
    4, "Device status/level value does not match request value")

REFRESH = (5, "Failed to refresh device")

SET_MODE = (6, "Failed to set alarm mode")

SET_MODE_AREA = (7, "Set mode response area does not match request area")

SET_MODE_MODE = (8, "Set mode response mode does not match request mode")

INVALID_ALARM_MODE = (9, "Mode is not of a known alarm mode value")

MISSING_ALARM_MODE = (10, "No alarm mode found in object")

INVALID_DEFAULT_ALARM_MODE = (
    11, "Default alarm mode must be one of 'home' or 'away'")

INVALID_DEVICE_ID = (12, "The given value is not a device or valid device ID")

INVALID_SETTING = (
    13, "Setting is not valid")

INVALID_SETTING_VALUE = (
    14, "Value for setting is not valid")

INVALID_AUTOMATION_REFRESH_RESPONSE = (
    15, "Automation refresh response did not match expected values.")

INVALID_AUTOMATION_EDIT_RESPONSE = (
    16, "Automation edit response did not match expected values.")

TRIGGER_NON_QUICKACTION = (
    17, "Can not trigger an automation that is not a manual quick-action.")

UNABLE_TO_MAP_DEVICE = (
    18, "Unable to map device json to device class - no type tag found.")

EVENT_CODE_MISSING = (
    19, "Event is not valid, start and end event codes are missing.")

EVENT_CODE_MISSING = (
    20, "Timeline event is not valid, event code missing.")

INVALID_TIMELINE_EVENT = (
    21, "Timeline event received missing an event code or type.")

EVENT_GROUP_INVALID = (
    22, "Timeline event group is not valid.")

EVENT_DEVICE_INVALID = (
    112, "Object given to event registration service is not a device object")
