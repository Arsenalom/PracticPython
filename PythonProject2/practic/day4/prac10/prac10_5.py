import unittest


class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self,age):
        if age <0:
            raise ValueError("возраст не может быть ")
        self.__age = age

class TestPerson(unittest.TestCase):
    def test_initialization(self):
        p = Person("gg",25)
        self.assertEqual(p.get_name(),"gg")
        self.assertEqual(p.get_age(), 25)

    def test_set_name(self):
        p = Person("Grigory", 22)
        p.set_name("Nol")
        self.assertEqual(p.get_name(), "Nol")

    def test_set_age_valid(self):
        p = Person("Antosha", 28)
        p.set_age(21)
        self.assertEqual(p.get_age(), 21)

    def test_set_age_invalid(self):
        p = Person("Kirill", 23)
        with self.assertRaises(ValueError):
            p.set_age(-5)

    def test_set_name_after(self):
        p = Person("IvanZolo2004", 22)
        p.set_name("Skynet")
        self.assertEqual(p.get_name(), "Skynet")

    def test_set_age_after(self):
        p = Person("JOJO", 17)
        p.set_age(56)
        self.assertEqual(p.get_age(), 56)