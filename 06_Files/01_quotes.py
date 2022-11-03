import random


def open_file():
    filename = input("Give name of file")
    with open(filename, encoding="utf-8") as file:
        return file.readlines()


def get_random_quote(list_of_quotes):
    return random.choice(list_of_quotes).strip()



def show(quote):
    print('quote of the day:\n')
    txt, author = quote.split(' -')
    print('*' * 100)
    print(txt.center(100))
    print(author.center(100))
    print('*' * 100)

def main():
    quotes = open_file()
    quote = get_random_quote(quotes)
    show(quote)


main()






