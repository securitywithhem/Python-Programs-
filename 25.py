'''25.Write a program, to create a child class Teacher (name, age) that will inherit the properties of Parent class Staff (role, department, salary) ''' 
class Staff():
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
class Teacher(Staff):
    def __init__(self, name, age, role, department, salary):
        super().__init__(role, department, salary)
        self.name = name
        self.age = age
#Example
teacher = Teacher(name="Alice", age=30, role="Teacher", department="Math", salary=50000)
# Printing the attributes
print(f"Name: {teacher.name}")
print(f"Age: {teacher.age}")
print(f"Role: {teacher.role}")
print(f"Department: {teacher.department}")
print(f"Salary: {teacher.salary}")