def maximum_of():
    a = input(int("podaj liczbę nr 1-."))
    b = input(int("podaj liczbę nr 2-."))
    c = input(int("podaj liczbę nr 3 -."))
    if a > b > c:
        print('najwyższa to', a)
    elif b > c > a:
        print('najwyższa to', b)
    elif c > a > b:
        print('najwyższa to', c)