import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import System.Drawing as sd
import Rhino.RhinoDoc as rr
import scriptcontext as sc

sc.doc=rr.ActiveDoc

def createColoredPoint(x,y,z,r,g,b):
    currentColor = [r,g,b]
    pt = rs.AddPoint(x,y,z)
    rs.ObjectColor(pt, currentColor)


rs.EnableRedraw(False)


for x in range(0,256, step):
    for y in range(0,256, step):
        for z in range(0,256,step):
            createColoredPoint(x,y,z,x,y,z)
rs.Redraw()