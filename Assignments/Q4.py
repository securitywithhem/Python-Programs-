def find_divisors(n):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    return divisors

def find_prime_factors(n):
    i = 2
    prime_factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            prime_factors.append(i)
    if n > 1:
        prime_factors.append(n)
    return prime_factors


def find_co_primes(n):
    co_primes = []
    for i in range(1, n * 2):
        if gcd(i, n) == 1:
            co_primes.append(i)
        if len(co_primes) == 5:
            break
    return co_primes

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a



n = int(input("Enter the Number : "))
Divisors = find_divisors(n)
PrimeFactors = find_prime_factors(n)
CoPrimeNumbers = find_co_primes(n)

print(f'DIVISORS : {Divisors}')
print(f'PRIMEFACTORS : {PrimeFactors}')
print(f'CO-PRIME NUMBERS : {CoPrimeNumbers}')