# -*- coding: utf-8 -*-
# Copyright (c) 2016 Sqreen. All Rights Reserved.
# Please refer to our terms for more information: https://www.sqreen.io/terms.html
""" Custom error page for Pyramid
"""
from ..exceptions import AttackBlocked
from .sqreen_error_page import BaseSqreenErrorPage
from .headers_insert import convert_to_str


class SqreenErrorPagePyramid(BaseSqreenErrorPage):

    @staticmethod
    def _get_exception(registry, request, context, *args, **kwargs):
        if not context:
            return

        # Ignore exception which are not attack blocked
        if not isinstance(context, AttackBlocked):
            return

        return context

    @staticmethod
    def _get_response(exception, content, status_code, headers={}):
        from pyramid.response import Response
        response = Response(content, status_code=status_code)

        for header_name, header_value in convert_to_str(headers.items()):
            response.headers[header_name] = header_value

        return response
