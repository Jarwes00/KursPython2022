from random import choice

# Napisz dekorator stars zmieniający sposób wyświetlania cytatu
# na taki:
#
# *********************************
#             cytat
# *********************************


def stars(func_as):
    def nested():
        text = func_as()

        stars = '*' * 100

        final = stars + '\n ' + text.center(100) + '\n' + stars

        return final
    return nested

@stars
def get_quote():
    quotes = [
        "Be or not to be",
        "Life is a long lesson in humility.",
        "Whatever you are, be a good one",
        "Be yourself; everyone else is already taken.",
        "Happiness depends upon ourselves.",
    ]
    return choice(quotes)


def main():
    get_quote()


if __name__ == "__main__":
    main()

    #
    # def uppercase(func_as_param):
    #     def biggy():
    #         text = func_as_param()
    #         return text.upper()
    #
    #     return biggy
    #
    #
    # @uppercase
    # def get_string():
    #     return "eeeesdafasdf"
    #
    #
    # print(get_string())
