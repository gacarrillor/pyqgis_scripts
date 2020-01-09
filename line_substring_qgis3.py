"""
Splits the selected line into several parts of the same length. 
This will delete the original line and copy its attributes to all new parts.

1. Select a line layer in the Layers Panel.
2. Select a single line in the canvas.
3. Set the parts variable: Number of parts you want the line to be split into.
4. Run the script.
"""
parts = 5

def split_line_part_equal_length(layer, line_part, parts, attrs):
    features = list()
    length = line_part.length()
    part_length = float(length/parts)
    for part in range(parts):
        start = part_length * part
        end = start + part_length
        geom = line_part.curveSubstring(start, end)
        
        new_feature = QgsFeature(layer.fields())
        new_feature.setGeometry(geom)
        new_feature.setAttributes(attrs)
        features.append(new_feature)
    
    return features

def split_line_equal_length(layer, feature, parts):
    line = feature.geometry()
    line_const = line.constGet()
    attrs = feature.attributes()
    
    print("part count:", line_const.partCount())
    new_features = list()
    
    if line_const.partCount() > 0:
        for i in range(line_const.partCount()):
            curve = line_const.geometryN(i)
            new_features.extend(split_line_part_equal_length(layer, curve, parts, attrs))
    
    layer.addFeatures(new_features)
    layer.deleteFeature(feature.id())

layer = iface.activeLayer()
if not layer.isEditable():
    iface.messageBar().pushMessage("First start the edit session...", Qgis.Warning)
elif len(layer.selectedFeatures()) != 1:
    iface.messageBar().pushMessage("First select only one line...", Qgis.Warning)
else:
    split_line_equal_length(layer, layer.selectedFeatures()[0], parts)
    iface.messageBar().pushMessage(f"Your line was splitted in {parts} parts! Remember to save changes.", Qgis.Success)
