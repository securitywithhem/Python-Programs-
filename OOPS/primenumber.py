# WAP to check whether the no. Is prime or not

number = int(input("Enter the number : "))
if(number%2!=0 or number%3!=0):
    print("A prime number")
else:
    print("Not a Prime number")