from gvsig import *
from commonsdialog import *


def main():
    layer = currentLayer()
    if layer is None:
        msgbox(
            "The layer should be charged and selected.",
            "NOTIFICATION", 1)
        return

    emax = 0.0
    emin = 0.0

    for feature in layer.features():
        if feature.ELEVATION > emax:
            emax = feature.ELEVATION
        if feature.ELEVATION < emin or emin == 0.0:
            emin = feature.ELEVATION
    msgbox("máximum Elevation=%s and minimum=%s" % (emax, emin),
           "Elevation", 0)
