# def decimal_to_binary(decimal_number):
#     if decimal_number == 0:
#         return "0"

#     is_negative = decimal_number < 0
#     decimal_number = abs(decimal_number)

#     integer_part = int(decimal_number)
#     fractional_part = decimal_number - integer_part

#     # Convert integer part to binary
#     integer_binary = bin(integer_part).replace("0b", "")

#     # Convert fractional part to binary
#     fractional_binary = []
#     while fractional_part:
#         fractional_part *= 2
#         bit = int(fractional_part)
#         fractional_binary.append(str(bit))
#         fractional_part -= bit

#         if len(fractional_binary) > 32:  # Limiting the precision to 32 bits
#             break

#     fractional_binary = ''.join(fractional_binary)

#     # Combine integer and fractional parts
#     if fractional_binary:
#         binary_representation = f"{integer_binary}.{fractional_binary}"
#     else:
#         binary_representation = integer_binary

#     if is_negative:
#         return f"-{binary_representation}"
#     else:
#         return binary_representation

# # Accept input from the user
# decimal_number = float(input("Enter a decimal number: "))
# binary_number = decimal_to_binary(decimal_number)
# print(f"Binary representation: {binary_number}")


# def binarytodecimal(binary):
#     return int(binary, 2)

# if __name__ == '__main__':
# #     print(binarytodecimal('100'))
# #     print(binarytodecimal('101'))
# #     print(binarytodecimal('1001'))


#     binary = input("Enter your binary Number : ")
#     decimal = binarytodecimal(binary)
#     print(f'DECIMALNUMBER : {decimal}')




def decimaltobinary(decimal):
    return bin(decimal).replace("0b","")
if __name__ == '__main__':
    decimal = int(input("Enter your Decimal Number : "))
    binary = decimaltobinary(decimal)
    print(f'BINARYNUMBER : {binary}')


def binary_to_octal():
    binary_num = input("Enter a positive binary number: ")
    
    # Check if the input is a valid binary number
    if not set(binary_num).issubset({'0', '1', '.'}):
        print("Invalid binary number. Please enter a number consisting of 0s, 1s, and an optional decimal point.")
        return
    
    # Split the binary number into integral and fractional parts
    parts = binary_num.split('.')
    
    # Convert the integral part to decimal
    integral_part = int(parts[0], 2)
    
    # Convert the fractional part to decimal
    fractional_part = 0
    if len(parts) > 1:
        fractional_part = sum([int(bit) * 2**(-i) for i, bit in enumerate(parts[1], start=1)])
    
    # Combine the integral and fractional parts to get the decimal number
    decimal_num = integral_part + fractional_part
    
    # Convert the decimal number to octal
    octal_num = oct(int(decimal_num)).replace("0o", "")
    
    print("The corresponding octal number is:", octal_num)

binary_to_octal()