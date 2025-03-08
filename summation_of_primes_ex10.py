"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17

Find the sum of all the primes below two million.
"""

# Code

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

limit = 2000000

primes = find_primes(limit)

result = 0

for s in primes:
    result += s

print(result)

# Output: 142913828922