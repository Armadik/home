numList = list(map(int, input().split()))
numList2 = list(map(int, input().split()))


def merge(A, B):
    return sorted(A + B)


print(*merge(numList, numList2))
