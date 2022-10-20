# Skorzystaj ze swojego kodu bmi.py.
# Rozbij liczenie bmi na funkcję obliczającą bmi na podstawie danych użytkownika oraz zwracającą odpowiednią wartość
# (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.




def calculate_bmi():
    wzrost = float(input('ile masz wzrostu? [m]'))
    masa = float(input("Ile ważysz? [kg]"))
    bmi = masa / (wzrost ** 2)
    print('Twoje BMI wynosi:', round(bmi, 2))
    return bmi


# ----------------

def get_bmi_state(bmi):
    if bmi < 18:
        return 'Niedowaga'
    elif bmi <= 25:
        return 'Waga prawidłowa'
    elif bmi <= 30:
        return 'Nadwaga'
    else:
        return 'Otyłość'

# main

result_bmi = calculate_bmi()
status = get_bmi_state(result_bmi)
print(status)