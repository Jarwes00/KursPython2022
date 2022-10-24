# Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a może AmericanExpress

# All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
# MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720.
# All have 16 digits.
# American Express card numbers start with 34 or 37 and have 15 digits.




def can_be_card_number(number):
    if card.isnumeric() and 13<= len(card) <= 16:
        print('to karta')
        return True
    else:
        print('musi zawierać cyfry!')
        return False


def is_visa(numer):
    return True if numer[0] == '4' and len(numer) in [13, 16] else False


def is_mastercard(numer):
    return True if len(numer) == 16 and \
                   (51 <= int(numer[0:2]) <= 55 or 2221 <= int(numer[0:4]) <= 2720) else False


def is_american(numer):
    return True if len(numer) == 15 and numer[0:2] in ['34', '37'] else False


def main():
    card = (input('Podaj nazwe karty --> '))
    if can_be_card_number(card):
        if is_visa(card):
            print('To jest Visa')
        elif is_mastercard(card):
            print("To jest Mastercard")
        elif is_american():
            print("To jest american express")
        else:
            print('nieznany numer karty')


main()