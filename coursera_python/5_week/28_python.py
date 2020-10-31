numList = list(map(int, input().split()))

for i in numList:
    if numList.count(i) == 1:
        print(i, end=" ")
