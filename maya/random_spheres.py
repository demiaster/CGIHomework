#importing Python Maya commands
import maya.cmds as cmds
#importing random for casual sphere positioning
import random

#creating a new sphere 'sphere'
cmds.sphere(name = 'sphere')

#declaring an empty list 'listOfClones'
listOfClones = []

#cloning 'sphere' 100 times, storing them in 'listOfClones'
for i in range(0, 100):
    clone = cmds.duplicate('sphere')
    listOfClones.append(clone[0])
    
for i in range(0, len(listOfClones)):
    cmds.move(random.gauss(0 , 1) * 2,
              random.gauss(0 , 1) * 2,
              random.gauss(0 , 1) * 2, listOfClones[i])