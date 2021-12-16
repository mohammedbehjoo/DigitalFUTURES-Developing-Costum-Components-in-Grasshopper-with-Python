# let me explain something before the next example:

# it is necessary because the next example is going to be a little bit complicated:

for i in range(x):
    print("i is equal to: ",i)
    print("x is equal to: ",x)
    print("the result of i divided by x is: ",i/x)



##########################
##########################
# after that do this:
import Rhino.Geometry as rg


panels = []
for i in range(x):
    for j in range(y):
        u = i/x
        v = j/y
        pt1 = initial_surface.PointAt(u, v)
        pt2 = initial_surface.PointAt(u + (h_left_up-u)/x, v + v_left_up/y)
        pt3 = initial_surface.PointAt(u + (h_right_up+u)/x, v + v_up_right/y)
        pt4 = initial_surface.PointAt(u + h_right_down/x, v + v_right_down/y)
        

				panel = rg.NurbsSurface.CreateFromCorners(pt1, pt2, pt3, pt4)
        panels.append(panel)



##########################
##########################
# if I do not want the panels to collide with each other I'm going to work with the normal vectors of the panels.
import Rhino.Geometry as rg


panels = []
for i in range(x):
    for j in range(y):
        u = i/x
        v = j/y
        pt1 = initial_surface.PointAt(u, v)
        pt2 = initial_surface.PointAt(u + (h_left_up-u)/x, v + v_left_up/y)
        pt3 = initial_surface.PointAt(u + (h_right_up+u)/x, v + v_up_right/y)
        pt4 = initial_surface.PointAt(u + h_right_down/x, v + v_right_down/y)
        n1 = initial_surface.NormalAt(u, v)
        n2 = initial_surface.NormalAt(u + (h_left_up-u)/x, v + v_left_up/y)
        n3 = initial_surface.NormalAt(u + (h_right_up+u)/x, v + v_up_right/y)
        n4 = initial_surface.NormalAt(u + h_right_down/x, v + v_right_down/y)

        pt1 += n1*factor_1
        pt2 += n2*factor_2
        pt3 += n3*factor_3
        pt4 += n4*factor_4

        panel = rg.NurbsSurface.CreateFromCorners(pt1, pt2, pt3, pt4)
        panels.append(panel)