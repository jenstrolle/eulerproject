def primes(n):
    D = {}

    q = 2
    while n > 0:
        if q not in D:
            yield q
            D[q*q] = [q]
            n -= 1
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


if __name__ == '__main__':
    print(list(primes(10001)))
