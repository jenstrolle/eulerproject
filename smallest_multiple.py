def prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    return False


def primesFromList(li):
    return [v for v in li if prime(v)]


def findFactorPowers(li):
    out = [0 for i in range(len(li))]
    for i, p in enumerate(li):
        _p = p
        while _p <= max(li):
            out[i] += 1
            _p *= p

    return out


p = list(range(1, 21))

pr = primesFromList(p)

fac = findFactorPowers(pr)


nums = [p**pwr for p, pwr in list(zip(pr, fac))]

tot = 1
for n in nums:
    tot = tot*n
print(tot)
