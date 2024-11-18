'''26.The Employee class represents an employee, either full-time or hourly. The Employee class should be an abstract class because there’re only full-time employees and hourly employees, no general employees exist.
a. The Employee class should have a property that returns the full name of an employee. In addition, it should have a method that calculates salary. The method for calculating salary should be an abstract method.
b. The FulltimeEmployee class inherits from the Employee class. It’ll provide the implementation for the get_salary() method.
c. The HourlyEmployee also inherits from the Employee class. However, hourly employees get paid by working hours and their rates. Therefore, you can initialize this information in the constructor of the class.
d. To calculate the salary for the hourly employees, you multiply the working hours and rates.'''
from abc import ABC, abstractmethod
class Employee(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @abstractmethod
    def get_salary(self):
        pass

class FulltimeEmployee(Employee):
    def __init__(self, first_name, last_name, annual_salary):
        super().__init__(first_name, last_name)
        self.annual_salary = annual_salary

    def get_salary(self):
        return self.annual_salary

class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, hours_worked, hourly_rate):
        super().__init__(first_name, last_name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def get_salary(self):
        return self.hours_worked * self.hourly_rate

# Main function
def main():
    # Create instances of full-time and hourly employees
    full_time_emp = FulltimeEmployee("John", "Doe", 60000)
    hourly_emp = HourlyEmployee("Jane", "Smith", 120, 20)

    # Display employee details and salaries
    print(f"Full-time Employee: {full_time_emp.full_name}")
    print(f"Salary: ${full_time_emp.get_salary()}\n")

    print(f"Hourly Employee: {hourly_emp.full_name}")
    print(f"Hours Worked: {hourly_emp.hours_worked}, Hourly Rate: ${hourly_emp.hourly_rate}")
    print(f"Salary: ${hourly_emp.get_salary()}")

if __name__ == "__main__":
    main()