import heapq

import functools

import sys

from collections import namedtuple

node = namedtuple('node', ['weight', 'numMerges', 'minMerges'])

class huffman():

    def __init__(self):
        # min-heap for weights
        self.minHeap = []
        self.numNodes = 0
        self.minMerges = sys.maxsize

    def insert(self, nodeTuple):
        heapq.heappush(self.minHeap, nodeTuple)

    def load(self):
        with open('huffman.txt') as filename:
            lines = filename.readlines()
            self.numNodes = int(lines[0].rstrip())
            for index in range(1, self.numNodes + 1):
                n = node(int(lines[index].rstrip()), 0, sys.maxsize)
                self.insert(n)

    def merge(self, n1, n2):
        return node(n1.weight + n2.weight, max(n1.numMerges, n2.numMerges) + 1,
                    min(n1.numMerges, n2.numMerges) + 1)

    def huffman(self):
        while len(self.minHeap) > 1:
            node1 = heapq.heappop(self.minHeap)
            node2 = heapq.heappop(self.minHeap)
            heapq.heappush(self.minHeap, self.merge(node1, node2))
        last = heapq.heappop(self.minHeap)
        return last.numMerges, last.minMerges




hm = huffman()
hm.load()
print("The max min is: {}".format(hm.huffman()))