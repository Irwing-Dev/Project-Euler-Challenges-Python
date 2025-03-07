"""
n! means n x n(n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x 8 x ... x 3 x 2 x 1 = 3628800, and the sum of the digits in the number 10! is
                    
                    3 + 6 + 2 + 8 + 8 + 0 + 0 = 27 

Find the sum of the digits in the number 100!.
"""

# Code

def factorial_digit_sum(number: int):
    factorial = number

    while number > 1:
        number -= 1

        factorial *= number

    digits_of_factorial = [int(n) for n in str(factorial)]

    sum_of_the_digits = 0

    for i in digits_of_factorial:
        sum_of_the_digits += i
    
    return sum_of_the_digits

print(factorial_digit_sum(100))