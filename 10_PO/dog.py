# class Student:
#     def __init__(self, name, lastname, age, email):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.email = email
#
# student_A = Student("Anna", "kowalska", 23, 'anna@annowska.com')


class Pies:
    def __init__(self, imie, kolor_sierci, rasa):
        self.imie = imie
        self.kolor_sierci = kolor_sierci
        self.rasa = rasa

    def szczek(self):
        return "wuf wuf"

    def turlanie(self):
        return '*fikołek*'

    def łapa(self):
        return "*daje łade*"


tupet = Pies("Kacz", "niebieski", "border")
bubel = Pies("temple", "zółty", "Owczarek")


print(tupet.imie)
print(tupet.szczek())
print(bubel.łapa())
