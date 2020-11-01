numList = list(map(int, input().split()))
numList2 = list(map(int, input().split()))
newList = []


def merge(A, B):
    for i in A:
        for d in B:
            if i == d:
                newList.append(i)
    return newList


print(*merge(numList, numList2))
