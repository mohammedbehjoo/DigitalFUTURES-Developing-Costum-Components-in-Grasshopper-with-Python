import rhinoscriptsyntax as rs
import ghpythonlib.components as ghcomp
import Rhino.Geometry as rg
import math



def vault_or_dome(pt1, pt2, pt3, pt4,height,sides_height):
    pt1=rs.coerce3dpoint(pt1)
    pt2=rs.coerce3dpoint(pt2)
    pt3=rs.coerce3dpoint(pt3)
    pt4=rs.coerce3dpoint(pt4)
    x = (pt1.X + pt2.X + pt3.X + pt4.X) / 4.0
    y = (pt1.Y + pt2.Y + pt3.Y + pt4.Y) / 4.0
    z = (pt1.Z + pt2.Z + pt3.Z + pt4.Z) / 4.0
    
    # something imp
    center_point = rs.AddPoint(x, y, z)
    center_point=rs.coerce3dpoint(center_point)

    # something imp
    center_vintage_point = rs.AddPoint(center_point.X, center_point.Y, center_point.Z + height)
    center_vintage_point=rs.coerce3dpoint(center_vintage_point)

    
    mid_point_1_x=(pt1.X + pt2.X)/2
    mid_point_1_y=(pt1.Y + pt2.Y)/2
    mid_point_1_z=(pt1.Z + pt2.Z)/2

    mid_point_2_x=(pt3.X + pt2.X)/2
    mid_point_2_y=(pt3.Y + pt2.Y)/2
    mid_point_2_z=(pt3.Z + pt2.Z)/2

    mid_point_3_x=(pt3.X + pt4.X)/2
    mid_point_3_y=(pt3.Y + pt4.Y)/2
    mid_point_3_z=(pt3.Z + pt4.Z)/2

    mid_point_4_x=(pt1.X + pt4.X)/2
    mid_point_4_y=(pt1.Y + pt4.Y)/2
    mid_point_4_z=(pt1.Z + pt4.Z)/2

    #sopmething imp 
    first_side_main_point = rs.AddPoint(mid_point_1_x, mid_point_1_y, mid_point_1_z+ center_vintage_point.Z + sides_height)
    first_side_main_point=rs.coerce3dpoint(first_side_main_point)

    second_side_main_point = rs.AddPoint(mid_point_2_x, mid_point_2_y, mid_point_2_z+ center_vintage_point.Z + sides_height)
    second_side_main_point=rs.coerce3dpoint(second_side_main_point)

    third_side_main_point = rs.AddPoint(mid_point_3_x, mid_point_3_y, mid_point_3_z+ center_vintage_point.Z + sides_height)
    third_side_main_point=rs.coerce3dpoint(third_side_main_point)

    fourth_side_main_point = rs.AddPoint(mid_point_4_x, mid_point_4_y, mid_point_4_z+ center_vintage_point.Z + sides_height)
    fourth_side_main_point=rs.coerce3dpoint(fourth_side_main_point)


    vector_up=ghcomp.UnitZ(1)

# something imp
    center_arch_list=[]
    center_arch_1 = rg.ArcCurve(rg.Arc(pt1, vector_up, center_vintage_point))
    center_arch_list.append(center_arch_1)
    center_arch_2= rg.ArcCurve(rg.Arc(pt2, vector_up, center_vintage_point))
    center_arch_list.append(center_arch_2)
    center_arch_3= rg.ArcCurve(rg.Arc(pt3, vector_up, center_vintage_point))
    center_arch_list.append(center_arch_3)
    center_arch_4= rg.ArcCurve(rg.Arc(pt4, vector_up, center_vintage_point))
    center_arch_list.append(center_arch_4)

    side_arch_list=[]
    side_arch_1=rg.ArcCurve(rg.Arc(pt1,vector_up,first_side_main_point))
    side_arch_list.append(side_arch_1)
    side_arch_2=rg.ArcCurve(rg.Arc(pt1,vector_up,fourth_side_main_point))
    side_arch_list.append(side_arch_2)
    side_arch_3=rg.ArcCurve(rg.Arc(pt2,vector_up,first_side_main_point))
    side_arch_list.append(side_arch_3)
    side_arch_4=rg.ArcCurve(rg.Arc(pt2,vector_up,second_side_main_point))
    side_arch_list.append(side_arch_4)
    side_arch_5=rg.ArcCurve(rg.Arc(pt3,vector_up,second_side_main_point))
    side_arch_list.append(side_arch_5)
    side_arch_6=rg.ArcCurve(rg.Arc(pt3,vector_up,third_side_main_point))
    side_arch_list.append(side_arch_6)
    side_arch_7=rg.ArcCurve(rg.Arc(pt4,vector_up,third_side_main_point))
    side_arch_list.append(side_arch_7)
    side_arch_8=rg.ArcCurve(rg.Arc(pt4,vector_up,fourth_side_main_point ))
    side_arch_list.append(side_arch_8)

# something imp
    struc=[]
    str_1 = rs.AddLoftSrf([center_arch_1,side_arch_1])
    str_1=rs.coercegeometry(str_1)
    struc.append(str_1)
    
    str_2 = rs.AddLoftSrf([center_arch_1,side_arch_2])
    str_2=rs.coercegeometry(str_2)
    struc.append(str_2)
    
    str_3 = rs.AddLoftSrf([center_arch_2,side_arch_3])
    str_3=rs.coercegeometry(str_3)
    struc.append(str_3)
    
    str_4 = rs.AddLoftSrf([center_arch_2,side_arch_4])
    str_4=rs.coercegeometry(str_4)
    struc.append(str_4)
    
    str_5 = rs.AddLoftSrf([center_arch_3,side_arch_5])
    str_5=rs.coercegeometry(str_5)
    struc.append(str_5)

    str_6 = rs.AddLoftSrf([center_arch_3,side_arch_6])
    str_6=rs.coercegeometry(str_6)
    struc.append(str_6)
    
    str_7 = rs.AddLoftSrf([center_arch_4,side_arch_7])
    str_7=rs.coercegeometry(str_7)
    struc.append(str_7)
    
    str_8 = rs.AddLoftSrf([center_arch_4,side_arch_8])
    str_8=rs.coercegeometry(str_8)
    struc.append(str_8)

    return struc

a=vault_or_dome(pt1, pt2, pt3, pt4,height,sides_height)