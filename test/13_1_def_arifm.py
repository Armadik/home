def myfunc(func, *args):
    return func(*args)


print(myfunc(lambda x, y: x*y, 3, 4))
print(myfunc(lambda x: x/100, 100))
print(myfunc(lambda x: x*x*x, 4))
print(myfunc(lambda x, y: x**y, 9, 3))

def my_func2(*args):
    try:
        result = eval(args[0])
    except SyntaxError:
        result = "Всё же самому нужно подумать"
    return result

