# Stwórz krotkę liczb całkowitych. Poproś użytkownika o podanie dowolnej liczby.
# Jeśli liczba znajduje się na krotce wyswietl jej indeks.
#enumerate() podaje index i value w wpisie.

krotka = 23, 43, 14, 5, 2, 55
num = int(input("wpisz dowolną liczbę"))

for index in range(len(krotka)):
    if krotka[index] == num:
        print("index", index)



