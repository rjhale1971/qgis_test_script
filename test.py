#!/usr/bin/python3 

import sys

# Inject plugin path, might need to be tweaked significantly. Sure there's more missing.
sys.path.insert(0, "/Applications/QGIS.app/Contents/Resources/python/plugins")

from qgis.core import (
     QgsApplication, 
     QgsProcessingFeedback, 
     QgsVectorLayer
)

# See https://gis.stackexchange.com/a/155852/4972 for details about the prefix 
QgsApplication.setPrefixPath('/usr', True)
#QgsApplication.setPrefixPath("Applications/QGIS-LTR.app/Contents/MacOS",True)
qgs = QgsApplication([], False)
qgs.initQgis()

# Append the path where processing plugin can be found
sys.path.append('/usr/share/qgis/python/plugins')
#sys.path.append("Applications/QGIS-LTR.app/Contents/Resources/python/plugins")


import processing
from processing.core.Processing import Processing
Processing.initialize()

processing.algorithmHelp("grass7:v.buffer")
