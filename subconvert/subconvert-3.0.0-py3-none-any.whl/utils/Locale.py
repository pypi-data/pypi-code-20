#-*- coding: utf-8 -*-

"""
Copyright (C) 2011, 2012, 2013 Michal Goral.

This file is part of Subconvert

Subconvert is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Subconvert is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Subconvert. If not, see <http://www.gnu.org/licenses/>.
"""

import os
import gettext
import pkg_resources

domain = "subconvert"
localedir = pkg_resources.resource_filename(domain, "locale")
gettext.bindtextdomain(domain, localedir)
gettext.textdomain(domain)

t = gettext.translation(
    domain=domain,
    localedir=localedir,
    fallback=True)

_ = t.gettext
P_ = t.ngettext
