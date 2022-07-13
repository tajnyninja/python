# Pierwiastek równiania kwadratowego

def roots(a, b, c):
    D = (b*b - 4*a*c) ** 0.5
    x_1 = (-b + D)/(2*a)
    x_2 = (-b - D)/(2*a)

    print('x1: {0}'.format(x_1))
    print('x2: {0}'.format(x_2))

if True:
    a = input('a: ')
    b = input('b: ')
    c = input('c: ')
    roots(float(a), float(b), float(c))

input()
