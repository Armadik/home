numList = list(map(int, input().split()))
p = 10000000000000000
for d in numList:
    if d > p:
        print(d, end=' ')
    p = d