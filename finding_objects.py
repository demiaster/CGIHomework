#importing Python Maya commands
import maya.cmds as cmds

name = 'jack'

#else/if statement to look for an object
#called 'jack'
if cmds.objExists(name) :
    v = input(float)
    cmds.sphere(name = 'jill', radius = v)
    
    #querying for 'jack' position
    x = cmds.getAttr('jack.tx')
    y = cmds.getAttr('jack.ty')
    z = cmds.getAttr('jack.tz')
    
    #setting 'jill' 5 unit away from 'jack'
    x = cmds.setAttr('jill.tx', x + 5)
    y = cmds.setAttr('jill.ty', y + 5)
    z = cmds.setAttr('jill.tz', z + 5)
    
else :
    print "%s does not exist!" % name
