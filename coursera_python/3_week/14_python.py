string = str(input())
if string.count("f") == 1:
    print(-1)
elif string.count("f") == 0:
    print(-2)
else:
    premier = string.find("f")
    two = string[premier + 1::].find("f")
    print(premier + two + 1)
