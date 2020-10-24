numList = list(map(int, input().split()))
x = int(input())

index = 1
for i in numList:
    if i >= x:
        index += 1

print(index)
