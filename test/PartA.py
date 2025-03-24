class House:
    def __init__(self, house_number, street, area , num_beds, price):
        self.house_number = house_number
        self.street = street
        self.area = area
        self.num_beds = num_beds
        self.price = price

    def house_info(self):
        print(f"House Number: {self.house_number}, Street name: {self.street}, Area: {self.area}, Num of Beds: {self.num_beds}, Price: {self.price}")

    def update_house_number(self, new_house_number):
        if isinstance(new_house_number, int):
            self.house_number = new_house_number
        else:
            print("Please refer to using numbers only")

    def update_street(self, new_street):
        if isinstance(new_street, str):
            self.street = new_street
        else:
            print("Please input an actual street name")

    def update_area(self, new_area):
        if isinstance(new_area, str):
            self.area =new_area
        else:
            print("Please input an area that exists")

    def update_num_beds(self, new_num_beds):
        if isinstance(new_num_beds, int):
            self.num_beds = new_num_beds
        else:
            print("PLEASE give an actual number of beds")

    def update_price(self,new_price):
        if isinstance(new_price, (int, float)):
            self.price = new_price
        else:
            print("Insert an actual number")


class RichHouse(House):
    def __init__(self, house_number, street, area, num_beds, price, pool, garage):
        super().__init__(house_number, street, area, num_beds, price)
        self.pool = pool
        self.garage = garage

    def house_info(self):
        super().house_info()
        print(f"Pool: {self.pool}, Garage size: {self.garage} cars")

    def update_pool(self, new_pool):
        if isinstance(new_pool, bool):
            self.pool = new_pool
        else:
            print("Invalid response")

    def update_garage(self, new_garage):
        if isinstance(new_garage, int):
            self.garage = new_garage
        else:
            print("Please input a valid amount of cars")

    
house1 = House(45, "Talbot Street", "Dublin 8", 2, 300000)
richhouse1 = RichHouse(89, "Dawson Street", "Dublin 1", 6, 950000, True, 5)

house1.house_info()
richhouse1.house_info()

house1.update_price(360000)
house1.update_num_beds(3)
richhouse1.update_pool(False)
richhouse1.update_garage(6)

house1.house_info()
richhouse1.house_info()
