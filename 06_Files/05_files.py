def get_words():
    filename = 'tekst.txt'
    with open(filename, encoding="utf-8") as file:
        word_list = file.read().split()

    return word_list

def find_longest(word):
    longest = ''
    for word in word:

        if len(word) > len(longest):
            longest = word
    return longest


def main():
    word_list = get_words()
    print(find_longest(word_list))

main()