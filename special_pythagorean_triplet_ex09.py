"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

                    a² + b² = c²

For example, 3² + 4² = 9 + 16 = 25 = 5², 3² + 4² = 5²

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc
"""

# Code

for a in range(1, 1000):
    for b in range(a + 1, 1000):
        c = (a ** 2 + b ** 2) ** 0.5
        if a + b + c == 1000:
            product_abc = a * b * c
            print(f"a = {a} \nb = {b} \nc = {int(c)} \na * b * c = {int(product_abc)}")
            break

# Output: 31875000