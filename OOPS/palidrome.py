string1 = str(input("Enter the string : "))
string2 = string1[::-1]
if string1 == string2:
    print("The string is palindrome")
else:
    print("The string is not palindrome")