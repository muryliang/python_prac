from queue import Queue

class Vertex:
    """this represent a vertex and vertexes connected to it"""

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = "white"
        self.prev = None
        self.discovery = 0
        self.finish = 0

    def setDiscovery(self, time):
        self.discovery = time

    def getDiscovery(self):
        return self.discovery

    def setFinish(self, time):
        self.finish = time

    def getFinish(self):
        return self.finish

    def getPrev(self):
        return self.prev

    def setPrev(self, prev):
        self.prev = prev

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)

        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def dfs(self, start, dest):
        self.getVertex(start).setPrev(None)
        q = Queue()
        q.enqueue(start)
        found = False
        while not q.isEmpty() and not found:
            name = q.dequeue()
            if name == dest:
                found = True
                break
            vetex = self.getVertex(name)
            for tmpv in vetex.getConnections():
                if tmpv.getColor() == "white":
                    tmpv.setColor("gray")
                    q.enqueue(tmpv.getId())
                    tmpv.setPrev(vetex)
            vetex.setColor("black")

        if found:
            print ("found")
            tmp = self.getVertex(dest)
            while tmp is not None:
                print (tmp.getId(), end=" -> ")
                tmp = tmp.getPrev()
        else:
            print ("not found")



if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    print (g.vertList)
    g.addEdge(0,1,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)
    for v in g:
        for w in v.getConnections():
            print ("(%s , %s)" %(v.getId(), w.getId()))
