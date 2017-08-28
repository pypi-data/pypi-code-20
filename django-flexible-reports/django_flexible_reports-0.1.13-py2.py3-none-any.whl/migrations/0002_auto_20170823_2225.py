# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-23 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flexible_reports', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='subtitle',
        ),
        migrations.RemoveField(
            model_name='reportelement',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='column',
            name='exclude_from_export',
            field=models.BooleanField(default=False, help_text='Exclude this column when exporting to other, non-browserformats, like MS Word or MS Excel', verbose_name='Exclude from export'),
        ),
        migrations.AddField(
            model_name='column',
            name='strip_html_on_export',
            field=models.BooleanField(default=True, help_text='Strip HTML tags when exporting to other, non-browser \n        formats, like MS Word or MS Excel. ', verbose_name='Strip HTML on export'),
        ),
        migrations.AlterField(
            model_name='column',
            name='attr_name',
            field=models.CharField(blank=True, help_text='\n        Attribute name on the parent table\'s base model.\n\n        If this column is sortable, that attribute is used to sort this\n        column.\n\n        In case no value is given in "Template" field,\n        this attribute will be used to get information from model\n        instances.\n\n        Warning, if you want to make this column sortable, you need to\n        provide this value.\n\n        This value can contain dot notation to reference fields in related\n        models.\n        ', max_length=200, null=True, verbose_name='Attribute name'),
        ),
        migrations.AlterField(
            model_name='column',
            name='footer_template',
            field=models.TextField(blank=True, default='{{ value }}', help_text='\n        Template for footer. Used only if "Display totals" is enabled. ', null=True, verbose_name='Footer template'),
        ),
        migrations.AlterField(
            model_name='column',
            name='sortable',
            field=models.BooleanField(default=True, verbose_name='Sortable'),
        ),
        migrations.AlterField(
            model_name='column',
            name='template',
            field=models.TextField(blank=True, default='{{ value }}', help_text='If empty, the value of the object\'s attribute from\n        "Attribute name" field will be used instead.\n\n        Template will get following values in it\'s context:\n        - *record*  -- data record for the current row\n        - *value*   -- value from `record` that corresponds to the current column\n        - *default* -- appropriate default value to use as fallback\n        ', null=True, verbose_name='Template'),
        ),
        migrations.AlterField(
            model_name='table',
            name='empty_template',
            field=models.TextField(blank=True, default='There is no data for this table.', help_text='\n        Template which will be displayed when there is no data for this\n        table.\n        ', null=True, verbose_name='Empty template'),
        ),
        migrations.AlterField(
            model_name='table',
            name='group_prefix',
            field=models.CharField(blank=True, help_text='this value is used as a prefix only when "Sort\n        option" is set to "sort in group"\n        ', max_length=200, null=True, verbose_name='Group prefix'),
        ),
        migrations.AlterField(
            model_name='table',
            name='sort_option',
            field=models.IntegerField(choices=[(0, "sort with other tables - if a column in this table is sorted, all the other tables\n    on the page with columns with identical name will be sorted too, as long\n    as they also are marked as 'sort with other tables'\n    "), (1, 'sort individually - this table will be sorted individually; even if other\n    tables on the page have columns with same label this table will be\n    sorted independently'), (2, 'sort in group - this table will be sorted together with a group of\n    tables; you must enter a prefix for this group')], default=0, verbose_name='Sort option'),
        ),
    ]
