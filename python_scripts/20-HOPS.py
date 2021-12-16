from flask import Flask
import ghhops_server as hs
import math
import rhinoinside
rhinoinside.load()
# System and Rhino can only be loaded after rhinoinside is initialized
import System  
import Rhino  

hops = hs.Hops(app=rhinoinside)


@hops.component(
    "/wave",
    name="wave",
    description="create a wave",
    inputs=[
        hs.HopsInteger("X", "x", "number of points in X axis"),
        hs.HopsInteger("Y", "y", "number of points in Y axis"),
        hs.HopsNumber("Height", "h", "height of waves"),
        hs.HopsNumber("amplitude", "a", "amplitude of the waves")
    ],
    outputs=[
        hs.HopsSurface("Surface", "S", "A surface made up of a list of points")
    ]
)
def wave(x, y, height, amplitude):
    points = System.Collections.Generic.List[Rhino.Geometry.Point3d]()
    for i in range(x):
        for j in range(y):
            pt = Rhino.Geometry.Point3d(float(i), float(j), math.sin(i * height) * math.sin(j * height) * amplitude)
            points.Add(pt)
    surface = Rhino.Geometry.NurbsSurface.CreateFromPoints(points, x, y, x, y)
    return surface

if __name__ == "__main__":
    hops.start(debug=True)