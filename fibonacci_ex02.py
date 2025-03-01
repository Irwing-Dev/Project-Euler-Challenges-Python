seq = [0, 1]
sum = 0
for i in range(0, 34):
    seq.append(seq[-1] + seq[-2])
    if seq[i] % 2 == 0:
        sum += seq[i]

print(sum)