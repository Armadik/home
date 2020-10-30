numList = list(map(int, input().split()))

numList.insert(0, numList[-1])
numList.pop()
print(*numList)
