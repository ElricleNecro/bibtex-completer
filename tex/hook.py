#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2011, 2012 Stephen Sugden <me@stephensugden.com>
# 2013 Bjoern Doebel <doebel@tudos.org>
#
# This file is part of YouCompleteMe.
#
# YouCompleteMe is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# YouCompleteMe is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with YouCompleteMe. If not, see <http://www.gnu.org/licenses/>.

from ycmd.completers.tex.bibtex_completer import BibTexCompleter

def GetCompleter(user_options):
    return BibTexCompleter(user_options)

# vim: set tw=79 :
