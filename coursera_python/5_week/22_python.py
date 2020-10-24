r = int(input())
numList = list(map(int, input().split()))
x = int(input())
for i in numList:
    if i == x:
        x = i
        break
else:
    if x < 0:
        x = 0
    else:
        x = max(numList)
print(x)