# importing Python Maya commands
import maya.cmds as cmds

import math


def moons(planet, number, distance, size):
    """creates and parents spheres (moons) around a planet
    :param planet: a string which is the name of an object
    :param number: number of spheres orbiting the planet
    :param distance: of the spheres (moons) from the planet
    :param size: radius of each spherical moon
    :return: returns a list with the names of the moons
             parented to the planet
    """

    deltaAngleGrade = float(360) / number
    deltaAngle = deltaAngleGrade * math.pi / 180
    angle = 0

    satellite = cmds.group(em=True, n='satellite')

    for i in range(0, number):
        cmds.duplicate(planet, name='moon%s' % i)

        # rotate moon
        cmds.xform('moon%s' % i, rotation=[angle, 0, 0], os=True)

        # translation to new position
        xDisplacement = distance * math.cos(angle)
        yDisplacement = distance * math.sin(angle)
        cmds.xform('moon%s' % i, translation=[xDisplacement, yDisplacement, 0], relative=True)

        # resize new moon
        cmds.scale(size, size, size, 'moon%s' % i, relative=True)

        # parenting
        cmds.parent('moon%s' % i, satellite)

        angle += deltaAngle
    cmds.parent(satellite, planet)


moons('sphere', 6, 6, 0.5)