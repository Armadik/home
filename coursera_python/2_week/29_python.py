n = int(input())
i = 0
new_ch = n
while n != 0:
    if n == 0:
        break
    if n > new_ch:
        i += 1
    new_ch = n
    n = int(input())
print(i)
