# Dla podanej przez użytkownika liście liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.

numbers = []
print("gimme me 5 integers ")
for _ in range(5):
    num = int(input("give me a number"))
    numbers.append(num)
if numbers[0] == numbers[-1]:
    print("last and first are the same")
else:
    print("last and first are not the same")

# druga opcja

print(f'firstr and last item are the same { numbers[0] == numbers[-1]}')3