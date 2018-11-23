from vertex import Vertex

class Graph:
    def __init__(self):
        self.vertexDictionary = {}
        self.numVertices = 0

    def displayDictionary(self):
        return self.vertexDictionary

    def __iter__(self):
        return iter(self.vertexDictionary.values())

    def addVertex(self, node):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(node)
        self.vertexDictionary[node] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertexDictionary:
            return self.vertexDictionary[n]
        else:
            return None
    
    def addEdge(self, frm, to, cost=0):
        ''' frm = the first unvisited node
           to = second unvisited node'''
        if frm not in self.vertexDictionary:
            self.addVertex(frm)
        if to not in self.vertexDictionary:
            self.addVertex(to)

        self.vertexDictionary[frm].addNeighbor(self.vertexDictionary[to], cost)
        self.vertexDictionary[to].addNeighbor(self.vertexDictionary[frm], cost)

    def getVertices(self):
        return self.vertexDictionary.keys()

    def setPrevious(self, current):
        self.previous = current

    def getPrevious(self, current):
        return self.previous

    def getEdgesMovie(self, G):
        edges = []
        for v in G:
            for w in v.getConnections():
                vid = v.getVertexID()
                wid = w.getVertexID()
                edges.append((vid, wid, v.getWeight(w)))
        return edges
