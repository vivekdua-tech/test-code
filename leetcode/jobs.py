
import heapq
from functools import cmp_to_key
import sys

class jobs():

    def __init__(self):
        # heap : KV: key : { weight and length } or list with tuples
        self.jobs = []
        self.ct = 0
        self.wct = 0
        # [(key, weight, len)]

    def compare(self, tup1, tup2):
        if tup1[0] > tup2[0]:
            return -1
        if tup1[0] < tup2[0]:
            return 1
        if tup1[1] > tup2[1]:
            return -1
        if tup1[1] < tup2[1]:
            return 1
        if tup1[2] < tup2[2]:
            return -1
        if tup1[2] > tup2[2]:
            return 1
        return 0


    def readFile(self):
        try:
            with open("jobs.txt") as f:
                lines = f.readlines()
                numjobs = int(lines[0].rstrip())
                print("the num jobsis: ", numjobs)
                for i in range(1, numjobs + 1):
                    weight = int(lines[i].rstrip().split(' ')[0])
                    len = int(lines[i].rstrip().split(' ')[1])
                    self.jobs.append((weight/len, weight, len))
            self.jobs = sorted(self.jobs, key = cmp_to_key(self.compare))
        except OSError:
            print('could not read file')
            sys.exit()

    def sum(self):
        for job in self.jobs:
            #print("diff: {} W: {} Len: {}".format(job[0], job[1], job[2]))
            self.ct += job[2]
            self.wct += job[1] * self.ct
        return self.wct


jobs = jobs()
jobs.readFile()

print(" the wct is: ", jobs.sum())



