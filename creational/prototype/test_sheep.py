from sheep import Sheep
import unittest


class TestSheep(unittest.TestCase):

    def setUp(self):
        self._sheep = Sheep('Dolly', 'Finn Dorset')

    def test_name_should_be_equal(self):
        cloned_sheep = self._sheep.clone()
        self.assertEqual(cloned_sheep.name, 'Dolly')

    def test_breed_should_be_equal(self):
        cloned_sheep = self._sheep.clone()
        self.assertEqual(cloned_sheep.breed, 'Finn Dorset')


if __name__ == '__main__':
    unittest.main()