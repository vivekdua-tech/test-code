


def findSecondMax(lst):
    compared = findMax(0, len(lst), lst)
    """ compared[0] is the len of the array
        compared[1] = max ( first element is the max)
        compared[2]...compared[k] are the numbers max got compared with
    """
    compared2 = findMax(2, compared[0], compared[2:])
    return compared2[1]

# i - start index
# N - len of the list
def findMax(i, N, lst):
    if i == (N - 1):
        compared = []
        compared[0] = 1
        compared[1] = lst[i]
        return compared

    mid = i + (N - 1)//2
    compared1 = findMax(i, (N - 1)//2, lst)
    compared2 = findMax(mid + 1, (N - 1)//2, lst)
    if compared1[1] > compared2[1]:
        k = compared1[0] + 1
        compared1[0] = k
        compared1[k] = compared2[1]
        return compared1
    else:
        k = compared2[0] + 1
        compared2[0] = k
        compared2[k] = compared1[1]
        return compared2
