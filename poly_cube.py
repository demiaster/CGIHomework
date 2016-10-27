#importing Python Maya commands
import maya.cmds as cmds

#create a polygonal cube
#if not specificated, length and depth are assigned
#to the default value of 1
cmds.polyCube(name = 'cube', width = 3)

#getting values of x, y, z translation
x = cmds.getAttr('cube.tx')
y = cmds.getAttr('cube.ty')
z = cmds.getAttr('cube.tz')

#creating a new string interpolated with x, y, z values
s = "[ %s, %s, %s ]" % (x, y, z)

#printing values
print s