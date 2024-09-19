# Q1). Create a class named BankAccount with the following specifications:
# Private instance variable named cust_name and balance. A constructor that reads the value and saves them to instance variables.deposit() function that add the balance.

class BankAccount:
    def __init__(self, cust_name, balance):
        self.__cust_name = cust_name
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def get_balance(self):
        return self.__balance
    def get_cust_name(self):
        return self.__cust_name
    

costumer_name = input("Enter the name of the Acc Holder : ")
balance = float(input("Enter the balance : "))
account = BankAccount(costumer_name, balance)
print("Account created successfully")
print("Account Holder Name : ", account.get_cust_name())
print("Account Balance : ", account.get_balance())
amount = float(input("Enter the amount to deposit : "))
account.deposit(amount)
print("Account Balance after deposit : ", account.get_balance())