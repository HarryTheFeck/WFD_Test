class House:
    def __init__(self, house_number, street, area , num_beds, price):
        self.house_number = house_number
        self.streat = street
        self.area = area
        self.num_beds = num_beds
        self.price = price

    def house_info(self):
        print(f"House Number: {self.house_number}, Street name: {self.street}, Area: {self.area}, Num of Beds: {self.numb_beds}, Price: {self.price}")

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

    def update(self,new_price):
        if isinstance(new_price, (int, float)):
            self.price = new_price
        else:
            print("Insert an actual number")


    
