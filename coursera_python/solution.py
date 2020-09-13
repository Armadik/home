old = int(input())
i_b = 1
i_n = 1
max_b = 1
max_n = 1
n = int(input())
while n != 0:
    if n > old:
        i_b += 1
        if max_b < i_b:
            max_b = i_b
    elif n < old:
        i_n = 1
        if max_n < i_n:
            max_n = i_n
    if n == old:
        i_b = 1
        i_n = 1
    old = n
    n = int(input())
    if n == 0:
        break
if max_b >= max_n:
    print(max_b)
else:
    print(max_n)
