# CAVEAT UTILITOR
#
# This file was automatically generated by Grako.
#
#    https://pypi.python.org/pypi/grako/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.


from __future__ import print_function, division, absolute_import, unicode_literals

from grako.buffering import Buffer
from grako.parsing import graken, Parser


KEYWORDS = {}


class CompositeModelExpressionBuffer(Buffer):
    def __init__(
        self,
        text,
        whitespace=None,
        nameguard=None,
        comments_re=None,
        eol_comments_re=None,
        ignorecase=None,
        namechars='',
        **kwargs
    ):
        super(CompositeModelExpressionBuffer, self).__init__(
            text,
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            namechars=namechars,
            **kwargs
        )


class CompositeModelExpressionParser(Parser):
    def __init__(
        self,
        whitespace=None,
        nameguard=None,
        comments_re=None,
        eol_comments_re=None,
        ignorecase=None,
        left_recursion=False,
        parseinfo=True,
        keywords=None,
        namechars='',
        buffer_class=CompositeModelExpressionBuffer,
        **kwargs
    ):
        if keywords is None:
            keywords = KEYWORDS
        super(CompositeModelExpressionParser, self).__init__(
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            left_recursion=left_recursion,
            parseinfo=parseinfo,
            keywords=keywords,
            namechars=namechars,
            buffer_class=buffer_class,
            **kwargs
        )

    @graken()
    def _result_(self):
        self._expr_()

    @graken()
    def _expr_(self):
        with self._choice():
            with self._option():
                self._term_()
                with self._group():
                    with self._choice():
                        with self._option():
                            self._token('+')
                        with self._option():
                            self._token('-')
                        self._error('expecting one of: + -')
                self._expr_()
            with self._option():
                self._term_()
            self._error('no available options')

    @graken()
    def _term_(self):
        with self._choice():
            with self._option():
                self._factor_()
                with self._group():
                    with self._choice():
                        with self._option():
                            self._token('*')
                        with self._option():
                            self._token('/')
                        self._error('expecting one of: * /')
                self._term_()
            with self._option():
                self._factor_()
            self._error('no available options')

    @graken()
    def _factor_(self):
        with self._choice():
            with self._option():
                self._token('(')
                self._expr_()
                self._token(')')
            with self._option():
                self._model_()
            self._error('no available options')

    @graken()
    def _model_(self):
        self._model_name_()
        with self._optional():
            self._token('(')
            self._nickname_()
            self._token(')')

    @graken()
    def _model_name_(self):
        self._pattern(r'[a-zA-Z_]\w*')

    @graken()
    def _nickname_(self):
        self._pattern(r'[a-zA-Z_]\w*')


class CompositeModelExpressionSemantics(object):
    def result(self, ast):
        return ast

    def expr(self, ast):
        return ast

    def term(self, ast):
        return ast

    def factor(self, ast):
        return ast

    def model(self, ast):
        return ast

    def model_name(self, ast):
        return ast

    def nickname(self, ast):
        return ast
