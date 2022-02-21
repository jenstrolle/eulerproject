def primes():
    D = {}

    q = 2
    while True:
        if q not in D:
            yield q
            D[q*q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def sum_of_primes(n):
    total = 0
    for p in primes():
        if p > n:
            return total
        total += p


if __name__ == '__main__':
    print(sum_of_primes(2000000))
