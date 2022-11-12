# Rozpoznawanie kart. Utwórz plik zawierający numery kart kredytowych. Sprawdź dla każdej kart jej typ.
# Podziel kart do plików wg typów np. visa.txt, mastercard.txt, americanexpress.txt.

def can_be_card_number(number):
    if number.isnumeric() and 13 <= len(number) <= 16:
        return True
    else:
        print("Nie to nie jest numer karty :D")
        return False


def append_card(file_name, card_to_append):
    with open(file_name, "a+") as file_object:
        file_object.write(card_to_append)

def is_visa(numer):
    return True if numer[0] == '4' and len(numer) in [13, 16] else False


def is_mastercard(number):
    return True if len(number) == 16 and \
                   (51 <= int(number[0:2]) <= 55 or 2221 <= int(number[0:4]) <= 2720) else False


def is_american_express(number):
    return True if len(number) == 15 and number[0:2] in ['34', '37'] else False


def main():
    card = input("Podaj numer karty ->")
    if can_be_card_number(card):
        if is_visa(card):
            print("To jest karta Visa")
            append_card('visa.txt', card)
        elif is_mastercard(card):
            print("To jest MasterCard")
            append_card('mastercard.txt', card)
        elif is_american_express(card):
            print("To jest AmericanExpress")
            append_card('americanexpress.txt', card)
        else:
            print("Nie znany numer karty")


# --- main ----
main()
