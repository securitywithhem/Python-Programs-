'''28.Write a program to create a class Medicine which stores type of medicine, name of company, date of manufacturing. Class Tablet is inherited from Medicine. Tablet class has name of tablet, quantity per pack, price of one tablet as members. Class Syrup is also inherited from Medicine and it has quantity per bottle, dosage unit as members. Both the classes contain necessary member functions for input and output data. Write an OOP program that enters data for tablet and syrup, also display the data. Use the concepts of Multiple Inheritance.'''
class Medicine:
    def __init__(self, type_of_medicine, company_name, manufacturing_date):
        self.type_of_medicine = type_of_medicine
        self.company_name = company_name
        self.manufacturing_date = manufacturing_date
    def display_medicine_info(self):
        print(f"Type of Medicine: {self.type_of_medicine}")
        print(f"Company Name: {self.company_name}")
        print(f"Manufacturing Date: {self.manufacturing_date}")
class Tablet(Medicine):
    def __init__(self, type_of_medicine, company_name, manufacturing_date, tablet_name, quantity_per_pack, price_per_tablet):
        super().__init__(type_of_medicine, company_name, manufacturing_date)  # Calling parent class constructor
        self.tablet_name = tablet_name
        self.quantity_per_pack = quantity_per_pack
        self.price_per_tablet = price_per_tablet
    def display_tablet_info(self):
        # Display information specific to Tablet
        self.display_medicine_info()
        print(f"Tablet Name: {self.tablet_name}")
        print(f"Quantity per Pack: {self.quantity_per_pack}")
        print(f"Price per Tablet: {self.price_per_tablet}")
class Syrup(Medicine):
    def __init__(self, type_of_medicine, company_name, manufacturing_date, quantity_per_bottle, dosage_unit):
        super().__init__(type_of_medicine, company_name, manufacturing_date)  # Calling parent class constructor
        self.quantity_per_bottle = quantity_per_bottle
        self.dosage_unit = dosage_unit
    def display_syrup_info(self):
        # Display information specific to Syrup
        self.display_medicine_info()
        print(f"Quantity per Bottle: {self.quantity_per_bottle}")
        print(f"Dosage Unit: {self.dosage_unit}")
tablet = Tablet("Tablet", "PharmaCo", "2023-01-15", "PainRelief", 30, 2.5)
print("Tablet Information:")
tablet.display_tablet_info()
syrup = Syrup("Syrup", "MediHealth", "2023-03-10", 100, "10 ml")
print("Syrup Information:")
syrup.display_syrup_info()