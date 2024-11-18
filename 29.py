'''29.Write a program to create class person having data member name and age. Create class company having data member company name and location. Derive child class Employee from class Person and Company having data member salary and skill. Create object of class Employee and display all the information'''
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class company:
    def __init__(self, companyname, location):
        self.companyname = companyname
        self.location = location
class Employee(person, company):
    def __init__(self, name, age, companyname, location, salary, skill):
        person.__init__(self, name, age)  # Call Person's __init__
        company.__init__(self, companyname, location)  # Call Company's __init__
        # super().__init__(name,age) #Throws Error
        # super().__init__(companyname,location)
        self.salary = salary
        self.skill = skill
    def display_employee(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Company Name: {self.companyname}")
        print(f"Location: {self.location}")
        print(f"Salary: {self.salary}")
        print(f"Skill: {self.skill}")
employee = Employee("John", 25, "ABC", "New York", 50000, "Python")
employee.display_employee()