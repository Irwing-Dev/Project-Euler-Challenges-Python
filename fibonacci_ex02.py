num = 1
sum = 0

while num < 1000:
    num += sum
    sum += num

    if num % 2 == 0 and num < 1000:
        print(num)
    if sum % 2 == 0 and num < 1000:
        print(sum)