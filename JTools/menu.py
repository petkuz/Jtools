import nuke

#asign variables
nodeBar=nuke.menu("Nodes")
JTools = nodeBar.addMenu('JTools', icon="JTools.png")

#create JTools menu items
JTools.addCommand( "JApplyMatte", "nuke.createNode('JApplyMatte')", icon="JApplyMatte.png")
JTools.addCommand( "JCleanPlate", "nuke.createNode('JCleanPlate')", icon="JCleanPlate.png")
JTools.addCommand( "JDespot", "nuke.createNode('JDespot')", icon="JDespot.png")
JTools.addCommand( "JFltatten", "nuke.createNode('JFltatten')", icon="JFltatten.png")
JTools.addCommand( "JPremult", "nuke.createNode('JPremult')", icon="JPremult.png")
JTools.addCommand( "JHilights", "nuke.createNode('JHilights')", icon="JHilights.png")
JTools.addCommand( "JShadows", "nuke.createNode('JShadows')", icon="JShadows.png")
JTools.addCommand( "JSmoothEdge", "nuke.createNode('JSmoothEdge')", icon="JSmoothEdge.png")
JTools.addCommand( "JPixelate", "nuke.createNode('JPixelate')", icon="JPixelate.png")