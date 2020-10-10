# PyQGIS scripts

This is a collection of PyQGIS scripts that I write for different purposes. 
The following scripts are available (under a GNU GPL v.2.0 license):

**QGIS v3.x**

 * Iterate vector layer features: [iterate_features.py](https://github.com/gacarrillor/pyqgis_scripts/blob/master/iterate_features.py)

   Allows you to iterate features of the active vector layer. It selects one feature at a time and pans (for point layers) or zooms to it (for the other geometry types or even geometryless tables).
   
   See http://gis.stackexchange.com/q/133189/4972 for instructions.
   
 * Split line in parts of the same length: [line_substring_qgis3.py](https://github.com/gacarrillor/pyqgis_scripts/blob/master/line_substring_qgis3.py)

   Splits the selected line into several parts of the same length. Deletes the original line and copy its attributes to all new parts. 
   It does not save the new lines, allowing you to check before saving yourself.
   
   Instructions: 
   1. Select a line layer in the Layers Panel.
   2. Select a single line in the canvas.
   3. Set the parts variable: Number of parts you want the line to be split into.
   4. Run the script.

**QGIS v2.x**

 * Iterate through layers and export map as PNG: [iterate_layers_export_png_qgis2.py](https://github.com/gacarrillor/pyqgis_scripts/blob/master/iterate_layers_export_png_qgis2.py)

   See http://gis.stackexchange.com/a/189825/4972 for instructions.

 * Snap a road network to a hexgrid: [snap_road_network_to_hexgrid_qgis2.py](https://github.com/gacarrillor/pyqgis_scripts/blob/master/snap_road_network_to_hexgrid_qgis2.py)

   See http://gis.stackexchange.com/a/189731/4972 for instructions.   
   
