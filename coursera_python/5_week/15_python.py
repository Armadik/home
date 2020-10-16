numList = list(map(int, input().split()))
p = numList[0]
i = 0
for d in numList[1::]:
    if d <= p:
        i += 1

    p = d
if i > 0:
    print('NO')
else:
    print('YES')
