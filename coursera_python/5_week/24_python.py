numList = list(map(int, input().split()))
x = numList[0]

i = 1
for d in numList:
    if d != x:
        i += 1
    x = d

print(i)
