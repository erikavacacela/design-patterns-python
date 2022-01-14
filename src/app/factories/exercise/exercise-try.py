import unittest

class GeneradorId:
    index = 0

    @staticmethod
    def generate_index():
        GeneradorId.index = GeneradorId.index + 1
        return GeneradorId.index


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonFactory:

    def __init__(self):
        pass
    
    def create_person(self, name):
        id = GeneradorId.generate_index()
        return Person(id, name)


class TestPersonFactory(unittest.TestCase):

    def test_should_return_person_when_create_person_is_sucessfull(self):
        expected_name = 'Sebastian'

        actual_person = PersonFactory().create_person(expected_name)

        self.assertEqual(expected_name, actual_person.name)

    def test_should_return_index_asc_when_person_is_created(self):
        expected_person_one = 1
        expected_person_two = 2
        expected_person_three = 2

        actual_person_one = PersonFactory().create_person('Person one')
        actual_person_two = PersonFactory().create_person('Person two')
        actual_person_three = PersonFactory().create_person('Person three')

        self.assertEqual(expected_person_one, actual_person_one.id)
        self.assertEqual(expected_person_two, actual_person_two.id)
        self.assertEqual(expected_person_three, actual_person_three.id)
