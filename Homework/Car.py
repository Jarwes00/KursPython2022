#  Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.
#
# Program zacznie ze stworzonym słownikiem o trzech kluczach:
# marka (str)
#
# model (str)
#
# rocznik (int)
#
# Wypisze ten słownik na ekran (bez żadnego formatowania)
#
# Sprawdzi, czy samochód ma minimum 25 lat. Jeśli tak, wypisze komunikat:
# “Gratulacje! Twój samochód (tutaj_marka) może być zarejestrowany jako zabytek.”
#
# Jeśli nie spełnia powyższego warunku, wypisze komunikat:
# “Twój samochód (tutaj_marka) jest jeszcze zbyt młody.”
#
# Gdy program będzie poprawnie działał, pozmieniaj wartości słownika (ale nie klucze!), aby zobaczyć, czy progam również zmienia swoje zachowanie.

def car_info():
    user_marka = input('podaj nazwę marki -> ')
    auto['marka'].append(user_marka)
    user_model = input('podaj nazwę modelu -> ')
    auto['model'].append(user_model)
    user_rocznik = int(input('podaj rocznik -> '))
    auto['rocznik'].append(user_rocznik)

# pyta i wprowadza dane do słownika


def antyk():
    if auto['rocznik'][0] <= 25:
        print('Gratulacje! Twój samochód', auto['marka'][0], 'może być zarejestrowany jako zabytek')
    else:
        print('Twój samochód', auto['marka'][0], 'jest jeszcze zbyt młody')

# sprawdza, czy auto jest młode, czy stare


auto = {
    'marka': [],
    'model': [],
    'rocznik': [],
}
print('-' * 100)
print(auto)
print('-' * 100)


def main():
    while True:
        car_info()
        antyk()
        print('-' * 100)
        print(auto)
        print('-' * 100)


main()
