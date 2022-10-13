#

fabula = int(input('podaj liczbe w skali od 1 - 10 na temat fabuły'))
okladka = int(input('podaj liczbe w skali od 1 - 10 na temat okladki'))
autor = int(input('podaj liczbe w skali od 1 - 10 na temat autora'))

calosc = (fabula + okladka + autor) / 3
if calosc > 7:
    print('bardzo dobre')
elif calosc >= 5:
    print('przecietna')
else:
    print('nie warta uwagi')