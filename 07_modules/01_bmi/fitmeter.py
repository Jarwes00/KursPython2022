from bmi import calculate_bmi, get_bmi_state


def open_file(filename):
    with open(filename) as file:
        return file.readline()


def main():
        w = float(input('Give me your weight'))
        h = float(input('Give me your height'))

        bmi = calculate_bmi(w, h)

        status = get_bmi_state(bmi)
        print(status)
        advice = open_file(status + '.txt')
        print(advice)


if __name__ == '__main__':
    main()
