from Location import *

class Node:
    def __init__(self, nPred, location, next, trail):
        self.nPred = nPred #int
        self.location = location #location
        self.next = next #Node
        self.trail = trail #SuccNode

class SuccNode:
    def __init__(self, succ, nextT, weight):
        self.succ = succ #Node
        self.nextT = nextT #SuccNode
        self.weight = weight #float

class Graph:
    def __init__(self, First):
        self.First = First #Node

    def SearchNode(self, loc):
        P = self.First
        while (P != None and (P.location.name != loc.name)):
            P = P.next 
        return P

    def SearchEdge(self, prec, succ): #SuccNode
        P = self.SearchNode(prec)
        if (P == None):
            return None
        T = P.trail 
        if (T == None):
            return None
        while (T.succ.location.name != succ and T.nextT != None):
            T = T.nextT
        if (T.succ.location.name != succ):
            return None 
        return T                    
            
    def InsertNode(self, location):
        Last = self.First
        
        P = Node(0, location, None, None)
        if (P != None):
            while (Last.next != None) :
                Last = Last.next
            Last.next = P
    
    def InsertEdge(self, source, destination):
        Pprec = self.SearchNode(source)
        Psucc = self.SearchNode(destination)

        weight = source.distance(destination)

        if (self.SearchEdge(source, destination) == None):
            T = Pprec.trail

            if (T == None):
                temp = SuccNode(Psucc, None, weight)
                Pprec.trail = temp
            else:
                while (T.nextT != None):
                    T = T.nextT 
                temp = SuccNode(Psucc, None, weight)
                T.nextT = temp
            Psucc.nPred += 1
        


    


