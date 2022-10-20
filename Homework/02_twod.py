# Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
# Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.

nr_one = int(input('Podaj dowolną liczbę nr 1 -> '))
nr_two = int(input('Podaj dowolną liczbę nr 2 -> '))
nr_both = (nr_one + nr_two)
if nr_both > 100:
    print(nr_both)
else:
    print('Koniec')