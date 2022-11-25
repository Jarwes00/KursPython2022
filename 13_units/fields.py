def check_values(*value):
    for item in value:
        if not isinstance(item, (int, float)):
            raise ValueError ("Bok musi być wartoscia numeryczna")


def square_area(a):
    check_values(a)
    return a*a


def rectangle_area(a, b):
    check_values(a, b)
    return a * b


def trapezoid_area(a, b, h):
    check_values(a, b, h)
    return (a+b)*h*0.5


def triangle_area(a, b):
    check_values(a, b)
    return a * b * 0.5
