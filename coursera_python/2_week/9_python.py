a = int(input())
b = int(input())
c = int(input())

if a > b + c or b > c + a or c > a + b:
    print("impossible")
elif a*a == c*c+b*b or c*c == a*a+b*b or b*b == c*c+a*a:
    print('rectangular')
elif a * a < b * b + c * c or b * b < a * a + c * c or c * c < b * b + a * a:
    print('acute')
elif a * a > b * b + c * c or c * c > b * b + a * a or b * b > a * a + c * c:
    print('obtuse')
