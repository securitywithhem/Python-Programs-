# Input data from keyboard in 1st 5 elements the last 5 elements must be  a[5]= count of odd Nos,a[6]= count of even nos,a[7]=sum of even nos,a[8]= sum of odd nos. ,a[9]= sum of 1st five.

numbers = []
for i in range(5):
    numbers.append(int(input("Enter the number: ")))
    print(numbers)


numbers_sum = sum(numbers)
odd_numbers = [i for i in numbers if (i%2!=0) ]
even_numbers = [i for i in numbers if i%2==0]

# print("Sum of all numbers is: ",numbers_sum)
# print("Sum of odd numbers is: ",sum(odd_numbers))
# print("Sum of even numbers is: ",sum(even_numbers))
# print("Count of odd numbers is: ",len(odd_numbers))
# print("Count of even numbers is: ",len(even_numbers))

count_of_oddnumbers = len(odd_numbers)
count_of_evennumbers = len(even_numbers)
sum_of_evennumbers = sum(even_numbers)
sum_of_oddnumbers = sum(odd_numbers)
sum_of_first_five = sum(numbers[:5])

numbers.append(count_of_oddnumbers)
numbers.append(count_of_evennumbers)
numbers.append(sum_of_evennumbers)
numbers.append(sum_of_oddnumbers)
numbers.append(sum_of_first_five)
print(numbers)