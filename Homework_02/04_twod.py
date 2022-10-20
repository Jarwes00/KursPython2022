# Utwórz zmienną przechowującą dowolny ciąg znaków. Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
# Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

x = 'fddasajkl434aa'
x_1 = len(x)
if x_1 > 5:
    print(x.replace('a', 'z'))
else:
    print('nic')
