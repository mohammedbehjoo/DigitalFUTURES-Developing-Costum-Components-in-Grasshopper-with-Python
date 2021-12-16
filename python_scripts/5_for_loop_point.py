import rhinoscriptsyntax as rs


a=rs.AddPoint([0,0,0])




###########################
###########################
import rhinoscriptsyntax as rs

a=[]
for i in range(x):
    point_1=rs.AddPoint(i,0,0)
    a.append(point_1)


###########################
###########################
# change it into a grid

import rhinoscriptsyntax as rs

a=[]
for i in range(x):
    for j in range(y):
        point_1=rs.AddPoint(i,j,0)
        
        a.append(point_1)


###########################
###########################