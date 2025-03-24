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
    def test_no_instance_of_richhouse(self):
        self.assertNotIsInstance(self.house, RichHouse)
    
    def test_no_instance_of_house(self):
        self.assertNotIsInstance(self.richhouse, House)

#B4

    def test_objects_are_not_identical(self):
        house2 = House(45, "Talbot Street", "Dublin 8", 2, 300000)
        self.assertIsNot(self.house, house2)
    
    def test_objects_are_identical(self):
        same_house = self.house
        self.assertIs(self.house, same_house)

#B5

    def test_update_house_number(self):
        self.house.update_house_number(50)
        self.assertEqual(self.house.house_number, 50)
    
    def test_update_street(self):
        self.house.update_street("Grafton Street")
        self.assertEqual(self.house.street, "Grafton Street")
    
    def test_update_area(self):
        self.house.update_area("Dublin 2")
        self.assertEqual(self.house.area, "Dublin 2")
    
    def test_update_num_beds(self):
        self.house.update_num_beds(3)
        self.assertEqual(self.house.num_beds, 3)
    
    def test_update_price(self):
        self.house.update_price(360000)
        self.assertEqual(self.house.price, 360000)
    
    def test_update_pool(self):
        self.richhouse.update_pool(False)
        self.assertFalse(self.richhouse.pool)
    
    def test_update_garage(self):
        self.richhouse.update_garage(6)
        self.assertEqual(self.richhouse.garage, 6)

# B6
if __name__ == "__main__":
    unittest.main()
