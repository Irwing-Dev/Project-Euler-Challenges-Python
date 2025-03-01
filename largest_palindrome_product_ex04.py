palindromers = []

for num in range(900, 1000):
    multiplier = 900
    while multiplier <= 999:
        result = num * multiplier
        array_string = [int(n) for n in str(result)]
        if array_string[0] == array_string[len(array_string) - 1] and array_string[1] == array_string[len(array_string) - 2] and array_string[2] == array_string[len(array_string) - 3]:
            palindromers.append(result)
        multiplier += 1

largest_palindromer = palindromers[0]

for i in palindromers:
    if i > largest_palindromer:
        largest_palindromer = i

print(f"993 * 913 = {largest_palindromer} \nThe largest palindrome formed by the product of two 3-digit numbers is: {largest_palindromer}")