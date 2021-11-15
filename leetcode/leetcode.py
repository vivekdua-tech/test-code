import json
import pdb
import os


# i - start index
# N - len of the list
def findMax(i, N, lst):
    if N == 1:
        compared = []
        compared.append(1)
        compared.append(lst[i])
        return compared

    mid = i + N//2
    compared1 = findMax(i, N//2, lst)
    compared2 = findMax(mid, N//2, lst)
    if compared1[1] > compared2[1]:
        k = compared1[0] + 1
        compared1[0] = k
        compared1.append(compared2[1])
        return compared1
    else:
        k = compared2[0] + 1
        compared2[0] = k
        compared2.append(compared1[1])
        return compared2

def findSecondMax(lst):
    compared = findMax(0, len(lst), lst)
    """ compared[0] is the len of the array
        compared[1] = max ( first element is the max)
        compared[2]...compared[k] are the numbers max got compared with
    """
    newLst = compared[2:]
    compared2 = findMax(0, len(newLst), newLst)
    return compared2[1]



lst = [2, 6, 9, 10, 34, 23, 21, 56]
findSecondMax(lst)

