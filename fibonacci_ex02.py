"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

                        1, 2, 3, 5, 8, 13, 21, 34, 55, 89,...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

# Code

seq = [0, 1]
sum = 0
for i in range(0, 34):
    seq.append(seq[-1] + seq[-2])
    if seq[i] % 2 == 0:
        sum += seq[i]

print(sum)

# Output: 4613732