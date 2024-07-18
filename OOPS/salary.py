# WAP to input emp id, name, basic salary, no. Of experience in years.... calculate HRA 35% of basic, BA 58% of basic, PF 9.5% of basic....also calculate bonus based on experience in yrs...if exp in yrs is >=30 bonus must be 59% of basic, if exp in yrs is >=23 bonus must be 51% of basic, if exp in yrs is >=15 bonus must be 45% of basic,
# If exp in yrs is >=7 bonus must be 33% of basic,  if exp in yrs is <7 bonus must be 16% of basic.....
# Calculate net salary=basic + ba+hra-pf+bonus

emp_id = int(input("Enter the employee Id : "))
emp_name = input("Enter the employee name : ")
basic_salary = int(input("Enter the basic salary : "))
no_of_experience = int(input("Enter the no. of experience in years : "))
hra = 0.35 * basic_salary
ba = 0.58 * basic_salary
pf = 0.095 * basic_salary
if no_of_experience >= 30:
    bonus = 0.59 * basic_salary
elif no_of_experience >= 23:
    bonus = 0.51 * basic_salary
elif no_of_experience >= 15:
    bonus = 0.45 * basic_salary
elif no_of_experience >= 7:
    bonus = 0.33 * basic_salary
elif no_of_experience < 7:
    bonus = 0.16 * basic_salary
net_salary = basic_salary + ba + hra - pf + bonus
print("Employee Id : ", emp_id)
print("Employee Name : ", emp_name)
print("Basic Salary : ", basic_salary)
print("No. of Experience : ", no_of_experience)
print("HRA : ", hra)
print("BA : ", ba)
print("PF : ", pf)
print("Bonus : ", bonus)
print("Net Salary : ", net_salary)

