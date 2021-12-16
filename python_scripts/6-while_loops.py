import rhinoscriptsyntax as rs
i=0
a=[]
while i<limit and reset==True:
    a.append(rs.AddPoint(i,0,0))
    i+=1