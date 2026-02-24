class Vehicle:
    def __init__(self, vehicle_id, brand):
        self.vehicle_id = vehicle_id
        self.brand = brand
        print(self.vehicle_id, self.brand)

class Car(Vehicle):
    def calculate_rent(self, days, price_per_day):
        rent = days * price_per_day
        print("Car Rent:", rent)

class Bike(Vehicle):
    def calculate_rent(self, hours, price_per_hour):
        rent = hours * price_per_hour
        print("Bike Rent:", rent)

class Truck(Vehicle):
    def calculate_rent(self, kms, price_per_km):
        rent = kms * price_per_km
        print("Truck Rent:", rent)

c1 = Car(101, "Toyota")
b1 = Bike(201, "Honda")
t1 = Truck(301, "Tata")

c1.calculate_rent(3, 2000)
b1.calculate_rent(5, 100)
t1.calculate_rent(50, 30)