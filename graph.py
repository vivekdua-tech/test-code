#!/usr/bin/python3

import sys
from collections import deque

# "Wash the dishes"==>"Have Lunch"
# "cook food"      ==>"Have Lunch"
# ..Order of tasks..
# IDEG: in-degree Number of tasks dependent on this tasks

#graph_tasks = { "wash the dishes" : ["have lunch"],
#                "cook food" : ["have lunch"],
#                "have lunch" : [],
#                "wash laundry" : ["dry laundry"],
#                "dry laundry" : ["fold laundry"],
#                "fold laundry" : [] }

# Dict having in-degree of all nodes - Init to '0'
# Iterate over the graph and get the in-degree of all nodes
# if IDEG is '0' then append to the Q
# While is not empty:
#   pop the first element with IDE zero
#   Add the element to the list<l>
#   for all nodes dependent on this node, reduce their IDEG by 1
#   If now, the IDEG is zero, all it to the Q
#   If the list is empty, there is cycle,
#   otherwise, the length of the list should be the len of the graph

def toposort(graph):
    in_degree = { u : 0 for u in graph }
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    Q = deque()
    for u in in_degree:
        if in_degree[u] == 0:
            Q.appendleft(u)
    L = [] #Empty list
    while Q:
        u = Q.pop()
        L.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                Q.appendleft(v)

    if len(L) == len(graph):
        return L
    else:
        return [] # Cycle
    
    
