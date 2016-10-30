# importing Python Maya commands
import maya.cmds as cmds


def makeClones(name, num):
    """ Creates a list of duplicate objects

    - **parameters**, **types**, **return** and **return types**::

         :param name: is the name of the Maya object to duplicate
         :param num: is the number of duplicate copies to make
         :type name: string
         :type num: int
         :return: return list with ’num’ duplicates of ’name’
         :rtype: list of maya objects

    """

    # declaring an empty list 'listOfClones'
    listOfClones = []

    # cloning 'sphere' 100 times, storing them in 'listOfClones'
    for i in range(0, num):
        clone = cmds.duplicate('sphere')
        listOfClones.append(clone[0])

    return listOfClones


def placeInRows(listName, unitsAppart, objectW, axis):
    """Place objects in a row along the X/Y/ Z major axis

    - **parameters**, **types**, **return** and **return types**::

        :param listName: is a Python list of object names
        :param unitsAppart: number of units the objects have to
                               be placed apart from each other
        :param objectW: width, breadth or height of objects in the list
        :param axis : is one of ’x/X ’ , ’y/Y’ , or ’z/Z’
                      The axis specifies the direction along
                      which objects are placed in a row

        :return: objects in the list are placed in a row along
                 ’axis’ and ’unitsAppart’ from each other
        :rtype: list of maya objects

    """

    # cicle through the whole list
    for i in range(0, len(listName)):

        # for every object except the first one
        if (i != 0):
            # saving infos of previous object
            prevIndex = i - 1
            prevObj = "%s.t%s" % (listName[prevIndex], axis)
            prevTX = cmds.getAttr(prevObj)

            # translating current object
            currentObj = "%s.t%s" % (listName[i], axis)
            cmds.setAttr(currentObj, prevTX + unitsAppart)

        # scaling object
        cmds.scale(objectW, objectW, objectW, listName[i])

    return listName
 
 

