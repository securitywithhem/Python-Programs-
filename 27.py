'''27.Write a program to create class vehicle with data member type of vehicle and engine no. Derive class Car from Vehicle having data member name of company. Derive class Sportscar from Car having data member called maneuverability. Create object of sports car and display all the information. Create another derived class from Vehicle class called Truck having data member loading capacity. Create object of class Car and Truck and display all the information.'''
class Vehicle():
    def __init__(self, type, engine_no):
        self.type = type
        self.engine_no = engine_no
    def display_vehicle(self):
        print(f"Type of Vehicle: {self.type}")
        print(f"Engine No: {self.engine_no}")
class Car(Vehicle):
    def __init__(self, type, engine_no, company_name):
        super().__init__(type, engine_no)
        self.company_name = company_name
    def display_car(self):
        print(f"Company Name: {self.company_name}")
class Sportscar(Car):
    def __init__(self, type, engine_no, company_name, maneuverability):
        super().__init__(type, engine_no, company_name)
        self.maneuverability = maneuverability
    def display_sportscar(self):
        print(f"Maneuverability: {self.maneuverability}")
class Truck(Vehicle):
    def __init__(self, type, engine_no, loading_capacity):
        super().__init__(type, engine_no)
        self.loading_capacity = loading_capacity
    def display_truck(self):
        print(f"Loading Capacity: {self.loading_capacity}")
sportscar = Sportscar("Sedan", "12345", "Toyota", "High")
sportscar.display_sportscar()
car = Car("Hatchback", "67890", "Honda")
car.display_car()
truck = Truck("Heavy-Duty", "54321", "15 Tons")
truck.display_truck()