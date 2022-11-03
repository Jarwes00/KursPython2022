def calculate_bmi(w, h):
    bmi = w / (h ** 2)
    print('BMI result:', round(bmi, 2))
    return bmi


def get_bmi_state(bmi):
    if bmi < 18:
        return 'underweight'
    elif bmi <= 25:
        return 'standard'
    elif bmi <= 30:
        return 'overweight'
    else:
        return 'obesity'


def main():
    result_bmi = calculate_bmi(+calculate_bmi())
    status = get_bmi_state(result_bmi)
    print(status)


if __name__ == '__main__':
    main()
