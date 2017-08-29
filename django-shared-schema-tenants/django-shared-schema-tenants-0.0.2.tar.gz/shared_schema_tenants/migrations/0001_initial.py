# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 23:37
from __future__ import unicode_literals

import django.utils.version
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import shared_schema_tenants.validators

try:
    import django.contrib.postgres.fields.jsonb
except ImportError:
    pass


sites_dep_migration = ('sites', '0002_alter_domain_unique',)
if django.utils.version.get_complete_version()[1] < 10:
    sites_dep_migration = ('sites', '0001_initial',)


tenant_fields = [
    ('created', model_utils.fields.AutoCreatedField(
        default=django.utils.timezone.now, editable=False, verbose_name='created')),
    ('modified', model_utils.fields.AutoLastModifiedField(
        default=django.utils.timezone.now, editable=False, verbose_name='modified')),
    ('name', models.CharField(max_length=255)),
    ('slug', models.CharField(max_length=255, primary_key=True, serialize=False)),
]

if 'postgresql' in settings.DATABASES['default']['ENGINE']:
    tenant_fields.extend([
        ('settings', django.contrib.postgres.fields.jsonb.JSONField(
            blank=True, default={}, null=True)),
        ('extra_data', django.contrib.postgres.fields.jsonb.JSONField(
            blank=True, default={}, null=True)),
    ])
else:
    tenant_fields.extend([
        ('_settings', models.TextField(blank=True, default="", null=True,
                                       validators=[shared_schema_tenants.validators.validate_json])),
        ('_extra_data', models.TextField(blank=True, default={}, null=True,
                                         validators=[shared_schema_tenants.validators.validate_json])),
    ])


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        sites_dep_migration,
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=tenant_fields,
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TenantRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('groups', models.ManyToManyField(blank=True,
                                                  related_name='user_tenant_groups', to='auth.Group')),
                ('permissions', models.ManyToManyField(blank=True,
                                                       related_name='user_tenant_permissions', to='auth.Permission')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                             related_name='relationships', to='shared_schema_tenants.Tenant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                           related_name='relationships', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TenantSite',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(
                    default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,
                                              related_name='tenant_site', to='sites.Site')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                             related_name='tenant_sites', to='shared_schema_tenants.Tenant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='tenantrelationship',
            unique_together=set([('user', 'tenant')]),
        ),
    ]
