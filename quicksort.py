"""
The file contains all of the integers between 1 and 10,000 (inclusive, with no repeats) in unsorted order.
The integer in the i^{th}i
th
  row of the file gives you the i^{th}i
th
  entry of an input array.

 Your task is to compute the total number of comparisons used to sort the given input file by QuickSort.  As you know, the number of comparisons depends on which elements are chosen as pivots, so we'll ask you to explore three different pivoting rules.

You should not count comparisons one-by-one.  Rather, when there is a recursive call on a subarray of length mm, you should simply add m-1m−1 to your running total of comparisons.  (This is because the pivot element is compared to each of the other m-1m−1 elements in the subarray in this recursive call.)

WARNING: The Partition subroutine can be implemented in several different ways, and different implementations can give you differing numbers of comparisons.  For this problem, you should implement the Partition subroutine exactly as it is described in the video lectures (otherwise you might get the wrong answer).

DIRECTIONS FOR THIS PROBLEM:

For the first part of the programming assignment, you should always use the first element of the array as the pivot element.

HOW TO GIVE US YOUR ANSWER:

Type the numeric answer in the space provided.

So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / other punctuation marks. You have 5 attempts to get the correct answer.

(We do not require you to submit your code, so feel free to use the programming language of your choice, just type the numeric answer in the following space.)


1 point
Enter answer here
2.
Question 2
GENERAL DIRECTIONS AND HOW TO GIVE US YOUR ANSWER:

See the first question.

DIRECTIONS FOR THIS PROBLEM:

Compute the number of comparisons (as in Problem 1), always using the final element of the given array as the pivot element.  Again, be sure to implement the Partition subroutine exactly as it is described in the video lectures.

Recall from the lectures that, just before the main Partition subroutine, you should exchange the pivot element (i.e., the last element) with the first element.


1 point
Enter answer here
3.
Question 3
GENERAL DIRECTIONS AND HOW TO GIVE US YOUR ANSWER:

See the first question.

DIRECTIONS FOR THIS PROBLEM:

Compute the number of comparisons (as in Problem 1), using the "median-of-three" pivot rule.  [The primary motivation behind this rule is to do a little bit of extra work to get much better performance on input arrays that are nearly sorted or reverse sorted.]  In more detail, you should choose the pivot as follows.  Consider the first, middle, and final elements of the given array.  (If the array has odd length it should be clear what the "middle" element is; for an array with even length 2k2k, use the k^{th}k
th
  element as the "middle" element. So for the array 4 5 6 7,  the "middle" element is the second one ---- 5 and not 6!)  Identify which of these three elements is the median (i.e., the one whose value is in between the other two), and use this as your pivot.  As discussed in the first and second parts of this programming assignment, be sure to implement Partition exactly as described in the video lectures (including exchanging the pivot element with the first element just before the main Partition subroutine).

EXAMPLE: For the input array 8 2 4 5 7 1 you would consider the first (8), middle (4), and last (1) elements; since 4 is the median of the set {1,4,8}, you would use 4 as your pivot element.

SUBTLE POINT: A careful analysis would keep track of the comparisons made in identifying the median of the three candidate elements.  You should NOT do this.  That is, as in the previous two problems, you should simply add m-1m−1 to your running total of comparisons every time you recurse on a subarray with length mm.


1 point
Enter answer here


"""

def  toarray():
    """ RETURN THE ARRAY given the file """
    array = []
    with open('/Users/vivekdua/PycharmProjects/pyclass/algorithms/QuickSort.txt') as f:
        lines = f.readlines()
        for line in lines:
            array.append(int(line))
    return array

def isSorted(l):
    return all(l[i] <= l[i+1] for i in range(len(l)-1))

def median_of_three(L, low, high):
    mid = low if (high - low) == 1 else (((high - low)//2) + low)
    a = L[low]
    b = L[mid]
    c = L[high]
    if a <= b <= c:
        return b, mid
    if c <= b <= a:
        return b, mid
    if a <= c <= b:
        return c, high
    if b <= c <= a:
        return c, high
    return a, low


def medianIndex(arr, low, mid, high):
    carr = []
    carr.append((arr[low], low))
    carr.append((arr[mid], mid))
    carr.append((arr[high], high))

    sortedArr = sorted(carr)
    return sortedArr[1][1]


def partitionLE(arr, low, high):
    """ last element as pivot"""
    #p = high
    #i = low
    #for j in range(low, high):
    #    if arr[j] < arr[p]:
    #        index1 = arr.index(arr[i])
    #        index2 = arr.index(arr[j])
    #        arr[index1], arr[index2] = arr[index2], arr[index1]
    #        i = i + 1
    ## swap the pivot with the first element of the bigger bucket
    #index1 = high
    #index2 = i
    #arr[index1], arr[index2] = arr[index2], arr[index1]
    #return i
    arr[low], arr[high] = arr[high], arr[low]
    return partitionFE(arr, low, high)


def partitionFE(arr, low, high):
    """ first element as pivot"""
    p = low
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] < arr[p]:
            index1 = arr.index(arr[i])
            index2 = arr.index(arr[j])
            arr[index1], arr[index2] = arr[index2], arr[index1]
            i = i + 1
    ## swap the pivot with the last element of the smaller bucket
    index1 = low
    index2 = i - 1
    arr[index1], arr[index2] = arr[index2], arr[index1]
    return i - 1


def partitionMedian(arr, low, high):
    """ median as the pivot"""
    """ [4, 9, 2, 1, 3, 6, 7]
         {4, 1, 7} -> 1 is the median - pick 1 as pivot
    """
    first = low
    last = high
    mid = low + (high - low)//2
    pIndex = medianIndex(arr, low, mid, high)
    #pivot, pIndex = median_of_three(arr, low, high)
    if pIndex == low:
        return partitionFE(arr, low, high)
    if pIndex == high:
        index1 = high
        index2 = low
        arr[index1], arr[index2] = arr[index2], arr[index1]
        return partitionFE(arr, low, high)
    if pIndex == mid:
        index1 = mid
        index2 = low
        arr[index1], arr[index2] = arr[index2], arr[index1]
        return partitionFE(arr, low, high)


def quickSort1(arr, low, high, comp):
    if low < high:
        comp += high - low
        pivotIndex = partitionFE(arr, low, high)
        comp = quickSort1(arr, low, pivotIndex - 1, comp)
        comp = quickSort1(arr, pivotIndex + 1, high, comp)
    return comp

def quickSort2(arr, low, high, comp):
    if low < high:
        comp += high - low
        pivotIndex = partitionLE(arr, low, high)
        comp = quickSort2(arr, low, pivotIndex - 1, comp)
        comp = quickSort2(arr, pivotIndex + 1, high, comp)
    return comp

def quickSort3(arr, low, high, comp):
    if low < high:
        comp += high - low
        pivotIndex = partitionMedian(arr, low, high)
        comp = quickSort3(arr, low, pivotIndex - 1, comp)
        comp = quickSort3(arr, pivotIndex + 1, high, comp)
    return comp


import sys
import numpy as np

sys.setrecursionlimit(10000)

#lst = toarray()
#comp = quickSort1(lst, 0, len(lst) - 1, 0)
#print("sorted: ", isSorted(lst))
##print("comparisons for FE  are: ", comp)
#lst = toarray()
#comp = quickSort2(lst, 0, len(lst) - 1, 0)
#print("sorted: ", isSorted(lst))
#print("comparisons for LE  are: ", comp)
lst = toarray()
#lst = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
comp = quickSort3(lst, 0, len(lst) - 1, 0)
print("sorted: ", isSorted(lst))
print("comparisons for ME  are: ", comp)

"""
/usr/local/bin/python3.9 /Users/vivekdua/PycharmProjects/pyclass/quicksort.py
sorted:  True
comparisons for FE  are:  162085
sorted:  True
comparisons for LE  are:  164123
sorted:  True
comparisons for ME  are:  159894
"""

## even_nums = [x for x in range(21) if x%2 == 0]



