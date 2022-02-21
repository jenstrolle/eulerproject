def collatz_len(n):
    i = 1
    while n != 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        i += 1
    return i


if __name__ == '__main__':
    best = 0
    for j in range(1, 1000001):
        cur = collatz_len(j)
        if cur > best:
            print(f'new best ({cur}) at: {j}')
            best = cur
