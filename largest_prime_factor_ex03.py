"""
The prime factors of 13295 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

def prime_factors(n):
    factors = []
    divider = 2
    while n > 1:
        while n % divider == 0:
            factors.append(divider)
            n //= divider
        divider += 1
    return factors

number = 600851475143
print(prime_factors(number))

# Output: 6857