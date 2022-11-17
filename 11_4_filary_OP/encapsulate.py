class Accountant:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
        self.__account_number = '12 3456 1235 1234 1234 1234 1234'

    def show_number(self):
        print(f'your bank account number: {self.__account_number}')

use_account = Accountant('Join', "Sniow")

# można wejrzeć poprzez metode, ale bez niej nie ma szans dostać się do account_number

print(use_account.__account_number)
use_account.show_number()