

# user_value = input("Podaj liczbę od 1 do 100")
# if user_value.isdigit():
#     user_value = int(user_value)
# else:
#     user_value = 1
#
# number = user_value / 4
# print(f" Number = { number }")

def get_calc():
    try:
        num = int(input("podaj cyfre"))
        x = 5 / num
    except ZeroDivisionError : #as err
        raise ValueError('lol dzielisz przez 0 xD')
    return x


def main():
    try:
        x = get_calc()
    except ZeroDivisionError as err:
        print('wystapił błąd')
        print('nie dziel przez 0')
        print(err)
    finally: # Zadziała jako ostatnia
        print('hello')
    # except ValueError:
    #     print('błąd')
    #     print('Nie jest liczbą')
    print("bye bye") # Do tego momentu nie dojdzie, jeżeli wywali błąd


if __name__ == '__main__':
    main()