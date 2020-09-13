n = int(input())
i = 0
old = n
m = 0
max_poc = 1
while n != 0:
    if n == 0:
        break
    if n == old:
        i += 1
        if max_poc <= i:
            max_poc = i
    elif n != old:
        i = 1
    old = n
    n = int(input())
print(max_poc)
