# -*- coding: utf-8 -*-
# Copyright (c) 2016 Sqreen. All Rights Reserved.
# Please refer to our terms for more information: https://www.sqreen.io/terms.html
""" Generic WSGI HTTP Request / Response stuff
"""
from logging import getLogger
from itertools import chain
from copy import copy
from traceback import format_stack

from .base import BaseRequest
from .ip_utils import get_real_user_ip

try:
    from Cookie import SimpleCookie
except ImportError:
    from http.cookies import SimpleCookie

try:
    from urllib.parse import parse_qs, quote
except ImportError:
    from urlparse import parse_qs
    from urllib import quote


LOGGER = getLogger(__name__)


class WSGIRequest(BaseRequest):
    """ Helper around raw wsgi environ
    """

    def __init__(self, environ):
        super(WSGIRequest, self).__init__()
        self.environ = environ

        form_environ = copy(self.environ)
        form_environ['QUERY_STRING'] = ''

        # TODO: Reactivate reading the body

        self.cookies = self._parse_cookies(form_environ.get('HTTP_COOKIES'))

    @staticmethod
    def _parse_cookies(cookies):
        if not cookies:
            return {}

        cookie = SimpleCookie()
        cookie.load(cookies)

        return {key: cookie[key].coded_value for key in cookie.keys()}

    @property
    def query_params(self):
        """ Return parsed query string from request
        """
        raw_query = self.environ.get('QUERY_STRING', '')
        try:
            return parse_qs(raw_query)
        except Exception:
            LOGGER.warning("Exception while parsing %s", raw_query, exc_info=True)
            return {}

    @property
    def form_params(self):
        # TODO: Reactivate reading the body
        return {}

    @property
    def cookies_params(self):
        return self.cookies

    @property
    def query_params_values(self):
        """ Return only query values as a list
        """
        return list(chain.from_iterable(self.query_params.values()))

    @property
    def client_ip(self):
        return get_real_user_ip(self.environ.get('REMOTE_ADDR'),
                                self.environ.get('HTTP_X_FORWARDED_FOR', ''))

    @property
    def hostname(self):
        return self.environ.get('HTTP_HOST', self.environ.get('SERVER_NAME'))

    @property
    def method(self):
        return self.environ.get('REQUEST_METHOD')

    @property
    def client_user_agent(self):
        return self.environ.get('HTTP_USER_AGENT')

    @property
    def referer(self):
        return self.environ.get('HTTP_REFERER')

    @property
    def scheme(self):
        return self.environ.get('wsgi.url_scheme')

    @property
    def server_port(self):
        return self.environ.get('SERVER_PORT')

    @property
    def remote_port(self):
        return self.environ.get('REMOTE_PORT')

    @property
    def path(self):
        return quote(self.environ.get('SCRIPT_NAME', '')) + quote(self.environ.get('PATH_INFO', ''))

    def get_header(self, name):
        """ Get a specific header name
        """
        return self.environ.get(name)

    @property
    def caller(self):
        return format_stack()

    @property
    def view_params(self):
        return {}

    @property
    def json_params(self):
        return {}
