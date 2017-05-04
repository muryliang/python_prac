#!/usr/bin/env python

# reTux File Localizer
# Copyright (C) 2016 onpon4 <onpon4@riseup.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import os
import shutil
import sys

import six

from six.moves.tkinter import Tk
# six.moves.tkinter_filedialog doesn't work correctly.
if six.PY2:
    import tkFileDialog as tkinter_filedialog
    import tkMessageBox as tkinter_messagebox
else:
    import tkinter.filedialog as tkinter_filedialog
    import tkinter.messagebox as tkinter_messagebox


if getattr(sys, "frozen", False):
    __file__ = sys.executable

FILEDIR = os.path.dirname(__file__)
CONFIG = os.path.join(os.path.expanduser("~"), ".config", "retux")


if __name__ == '__main__':
    if not os.path.exists(CONFIG):
        os.makedirs(CONFIG)

    tkwindow = Tk()
    tkwindow.withdraw()
    fnames = tkinter_filedialog.askopenfilenames(
        filetypes=[("all files", ".*")], initialdir=FILEDIR)
    for fname in fnames:
        rp = os.path.relpath(fname, FILEDIR)
        if not rp.startswith(os.pardir):
            cd = os.path.dirname(os.path.join(CONFIG, rp))
            if not os.path.exists(cd):
                os.makedirs(cd)

            new_name = os.path.join(cd, os.path.basename(fname))
            if os.path.isfile(new_name):
                os.remove(new_name)
            elif os.path.isdir(new_name):
                shutil.rmtree(new_name)

            shutil.move(fname, cd)
            tkinter_messagebox.showinfo(
                "Message", 'Moved "{}" to "{}"'.format(fname, cd))
        else:
            tkinter_messagebox.showinfo(
                "Message",
                '"{}" was not localized (invalid location)'.format(fname))
    tkwindow.destroy()
