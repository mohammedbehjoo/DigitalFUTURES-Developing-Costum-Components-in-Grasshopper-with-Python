# start with this:
import rhinoscriptsyntax as rs
import math

a = []
for i in range(x):
    for j in range(y):
        a.append(rs.AddPoint(i, j, math.sin(i*height) * math.sin(j*height) * distance))



##########################
##########################
# we can make a function(definition)

import rhinoscriptsyntax as rs
import math
a=[]
def points(x,y):
    for i in range(x):
        for j in range(y):
            a.append(rs.AddPoint(i, j, math.sin(i*height) * math.sin(j*height) * amplitude))
    return a
points(x,y)



##########################
##########################
# then: add t

import rhinoscriptsyntax as rs
import math

if "p" in globals():
    p+=0.1
else:
    p=0

a = []
for i in range(x):
    for j in range(y):
        a.append(rs.AddPoint(i, j, math.sin(i*height) * math.sin(j*height) * amplitude))