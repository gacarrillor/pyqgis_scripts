# -*- coding: utf-8 -*-
# ***************************************************************************
#
# Iterate through layers in the ToC and export the canvas as PNG
#
# Copyright (C) 2016 Germán Carrillo  (geotux_tuxman@linuxmail.org)
#
# ***************************************************************************
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify        *
# *   it under the terms of the GNU General Public License as published by        *
# *   the Free Software Foundation; either version 2 of the License, or           *
# *   (at your option) any later version.                                      *
# *                                                                         *
# ***************************************************************************

from qgis.core import QgsApplication, QgsMapLayerRegistry, QgsVectorLayer, QgsProject
from qgis.gui import QgsMapCanvas, QgsMapCanvasLayer, QgsLayerTreeMapCanvasBridge
from PyQt4.QtCore import QTimer, QSize

qgisApp = QgsApplication([], True)
qgisApp.setPrefixPath("/usr", True)
qgisApp.initQgis()

# Required variables with your shapefile paths and names
pngsPath = '/tmp/'
boundaryLayer = QgsVectorLayer('/docs/geodata/colombia/colombia_wgs84.shp', 'boundary', 'ogr')
climitsLayer = QgsVectorLayer('/docs/geodata/colombia/colombia-geofabrik/railways.shp', 'climits', 'ogr')
otherLayers = {'Div1_Irrig_1956_0': QgsVectorLayer('/docs/geodata/colombia/colombia-geofabrik/points.shp', 'Div1_Irrig_1956_0', 'ogr'), 
    'Div1_Irrig_1956_1':QgsVectorLayer('/docs/geodata/colombia/colombia-geofabrik/places.shp', 'Div1_Irrig_1956_1', 'ogr'), 
    'Div1_Irrig_1956_2': QgsVectorLayer('/docs/geodata/colombia/colombia-geofabrik/natural.shp', 'Div1_Irrig_1956_2', 'ogr')}

canvas = QgsMapCanvas()
canvas.resize(QSize(500, 500)) # You can adjust this values to alter image dimensions
canvas.show()

# Add layers to map canvas taking the order into account
QgsMapLayerRegistry.instance().addMapLayer( boundaryLayer)
QgsMapLayerRegistry.instance().addMapLayers( otherLayers.values() )
QgsMapLayerRegistry.instance().addMapLayer( climitsLayer )
layerSet = [QgsMapCanvasLayer(climitsLayer)]
layerSet.extend([QgsMapCanvasLayer(l) for l in otherLayers.values() ])
layerSet.append(QgsMapCanvasLayer(boundaryLayer))
canvas.setLayerSet( layerSet )

root = QgsProject.instance().layerTreeRoot()
bridge = QgsLayerTreeMapCanvasBridge(root, canvas)

count = 0
def prepareMap(): # Arrange layers
    for lyr in otherLayers.values(): # make all layers invisible
        root.findLayer( lyr.id() ).setVisible(0) # Unchecked
    root.findLayer( otherLayers.values()[count].id() ).setVisible(2) # Checked
    canvas.zoomToFullExtent()
    QTimer.singleShot(1000, exportMap) # Wait a second and export the map

def exportMap(): # Save the map as a PNG
    global count # We need this because we'll modify its value
    canvas.saveAsImage( pngsPath + otherLayers.keys()[count] + ".png" )
    print "Map with layer",otherLayers.keys()[count],"exported!"
    if count < len(otherLayers)-1:
        QTimer.singleShot(1000, prepareMap) # Wait a second and prepare next map
    else: # Time to close everything
        qgisApp.exitQgis()
        qgisApp.exit() 
    count += 1

prepareMap() # Let's start the fun
qgisApp.exec_()


