n = int(input())
i = 1
d_max = 0
while n != 0:
    if n == 0:
        break
    elif n >= d_max:
        if n != d_max:
            i = 1
        d_max_old = d_max
        d_max = n
        if d_max == d_max_old:
            i += 1
    n = int(input())
print(i)
