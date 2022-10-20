
def add_book():
    title = input('podaj tytuł książki')
    rate = int(input('podaj ocene książki'))
    list_book.append([title, rate])

list_book = []
for i in range(3):
    print("książka", i+1)
    add_book()
print(list_book)

# ---------------------------------------

def get_book():
    while True:
        numer = int(input("podaj numer ksiazki"))
        if 3 >= numer >= 1:
            print("tytul - ", list_book[numer - 1][0], "ocena - ", list_book[numer - 1][1])
            break
        else:
            print("numer nie istnieje")

get_book()
get_book()
