def is_perfect(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n

n = int(input("Enter the Number to check it is Perfect or not :  "))
print(is_perfect(n))