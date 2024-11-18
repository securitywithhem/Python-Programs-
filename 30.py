'''30.Write a Python program to create a Vehicle class with max_speed and mileage instance attributes. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class. Create a Bus object that will inherit all of the variables and methods of the parent Vehicle class and display it. Create a Bus class that inherits
from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.'''

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    def display(self):
        print(f"Max Speed: {self.max_speed} km/h, Mileage: {self.mileage} km/l")
    def fare(self):
        capacity = self.seating_capacity()
        return capacity * 100

class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)
    def seating_capacity(self, capacity=50):
        return capacity
    def fare(self):
        default_fare = super().fare()
        maintenance_charge = default_fare * 0.1
        return default_fare + maintenance_charge

# Create a Bus object
bus = Bus(max_speed=120, mileage=15)
bus.display()
print(f"Seating Capacity: {bus.seating_capacity()}")
print(f"Total Fare for Bus: Rs.{bus.fare():.2f}")
