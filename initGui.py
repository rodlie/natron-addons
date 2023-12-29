from NatronGui import *
from PySide.QtGui import *

from addons.extractLayers.extractLayers import *
NatronGui.natron.addMenuCommand('Add-ons/Extract Layers from Reader(s)', 'extractLayers', QtCore.Qt.Key.Key_E, QtCore.Qt.KeyboardModifier.ControlModifier)

from addons.transformJSON.transformJSON import *
NatronGui.natron.addMenuCommand('Add-ons/Export selected transforms to JSON', 'transformJSON')
