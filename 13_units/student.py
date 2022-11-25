class Student:
    min_avg = 4.5
    university = 'New York Academy'

    def __init__(self, name, last, age, student_avg, scholarship):
        self.name = name
        self.last = last
        self.age = age
        self.student_avg = student_avg
        self.scholarship = scholarship


    def __str__(self):
        return f'Student: {self.name.capitalize()} {self.last.capitalize()} - age: {self.age}'

    @property
    def email(self):
      return self.name + '.' + self.last + '@university.com'

    def grant_scholarship(self):
        if self.student_avg > self.min_avg:
            print('Przyznano stypendium')
            self.scholarship = True
        else:
            print('Odmowa przyznania stypendium')
            self.scholarship = False
    @property
    def fullname(self):
      return f"{self.name} {self.last}"

    @fullname.setter
    def fullname(self, first_last):
      self.name, self.last = first_last.split()

    @fullname.deleter
    def fullname(self):
      self.name = None
      self.last = None
      print("Dane usunięte")


student_anna = Student('asia', 'kowalska', 23)
print(student_anna)
print(student_anna.email)
student_anna.name = "joanna"
print(student_anna)
print(student_anna.email)

print(student_anna.fullname)
student_anna.fullname = "iga nowak"
print(student_anna)

del student_anna.fullname
print(student_anna.name, student_anna.last, student_anna.age)