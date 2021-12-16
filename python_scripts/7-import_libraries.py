import math

print(math.sin(math.pi))

###########################
###########################
# change it into this:

import rhinoscriptsyntax as rs
a=[]
pt1=rs.AddPoint(0,0,0)
pt2=rs.AddPoint(5,0,0)
a.append(rs.AddLine(pt1,pt2))


###########################
###########################
# then into this:

import rhinoscriptsyntax as rs
a=[]

a.append(rs.AddLine(point1,point2))