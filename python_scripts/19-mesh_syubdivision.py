import Rhino.Geometry as rg

def mesh_ex(mesh):
  
    normals=[]
    repeated_vertices=[]
    temp_points=[]
    for i in mesh.Normals:
        normals.append(i)

    for i in range(len(mesh.Vertices)):
        repeated_vertices.append(rg.Point3d(mesh.Vertices[i]))
        temp_points.append(rg.Point3d(mesh.Vertices[i])+rg.Vector3d(normals[i]))
        
    return repeated_vertices

a=mesh_ex(mesh)


# then into this:
import Rhino.Geometry as rg

def mesh_ex(mesh,dist):
    temp_mesh=rg.Mesh()
    normals=[]
    repeated_vertices=[]

    for i in mesh.Normals:
        normals.append(rg.Vector3d(i)*dist)
    for i in range(len(mesh.Vertices)):
        temp_point=rg.Point3d(mesh.Vertices[i])+normals[i]
        repeated_vertices.append(temp_point)
        temp_mesh.Vertices.Add(temp_point)

    for i in range(len(mesh.Faces)):
        if mesh.Faces[i].IsQuad:
            vertice_index_1 = mesh.Faces[i].A
            vertice_index_2 = mesh.Faces[i].B
            vertice_index_3= mesh.Faces[i].C
            vertice_index_4= mesh.Faces[i].D
            
            point_1 = repeated_vertices[vertice_index_1]
            point_2 = repeated_vertices[vertice_index_2]
            point_3 = repeated_vertices[vertice_index_3]
            point_4 = repeated_vertices[vertice_index_4]
            
            mid_1 = (point_1+point_2)/2 
            mid_2 = (point_2+point_3)/2 
            mid_3 = (point_3+point_4)/2 
            mid_4 = (point_4+point_1)/2 
            mid_5 = (point_1+point_2+point_3+point_4)/4 
            mid_5 += rg.Vector3d(mesh.FaceNormals[i])*dist
            
#           adding mesh vertices to the temp_mesh
            vertice_1=temp_mesh.Vertices.Add(mid_1)
            vertice_2=temp_mesh.Vertices.Add(mid_2)
            vertice_3=temp_mesh.Vertices.Add(mid_3)
            vertice_3=temp_mesh.Vertices.Add(mid_4)
            vertice_4=temp_mesh.Vertices.Add(mid_5)
            
#           making faces from the vertices of the temp_mesh
            temp_mesh.Faces.AddFace(vertice_1,widx1,widx5,widx4)

    return vertice_1,vertice_2,vertice_3,vertice_4,vertice_5
a,b,c,d,e=mesh_ex(mesh,distance_factor_1)


# then: let's try to find out which ones are the desired vertices
import Rhino.Geometry as rg

def mesh_ex(mesh,dist):
    temp_mesh=rg.Mesh()
    normals=[]
    repeated_vertices=[]

    for i in mesh.Normals:
        normals.append(rg.Vector3d(i)*dist)
    for i in range(len(mesh.Vertices)):
        temp_point=rg.Point3d(mesh.Vertices[i])+normals[i]
        repeated_vertices.append(temp_point)
        temp_mesh.Vertices.Add(temp_point)

    for i in range(len(mesh.Faces)):
        if mesh.Faces[i].IsQuad:
            vertice_index_1 = mesh.Faces[i].A
            vertice_index_2 = mesh.Faces[i].B
            vertice_index_3= mesh.Faces[i].C
            vertice_index_4= mesh.Faces[i].D
            
            point_1 = repeated_vertices[vertice_index_1]
            point_2 = repeated_vertices[vertice_index_2]
            point_3 = repeated_vertices[vertice_index_3]
            point_4 = repeated_vertices[vertice_index_4]
            
            mid_1 = (point_1+point_2)/2 
            mid_2 = (point_2+point_3)/2 
            mid_3 = (point_3+point_4)/2 
            mid_4 = (point_4+point_1)/2 
            mid_5 = (point_1+point_2+point_3+point_4)/4 
            mid_5 += rg.Vector3d(mesh.FaceNormals[i])*dist
            
#           adding mesh vertices to the temp_mesh
            v1=temp_mesh.Vertices.Add(mid_1) #1
            v2=temp_mesh.Vertices.Add(mid_2) #2
            v3=temp_mesh.Vertices.Add(mid_3) #3
            v4=temp_mesh.Vertices.Add(mid_4) #4
            v5=temp_mesh.Vertices.Add(mid_5) #5
            
#           making faces from the vertices of the temp_mesh
            temp_mesh.Faces.AddFace(vertice_index_1,v1,v5,v4)
            temp_mesh.Faces.AddFace(vertice_index_2,v1,v5,v2)

    temp_mesh.Normals.ComputeNormals()

#    return mid_1,mid_2,mid_3,mid_4,mid_5
    return temp_mesh
#a,b,c,d,e=mesh_ex(mesh,distance_factor_1)
a=mesh_ex(mesh,distance_factor_1)



###########################
###########################
# then:
import Rhino.Geometry as rg


def mesh_ex(mesh,dist_1,dist_2,iter):
    temp_mesh=rg.Mesh()
    normals=[]
    repeated_vertices=[]

    for i in mesh.Normals:
        normals.append(rg.Vector3d(i)*dist_1)
    for i in range(len(mesh.Vertices)):
        temp_point=rg.Point3d(mesh.Vertices[i])+normals[i]
        repeated_vertices.append(temp_point)
        temp_mesh.Vertices.Add(temp_point)

    for i in range(len(mesh.Faces)):
        if mesh.Faces[i].IsQuad:
            vertice_index_1 = mesh.Faces[i].A
            vertice_index_2 = mesh.Faces[i].B
            vertice_index_3= mesh.Faces[i].C
            vertice_index_4= mesh.Faces[i].D
            
            point_1 = repeated_vertices[vertice_index_1]
            point_2 = repeated_vertices[vertice_index_2]
            point_3 = repeated_vertices[vertice_index_3]
            point_4 = repeated_vertices[vertice_index_4]
            
            mid_1 = (point_1+point_2)/2 
            mid_2 = (point_2+point_3)/2 
            mid_3 = (point_3+point_4)/2 
            mid_4 = (point_4+point_1)/2 
            mid_5 = (point_1+point_2+point_3+point_4)/4 
            mid_5 += rg.Vector3d(mesh.FaceNormals[i])*dist_2
            
#           adding mesh vertices to the temp_mesh
            v1=temp_mesh.Vertices.Add(mid_1) #1
            v2=temp_mesh.Vertices.Add(mid_2) #2
            v3=temp_mesh.Vertices.Add(mid_3) #3
            v4=temp_mesh.Vertices.Add(mid_4) #4
            v5=temp_mesh.Vertices.Add(mid_5) #5
            
#           making faces from the vertices of the temp_mesh
            temp_mesh.Faces.AddFace(vertice_index_1,v1,v5,v4)
            temp_mesh.Faces.AddFace(vertice_index_2,v2,v5,v1)
            temp_mesh.Faces.AddFace(vertice_index_3,v3,v5,v2)
            temp_mesh.Faces.AddFace(vertice_index_4,v4,v5,v3)

    temp_mesh.Normals.ComputeNormals()

    if iter>1:
        return mesh_ex(temp_mesh,dist_1,dist_2,iter-1)
    return temp_mesh

a=mesh_ex(mesh,distance_factor_1,distance_factor_2,iteration)