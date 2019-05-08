import xml.etree.ElementTree as ET
import xml.dom.minidom
import os
import pyperclip
import Line as shape #set shape to import here

print("PyArray2SpaceEng by CodeArc13")

#regular camelCase used for all python variables unless they are specified in the blueprint XML, 
    #in which case they are Capitalised.
coordSet = set()

bluePrintsDir = os.path.expandvars("%APPDATA%\SpaceEngineers\Blueprints\local\\")
idName = shape.__name__ #use module name as blueprint display name
bluePrintFolder = bluePrintsDir + idName
idNameNumbered = idName #only changes when more than one blueprint of the shape already exists

if os.path.isdir(bluePrintFolder):
    folderNumber = 1
    while os.path.isdir(bluePrintFolder + "_" + str(folderNumber)):
        folderNumber += 1
    idNameNumbered = idName + "_" + str(folderNumber)
    bluePrintFolder = bluePrintsDir + idNameNumbered


userName = "BravelyBoldSirRobin"
workshopIdNumber = "0"
ownerSteamIdNumber = "0"
pointsNumber = "0"
entityIdNumber = "0" #will be random number
localCoordSysNumber = "0"

#This is the main generator file. Parametric plots must go in their own files and be called by this
    #and pass back a set of coordinate tuples.
print("Creating " + idName)

def plotBlocks():
    blocksWritten = 0
    coordSet = shape.plot()
    for coord in coordSet:
        (x, y, z) = coord
        MyObjectBuilder_CubeBlock = ET.SubElement(CubeBlocks, "MyObjectBuilder_CubeBlock")
        MyObjectBuilder_CubeBlock.set("xsi:type","MyObjectBuilder_CubeBlock")
        SubtypeName = ET.SubElement(MyObjectBuilder_CubeBlock, "SubtypeName").text = "LargeHeavyBlockArmorBlock"
        Min = ET.SubElement(MyObjectBuilder_CubeBlock, "Min")
        Min.set("x", str(x))
        Min.set("y", str(y))
        Min.set("z", str(z))
        blocksWritten += 1
        print(str(blocksWritten) + " Blocks written ", end="\r", flush=True)
    print(str(blocksWritten) + " Blocks written ")


Definitions = ET.Element("Definitions", **{"xmlns:xsd": "http://www.w3.org/2001/XMLSchema"}, **{"xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance"})
ShipBlueprints = ET.SubElement(Definitions, "ShipBlueprints")
ShipBlueprint = ET.SubElement(ShipBlueprints, "ShipBlueprint")
ShipBlueprint.set("xsi:type","MyObjectBuilder_ShipBlueprintDefinition")
Id = ET.SubElement(ShipBlueprint, "Id")
Id.set("Type", "MyObjectBuilder_ShipBlueprintDefinition")
Id.set("Subtype", idName)
DisplayName = ET.SubElement(ShipBlueprint, "DisplayName").text = userName
CubeGrids = ET.SubElement(ShipBlueprint, "CubeGrids")
CubeGrid = ET.SubElement(CubeGrids, "CubeGrid")
SubtypeName = ET.SubElement(CubeGrid, "SubtypeName")
EntityId = ET.SubElement(CubeGrid, "EntityId").text = entityIdNumber
PersistentFlags = ET.SubElement(CubeGrid, "PersistentFlags").text = "CastShadows InScene"
PositionAndOrientation = ET.SubElement(CubeGrid, "PositionAndOrientation")
Position = ET.SubElement(PositionAndOrientation, "Position")
Position.set("x", "0")
Position.set("y", "0")
Position.set("z", "0")
Forward = ET.SubElement(PositionAndOrientation, "Forward")
Forward.set("x", "0")
Forward.set("y", "0")
Forward.set("z", "0")
Up = ET.SubElement(PositionAndOrientation, "Up")
Up.set("x", "0")
Up.set("y", "0")
Up.set("z", "0")
Orientation = ET.SubElement(PositionAndOrientation, "Orientation")
X = ET.SubElement(Orientation, "X").text = "0"
Y = ET.SubElement(Orientation, "Y").text = "0"
Z = ET.SubElement(Orientation, "Z").text = "0"
W = ET.SubElement(Orientation, "W").text = "0"
GridSizeEnum = ET.SubElement(CubeGrid, "GridSizeEnum").text = "Large"
CubeBlocks = ET.SubElement(CubeGrid, "CubeBlocks")

plotBlocks() #where blocks are actually plotted

IsStatic = ET.SubElement(CubeGrid, "IsStatic").text = "true"
DisplayName = ET.SubElement(CubeGrid, "DisplayName").text = idName
DestructibleBlocks = ET.SubElement(CubeGrid, "DestructibleBlocks").text = "true"
IsRespawnGrid = ET.SubElement(CubeGrid, "IsRespawnGrid").text = "false"
LocalCoordSys = ET.SubElement(CubeGrid, "LocalCoordSys").text = localCoordSysNumber
TargetingTargets = ET.SubElement(CubeGrid, "TargetingTargets")

 
WorkshopId = ET.SubElement(ShipBlueprint, "WorkshopId").text = workshopIdNumber
OwnerSteamId = ET.SubElement(ShipBlueprint, "OwnerSteamId").text = ownerSteamIdNumber
Points = ET.SubElement(ShipBlueprint, "Points").text = pointsNumber

tree = ET.ElementTree(Definitions)
tree = tree.getroot()
treeStr = ET.tostring(tree, encoding="unicode", method="xml", short_empty_elements=False)

print("Writing blueprint file please wait...")

dom = xml.dom.minidom.parseString(treeStr)
prettyXmlString = dom.toprettyxml()
os.mkdir(bluePrintFolder)
textFile = open(bluePrintFolder + "\\bp.sbc", "w")
textFile.write(prettyXmlString)
textFile.close()

pyperclip.copy(idNameNumbered)
print(idNameNumbered + " created and name copied to clipboard for easy blueprint searching.")

