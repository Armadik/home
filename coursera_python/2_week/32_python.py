n = int(input())
i = 0
m = 0
while i != n:
    i += 1
    s_i = str(i)
    if s_i == s_i[::-1]:
        m += 1
print(m)
