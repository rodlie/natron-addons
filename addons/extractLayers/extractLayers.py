# Extract layers from selected reader nodes
from NatronGui import *

def extractLayers() :
	app = natron.getGuiInstance(0)
	ignoreLayers = ['uk.co.thefoundry.OfxImagePlaneColour', 'uk.co.thefoundry.OfxImagePlaneStereoDisparityLeft', 'uk.co.thefoundry.OfxImagePlaneStereoDisparityRight', 'uk.co.thefoundry.OfxImagePlaneBackMotionVector', 'uk.co.thefoundry.OfxImagePlaneForwardMotionVector', 'Deep', 'Depth', 'Mask', 'Motion']
	shuffleNodeID = 'net.sf.openfx.ShufflePlugin'
	readNodeID = 'fr.inria.built-in.Read'
	dotNodeID = 'fr.inria.built-in.Dot'
	backdropNodeID = 'fr.inria.built-in.BackDrop'
	currentNodeSpacingY = 300
	newShuffleNodeSpacingX = 45
	newShuffleNodeSpacingY = 200
	for currentNode in app.getSelectedNodes() :
		if currentNode.getPluginID() != readNodeID :
			continue
		readNodePosition = currentNode.getPosition()
		rootNodeDot = app.createNode(dotNodeID)
		rootNodeDot.setPosition(readNodePosition[0] + ( (currentNode.getSize()[0]/2) - (rootNodeDot.getSize()[0]/2) ), readNodePosition[1] + currentNodeSpacingY)
		rootNodeDot.connectInput(0, currentNode)
		rootNodeDotPosition = rootNodeDot.getPosition()
		firstShuffleNode = app.createNode(shuffleNodeID)
		firstShuffleNode.setLabel('extractLayers')
		firstShuffleNode.setPosition(rootNodeDotPosition[0] - newShuffleNodeSpacingX, rootNodeDotPosition[1] + newShuffleNodeSpacingY)
		firstShuffleNode.setColor(1, 0.5, 0.15)
		firstShuffleNode.connectInput(0, rootNodeDot)
		layers = [i for i in firstShuffleNode.getParam('outputLayer').getOptions() if i not in ignoreLayers]
		list.sort(layers)
		if not layers :
			natron.warningDialog( 'Unable to extract layers', 'Unable to extract any layers from ' + currentNode.getLabel() )
		layerCounter = 0
		for layer in layers :
			outputLayer = 'B.' + str(layer) + '.' + 'R'
			if layerCounter == 0 :
				firstShuffleNode.setLabel( str(layer) )
				firstShuffleNode.getParam('outputR').set(outputLayer)
				newBackdropNode = app.createNode(backdropNodeID)
				newBackdropNode.setPosition(rootNodeDotPosition[0] - newShuffleNodeSpacingY, rootNodeDotPosition[1] - 120)
				newBackdropNode.setSize(len(layers) * 400, 500)
				newBackdropNode.setColor(0.5, 0.35, 0.12)
				newBackdropNode.setLabel(currentNode.getLabel() + 'Layers')
			else :
				newDotNode = app.createNode(dotNodeID)
				newDotNode.setPosition(rootNodeDotPosition[0] + 400, rootNodeDotPosition[1])
				newDotNode.connectInput(0, rootNodeDot)
				rootNodeDotPosition = newDotNode.getPosition()
				newShuffleNode = app.createNode(shuffleNodeID)
				newShuffleNode.setLabel( str(layer) )
				newShuffleNode.setPosition(rootNodeDotPosition[0] - newShuffleNodeSpacingX, rootNodeDotPosition[1] + newShuffleNodeSpacingY)
				newShuffleNode.setColor(1, 0.5, 0.15)
				newShuffleNode.connectInput(0, newDotNode)
				newShuffleNode.getParam('outputR').set(outputLayer)
			layerCounter += 1
