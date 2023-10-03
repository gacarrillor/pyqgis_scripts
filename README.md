# PyQGIS scripts

This is a collection of PyQGIS scripts that I write for different purposes. 
The following scripts are available (under a GNU GPL v3.0 license):

**QGIS v3.x**

+ Run custom algorithm from PyQGIS standalone script: [run_processing_custom_alg_standalone.py](https://github.com/gacarrillor/pyqgis_scripts/blob/master/pyqgis_custom_processing_algorithm_standalone/run_processing_custom_alg_standalone.py)

  Allows you to run a custom Processing algorithm from a PyQGIS standalone script. For that, it calls a custom algorithm provider, which in turn uses the custom Processing algorithm. All of them (3 files) are available in the same folder as the standalone script.

  See https://gis.stackexchange.com/q/408684/4972 for instructions.

 * Iterate vector layer features: [iterate_features.py](https://github.com/gacarrillor/pyqgis_scripts/blob/master/iterate_features.py)

   Allows you to iterate features of the active vector layer. It selects one feature at a time and pans (for point layers) or zooms to it (for the other geometry types or even geometryless tables).
   
   See http://gis.stackexchange.com/q/133189/4972 for instructions.
   
   ![image](https://i.stack.imgur.com/Ua96m.gif)

 * Split line in parts of the same length: [line_substring_qgis3.py](https://github.com/gacarrillor/pyqgis_scripts/blob/master/line_substring_qgis3.py)

   Splits the selected line into several parts of the same length. Deletes the original line and copy its attributes to all new parts. 
   It does not save the new lines, allowing you to check before saving yourself.
   
   Instructions: 
   1. Select a line layer in the Layers Panel.
   2. Select a single line in the canvas.
   3. Set the parts variable: Number of parts you want the line to be split into.
   4. Run the script.
   
 * Extend C++ QGIS Processing Algorithms: [extend_c_plus_plus_qgis_alg.py](https://github.com/gacarrillor/pyqgis_scripts/blob/master/extend_c_plus_plus_qgis_alg.py)

   The vast majority of C++ QGIS algorithms cannot be subclassed, but we can extend them (think of using their input/output parameters, flags, etc.) adding some custom logic for our own purposes.

**QGIS v2.x**

 * Iterate through layers and export map as PNG: [iterate_layers_export_png_qgis2.py](https://github.com/gacarrillor/pyqgis_scripts/blob/master/iterate_layers_export_png_qgis2.py)

   See http://gis.stackexchange.com/a/189825/4972 for instructions.

 * Snap a road network to a hexgrid: [snap_road_network_to_hexgrid_qgis2.py](https://github.com/gacarrillor/pyqgis_scripts/blob/master/snap_road_network_to_hexgrid_qgis2.py)

   See http://gis.stackexchange.com/a/189731/4972 for instructions.   
   ![image](https://user-images.githubusercontent.com/652785/236654701-4daa2124-0651-4de2-996c-5b18f10d5d3a.png)
   ![image](https://user-images.githubusercontent.com/652785/236654715-20256830-1a0d-44a2-b320-5cf56b4f870c.png)



