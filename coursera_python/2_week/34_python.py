old = int(input())
i_b = 0
max_b = 0
n = int(input())
while n != 0:
    if n > old or n < old:
        i_b += 1
        print(max_b, i_b)
        if max_b < i_b:
            max_b = i_b
    if n == old:
        i_b = 0
    old = n
    n = int(input())
    if n == 0:
        break
print(max_b)
