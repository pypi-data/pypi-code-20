from shared_schema_tenants.settings import (
    DEFAULT_TENANT_SETTINGS_FIELDS, DEFAULT_TENANT_SETTINGS)

from shared_schema_tenants.helpers.tenant_json_field import TenantJSONFieldHelper


class TenantSettingsHelper(TenantJSONFieldHelper):

    def __init__(self, instance=None):
        super(TenantSettingsHelper, self).__init__(
            instance_field_name='settings', instance=instance,
            tenant_fields=DEFAULT_TENANT_SETTINGS_FIELDS,
            tenant_default_fields_values=DEFAULT_TENANT_SETTINGS)
