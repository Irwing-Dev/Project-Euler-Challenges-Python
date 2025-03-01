number_init = 10000 # 100 * 100
number_end = 998001 # 999 * 999

two_digits_init = 100
two_digits_end = 9801

palindromers = []

for num in range(two_digits_init, two_digits_end):
    array_string = [int(dig) for dig in str(num)]
    if len(array_string) == 4:
        if array_string[0] == array_string[len(array_string) - 1] and array_string[1] == array_string[len(array_string) - 2] and array_string[2] == array_string[len(array_string) - 3]:            
            if num % 91 == 0:
                palindromers.append(num)

print(palindromers[0], len(palindromers))

print(palindromers[len(palindromers) - 1])
# print(palindromers[0] / 11) == 9091