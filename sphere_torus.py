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

#translate 'torus' by 1 unit along the x-axis
cmds.move(1, 0, 0, 'torus')

#scale 'torus' by half along y-axis
cmds.scale(1, 0.5, 1, 'torus')

#rotate 'torus by 45 degrees about the z-axis
cmds.rotate(0, 0, 45, 'torus')

#now move, scale, rotate 'torus' relative to its current
#position, scale, rotation
cmds.move(2, 0, 0, 'torus', relative = True)
cmds.scale(1, 0.7, 1, 'torus', relative = True)
cmds.rotate(0, 0, 10, 'torus', relative = True)
