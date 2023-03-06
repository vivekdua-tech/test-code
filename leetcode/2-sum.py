

"""
 how many "t"s in the interval [-10000,10000]  that satisfy x+y=t with x, y in the hash table
"""

import functools
"""
https://medium.com/analytics-vidhya/bisect-module-in-python-6b78f8c37beb
"""
from bisect import bisect_left, bisect_right

class twoSum():

    def __init__(self):
        self.sum = {} # { key in the range -10000 and 10000 inclusive and value as either 0 or 1. }
        self.elementSet = set() # all elements in a set
        self.target_values = set()

    def readFile(self):

        with open("2sum.txt") as f:
            lines = f.readlines()
            for line in lines:
                self.elementSet.add(int(line.strip()))
        self.elementSet = sorted(self.elementSet)

    def compute2Sum(self):
            for element in self.elementSet:
                # get the left-range - element index and the right-range - element index
                #  ---|---------|---- Window means all elements in that window add to within the range of {lr, rr}
                low = bisect_left(self.elementSet, -10000 - element)
                high = bisect_right(self.elementSet, 10000 - element)
                for pair_element in self.elementSet[low:high]:
                    if pair_element != element:
                        self.target_values.add(element + pair_element)

    def result(self):
        return len(self.target_values)

    def test(self):
        for i in range(3, 11):
            self.sum[i] = 0
        elements = [-3, -1, 1, 2, 9, 11, 7, 6, 2]
        for i in elements:
            self.elementHash[i] = 1
        self.compute2Sum()



twoSum = twoSum()
#twoSum.test()
twoSum.readFile()
twoSum.compute2Sum()
print("sum is: " , twoSum.result())



