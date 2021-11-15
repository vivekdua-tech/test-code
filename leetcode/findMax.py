import json
import pdb
import os



"""
You are given as input an unsorted array of n distinct numbers, where n is a power of 2. 
Give an algorithm that identifies the second-largest number in the array, and that uses at 
most n + log 2n−2 comparisons.

You are a given a unimodal array of n distinct elements, meaning that its entries are in 
increasing order up until its maximum element, after which its elements are in decreasing order. 
Give an algorithm to compute the maximum element that runs in O(log n) time.

You are given a sorted (from smallest to largest) array A of n distinct integers which 
can be positive, negative, or zero. You want to decide whether or not there is an 
index i such that A[i] = i. Design the fastest algorithm that you can for solving 
this problem.

You are given an n by n grid of distinct numbers. A number is a local minimum if 
it is smaller than all of its neighbors. (A neighbor of a number is one immediately 
above, below, to the left, or the right. Most numbers have four neighbors; numbers 
on the side have three; the four corners have two.) Use the divide-and-conquer 
algorithm design paradigm to compute a local minimum with only O(n) comparisons 
between pairs of numbers. (Note: since there are n^2n 2
  numbers in the input, you cannot afford to look at all of them. 
  Hint: Think about what types of recurrences would give you the desired upper bound.)
"""
##
## Given a unimodal array[rising and then declining array] find the max element in O(logn) time
def findMax(lst):

    mid = len(lst)//2
    # base case
    if len(lst) == 1:
        return lst[0]
    if len(lst) >= 3 and lst[mid] >= lst[mid + 1] and lst[mid] >= lst[mid - 1]:
        return lst[mid]

    left = lst[:mid]
    right = lst[mid:]
    if lst[mid + 1] > lst[mid]:
        ## rising trend
        return findMax(lst[mid + 1:])
    else:
        return findMax(lst[:mid])


lst = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 16, 22, 9, 4]
print("the max is: ", findMax(lst))


