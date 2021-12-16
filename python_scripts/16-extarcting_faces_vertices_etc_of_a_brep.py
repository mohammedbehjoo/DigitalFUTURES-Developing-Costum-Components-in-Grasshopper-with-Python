import ghpythonlib.components as ghcomp
import rhinoscriptsyntax as rs

faces,edges,vertices=ghcomp.DeconstructBrep(brep)
face=faces[index]
curve_of_face=ghcomp.BrepWireframe(face)
curves=curve_of_face
curve_of_face=curve_of_face[index_crv]
points_of_face,_=ghcomp.Discontinuity(curve_of_face)
all_points_of_curve,_=ghcomp.Discontinuity(curves)
center_of_surface,_=rs.SurfaceAreaCentroid(face)


# polyline with an arbitrary formula

import rhinoscriptsyntax as rs
import math
import random



x_cor=[]
y_cor=[]

for i in range(x):
    x_cor.append((random.random()*random_factor)+factor_a+0.5*i*math.cos(0.5*i))
    y_cor.append((random.random()*random_factor)+factor_b+0.2*i*math.sin(0.2*i))


# then:
import rhinoscriptsyntax as rs
import math
import random

if"t" in globals():
    t+=0.1
else:
    t=0

x_cor=[]
y_cor=[]
points=[]
for i in range(x):
    x_cor=(random.random()*random_factor)+factor_a+0.5*i*math.cos(0.5*i)
    y_cor=(random.random()*random_factor)+factor_b+0.2*i*math.sin(0.2*i)
    print(len(points))
    if len(points)<limit:
        points.append(rs.AddPoint(x_cor,y_cor,0))
    if len(points)>=limit:
        points.pop()
polyline=rs.AddPolyline(points)



