import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import math

def fractal(pt1,pt2,angle):
#   creating a curve to extract its division points
    line=rs.AddLine(pt1,pt2)
    points=rs.DivideCurve(line,4)

#  1/3 point 
    between_points_1=points[1]
    between_points_2=points[3]

#   mid vector
    mid_vec= rg.Vector3d(points[2].X - points[1].X, points[2].Y - points[1].Y, points[2].Z - points[1].Z)
    mid_vec.Rotate(math.radians(angle), rg.Vector3d.ZAxis)
    mid_vec=rs.VectorUnitize(mid_vec)
    mid_vec*=length

#    mid point 
    mid_point=((pt2+pt1)/2)+mid_vec
    
#   returning points 
    return pt1,between_points_1,mid_point,between_points_2,pt2

a=fractal(first,second,angle)


###########################
###########################
# then change it into this:
import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import math

def create_points(first_point,second_point):
#   creating a curve to extract its division points
    line=rs.AddLine(first_point,second_point)
    points=rs.DivideCurve(line,4)

#  1/3 point 

    between_points_1=points[1]
    between_points_2=points[3]
    
#   mid vector
    mid_vec= rg.Vector3d(points[2].X - points[1].X, points[2].Y - points[1].Y, points[2].Z - points[1].Z)
    mid_vec.Rotate(math.radians(angle), rg.Vector3d.ZAxis)
    mid_vec=rs.VectorUnitize(mid_vec)
    mid_vec*=length

#    mid point 
    mid_point=((second_point+first_point)/2)+mid_vec

#   returning points 
    return first_point,between_points_1,mid_point,between_points_2,second_point

def snowflake(first_point,second_point,iteration,poly_list):
    if iteration>0:
        temp_points=create_points(first_point,second_point)
        poly=rs.AddPolyline([temp_points[0],temp_points[1],temp_points[2],temp_points[3],temp_points[4]])
        if iteration==1:
            poly_list.append(poly)
        snowflake(temp_points[0],temp_points[1],iteration-1,poly_list)
        snowflake(temp_points[1],temp_points[2],iteration-1,poly_list)
        snowflake(temp_points[2],temp_points[3],iteration-1,poly_list)
        snowflake(temp_points[3],temp_points[4],iteration-1,poly_list)
    return poly_list



b=[]
a=snowflake(first,second,iteration,b)