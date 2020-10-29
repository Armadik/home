numList = list(map(int, input().split()))
newList = []


def f(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]


for i in f(numList, 2):
    newList.append(i[::-1])

for d in newList:
    print(*d[0::], end=" ")
