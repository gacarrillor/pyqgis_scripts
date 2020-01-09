# -*- coding: utf-8 -*-
# ***************************************************************************
#
# Snap a road network to a hexgrid
# This is supposed to be run from the QGIS Python console.
#
# Copyright (C) 2016 Germán Carrillo  (gcarrillo@linuxmail.org)
#
# ***************************************************************************
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify        *
# *   it under the terms of the GNU General Public License as published by        *
# *   the Free Software Foundation; either version 2 of the License, or           *
# *   (at your option) any later version.                                      *
# *                                                                         *
# ***************************************************************************
hexgrid = QgsVectorLayer("/docs/borrar/hex_grid_question/layers/normal-hexgrid.shp", "hexgrid", "ogr")
roads = QgsVectorLayer("/docs/borrar/hex_grid_question/layers/roads_multipart.shp", "roads", "ogr")  # Must be multipart!

roadFeat = roads.getFeatures().next() # We just have 1 geometry
road = roadFeat.geometry() 
indicesHexSides = ((0,1), (1,2), (2,3), (3,4), (4,5), (5,0))

epsilon = 0.01
# Function to compare whether 2 segments are equal (even if inverted)
def isSegmentAlreadySaved(v1, v2):
    for segment in listSegments:        
        p1 = QgsPoint(segment[0][0], segment[0][1])
        p2 = QgsPoint(segment[1][0], segment[1][1])
        if v1.compare(p1, epsilon) and v2.compare(p2, epsilon) \
            or v1.compare(p2, epsilon) and v2.compare(p1, epsilon):
            return True
    return False

# Let's find the nearest sides of hexagons where routes cross
listSegments = []
for hexFeat in hexgrid.getFeatures():
    hex = hexFeat.geometry()
    if hex.intersects( road ):
        for side in indicesHexSides:
            triangle = QgsGeometry.fromPolyline([hex.centroid().asPoint(), hex.vertexAt(side[0]), hex.vertexAt(side[1])])
            if triangle.intersects( road ):
                # Only append new lines, we don't want duplicates!!!
                if not isSegmentAlreadySaved(hex.vertexAt(side[0]), hex.vertexAt(side[1])): 
                    listSegments.append( [[hex.vertexAt(side[0]).x(), hex.vertexAt(side[0]).y()], [hex.vertexAt(side[1]).x(),hex.vertexAt(side[1]).y()]] )  
                    
                    
                    
# Let's remove open segments
lstVertices = [tuple(point) for segment in listSegments for point in segment]
dictConnectionsPerVertex = dict((tuple(x),lstVertices.count(x)-1) for x in set(lstVertices))

# A vertex is not connected and the other one is connected to 2 segments
def segmentIsOpen(segment):
    return dictConnectionsPerVertex[tuple(segment[0])] == 0 and dictConnectionsPerVertex[tuple(segment[1])] >= 2 \
        or dictConnectionsPerVertex[tuple(segment[1])] == 0 and dictConnectionsPerVertex[tuple(segment[0])] >= 2

# Remove open segments
segmentsToDelete = [segment for segment in listSegments if segmentIsOpen(segment)]        
for toBeDeleted in segmentsToDelete:
    listSegments.remove( toBeDeleted )


# Create a memory layer and load it to QGIS map canvas
vl = QgsVectorLayer("LineString", "Snapped Routes", "memory")
pr = vl.dataProvider()
features = []
for segment in listSegments:
    fet = QgsFeature()
    fet.setGeometry( QgsGeometry.fromPolyline( [QgsPoint(segment[0][0], segment[0][1]), QgsPoint(segment[1][0], segment[1][1])] ) )
    features.append(fet)

pr.addFeatures( features )
vl.updateExtents()
QgsMapLayerRegistry.instance().addMapLayer(vl)


