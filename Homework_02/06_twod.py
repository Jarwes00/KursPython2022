# Zapytaj użytkownika o numer od 1 do 100, jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl komunikat “gratulacje!”,
# w przeciwnym razie wyświetl “pudło!”.

x = 58
x_2 = int(input('podaj liczbę od 1 - 100 -> '))

if x == x_2:
    print("gratulacje")
else:
    print('pudło!')