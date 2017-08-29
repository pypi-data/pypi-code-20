#!python
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
# 
# The contents of this file are subject to the Mozilla Public License
# Version 1.1 (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
# 
# Software distributed under the License is distributed on an "AS IS"
# basis, WITHOUT WARRANTY OF ANY KIND, either express or implied. See the
# License for the specific language governing rights and limitations
# under the License.
# 
# The Original Code is Komodo code.
# 
# The Initial Developer of the Original Code is ActiveState Software Inc.
# Portions created by ActiveState Software Inc are Copyright (C) 2000-2007
# ActiveState Software Inc. All Rights Reserved.
# 
# Contributor(s):
#   ActiveState Software Inc
# 
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
# 
# ***** END LICENSE BLOCK *****

"""UDL (User-Defined Language) support for codeintel."""

from __future__ import absolute_import
import os
from os.path import dirname, join, abspath, normpath, basename, exists
import sys
import re
import logging
import threading
import operator
import traceback
from pprint import pprint, pformat
import six

import SilverCity
from SilverCity import ScintillaConstants
from SilverCity.ScintillaConstants import * #XXX import only what we need
from SilverCity.Lexer import Lexer

from codeintel2.common import *
from codeintel2.citadel import CitadelBuffer
#from codeintel2.javascript_common import trg_from_pos as javascript_trg_from_pos

if _xpcom_:
    from xpcom import components
    from xpcom.server import UnwrapObject

log = logging.getLogger("codeintel.udl")
#log.setLevel(logging.DEBUG)

#XXX We need to have a better mechanism for rationalizing and sharing
#    common lexer style classes. For now we'll just HACKily grab from
#    Komodo's styles.py. Some of this is duplicating logic in
#    KoLanguageServiceBase.py.
_ko_src_dir = normpath(join(dirname(__file__), *([os.pardir]*3)))
sys.path.insert(0, join(_ko_src_dir, "schemes"))
try:
    import styles
finally:
    del sys.path[0]
    del _ko_src_dir




#---- module interface

# Test 'udl/general/is_udl_x_style' tests these.
def is_udl_m_style(style):
    return (ScintillaConstants.SCE_UDL_M_DEFAULT <= style
            <= ScintillaConstants.SCE_UDL_M_UPPER_BOUND)
def is_udl_css_style(style):
    return (ScintillaConstants.SCE_UDL_CSS_DEFAULT <= style
            <= ScintillaConstants.SCE_UDL_CSS_UPPER_BOUND)
def is_udl_csl_style(style):
    return (ScintillaConstants.SCE_UDL_CSL_DEFAULT <= style
            <= ScintillaConstants.SCE_UDL_CSL_UPPER_BOUND)
def is_udl_ssl_style(style):
    return (ScintillaConstants.SCE_UDL_SSL_DEFAULT <= style
            <= ScintillaConstants.SCE_UDL_SSL_UPPER_BOUND)
def is_udl_tpl_style(style):
    return (ScintillaConstants.SCE_UDL_TPL_DEFAULT <= style
            <= ScintillaConstants.SCE_UDL_TPL_UPPER_BOUND)

#XXX Redundant code from koUDLLanguageBase.py::KoUDLLanguage
# Necessary because SilverCity.WordList splits input on white-space

_re_bad_filename_char = re.compile(r'([% 	\x80-\xff])')
def _lexudl_path_escape(m):
    return '%%%02X' % ord(m.group(1))
def _urlescape(s):
    return _re_bad_filename_char.sub(_lexudl_path_escape, s)

class UDLLexer(Lexer):
    """LexUDL wants the path to the .lexres file as the first element of
    the first keywords list.
    """
    _lock = threading.Lock()
    _lexresfile_from_lang = None
    _extra_lexer_dirs = set()

    def __init__(self):
        self._properties = SilverCity.PropertySet()
        self._lexer = SilverCity.find_lexer_module_by_id(ScintillaConstants.SCLEX_UDL)
        lexres_path = _urlescape(self._get_lexres_path())
        log.debug("escaped lexres_path: %r", lexres_path)
        self._keyword_lists = [
            SilverCity.WordList(lexres_path),
        ]

    def tokenize_by_style(self, text, call_back=None):
        """LexUDL.cxx currently isn't thread-safe."""
        self._lock.acquire()
        try:
            return Lexer.tokenize_by_style(self, text, call_back)
        finally:
            self._lock.release()

    @staticmethod
    def add_extra_lexer_dirs(dirs):
        UDLLexer._extra_lexer_dirs.update(dirs)
        UDLLexer._lexresfile_from_lang = None

    if _xpcom_:
        # Presume we are running under Komodo. Look in the available
        # lexres dirs from extensions.

        @staticmethod
        def _generate_lexer_mapping():
            """Return dict {name > filename} of all lexer resource files (i.e.
            those ones that can include compiled UDL .lexres files).
    
            It yields directories that should "win" first.
            """
            from glob import glob
            from directoryServiceUtils import getExtensionLexerDirs
            lexresfile_from_lang = {}
            koDirs = components.classes["@activestate.com/koDirs;1"] \
                .getService(components.interfaces.koIDirs)

            # Find all possible lexer dirs.
            lexer_dirs = []
            lexer_dirs.append(join(koDirs.userDataDir, "lexers"))    # user
            lexer_dirs += getExtensionLexerDirs()                    # extensions
            lexer_dirs.append(join(koDirs.commonDataDir, "lexers"))  # site/common
            lexer_dirs.append(join(koDirs.supportDir, "lexers"))     # factory
            for extra_dir in UDLLexer._extra_lexer_dirs:
                lexer_dirs.append(extra_dir)

            # Find all .lexeres files in these lexer dirs.
            for d in reversed(lexer_dirs):  # first come, first served
                lexer_files = glob(join(d, "*.lexres"))
                for f in lexer_files:
                    # Get lowered name without the ".lexres" extension.
                    name = basename(f).lower().rsplit(".", 1)[0]
                    lexresfile_from_lang[name] = f
            return lexresfile_from_lang

    else:
        @staticmethod
        def _generate_lexer_mapping():
            """Return dict {name > filename} of all lexer resource files (i.e.
            those ones that can include compiled UDL .lexres files).

            It yields directories that should "win" first.
            """
            from glob import glob
            lexresfile_from_lang = {}

            # Find all possible lexer dirs.
            lexer_dirs = []
            lexer_dirs.append(join(dirname(__file__), "lexers"))
            for extra_dir in UDLLexer._extra_lexer_dirs:
                lexer_dirs.append(extra_dir)

            # Find all .lexeres files in these lexer dirs.
            for d in reversed(lexer_dirs):  # first come, first served
                lexer_files = glob(join(d, "*.lexres"))
                for f in lexer_files:
                    # Get lowered name without the ".lexres" extension.
                    name = basename(f).lower().rsplit(".", 1)[0]
                    lexresfile_from_lang[name] = f
            return lexresfile_from_lang

    def _get_lexres_path(self):
        lexresfile_from_lang = UDLLexer._lexresfile_from_lang
        if lexresfile_from_lang is None:
            # Generate and cache it.
            lexresfile_from_lang = self._generate_lexer_mapping()
            UDLLexer._lexresfile_from_lang = lexresfile_from_lang

        lexres_file = lexresfile_from_lang.get(self.lang.lower())
        if lexres_file is None:
            raise CodeIntelError("could not find lexres file for %s: "
                                 "`%s.lexres' does not exist in any "
                                 "of the lexer dirs"
                                 % (self.lang, self.lang))
        return lexres_file



class UDLBuffer(CitadelBuffer):
    """A CodeIntel Buffer for a UDL-lexer-based language."""
    sce_prefixes = ["SCE_UDL_"]
    #XXX Not sure that this indirection will be useful, but we'll see.

    # Sub-classes must set the following of these that are appropriate:
    m_lang = None
    css_lang = None
    csl_lang = None
    ssl_lang = None
    tpl_lang = None

    def lang_from_style(self, style):
        if (ScintillaConstants.SCE_UDL_M_DEFAULT <= style
              <= ScintillaConstants.SCE_UDL_M_UPPER_BOUND):
            return self.m_lang
        elif (ScintillaConstants.SCE_UDL_CSS_DEFAULT <= style
              <= ScintillaConstants.SCE_UDL_CSS_UPPER_BOUND):
            return self.css_lang
        elif (ScintillaConstants.SCE_UDL_CSL_DEFAULT <= style
              <= ScintillaConstants.SCE_UDL_CSL_UPPER_BOUND):
            return self.csl_lang
        elif (ScintillaConstants.SCE_UDL_SSL_DEFAULT <= style
              <= ScintillaConstants.SCE_UDL_SSL_UPPER_BOUND):
            return self.ssl_lang
        elif (ScintillaConstants.SCE_UDL_TPL_DEFAULT <= style
              <= ScintillaConstants.SCE_UDL_TPL_UPPER_BOUND):
            return self.tpl_lang
        else:
            raise ValueError("unknown UDL style: %r" % style)

    def lang_from_pos(self, pos):
        style = self.accessor.style_at_pos(pos)
        return self.lang_from_style(style)

    _udl_family_from_lang_cache = None
    @property
    def udl_family_from_lang(self):
        if self._udl_family_from_lang_cache is None:
            self._udl_family_from_lang_cache = dict(
                (uf, L) for (uf, L) in [
                    (self.m_lang, "M"),
                    (self.css_lang, "CSS"),
                    (self.csl_lang, "CSL"),
                    (self.ssl_lang, "SSL"),
                    (self.tpl_lang, "TPL"),
                    ]
                if L is not None
            )
        return self._udl_family_from_lang_cache

    def text_chunks_from_lang(self, lang):
        """Generate a list of text chunks of the given language content.

        For a single-language buffer this is trivial: 1 chunk of the whole
        buffer. For multi-language buffers, less so.

        Generates 2-tuples:
            (POSITION-OFFSET, TEXT-CHUNK)
        """
        udl_family_from_lang = self.udl_family_from_lang
        if len(udl_family_from_lang) == 1:
            yield 0, self.accessor.text
        elif lang not in udl_family_from_lang:
            pass
        elif hasattr(self.accessor, "udl_family_chunk_ranges"):
            udl_family = self.udl_family_from_lang[lang]
            text = self.accessor.text  #Note: assuming here that `text` is in *bytes*
            for u, start, end in self.accessor.udl_family_chunk_ranges:
                if u == udl_family:
                    yield start, text[start:end]
        else:
            min_style, max_style = {
                self.m_lang:   (ScintillaConstants.SCE_UDL_M_DEFAULT,
                                ScintillaConstants.SCE_UDL_M_UPPER_BOUND),
                self.css_lang: (ScintillaConstants.SCE_UDL_CSS_DEFAULT,
                                ScintillaConstants.SCE_UDL_CSS_UPPER_BOUND),
                self.csl_lang: (ScintillaConstants.SCE_UDL_CSL_DEFAULT,
                                ScintillaConstants.SCE_UDL_CSL_UPPER_BOUND),
                self.ssl_lang: (ScintillaConstants.SCE_UDL_SSL_DEFAULT,
                                ScintillaConstants.SCE_UDL_SSL_UPPER_BOUND),
                self.tpl_lang: (ScintillaConstants.SCE_UDL_TPL_DEFAULT,
                                ScintillaConstants.SCE_UDL_TPL_UPPER_BOUND),
            }[lang]

            in_chunk = False
            pos_offset = None
            for token in self.accessor.gen_tokens():
                if in_chunk:
                    if not (min_style <= token["style"] <= max_style):
                        # SilverCity indeces are inclusive at the end.
                        end_index = token["end_index"] + 1
                        yield (pos_offset,
                               self.accessor.text_range(pos_offset, end_index))
                        in_chunk = False
                else:
                    if min_style <= token["style"] <= max_style:
                        in_chunk = True
                        pos_offset = token["start_index"]
            if in_chunk:
                yield (pos_offset,
                       self.accessor.text_range(pos_offset,
                                                self.accessor.length()))

    def scoperef_from_pos(self, pos):
        """Return the scoperef for the given position in this buffer.

        A "scoperef" is a 2-tuple:
            (<blob>, <lpath>)
        where <blob> is the ciElementTree blob for the buffer content
        and <lpath> is an ordered list of names into the blob
        identifying the scope.
        
        If no relevant scope is found (e.g. for example, in markup
        content in PHP) then None is returned.

        See Buffer.scoperef_from_pos() docstring for more details.
        """
        lang = self.lang_from_pos(pos)
        try:
            blob = self.blob_from_lang[lang]
        except (KeyError, TypeError):
            return None
        line = self.accessor.line_from_pos(pos) + 1 # convert to 1-based
        return self.scoperef_from_blob_and_line(blob, line)

    def trg_from_pos(self, pos, implicit=True):
        if pos == 0:
            return None
        lang = self.lang_from_pos(pos-1)
        if lang is None:
            style = self.accessor.style_at_pos(pos)
            style_names = self.style_names_from_style_num(style)
            raise CodeIntelError("got unexpected style in `%s': %s %s"
                                 % (basename(self.path), style, style_names))
        try:
            langintel = self.mgr.langintel_from_lang(lang)
        except KeyError:
            return None
        return langintel.trg_from_pos(self, pos, implicit=implicit)

    def preceding_trg_from_pos(self, pos, curr_pos):
        if curr_pos == 0:
            return None
        lang = self.lang_from_pos(curr_pos-1)
        try:
            langintel = self.mgr.langintel_from_lang(lang)
        except KeyError:
            return None
        return langintel.preceding_trg_from_pos(self, pos, curr_pos)

    def curr_calltip_arg_range(self, trg_pos, calltip, curr_pos):
        if curr_pos == 0:
            return None
        lang = self.lang_from_pos(curr_pos-1)
        try:
            langintel = self.mgr.langintel_from_lang(lang)
        except KeyError:
            return (-1, -1)
        try:
            return langintel.curr_calltip_arg_range(self, trg_pos, calltip,
                                                    curr_pos)
        except AttributeError:
            # This can happen if we accidentally move into a non-programming
            # language during a calltip. E.g. bug 69529. Cancel the calltip
            # in this case.
            return (-1, -1)

    def async_eval_at_trg(self, trg, ctlr):
        try:
            langintel = self.mgr.langintel_from_lang(trg.lang)
        except KeyError:
            return None
        return langintel.async_eval_at_trg(self, trg, ctlr)

    # Override Citadel.defn_trg_from_pos()
    def defn_trg_from_pos(self, pos, lang=None):
        # Work out the language from the position, as the citadel buffer will
        # use the buffer language, we want a language specific to this pos.
        return CitadelBuffer.defn_trg_from_pos(self, pos,
                                               lang=self.lang_from_pos(pos))

    def libs(self):
        """A simple `.libs' property does not work for multi-lang buffers.
        Use `.libs_from_lang(lang)' instead.
        """
        raise RuntimeError("`.libs' invalid for multi-lang buffers: use "
                           "`mgr.langintel_from_lang(lang).libs_from_buf(buf)' "
                           "directly")

    def style_names_from_style_num(self, style_num):
        #XXX Would like to have python-foo instead of p_foo or SCE_P_FOO, but
        #    that requires a more comprehensive solution for all langs and
        #    multi-langs.
        style_names = []

        # Get the constant name from ScintillaConstants.
        if "UDL" not in self._style_name_from_style_num_from_lang:
            name_from_num \
                = self._style_name_from_style_num_from_lang["UDL"] = {}
            if self.sce_prefixes is None:
                raise CodeIntelError("'sce_prefixes' not set on class %s: cannot "
                                     "determine style constant names"
                                     % self.__class__.__name__)
            for attr in dir(ScintillaConstants):
                for sce_prefix in self.sce_prefixes:
                    if attr.startswith(sce_prefix):
                        name_from_num[getattr(ScintillaConstants, attr)] = attr
        else:
            name_from_num \
                = self._style_name_from_style_num_from_lang["UDL"]
        const_name = name_from_num[style_num]
        style_names.append(const_name)
        
        # Get a style group from styles.py.
        if "UDL" in styles.StateMap:
            for style_group, const_names in styles.StateMap["UDL"].items():
                if const_name in const_names:
                    style_names.append(style_group)
                    break
        else:
            log.warn("lang '%s' not in styles.StateMap: won't have "
                     "common style groups in HTML output" % "UDL")
        
        return style_names

    __string_styles = None
    def string_styles(self):
        if self.__string_styles is None:
            state_map = styles.StateMap["UDL"]
            self.__string_styles = [
                getattr(ScintillaConstants, style_name)
                for style_class in ("strings", "stringeol")
                for style_name in state_map.get(style_class, [])
            ]
        return self.__string_styles

    __comment_styles = None
    def comment_styles(self):
        if self.__comment_styles is None:
            state_map = styles.StateMap["UDL"]
            self.__comment_styles = [
                getattr(ScintillaConstants, style_name)
                for style_class in ("comments", "here documents",
                                    "data sections")
                for style_name in state_map.get(style_class, [])
            ]
        return self.__comment_styles

    __number_styles = None
    def number_styles(self):
        if self.__number_styles is None:
            state_map = styles.StateMap["UDL"]
            self.__number_styles = [
                getattr(ScintillaConstants, style_name)
                for style_class in ("numbers",)
                for style_name in state_map.get(style_class, [])
            ]
        return self.__number_styles


class XMLParsingBufferMixin(CitadelBuffer):
    """A mixin for UDLBuffer-based buffers of XML-y/HTML-y languages to
    support the following:

    - An "xml_tree" attribute that is a XML parse tree of the document
      (lazily done from koXMLTreeService)
    - An "xml_parse()" method to force a re-parse of the document.

    TODO: locking?
    """
    def __init__(self, *args, **kwargs):
        super(XMLParsingBufferMixin, self).__init__(*args, **kwargs)
        self.env.add_pref_observer("default%sDecl" % self.m_lang,
                                   self.__on_pref_change)

    def scan(self, mtime=None, skip_scan_time_check=False, reporter=None):
        """Rescan the buffer.
        In the XML parsing buffer's case, we should do whatever the normal
        thing is, plus force a reparse of the XML.
        """
        super(XMLParsingBufferMixin, self).scan(mtime, skip_scan_time_check, reporter=reporter)
        # Reset xml tree cache, so sections list works correctly - bug 101442.
        self._xml_tree_cache = None

    _xml_tree_cache = None
    _xml_default_dataset_info = None
    @property
    def xml_tree(self):
        if self._xml_tree_cache is None:
            self.xml_parse()
        return self._xml_tree_cache

    @LazyClassAttribute
    def __blank_out_non_new_line_table(self):
        """Table for string.translate to replace everything with spaces, except
        for new lines."""
        table = [b' ' for i in range(256)]
        table[ord(b'\n')] = b'\n'
        table[ord(b'\r')] = b'\r'
        return b"".join(table)

    def xml_parse(self):
        from koXMLTreeService import getService
        path = self.path
        if isUnsavedPath(self.path):
            # The "<Unsaved>/..." special path can *crash* Python if trying to
            # open it. Besides, the "<Unsaved>" business is an internal
            # codeintel detail.
            path = None
        content = self.accessor.text
        if hasattr(self, "text_chunks_from_lang"):
            # Grab only the text that's in markup regions; this skils scripts
            # that might have things that look like tags, see bug 101280
            stripped = b''
            was_unicode = isinstance(content, six.text_type)
            if was_unicode:
                content = content.encode("utf-8")
            trans_tbl = self.__blank_out_non_new_line_table
            for offset, text in self.text_chunks_from_lang(self.m_lang):
                if isinstance(text, six.text_type):
                    text = text.encode("utf-8")
                skipped_text = content[len(stripped):offset]
                stripped += skipped_text.translate(trans_tbl) + text
            content = stripped
            if was_unicode:
                content = content.decode("utf-8")
        self._xml_tree_cache = getService().getTreeForURI(path, content)

    def xml_default_dataset_info(self, node=None):
        if self._xml_default_dataset_info is None:
            import koXMLDatasetInfo
            datasetSvc = koXMLDatasetInfo.getService()
            self._xml_default_dataset_info = (datasetSvc.getDefaultPublicId(self.m_lang, self.env),
                                            None,
                                            datasetSvc.getDefaultNamespace(self.m_lang, self.env))
        return self._xml_default_dataset_info

    def xml_tree_handler(self, node=None):
        import koXMLDatasetInfo
        return koXMLDatasetInfo.get_tree_handler(self._xml_tree_cache, node, self.xml_default_dataset_info(node))
    
    def xml_node_at_pos(self, pos):
        import koXMLTreeService
        self.xml_parse()
        tree = self._xml_tree_cache
        if not tree:
            return None
        line, col = self.accessor.line_and_col_at_pos(pos)
        node = tree.locateNode(line, col)
        # XXX this needs to be worked out better
        last_start = self.accessor.text.rfind('<', 0, pos)
        last_end = self.accessor.text.find('>', last_start, pos)
        if node is None and last_start >= 0:
            node = koXMLTreeService.elementFromText(tree, self.accessor.text[last_start:last_end], node)
        if node is None or node.start is None:
            return node
        # elementtree line numbers are 1 based, convert to zero based
        node_pos = self.accessor.pos_from_line_and_col(node.start[0]-1, node.start[1])
        if last_end == -1 and last_start != node_pos:
            #print "try parse ls %d le %d np %d pos %d %r" % (last_start, last_end, node_pos, pos, accessor.text[last_start:pos])
            # we have a dirty tree, need to create a current node and add it
            newnode = koXMLTreeService.elementFromText(tree, self.accessor.text[last_start:pos], node)
            if newnode is not None:
                return newnode
        return node

    def __on_pref_change(self, env, pref_name):
        log.debug("on pref change: %s", pref_name)
        self._xml_default_dataset_info = None

class _NotYetSet(object):
    # Used below to distinguish from None.
    pass

class UDLCILEDriver(CILEDriver):
    ssl_lang = None   # Sub-classes must set one or both of these for
    csl_lang = None   #    citadel-scanning support.
    css_lang = None

    _master_cile_driver = None
    slave_csl_cile_driver = _NotYetSet # to distinguish from None
    slave_css_cile_driver = _NotYetSet # to distinguish from None

    @property
    def master_cile_driver(self):
        """The primary CILE driver for this multi-lang lang.

        This is the CILE driver for the SSL lang, if there is one, otherwise
        for the csl_lang.

        Side effect: `self.slave_csl_cile_driver' is determined the
        first time this is called. A little gross, I know, but it
        avoids having a separate property.
        Note: `self.slave_css_cile_driver` follows the same logic.
        """
        if self._master_cile_driver is None:
            if self.ssl_lang is not None:
                self._master_cile_driver \
                    = self.mgr.citadel.cile_driver_from_lang(self.ssl_lang)
                self.slave_csl_cile_driver \
                    = self.mgr.citadel.cile_driver_from_lang(self.csl_lang)
            else:
                self._master_cile_driver \
                    = self.mgr.citadel.cile_driver_from_lang(self.csl_lang)
                self.slave_csl_cile_driver = None
            if self.css_lang is not None:
                self.slave_css_cile_driver \
                    = self.mgr.citadel.cile_driver_from_lang(self.css_lang)
        return self._master_cile_driver

    def scan_purelang(self, buf):
        return self.master_cile_driver.scan_multilang(
                        buf, self.slave_csl_cile_driver,
                        self.slave_css_cile_driver)



