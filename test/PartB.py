import unittest
from PartA import House, RichHouse

class TestHouse(unittest.TestCase):
    def setUp(self):
        self.house = House(45, "Talbot STreet", "Dubin 8", 2, 300000)
        self.richhouse = RichHouse(89, "Dawson Street", "Dublin 1", 6, 950000, True, 5)

#B2

    def test_instance_of_house(self):
        self.assertIsInstance(self.house, House)

    def test_instance_of_richhouse(self):
        self.assertIsInstance(self.richhouse, RichHouse)


#B3

    

