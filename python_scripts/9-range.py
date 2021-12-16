import rhinoscriptsyntax as rs


for i in range(x):
    for j in range(y):
        a=rs.AddCircle([i,j,0],radius+1)

##########################
##########################
#then turn into this:
import rhinoscriptsyntax as rs


a=[]
for i in range(x):
    for j in range(y):
        point=rs.AddPoint(i,j,0)
        circle=rs.AddCircle(point,radius)
        a.append(circle)

##########################
##########################
# then this:
import rhinoscriptsyntax as rs


a=[]
for i in range(x):
    for j in range(y):
        point=rs.AddPoint(i,j,0)
        circle=rs.AddCircle(point,radius)
        a.append(circle)

##########################
##########################
# then into this:
import rhinoscriptsyntax as rs


a=[]
b=[]
for i in range(x):
    for j in range(y):
        point=rs.AddPoint(i*dist_x,j*dist_y,0)
        b.append(rs.AddCone(point,height,radius,cap))
        circle=rs.AddCircle(point,radius)
        a.append(circle)

##########################
##########################
# then into this:
import rhinoscriptsyntax as rs


a=[]
b=[]
for i in range(x):
    for j in range(y):
        point=rs.AddPoint(i*dist_x,j*dist_y,0)
        point_height=rs.AddPoint(i*dist_x,j*dist_y,height)
        b.append(rs.AddCone(point,point_height,radius,cap))
        circle=rs.AddCircle(point,radius)
        a.append(circle)


##########################
##########################
# then trun it to this:
import rhinoscriptsyntax as rs


a=[]
b=[]
for i in range(x):
    for j in range(y):
        point=rs.AddPoint(i*dist_x,j*dist_y,0)
        distance=rs.Distance(point,attractor)
        distance*=dist_factor
        if distance>dist_x/2:
            distance=dist_x/2
        point_height=rs.AddPoint(i*dist_x,j*dist_y,height)
        b.append(rs.AddCone(point,point_height,distance,cap))

##########################
##########################
# then:
import rhinoscriptsyntax as rs


a=[]
b=[]
for i in range(x):
    for j in range(y):
        point=rs.AddPoint(i*dist_x,j*dist_y,0)
        distance=rs.Distance(point,attractor)
        height=distance
        distance*=dist_factor
        if distance>dist_x/2:
            distance=dist_x/2
        point_height=rs.AddPoint(i*dist_x,j*dist_y,height)
        b.append(rs.AddCone(point,point_height,distance,cap))