numList = list(map(int, input().split()))
m_deg = max(numList)
c = 0
p = 0

for d in numList:
    c += 1
    if d == m_deg:
        p = c

print(m_deg, p - 1)