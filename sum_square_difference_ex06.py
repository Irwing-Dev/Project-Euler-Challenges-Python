""""
The sum of the squares of the first ten natural numbers is,

                        1² + 2² + ... + 10² = 385

The square of the sum of the first ten natural numbers is,

                        (1 + 2 + ... + 10)² = 55² = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

# Code

def sum_of_the_squares():
    squares = []
    sum_sqaures = 0
    for i in range(1, 101):
        squares.append(i**2)
    for n in squares:
        sum_sqaures += n
    return sum_sqaures

def squares_of_the_sum():
    numbers = []
    sum_numbers = 0
    for i in range(1, 101):
        numbers.append(i)
    for n in numbers:
        sum_numbers += n
    return sum_numbers**2

difference = squares_of_the_sum() - sum_of_the_squares()

print(f"The square of the sum is: {squares_of_the_sum()} and the sum of the squares is: {sum_of_the_squares()} \nThe subtraction of them is: {difference}")

# Output: 25164150