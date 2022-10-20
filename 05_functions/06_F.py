#  Nie korzystając z funkcji wbudowanej max(), napisz funkcję znajdującą maksymalną wartość z 3 liczb.
#  maximum_of(a, b, c).

def maximum_of(a, b, c):

    if a > b > c or a > c > b:
        return a
    elif b > c > a or b > a > c:
        return b
    else:
        return c


# main
a = int(input("podaj liczbę nr 1-."))
b = int(input("podaj liczbę nr 2-."))
c = int(input("podaj liczbę nr 3 -."))

result = maximum_of(a, b, c)
print(result)


# ___________________________
