#!/usr/bin/python3
import os
import sys

from qgis.core import (
     QgsApplication,
     QgsProcessingFeedback,
     QgsVectorLayer
)

exec_dir = sys.executable
app_name = [i for i in exec_dir.split(os.sep) if i.startswith('QGIS')][0]

# See https://gis.stackexchange.com/a/155852/4972 for details about the prefix
QgsApplication.setPrefixPath(f"/Applications/{app_name}/Contents/MacOS",True)
qgs = QgsApplication([], False)
qgs.initQgis()

# Append the path where processing plugin can be found
sys.path.append(f"/Applications/{app_name}/Contents/Resources/python/plugins")


import processing
from processing.core.Processing import Processing
Processing.initialize()

processing.algorithmHelp("grass7:v.buffer")
