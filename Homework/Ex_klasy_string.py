# Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.

s1 = "maslo"
s2 = "maslane"

srodek = int(len(s1)/2
             )
s1_1 = s1[0:srodek]
s1_2 = s1[srodek:len(s1)]
s3 = s1_1 + s2 + s1_2
print(s3
      )
# Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
tytul = input(str(('Podaj tytuł ksiązki')
                        ))

strony = input('podaj liczbę stron'
               )
nazwisko = input(str('podaj nazwisko autora')
                 )
y = int(strony.isalpha()
        )
tytul_1 = tytul.replace(" ", ""
                        )
x = tytul_1.isalpha(
)
tytul_t = tytul.title(
)
nazwisko_t = nazwisko.title(
)
calosc = tytul + strony + nazwisko

print(x, y
      )
print(tytul_t, nazwisko_t
      )
print(tytul_t, nazwisko_t, strony
      )
print(len(calosc)
      )




