from dfsgraph import DFSGraph

def knightGraph(bdSize):
    ktGraph = DFSGraph()

    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPosition = genLegalMoves(row, col, bdSize)
            for e in newPosition:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph

def posToNodeId(row, col, size):
    return (row * size) + col

def genLegalMoves(row, col, size):
    newMoves = []
    moveOffsets = [(-1,-2),(-1,2),(-2,-1),(-2,1),
                    (1,-2),(1,2),(2,-1),(2,1)]
    for i in moveOffsets:
        newX = row + i[0]
        newY = col + i[1]
        if legalCoord(newX,size) and legalCoord(newY, size):
            newMoves.append((newX, newY))
    return newMoves

def legalCoord(x, size):
    if x < 0 or x >= size:
        return False
    else:
        return True

def knightTour(n, path, u, limit):
    u.setColor('gray')
    path.append(u.getId())
    if len(path) < limit:
        nbrList = orderByAvail(u)
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == "white":
                done = knightTour(n, path, nbrList[i], limit)
            i += 1
        if not done:
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done

def orderByAvail(n):
    resList = []
    for v in n.getConnections():
        c = 0
        for w in v.getConnections():
            if w.getColor() == "white":
                c += 1
        resList.append((c, v))
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]


if __name__ == "__main__":
    k = 8
    g = knightGraph(k)
    path = list()
    g.dfs()
    g.SCC(g)
#    print (knightTour(0, path, g.getVertex(0), k**2))
#    print (path)
