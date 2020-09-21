v_a = str(input())
t = ''
for i in range(len(v_a)):
    if i % 3 != 0:
        t = t + v_a[i]
print(t)
