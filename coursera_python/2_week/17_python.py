now = int(input())
min_del = int(2)

while ((now/min_del) % 1) != 0:
    min_del = min_del + 1
print(min_del)