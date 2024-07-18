# WAP to display a set of prime no. Between the given input range from the user.

strating_number = int(input("Enter the STRAT number : "))
ending_number = int(input("Enter the END number : "))
print("Prime numbers between", strating_number, "and", ending_number, "are:")
for number in range(strating_number, ending_number + 1):
    if number > 1:
        for i in range(2, number):
            if (number%2!=0 or number%3!=0):
                break
            else:
                print(number, end=" ")



def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

primes = get_primes_in_range(start, end)

print("Prime numbers between", start, "and", end, "are:")
print(primes)
