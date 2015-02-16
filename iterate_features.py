# -*- coding: utf-8 -*-
# ***************************************************************************
#
# Iterate through a vector layer features by pressing the SpaceBar
#
# Copyright (C) 2015 Germán Carrillo  (geotux_tuxman@linuxmail.org)
#
# ***************************************************************************
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify        *
# *   it under the terms of the GNU General Public License as published by        *
# *   the Free Software Foundation; either version 2 of the License, or           *
# *   (at your option) any later version.                                      *
# *                                                                         *
# ***************************************************************************
from qgis.utils import iface
from PyQt4.QtGui import QShortcut, QKeySequence
from PyQt4.QtCore import Qt

myIt = None
activeLayerId = ""

def enterPressed():
    global myIt
    myIt = None
    print "Iteration finished!"

def spaceBarPressed():
    global myIt, activeLayerId
    aLayer = iface.activeLayer()
    if not aLayer or not aLayer.type() == 0:
        print "Please first select a vector layer in the ToC."
        return
    if activeLayerId != aLayer.id():
        activeLayerId = aLayer.id()
        myIt = None
    if not myIt:
        myIt = aLayer.getFeatures()

    feat = next( myIt, None )
    if feat:
        aLayer.removeSelection()
        aLayer.select( feat.id() )
        iface.actionZoomToSelected().trigger()
        print "Selected feature:",str( feat.id() )
    else:
        print "We reached the last feature of this layer already.\n" + \
            "If you want to restart press the Escape key."
    
shortcutEnter = QShortcut(QKeySequence(Qt.Key_Escape), iface.mapCanvas())
shortcutEnter.setContext(Qt.ApplicationShortcut)
shortcutEnter.activated.connect(enterPressed)

shortcutSpaceBar = QShortcut(QKeySequence(Qt.Key_Space), iface.mapCanvas())
shortcutSpaceBar.setContext(Qt.ApplicationShortcut)
shortcutSpaceBar.activated.connect(spaceBarPressed)
