#importing Python Maya commands
import maya.cmds as cmds

#creating a sphere and storing its name
cmds.sphere(name = 'sphere', radius = 2)
name = 'sphere'

#quering and printing radius of the sphere
r = cmds.sphere(name, query = True, radius = True)
print r

#assigning new value for radius
cmds.sphere('sphere', edit = True, radius = 4)

#deleting all objects from the scene
cmds.select(all = True)
cmds.delete()

#creating a new shape: torus
cmds.torus(name = 'torus', radius = 4, heightRatio = 0.5)
