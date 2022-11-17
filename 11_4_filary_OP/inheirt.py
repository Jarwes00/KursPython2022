class Worker():
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def show_salary(self):
        print("Your salary is > 3000")


class Accountant(Worker):

    def billing(self):
        print("billing is")


bookkeeper = Accountant("John", "Snow")
print(bookkeeper.show_salary())

# smartwatch, watch, phone, useful