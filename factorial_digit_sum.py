fac = 1

for i in range(1, 101):
    fac *= i

print(sum([int(i) for i in str(fac)]))
