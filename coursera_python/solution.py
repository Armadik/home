numList = list(map(int, input().split()))
p = numList[0]
for d in numList:
    if d > p:
        print(d, end=' ')
    p = d
