x = int(input())
y = int(input())
i = 1

while x < y:
    i = i + 1
    x = x + x / 10
print(i)
