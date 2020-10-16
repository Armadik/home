numList = list(map(int, input().split()))
p = numList[0]

for d in numList[1::]:
    if d > 0 and p > 0:
        print(p, d)
        break
    elif d < 0 and p < 0:
        print(p, d)
        break
    p = d
