numList = list(map(int, input().split()))
p = int(input())
numList.pop(p)
print(*numList)
