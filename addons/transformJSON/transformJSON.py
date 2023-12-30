# Export selected transforms X/Y to JSON
from NatronGui import *
import json, time, subprocess, os, platform

def transformJSON() :
	app1 = natron.getGuiInstance(0)
	frames = app1.getProjectParam('frameRange').get()
	for currentNode in app1.getSelectedNodes() :
		if currentNode.getPluginID() !=  'net.sf.openfx.TransformPlugin' :
			continue
		cords = []
		for frame in range(frames.x, frames.y + 1):
			translate = currentNode.getParam('translate').get(frame)
			center = currentNode.getParam('center').get(frame)
			cords.append({'x1' : translate.x, 'y1' : translate.y, 'x2' : center.x, 'y2' : center.y})
		filepath = os.path.expanduser('~') + "/Natron-" + currentNode.getLabel() + "-" + time.strftime("%Y%m%d%H%M%S") + ".json"
		file = open(filepath, "w")
		file.write(json.dumps(cords))
		file.close()
		if platform.system() == 'Darwin':
			subprocess.call(('open', filepath))
		elif platform.system() == 'Windows':
			os.startfile(filepath)
		else:
			subprocess.call(('xdg-open', filepath))
