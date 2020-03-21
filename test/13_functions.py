def solve(s):
    ''' Функция solve(s) принимает список
        создает пустой список
        находит элементы с четным индексом (включая 0)
        заносит их в созданный список и возвращает его
    '''
    assert type(s) == list
    c = []
    for i in range(len(s)-1):
        if i == 0 or i%2 == 0:
            c.append(s[i])
    return c


test1 = (1, 2, 4, 4)
test3 = {"a": 1, "c": 3}
test2 = list('aasdas')
print(type(test2))
print(solve(test2))