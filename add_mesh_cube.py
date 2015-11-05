import rhinoscriptsyntax as rs



def constructMeshBox(INPUTPNTS,SIZE):
    vertices = []
    vertices.append((0.0,0.0,0.0))
    vertices.append((SIZE, 0.0, 0.0))
    vertices.append((SIZE, SIZE, 0.0))
    vertices.append((0.0, SIZE, 0.0))
    vertices.append((0.0, 0.0, SIZE))
    vertices.append((SIZE, 0.0, SIZE))
    vertices.append((SIZE, SIZE, SIZE))
    vertices.append((0.0, SIZE, SIZE))
    faceVertices = []
    faceVertices.append((0,1,2,3))
    faceVertices.append((0,1,5,4))
    faceVertices.append((1,2,6,5))
    faceVertices.append((2,3,7,6))
    faceVertices.append((3,0,4,7))
    faceVertices.append((4,5,6,7))
    tempMesh = rs.AddMesh(vertices,faceVertices)

    for pt in INPUTPNTS:
        tempVec = rs.VectorCreate(pt,[0.5,0.5,0.5])
        rs.CopyObject(tempMesh,tempVec)

    rs.DeleteObject(tempMesh)
    
    
    
def main():
    rs.EnableRedraw(False)
    pnts = []
    strPnts = rs.GetObjects("please select pnts",rs.filter.point)
    for pnt in strPnts:
        pointCoord = rs.PointCoordinates(pnt)
        pnt = rs.VectorCreate(pointCoord,[0,0,0])
        pnts.append(pnt)
    constructMeshBox(pnts,0.75)
    rs.EnableRedraw(True)
        
main()        
rs.ObjectsByLayer()