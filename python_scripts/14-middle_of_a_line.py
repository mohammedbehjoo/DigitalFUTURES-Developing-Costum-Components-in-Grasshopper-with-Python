import rhinoscriptsyntax as rs

mid_point=(first_point+second_point)/2
a=mid_point


##########################
##########################
# then:
import rhinoscriptsyntax as rs

mid_point=(first_point+second_point)/2
a=mid_point



##########################
##########################
# then:
import rhinoscriptsyntax as rs

mid_point=(first_point*(1-parameter))+(second_point*parameter)
a=mid_point

##########################
##########################
# then: pay attention to the list access of the points because we do not have a single item anymore. we have a bunch of items. so we should set it to list access
import rhinoscriptsyntax as rs

#print(len(points))
a=[]
for i in range(len(points)-1):
    a.append((points[i]*0.75)+(points[i+1]*0.25))



##########################
##########################
# then:
import rhinoscriptsyntax as rs

#print(len(points))
mid_point=[]
for i in range(len(points)-1):
    mid_point.append((points[i]*0.75)+(points[i+1]*0.25))
    mid_point.append((points[i]*0.25)+(points[i+1]*0.75))



##########################
##########################
# then:
import rhinoscriptsyntax as rs

#print(len(points))
mid_point=[]
for i in range(len(points)-1):
    mid_point.append((points[i]*0.75)+(points[i+1]*0.25))
    mid_point.append((points[i]*0.25)+(points[i+1]*0.75))