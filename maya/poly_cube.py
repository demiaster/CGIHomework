#importing Python Maya commands
import maya.cmds as cmds

#create a polygonal cube 'cube'
#if not specificated, length and depth are assigned
#to the default value of 1
cmds.polyCube(name = 'cube', width = 3)

#get x, y, z translation values of 'cube'
x = cmds.getAttr('cube.tx')
y = cmds.getAttr('cube.ty')
z = cmds.getAttr('cube.tz')

#create a new string interpolated with x, y, z values
s = "[ %s, %s, %s ]" % (x, y, z)

#print values
print s

#create a second polygonal cube 'qube'
cmds.polyCube(name = 'qube', width = 3)

#using setAttr to change x, y, z translation value
#for 'cube'

cmds.setAttr('qube.tx', 1)
cmds.setAttr('qube.ty', 2)
cmds.setAttr('qube.tz', 3)