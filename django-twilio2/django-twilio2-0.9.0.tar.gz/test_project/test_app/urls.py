# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url

from .views import (
    response_view, str_view, bytes_view, verb_view,
    BytesView, StrView, ResponseView, VerbView
)

# Test URLs for our ``django_twilio.decorators`` module.
urlpatterns = [
    url(r'^test_app/decorators/response_view/$', response_view),
    url(r'^test_app/decorators/response_class_view/$', ResponseView.as_view()),
    url(r'^test_app/decorators/str_view/$', str_view),
    url(r'^test_app/decorators/str_class_view/$', StrView.as_view()),
    url(r'^test_app/decorators/bytes_view/$', bytes_view),
    url(r'^test_app/decorators/bytes_class_view/$', BytesView.as_view()),
    url(r'^test_app/decorators/verb_view/$', verb_view),
    url(r'^test_app/decorators/verb_class_view/$', VerbView.as_view())
]
