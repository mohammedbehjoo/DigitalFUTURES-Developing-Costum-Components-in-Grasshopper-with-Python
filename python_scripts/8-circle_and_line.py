import rhinoscriptsyntax as rs

a=rs.AddPoint([0,0,0])
b=rs.AddLine([0,0,0],[10,0,0])
c=rs.AddCircle([0,0,0],10)


##########################
##########################
# then turn it into this:

import rhinoscriptsyntax as rs


a=rs.AddPoint(point_1)
b=rs.AddLine(point_1,point_2)
c=rs.AddCircle(point_1,radius)