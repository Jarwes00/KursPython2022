import random


def print_word(word, chars):
    word_to_print = ''
    for char in word:
        if char in chars:
            word_to_print += char
        else:
            word_to_print += '_'
        word_to_print += " "
    print(word_to_print)


word_list = ['kasztan', 'maslo', 'ciagnik', 'chlebak', 'kapusta', 'sezam']


word = random.choice(word_list).upper()

word_set = set(word)
guessed_chars = set()
bad_guesses_left = 8
running = True
while running:
    guess = ''
    while len(guess) <= 0:
        guess = input('Give me a letter: ').upper()
    if len(guess) > 1:
        if guess.upper() == word.upper():
            print('Congratulation! You won!')
            running = False
        else:
            bad_guesses_left -= 1
            if bad_guesses_left <= 0:
                running = False
                print("Sorry, you lost!")
            else:
                print(f'Wrong answer, guesses left: {bad_guesses_left}.')
    else:
        if guess in word_set:
            guessed_chars.add(guess)
            print_word(word, guessed_chars)
            if word_set == guessed_chars:
                print('Congratulation! You won!')
                running = False
        else:
            bad_guesses_left -= 1
            if bad_guesses_left <= 0:
                running = False
                print("Sorry, you lost!")
            else:
                print(f"Word does not contain \'{guess}\', guesses left: {bad_guesses_left}.")


ff


