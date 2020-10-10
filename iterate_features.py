# ***************************************************************************
#
# Iterate vector layer features by pressing the SpaceBar
#
# 2015 Germán Carrillo  (gcarrillo@linuxmail.org)
#
# ***************************************************************************
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify        *
# *   it under the terms of the GNU General Public License as published by        *
# *   the Free Software Foundation; either version 2 of the License, or           *
# *   (at your option) any later version.                                      *
# *                                                                         *
# ***************************************************************************
from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtGui import QKeySequence
from qgis.PyQt.QtWidgets import QShortcut
from qgis.core import QgsMapLayer, QgsFeatureRequest, QgsWkbTypes
from qgis.utils import iface

myIt = None
activeLayerId = ""

def escapePressed():
    global myIt
    myIt = None
    iface.messageBar().pushInfo("Feature iterator", "Iteration reset!")

def spaceBarPressed():  
    global myIt, activeLayerId
    aLayer = iface.activeLayer()
    if not aLayer or not aLayer.type() == QgsMapLayer.VectorLayer:
        iface.messageBar().pushInfo("Feature iterator",
            "First select a vector layer in the layers panel.")
        return
    if activeLayerId != aLayer.id():
        activeLayerId = aLayer.id()
        myIt = None
    if not myIt:
        request = QgsFeatureRequest().setFlags(QgsFeatureRequest.NoGeometry).setNoAttributes()
        myIt = aLayer.getFeatures(request)

    feat = next( myIt, None )
    if feat:
        aLayer.selectByIds( [feat.id()] )
        if aLayer.geometryType() == QgsWkbTypes.PointGeometry:
            iface.actionPanToSelected().trigger()  # Pan to points
        else:
            iface.actionZoomToSelected().trigger()  # Zoom to the rest
    else:
        iface.messageBar().pushInfo("Feature iterator",
            "We reached the last feature of this layer already.\n" + \
            "If you want to restart press the Escape key.")

shortcutEscape = QShortcut(QKeySequence(Qt.Key_Escape), iface.mapCanvas())
shortcutEscape.setContext(Qt.ApplicationShortcut)
shortcutEscape.activated.connect(escapePressed)

shortcutSpaceBar = QShortcut(QKeySequence(Qt.Key_Space), iface.mapCanvas())
shortcutSpaceBar.setContext(Qt.ApplicationShortcut)
shortcutSpaceBar.activated.connect(spaceBarPressed)
