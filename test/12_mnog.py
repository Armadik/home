#1
chic = {1, 2, 3, 2, 1}
print(set(chic))
print(len(set(chic)))

#2
primer1 = {1, 2, 3, 45}
primer2 = {1, 4, 5, 45}
print(primer1.intersection(primer2))

#3
test1 = {1, 2, 3, 3, 3, 4, 5}
test3 = {1, 4, 5}
m_test1 = set(test1)
m_test3 = set(test3)
print(m_test3.issubset(m_test1))

