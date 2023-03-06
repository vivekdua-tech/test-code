'''''''''''''''''''''''''''''''''''''''

import heapq
import functools
import sys
from collections import namedtuple

uf = namedtuple('uf', ['parent', 'rank'], defaults=[0,0])

class clusters():

    def __init__(self):
        # min-heap for edge cost (cost, src-node, dst-node)
        # parent/rank for each node {index: (parent, rank)}
        self.minheap = []
        self.unionfind = {}
        self.numnodes = 0
        self.numclusters = 0

    def insert(self, i):
        heapq.heappush(self.minheap, i)
        self.unionfind[i[1]] = uf(i[1], 0)
        self.unionfind[i[2]] = uf(i[2], 0)

    def pop(self):
        return heapq.heappop(self.minheap)

    def loadGraph(self):
        with open("cluster.txt") as filename:
            lines = filename.readlines()
            self.numnodes = int(lines[0].rstrip())
            self.numclusters = self.numnodes
            for i in range(1, self.numnodes + 1):
                src = int(lines[i].rstrip().split(' ')[0])
                dst = int(lines[i].rstrip().split(' ')[1])
                cost = int(lines[i].rstrip().split(' ')[2])
                self.insert((cost, src, dst))

    def find(self, i):
        if self.unionfind[i][0] != i:
            self.find(self.unionfind[i][0])
        return self.unionfind[i][0]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        try:
            if self.unionfind[xroot].rank > self.unionfind[yroot].rank:
                ufy = uf(xroot, self.unionfind[yroot].rank)
                self.unionfind[yroot] = ufy
            elif self.unionfind[yroot].rank > self.unionfind[xroot].rank:
                ufx = uf(yroot, self.unionfind[xroot].rank)
                self.unionfind[xroot] = ufx
            else:
                ufy = uf(xroot, self.unionfind[yroot].rank)
                ufx = uf(self.unionfind[xroot].parent,
                        self.unionfind[xroot].rank + 1)
                self.unionfind[yroot] = ufy
                self.unionfind[xroot] = ufx
        except AttributeError as e:
                print("yroot: {} xroot:{}".format(yroot, xroot))
                sys.exit(1)
        self.numclusters -= 1

    def cluster(self, num):

        while self.numclusters > num:
            # pick the min edge
            edge = self.pop()
            if self.find(edge[1]) != self.find(edge[2]):
                # merge
                self.union(edge[1], edge[2])

    def dump(self):
        x = self.pop()
        while x:
            print("cost:{}  src:{}  dst:{} ".format(x[0], x[1], x[2]))
            x = self.pop()


if __name__ == '__main__':
    cl = clusters()
    cl.loadGraph()
    cl.cluster(4)
    cl.dump()

'''''''''''''''''''''''''''''


f = open('cluster.txt', 'r')

graph = {}
f.readline()
ls = f.readline()
while ls:
    data = list(map(int, ls.split(' ')))
    graph[(data[0], data[1])] = data[2]
    ls = f.readline()
f.close()

g = graph.copy()

c = list(range(1, 501))
cnum = 500
while True:
    edge = min(g, key=g.get)
    d = g.pop(edge)
    l1, l2 = c[edge[0]-1], c[edge[1]-1]
    if l1 != l2 and cnum > 4:
        cnum -= 1
        for i in range(500):
            c[i] = l1 if c[i] == l2 else c[i]
    elif l1 != l2 and cnum == 4:
        print(edge, l1, l2, d)
        break
