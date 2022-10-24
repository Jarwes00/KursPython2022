import random


def get_pattern(length):
    result = []
    for i in range(length-1):
        result.append(random.choice([True, False]))
    result.append(False)
    return result


nicknames = ['Waza', 'Niemrawy', 'Młody', 'Szybki', 'Bramkostrzelny', 'Plazmowy', 'Koktajlowy', 'Drewniany', 'Kapryśny']
numbers = ['I', 'II', 'III', 'MXL', 'LVII', 'MCMLXXVI', 'V', "LV", 'X', 'IV', 'L']
vowels = ['A', 'E', 'I', 'O', 'U']
consonant = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'X', 'Y', 'Z', 'W']

length = int(input("Specify length: "))
pattern = get_pattern(length)

result = ""
for i in pattern:
    if i:
        result += random.choice(vowels)
    else:
        result += random.choice(consonant)
result = result.capitalize() + ' ' + random.choice(numbers) + ' ' + random.choice(nicknames)
print(result)
