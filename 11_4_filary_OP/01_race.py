class Zwierzeta:
    heterotroph = True

    def __init__(self):
        print('zwirzeta')
    def chodzenie(self):
        print('chodzi')


class Ssaki(Zwierzeta):
    def __init__(self,):
        print('ssak')

    def rodzenie(self):
        print('nie jaja')


class Kot(Ssaki):
    def __init__(self):
        print('kot')

    def nazwa(self):
        print('jestem kotem')


class Pies(Ssaki):
    def __init__(self):
       print('pies')

    def nazwa(self):
        print('jestem psem')


class Czlowiek(Ssaki):
    def __init__(self):
        print('człowiek')

    def nazwa(self):
        print('jestem człowiekiem')


animal = Zwierzeta()
print(Zwierzeta.heterotroph)
print('-' * 10)
pies = Pies()
ssaki = Ssaki()
kot = Kot()
print(kot.heterotroph)
print('-' * 10)
czlowiek = Czlowiek()
czlowiek.rodzenie()
print('-' * 10)
czlowiek.chodzenie()
print(kot.rodzenie())