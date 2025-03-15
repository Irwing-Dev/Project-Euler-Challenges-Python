"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99

Find the largest palindrome made from the product of two 3-digit numbers.
"""

#Code

class Palindromer:
    def __init__(self, n, mult, res):
        self.n = n
        self.mult = mult
        self.res = res       

palindromers = []

for num in range(900, 1000):
    multiplier = 900
    while multiplier <= 999:
        result = num * multiplier
        array_string = [int(n) for n in str(result)]
        if array_string[0] == array_string[len(array_string) - 1] and array_string[1] == array_string[len(array_string) - 2] and array_string[2] == array_string[len(array_string) - 3]:
            palindromers.append(Palindromer(num, multiplier, result))
        multiplier += 1

largest_palindromer = palindromers[len(palindromers) - 1]

print(f"{largest_palindromer.n} * {largest_palindromer.mult} \nThe largest palindrome formed by the product of two 3-digit numbers is: {largest_palindromer.res}")

# Output: 906609