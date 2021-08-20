import sys
from qgis.core import (
     QgsApplication, 
     QgsVectorLayer
)

# See https://gis.stackexchange.com/a/155852/4972 for details about the prefix 
QgsApplication.setPrefixPath('/docs/dev/qgis/core/QGIS/build_master/output', True)
qgs = QgsApplication([], False)
qgs.initQgis()

# Append the path where processing plugin can be found
sys.path.append('/docs/dev/qgis/core/QGIS/build_master/output/python/plugins')

import processing
from processing.core.Processing import Processing
Processing.initialize()

# Add our own algorithm provider
from example_algorithm_provider import ExampleAlgorithmProvider
provider = ExampleAlgorithmProvider()
QgsApplication.processingRegistry().addProvider(provider)

# Run our custom algorithm
layer = QgsVectorLayer("/docs/geodata/bogota/ideca/Loca.shp", "layer", "ogr")
params = {'INPUT': layer}
print("RESULT:", processing.run("my_provider:my_algorithm", params)['OUTPUT'])

