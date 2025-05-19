class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def car_info(self):
        print(f"Car: {self.brand} {self.model}, come out Year: {self.year}")
        
my_car = Car("BMW", "X5", 2022)
my_car.car_info()       