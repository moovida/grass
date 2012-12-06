#!/usr/bin/env python
############################################################################
#
# MODULE:    g.gui.psmap
# AUTHOR(S): Anna Kratochvilova <kratochanna gmail.com>
# PURPOSE:   Cartographic Composer
# COPYRIGHT: (C) 2011-2012 by Anna Kratochvilova, and the GRASS Development Team
#
#  This program is free software; you can 1redistribute it and/or
#  modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation; either version 2 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
############################################################################

#%module
#% description: Tool for creating hardcopy map outputs.
#% keywords: general
#% keywords: gui
#% keywords: printing
#%end
#%option G_OPT_F_INPUT
#% key: file
#% label: File containing mapping instructions
#% description: See ps.map manual for details
#% key_desc: name
#% required: no
#%end

import os
import sys
import gettext

import  wx

import grass.script as grass

sys.path.append(os.path.join(os.environ['GISBASE'], "etc", "gui", "wxpython"))

from psmap.frame        import PsMapFrame
from psmap.instructions import Instruction

def main():
    gettext.install('grasswxpy', os.path.join(os.getenv("GISBASE"), 'locale'), unicode = True)
    
    app = wx.PySimpleApp()
    wx.InitAllImageHandlers()
    frame = PsMapFrame(parent = None)
    if options['file']:
        grass.fatal(_("To be implemented"))
    
    frame.Show()
    
    app.MainLoop()

if __name__ == "__main__":
    options, flags = grass.parser()
    main()
