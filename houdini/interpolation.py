import math

node = hou.pwd()
geo = node.geometry()

# Add code to modify contents of geo.
# Use drop down menu to select examples.

# read degree of rotation and tranform into radians
degNodeL = hou.node('/obj/geo1/AngleL')
thetaL = math.radians(degNodeL.evalParm('value1v1'))
halfthetaL = thetaL/2.0
# end read degree

# read rotation axis and normalise
axisNodeL = hou.node('/obj/geo1/AxisL')
axisValueL = axisNodeL.evalParmTuple('value1v')[0:3]
# by default evalParmTuple will return a tuple with 4 element
axisL = hou.Vector3(axisValueL)
if axisL.length() < 1e-8: 
    axisL = hou.Vector3(1,0,0)
    print "Warning: rotation axis has zero length. It is set to (1,0,0)"
axisL = axisL.normalized()
# end read axis

# read degree of rotation and tranform into radians
degNodeR = hou.node('/obj/geo1/AngleR')
thetaR = math.radians(degNodeR.evalParm('value1v1'))
halfthetaR = thetaR/2.0
# end read degree

# read rotation axis and normalise
axisNodeR = hou.node('/obj/geo1/AxisR')
axisValueR = axisNodeR.evalParmTuple('value1v')[0:3]
# by default evalParmTuple will return a tuple with 4 element
axisR = hou.Vector3(axisValueR)
if axisR.length() < 1e-8: 
    axisR = hou.Vector3(1,0,0)
    print "Warining: rotation axis has zero length. It is set to (1,0,0)"
axisR = axisR.normalized()
# end read axis

# read ratio
ratioNode = hou.node('/obj/geo1/Ratio')
Ratio = ratioNode.evalParm('value1v1')
# end read ratio




#rotQuaternion = hou.Quaternion(math.cos(halftheta), axis*math.sin(halftheta))
qL = hou.Quaternion(axisL[0]*math.sin(halfthetaL), axisL[1]*math.sin(halfthetaL), axisL[2]*math.sin(halfthetaL), math.cos(halfthetaL))
#qLC = hou.Quaternion( -axisL[0]*math.sin(halfthetaL), -axisL[1]*math.sin(halfthetaL), -axisL[2]*math.sin(halfthetaL), math.cos(halfthetaL))


qR = hou.Quaternion(axisR[0]*math.sin(halfthetaR), axisR[1]*math.sin(halfthetaR), axisR[2]*math.sin(halfthetaR), math.cos(halfthetaR))
#qRC = hou.Quaternion( -axisR[0]*math.sin(halfthetaR), -axisR[1]*math.sin(halfthetaR), -axisR[2]*math.sin(halfthetaR), math.cos(halfthetaR))

dotProduct = qL.dot(qR)
angleQ = math.acos(dotProduct)
#find angle between two quaternion

if (angleQ > 1.0e-6) : 
    w1 = math.sin((1-Ratio)*angleQ)/math.sin(angleQ)
    w2 = math.sin(Ratio*angleQ)/math.sin(angleQ)
    rotQuaternion = qL*w1 + qR*w2
else:
    rotQuaternion = qL * (1 - Ratio) + qR * (Ratio)
rotConjQuaternion = hou.Quaternion(-rotQuaternion[0], -rotQuaternion[1], -rotQuaternion[2], rotQuaternion[3])


#note in Houdidi Quaternion stored as (virtual vector, real number)!!!!




for point in geo.points():
    pos = point.attribValue("P")
    #it seems differnt from pos = point.position
    posQuaternion = hou.Quaternion(pos[0], pos[1], pos[2], 0)
    posQuaternion = rotQuaternion*posQuaternion*rotConjQuaternion
    #rotate happens by the quaternion multiplication
    #print posQuaternion
    pos = (posQuaternion[0],posQuaternion[1],posQuaternion[2])
    point.setPosition(pos)
