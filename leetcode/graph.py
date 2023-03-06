
from collections import defaultdict
import sys
import threading


class Graph:

    def __init__(self, vertex):
        self.numVertex = vertex
        self.graph = defaultdict(list)

    def add_edge(self, s, d):
        self.graph[s].append(d)

    def constructGraph(self):
        with open('./SCC.txt') as f:
            lines = f.readlines()
            for line in lines:
                src = int(line.split(' ')[0])
                dst = int(line.split(' ')[1])
                self.graph[src].append(dst)


    def DFS(self, visited, num, src):
        visited[src] = True
        if src in list(self.graph.keys()):
            dstList = self.graph[src]
            for dst in dstList:
                if visited[dst] is False:
                    self.DFS(visited, num, dst)
        num = num + 1

    def DFSOrder(self, src, visited, stack):
        visited[src] = True
        if src in list(self.graph.keys()):
            for i in self.graph[src]:
                if visited[i] is False:
                    self.DFSOrder(i, visited, stack)
        stack = stack.append(src)


    def reverseGraph(self):
        g = Graph(self.numVertex)

        for key in self.graph.keys():
            for j in self.graph[key]:
                g.add_edge(j, key)
        return g


    def printScc(self):
        stack = []

        visited = [False for i in range(1, self.numVertex + 1)]

        for i in range(self.numVertex):
            if i in self.graph.keys() and \
                    visited[i] is False:
                self.DFSOrder(i, visited, stack)

        reverseGraph = self.reverseGraph()

        visited = [False for i in range(1, self.numVertex + 1)]

        while len(stack):
            i = stack.pop()
            if visited[i] is False:
                num = 0
                reverseGraph.DFS(visited, num, i)
                print("numScc: ", num)



def main():
    g = Graph(875714)
    g.constructGraph()
    g.printScc()


if __name__ == '__main__':
    threading.stack_size(67108864)  # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target=main)  # instantiate thread object
    thread.start()  # run program at target






