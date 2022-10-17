# Utwórz 2 krotki.
# Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki,
# a oraz nieparzystych elementów z drugiej. Przekształć powstałą listę w set.

numbers = (1, 2, 3, 4, 2, 4, 1, 10)
letters = ('a', 'b', 'c', 'd', 'b', 'a',)

print(numbers[::2])
print(letters[1::2])

new_list = list(numbers[::2] + letters[1::2])

print(set(new_list))
