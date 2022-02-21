from math import prod


with open('inputs/digits.txt', 'r') as f:
    nums = ''
    for line in f:
        nums += line.strip()

p_size = 13
cur = 0
for i in range(0, len(nums)):

    number = [int(i) for i in nums[i:i+p_size]]

    product = prod(number)
    if product > cur:
        cur = product

    if len(number) != p_size:
        print(cur)
        break
