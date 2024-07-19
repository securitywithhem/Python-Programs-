# WAP to with list of 5 elements find the max. from the inputed nos without using library functions.

numbers = []
for i in range(5):
    numbers.append(int(input("Enter the Number : ")))
print(numbers)

max_number = numbers[0]

for num in numbers:
    if num > max_number:
        max_number = num

print("The maximum number is :", max_number)