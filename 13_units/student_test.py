import unittest
from student import Student


class TestStudent(unittest.TestCase):
    def test_fullname_change(self):
        stA = Student('Anna', 'Smith', 4.6)
        self.assertEqual(stA.fullname, 'Anna Smith')

        stA.last = 'Married'
        self.assertEqual(stA.fullname, 'Anna Married')

    def test_grand_scholarship(self):
        granted = Student('anna', 'smith', 4.6, None)
        ungranted = Student('John', 'snow', 3.6, None)

        granted.grant_scholarship()
        self.assertEqual(granted.scholarship, True)