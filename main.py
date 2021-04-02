from Graph import *

def cariWeight(loc1, loc2):
    return (loc1.longitude + loc2.longitude + loc1.latitude + loc2.latitude)

Kubus = Location(3.0, 5.0, "Kubus")
simpangan1 = Location(4.0, 5.0, "Simpangan 1")
simpangan2 = Location(0.0, 0.0, "Simpangan 2")
simpangan3 = Location(0.0, 0.0, "Simpangan 3")

A = Node(0, Kubus, None, None)

graph = Graph(A)
graph.InsertNode(simpangan1)
graph.InsertNode(simpangan2)
graph.InsertNode(simpangan3)

weight1 = cariWeight(Kubus, simpangan1)
weight2 = cariWeight(Kubus, simpangan2)
weight3 = cariWeight(simpangan2, simpangan3)
weight4 = cariWeight(Kubus, simpangan3)

graph.InsertEdge(Kubus, simpangan1)
graph.InsertEdge(Kubus, simpangan2)
graph.InsertEdge(simpangan2, simpangan3)
graph.InsertEdge(Kubus, simpangan3)

#DEBUG
print(graph.First.location.name)

print(graph.SearchNode(Kubus).location.name)
print(graph.SearchNode(simpangan1).location.name)
print(graph.First.nPred)

TrailA = A.trail
while (TrailA != None):
    print(TrailA.weight)
    TrailA = TrailA.nextT

#Parameter SearchNode, InsertNode, InsertEdge: Location
