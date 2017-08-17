from graph import Graph

class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPrev(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self, startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPrev(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

    def SCC(self, g):
        """ self is the transpose of graph
        g: the origin graph
        """

        vertexList = list(g.getVertices())
        vertexList.sort(key = lambda x:g.getVertex(x).getFinish(), reverse=True)
        mVertexList = list()
        for aVertex in vertexList:
            vertex = self.getVertex(aVertex)
            vertex.setColor('white')
            vertex.setPrev(-1)
            mVertexList.append(vertex)
        for aVertex in mVertexList:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

        scc = dict()
        for vtx in self:
            tmp = vtx
            while tmp.getPrev() != -1:
                tmp = tmp.getPrev()
            if scc.get(tmp.getId(), None) is None:
                scc[tmp.getId()] = list()
            scc[tmp.getId()].append(vtx)
        for key in scc.keys():
            print ("scc of %s len: %d is:"%(key, len(scc[key])), scc[key])

def dijkstra(g, start):
    for vertex in g.getVertices():
        g.getVertex(vertex).setDist(1000)
    g.getVertex(start).setDist(0)
    pq = PriorityQueue()
    pq.buildHeap([(v.getDist(), v) for v in g])
    while not pq.isEmpty():
        curmin = pq.delMin()
        for nextVertex in curmin.getConnections():
            newDist = curmin.getDist() + curmin.getWeight(nextVertex)
            if newDist < nextVertex.getDist():
                nextVertex.setPrev(curmin)
                nextVertex.setDist(newDist)
                pq.decreaseKey(nextVertex, newDist)


def prim(g, start):
    pq = PriorityQueue()
    for v in g:
        v.setDist(1000)
        v.setPrev(None)
    start.setDist(0)
    pq.buildHeap([(v.getDist(), v) for v in g])
    while not pq.isEmpty():
        curmin = pq.delMin()
        for nextVert in curmin.getConnections():
            newcost = newVert.getWeight()
            if nextVert in pq and newcost<nextVert.getDist():
                nextVert.setPrev(curmin)
                nextVert.setDist(newCost)
                pq.decreaseKey(nextVert, newCost)
