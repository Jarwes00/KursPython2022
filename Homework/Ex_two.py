#Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.
#Zmodyfikuj skrypt tak, by przyjmował wartości od użytkownika.

distance = float(input('Proszę wpisać ilość kilometrów: [km]')
         )
Price = float(input('Proszę wpisać koszt benzyny [zł}')
         )
spalanie = float(input('Proszę wpisać jakie spalanie na 100km ma Pana/Pani auto. Np. [6.4]'))

result = float((Price * distance)/100 * (spalanie))

print('Cena za trase wynosi', round(result, 2)
      )