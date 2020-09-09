now = int(input())
seqSum = 0
while now != 0:
    seqSum = seqSum + now
    now = int(input())
print(seqSum)


now = -1
while now != 0:
    now = int(input())
    if now <= 0:
        continue
    print(now)
