"""
The goal of this problem is to implement the "Median Maintenance" algorithm (covered in the Week 3 lecture on heap applications).  The text file contains a list of the integers
from 1 to 10000 in unsorted order; you should treat this as a stream of numbers, arriving one by one.
Letting x_ix i denote the iith number of the file.

median_k = (k + 1)/2 smallest number among x1, x2,....xk. if k is odd
median_k = K/2 smallest number among x1. x2...xk if k is even.

compute : m1 + m2 + ... m10000) mod 10000

OPTIONAL EXERCISE: Compare the performance achieved by heap-based and search-tree-based implementations of the algorithm

https://realpython.com/python-heapq-module/

"""

import heapq
import functools

class Medianheap():

    def __init__(self):
        self.low = [] # max heap
        self.high = [] # min heap
        self.medianlist = []

    def insertlow(self, i):
        self.low.append(i)
        heapq._heapify_max(self.low)

    def inserthigh(self, i):
        self.high.append(i)
        heapq.heapify(self.high)

    def insert(self, i):

        if len(self.low) == 0:
            self.insertlow(i)
            return

        # Figure where should the int go to ?
        if i < self.low[0]:
            self.insertlow(i)
            if len(self.low) > len(self.high):
                item = heapq._heappop_max(self.low)
                self.inserthigh(item)
        else:
            self.inserthigh(i)
            if len(self.high) > len(self.low) + 1:
                item = heapq.heappop(self.high)
                self.insertlow(item)


    def getMedian(self):
        # if even then median is low[0]
        # if odd then median is  low[0] if len(low) > len(high)
        # if odd then median is high[0] if len(high) > len(low)
        if (len(self.low) == len(self.high) and
                (len(self.low) + len(self.high)) % 2 == 0):
            return self.low[0]
        elif len(self.low) == len(self.high) + 1:
            return self.low[0]
        elif len(self.high) == len(self.low) + 1:
            return self.high[0]
        else:
            print("heaps are imbalanced...")
            return 0


    def pushElements(self):
        medianlist = []
        with open("Median.txt") as f:
            lines = f.readlines()
            for line in lines:
                element = int(line.strip())
                self.insert(element)
                self.medianlist.append(self.getMedian())

    def getModulo(self):
        return sum(self.medianlist) % 10000

    def getMedianList(self):
        return self.medianlist



heap = Medianheap()
heap.pushElements()
print("Modulo is: ", heap.getModulo())
print(heap.getMedianList()[:10])



heap_low = None
heap_high = None


def MedianMaintenance_init():
    global heap_low, heap_high

    heap_low = []
    heap_high = []


def MedianMaintenance_insert(x):
    '''
    Maintains the median of a stream
    of numbers in 'real-time'
    using O(log(n)) time for each
    insert operation.

    (implementation via heaps)
    '''

    global heap_low, heap_high

    # heapq is a MIN-heap, so we need
    # to revert elements in heap_low
    # (which should be a MAX-heap).

    if (len(heap_low) == 0):
        heapq.heappush(heap_low, -x)
    else:
        m = -heap_low[0]
        if x > m:
            heapq.heappush(heap_high, x)
            if len(heap_high) > len(heap_low):
                y = heapq.heappop(heap_high)
                heapq.heappush(heap_low, -y)
        else:
            heapq.heappush(heap_low, -x)
            if len(heap_low) - len(heap_high) > 1:
                y = -heapq.heappop(heap_low)
                heapq.heappush(heap_high, y)

    return -heap_low[0]


def test():
    data = [1, 5, 2, 4, 3]

    MedianMaintenance_init()

    for x in data:
        print(MedianMaintenance_insert(x))



lines = open('Median.txt').read().splitlines()
data = map(lambda x: int(x), lines)
medians = []

MedianMaintenance_init()

for x in data:
    median = MedianMaintenance_insert(x)
    medians.append(median)

print(functools.reduce(lambda x, y: (x + y) % 10000, medians))
print(medians[:10])



"""
Filer, Map and Reduce functionality

>>> def f(x):
        return x % 2 != 0 and x % 3 != 0
>>> filter(f, range(2, 25))
[5, 7, 11, 13, 17, 19, 23]

>>> def cube(x):
        return x*x*x
>>> map(cube, range(1, 11))
[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

>>> def add(x,y):
        return x+y
>>> reduce(add, range(1, 11))
55


https://levelup.gitconnected.com/25-useful-python-one-liners-that-you-should-ec613df18260

"""



