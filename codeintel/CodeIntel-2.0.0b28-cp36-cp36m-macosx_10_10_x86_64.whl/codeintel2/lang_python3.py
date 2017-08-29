#!/usr/bin/env python
# Copyright (c) 2010 ActiveState Software Inc.
# See LICENSE.txt for license details.

"""Python 3 support for CodeIntel"""

from __future__ import absolute_import
import logging

from codeintel2.common import LazyClassAttribute
from codeintel2.lang_python import (PythonLexer, PythonLangIntel,
                                    PythonImportsEvaluator, PythonBuffer,
                                    PythonImportHandler, PythonCILEDriver)


#---- globals

lang = "Python3"
log = logging.getLogger("codeintel.python3")
#log.setLevel(logging.DEBUG)


#---- language support

class Python3Lexer(PythonLexer):
    lang = lang

class Python3LangIntel(PythonLangIntel):
    lang = lang
    interpreterPrefName = "python3"
    extraPathsPrefName = "python3ExtraPaths"
    excludePathsPrefName = "python3ExcludePaths"

    @LazyClassAttribute
    def keywords(self):
        from SilverCity.Keywords import python3_keywords
        return python3_keywords.split(" ")

class Python3Buffer(PythonBuffer):
    lang = lang

class Python3ImportHandler(PythonImportHandler):
    lang = lang

class Python3CILEDriver(PythonCILEDriver):
    lang = lang

#---- registration

def register(mgr):
    """Register language support with the Manager."""
    mgr.set_lang_info(lang,
                      silvercity_lexer=Python3Lexer(),
                      buf_class=Python3Buffer,
                      langintel_class=Python3LangIntel,
                      import_handler_class=Python3ImportHandler,
                      cile_driver_class=Python3CILEDriver,
                      is_cpln_lang=True)
