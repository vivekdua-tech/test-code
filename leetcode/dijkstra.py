from collections import defaultdict
import sys
import threading
import math
import re

class graph():

    def __init__(self):
        self.nodes = []
        self.edges = {}
        self.sp = {} # {2 : 34 , 4 : 35, 7 : 23 }
        self.x = []

    def loadGraph(self):
        edges = {}
        with open("dijkstraData.txt") as filename:
            lines = filename.readlines()
            for line in lines:
                line = line.rstrip()
                lst = list(line.split('\t'))
                node = int(lst[0])
                self.nodes.append(node)
                self.edges[node] = []
                for edge in lst[1:]:
                    edge = edge.rstrip()
                    destnode = int(edge.split(',')[0])
                    weight   = int(edge.split(',')[1])
                    self.edges[node].append((destnode, weight))

    def pickMinEdge(self):
        pc = {}
        for node in self.x:
            for w, weight in self.edges[node]:
                if w in self.x:
                    continue
                if self.sp[node] + weight < self.sp[w]:
                    pc[(node, w)] = self.sp[node] + weight
        return min(list(pc.items()), key = lambda x : x[1])[0]

    def findWeight(self, src, dst):
        for tup in self.edges[src]:
            if tup[0] == dst:
                return tup[1]


    def dijkstra(self):
        self.x.append(1)
        self.sp[1] = 0
        for node in self.nodes:
            if node != 1:
                self.sp[node] = math.inf
        while len(self.x) != len(self.nodes):
            tup = self.pickMinEdge()
            src = tup[0]
            dst = tup[1]
            weight = self.findWeight(src, dst)
            self.x.append(dst)
            self.sp[dst] = self.sp[src] + weight


    def readSp(self, nodes):
        returnLst = []
        for node in nodes:
            returnLst.append(self.sp[node])
        return returnLst

g = graph()
g.loadGraph()
g.dijkstra()
nodes = [7,37,59,82,99,115,133,165,188,197]
splist = g.readSp(nodes)
for i in splist:
    print(i, ",")
