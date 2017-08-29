# coding=utf-8
"""
"""
from __future__ import absolute_import, print_function

import wtforms.fields
from flask_wtf.file import FileField
from flask_wtf.html5 import IntegerField, TelField
from wtforms.ext.sqlalchemy.fields import QuerySelectField

import abilian.web.forms.fields as awbff
from abilian.i18n import country_choices
from abilian.web.forms import widgets as abilian_widgets
from abilian.web.forms.filters import lowercase, strip, uppercase
from abilian.web.forms.validators import VALIDATORS

__all__ = (
    'FORM_FIELDS',
    'FORM_FILTERS',
    'LIST_GENERATORS',
    'WIDGETS',
    'VALIDATORS',
)

# Postgres crops identifiers names silently. This can be a problem with alembic
# autogenerated revsions since intended column name will differ from actual name
# in database
#
MAX_IDENTIFIER_LENGTH = 63

FORM_FIELDS = (
    wtforms.fields.SelectField,
    wtforms.fields.BooleanField,
    wtforms.fields.TextField,
    wtforms.fields.TextAreaField,
    wtforms.fields.FloatField,
    wtforms.fields.DecimalField,
    wtforms.fields.IntegerField,
    QuerySelectField,
    FileField,
    TelField,
    IntegerField,
    awbff.Select2Field,
    awbff.Select2MultipleField,
    awbff.DateField,
)
FORM_FIELDS = {t.__name__: t for t in FORM_FIELDS}

FORM_FILTERS = {
    'strip': strip,
    'uppercase': uppercase,
    'lowercase': lowercase,
}

WIDGETS = (
    abilian_widgets.BooleanWidget,
    abilian_widgets.URLWidget,
    abilian_widgets.EmailWidget,
    abilian_widgets.MoneyWidget,
    abilian_widgets.HoursWidget,
)
WIDGETS = {t.__name__: t for t in WIDGETS}

LIST_GENERATORS = {'country': country_choices}


def update(module):
    """Install new column types, form fields, widgets, validators found in `module`."""
    for attr in __all__:
        values = getattr(module, attr, None)
        if values is None:
            continue

        definitions = globals()[attr]
        definitions.update(values)
