one = int(input())
two = int(input())
tree = int(input())
if one >= two:
    if one >= tree:
        print(one)
    else:
        print(tree)
else:
    two >= one
    if two >= tree:
        print(two)
    else:
        tree >= one
        if tree >= two:
            print(tree)