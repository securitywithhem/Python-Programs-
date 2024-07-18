# WAP to input costomer id, customer name, electricity unit charges used...... calculate electricity bill according to the given condition.....
# For the first 50 units ₹0.50 per unit.
# For the next 100 units ₹0.75 per unit.
# For the next 100 units ₹1.20 per unit.
# For unit above 250 ₹1.50 per unit 

# And additional surcharge of 20% is added to the bill.


customer_id = int(input("Enter the Id : "))
customer_name = input("Enter the name : ")
electricity_unit = int(input("Enter the electricity unit : "))
if electricity_unit <= 50:
    bill = electricity_unit * 0.50
elif electricity_unit <= 150:
    bill = (electricity_unit - 50)* 0.75 + 25
elif electricity_unit <= 250:
    bill = (electricity_unit - 150)* 1.20 + 100
else:
    bill = (electricity_unit - 250)* 1.50 + 220
bill = bill + (bill * 20/100)
print("Customer Id : ", customer_id)
print("Customer Name : ", customer_name)
print("Electricity Unit : ", electricity_unit)
print("Bill : ", bill)
