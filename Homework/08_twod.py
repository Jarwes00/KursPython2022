# Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
# Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.

x = int(input('podaj dowolną liczbę 1 -> '))
x_2 = int(input('podaj dowolną liczbę 2 -> '))
x_3 = int(input('podaj dowolną liczbę 3 -> '))

x_final = [x, x_2, x_3]

x_final.sort()
print(x_final)
