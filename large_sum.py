with open('inputs/100_dig_sum.txt', 'r') as f:
    total = 0
    for line in f:
        total += int(line.strip())
    print(str(total)[:10])
