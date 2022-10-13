#

wzrost = float(input('ile masz wzrostu? [m]'))
masa = float(input("Ile ważysz? [kg]"))
bmi = masa / (wzrost ** 2)
print('Twoje BMI wynosi:', round(bmi, 2))

if bmi <18:
    print('Niedowaga')
elif bmi <=25:
    print('Waga prawidłowa')
elif bmi <=30:
    print('Nadwaga')
else:
    print('Otyłość')
