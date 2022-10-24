def print_word(word, guessed_chars):
    word_to_print = ''
    for char in word:
        if char in guessed_chars:
            word_to_print += char
        else:
            word_to_print += '_'
        word_to_print += " "
    print(word_to_print)


word = 'haslo'.upper()

word_set = set(word.upper())
guessed_chars = set()
bad_guesses_left = 5

while bad_guesses_left > 0 and word_set != guessed_chars:
    guess = ''
    while len(guess) <= 0:
        guess = input('Podaj litere: ').upper()
    if len(guess) > 1:
        if guess.upper() == word.upper():
            print('Wygrana!')
            break
        else:
            bad_guesses_left -= 1
            print(f'Błędne haslo, Pozostało {bad_guesses_left} prób')
    else:
        if guess in word_set:
            guessed_chars.add(guess)
            print_word(word, guessed_chars)
        else:
            bad_guesses_left -= 1

            print(f"Litera \'{guess}\' nie znajduje się w haśle")
            print(f'Pozostało {bad_guesses_left} prób')


