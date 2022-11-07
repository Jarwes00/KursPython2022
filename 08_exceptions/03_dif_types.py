#  Stwórz listę 10 elementową (różne typy!).
#  Pozwól użytkownikowi podać dowolny index.
#  Podziel 1 przez liczbę pod indexem wybranym przez użytkownika. Obsłuż błędy.

items = [12, 'string', 0, '23', int, print, True, (), {"key": 'klucz'}]



for i in items:
    try:
        index = int(input('Podaj dowolny idex -->'))
        wynik = 1 / items[index]
    except SyntaxError:
        print('Nie da się')
    except ZeroDivisionError:
        print('No chciałbym, ale nie')
    except NameError:
        print('nwm co sie dzieje, ale buja')
    except TypeError:
        print('Eszkere')
    except IndexError:
        print('Wyszedłeś poza', i)

