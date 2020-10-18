numList = list(map(int, input().split()))
if len(numList) < 2:
    numList += 0, 0
p = int(numList[0])
c = int(numList[1])
i = 0

for d in numList[2::]:
    if p < c > int(d):
        i += 1
    p = c
    c = d

print(i)
