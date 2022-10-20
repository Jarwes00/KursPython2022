# Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N
# (N podane przez użytkownika, ale nie większe niż 8).

x = int(input('podaj dowolną liczbę w zakresie od 0 do 8 ->'))
silnia = 1
if x < 8:
    for x in range(1, x+1):
        silnia = silnia * x
    print(silnia)
else:
    print('za dużo!')

