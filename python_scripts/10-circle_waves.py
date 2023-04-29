import rhinoscriptsyntax as rs


a=[]
for radius in range(radius_start,radius_end):
    a.append(rs.AddCircle([0,0,0],radius))



##########################
##########################
# then:
import rhinoscriptsyntax as rs


a=[]
for radius in range(radius_start,radius_end):
    a.append(rs.AddCircle([0,0,0],radius))

##########################
##########################
# then:
import rhinoscriptsyntax as rs
import math

a=[]
for radius in range(radius_start,radius_end):
    a.append(rs.AddCircle([x,y,math.sin(radius/distance_between)*k],radius))



##########################
##########################
# then something new:
import rhinoscriptsyntax as rs
import math

if "p" in globals():
    p+=0.1
else:
    p=0

a=[]
for i in range(x):
    for j in range(y):
        z=math.sin(p)       # the sinus function interval is between [-1,1]
        point=rs.AddPoint(i,j,z)
        a.append(point)



##########################
##########################
# then:
import rhinoscriptsyntax as rs
import math

if "p" in globals():
    p+=0.1
else:
    p=0


    
    

a=[]
#x and y variables are int variables. initialize them in the grasshopper
for i in range(x):
    for j in range(y):
        pt=rs.AddPoint(i,j,0)
        #should Initialize center_of_the_circle in grasshopper environment as a Point3D
        center_dist=rs.Distance(center_of_the_circle,pt)
        z=math.sin(p+center_dist)
        a.append(rs.AddPoint(i,j,z))
