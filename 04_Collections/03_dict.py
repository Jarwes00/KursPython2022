#Utwórz dowolną tablicę n x n zawierającą dowolny znak, a następnie wyświetl jej elementy w formie tabeli n x n.
# Elementy powinny być oddzielone spacją

n = int(input("podaj liczbę: "))

tab = [["-"] * n] * n

for row in tab:
    print(' '.join(row))


