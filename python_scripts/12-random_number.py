import rhinoscriptsyntax as rs
import math

a=[]
for i in range(number):
    x=(math.cos(i)*factor_x)
    y=(math.sin(i)*factor_y)
    p=rs.AddPoint(x,y,0)
    a.append(p)



##########################
##########################
# then:
import rhinoscriptsyntax as rs
import math

a=[]
for i in range(number):
    x=(math.cos(i)*factor_x)
    y=(math.sin(i)*factor_y)
    p=rs.AddPoint(x,y,0)
    a.append(p)