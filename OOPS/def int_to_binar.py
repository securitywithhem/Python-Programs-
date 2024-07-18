def int_to_binary(number):
    binary = ""
    lst = []
    while number > 0:
        binary = (number % 2) 
        number %= 2
        lst.append(binary)
        return binary
    print(lst)
    
number = int(input("Enter the number:  "))
print(int_to_binary(number))
