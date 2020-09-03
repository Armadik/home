now = int(input())
nowMin = now
while now != 0:
    if now < nowMin:
        nowMin = now
    now = int(input())
print(nowMin)

i = 1
while True:
    print(i)
    i = i + 1
    if i > 100:
        break
