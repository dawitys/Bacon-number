import time 
from graph import Graph
from que import Queue

def BFSTraversal(G, s, l):
    start = G.getVertex(s) #start node and its adjacents
    start.setDistance(0)
    distance = 0
    start.setPrevious(None)
    vertQueue = Queue()
    vertQueue.enQueue(start)

    while (not vertQueue.isEmpty()):
        currentVert = vertQueue.deQueue()
        currentVert.setVisited()
        for nbr in currentVert.getConnections():    # for each neiggbors of currenVert
            if (nbr.visited == False): #if it is unvisited
                nbr.setVisited() #mark it as it is on the same level
                nbr.setDistance(currentVert.getDistance() + 1) #dist + 1 since it is one level far from currentVert
                if(nbr.id.strip() == l.id.strip()): #if nbr is neighbor of currentVert
                    distance = nbr.getDistance() # get dist of the nbr from the startNode
                    print("Distance  between <<",s,">> and <<",l.id,">> is: ",distance)
                    break
                nbr.setPrevious(currentVert)
                vertQueue.enQueue(nbr)



    if(distance == 0):
                print("They do not work together.\n\tThere is(are) no actor(s) who work(s) with both")
    return distance

def BFS(G, s, l):
    if(G.getVertex(s) == None or G.getVertex(l) == None):
        print("Actors does not exist")
        return
    for v in G:
        if (v.getVertexID() == s):
            BFSTraversal(G, v.getVertexID(), G.getVertex(l))

def distance(graph,start,end):
    return BFS(graph,start,end)
#------------------------------FILE INPUT-----------------------------------#
t1=time.time()
def load_graph(filename):
    enterFile = open(filename,"r",encoding="utf-8")
    fileLines = enterFile.readlines()
    grph = Graph() #Graph object

    for i in fileLines:
        i.strip()
        if i[-1]=="\n":
            i=i[:-1]
        data_in_line = i.split("/") # List of film and actors participated on it

        # add actors in the graph as a node
        for j in range(1, len(data_in_line)):               #k[0] is title of the film
            if grph.getVertex(data_in_line[j]) == None:     #if it does not exist
                grph.addVertex(data_in_line[j])

        # add start actor and end actor in the graph as an edge and film title as a weight
        for p in range(1, len(data_in_line)):
            for m in range(p+1, len(data_in_line)): #start from where it stops to the last actor
                grph.addEdge(data_in_line[p], data_in_line[m], data_in_line[0])

    return grph

def main():
    gr=load_graph("casts.txt")
    distance(gr,"Bessey, Michael","Hedengren, David Finch")
    u = input("Enter the start actor (full name) separating with comma:\n\t>>> ")
    v = input("Enter the last actor (full name) separating with comma:\n\t>>> ")
    gr=load_graph("casts.txt")
    print(distance(gr, u, v))
  

main()
t2=time.time()
print(t2-t1)
