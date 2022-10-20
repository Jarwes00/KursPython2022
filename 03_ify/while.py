price = 15
while price > 10:
    print(price, "$ - za drogo")
    price = price - 2
print(price, "$ super promocja!")

# źle

num = 3

while True:
    subject = input('podaj przedmiot')
    grade = input('podaj ocene')
    print(subject, ":", grade)
    num -= 1

