import unittest
from item import Item
from person import Person


class ItemTest(unittest.TestCase):
    def setUp(self):
        self.item=Item('0123','Calculator', 0.5, 25.96, False)

    def test_itemstring(self):
        self.assertEqual(str(self.item), '0123:Calculator;')

    def test_getitemprice(self):
        self.assertEqual(self.item.getitemPrice(), 25.96)

    def test_setitemName(self):
        self.item.setitemName('Calculator BAII Plus')
        self.assertEqual(self.item.getitemName(),'Calculator BAII Plus')

    def test_setitemRestricted(self):
        self.item.setitemRestricted(True)
        self.assertEqual(self.item.getitemRestricted(), True)


class PersonTest(unittest.TestCase):
    def setUp(self):
        self.person=Person('Do Couto','Marion','000-111-2233','000@gmail.com')

    def test_getLastName(self):
        self.assertEqual(self.person.getLastname(), 'Do Couto')

    def test_getEmail(self):
        self.assertEqual(self.person.getEmail(), '000@gmail.com')

    def test_setFirstName(self):
        self.person.setFirstname('Marlon')
        self.assertEqual(self.person.getFirstname(), 'Marlon')

    def test_setPhoneNumber(self):
        self.person.setPhonenumber('000-111-4455')
        self.assertEqual(self.person.getPhonenumber(),'000-111-4455')

    def person_stringtest(self):
        self.assertEqual(str(self.person),'This customer is Marlon Do Couto.')