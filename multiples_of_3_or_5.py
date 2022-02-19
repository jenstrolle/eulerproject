n = 1000


def div(i, d):
    return (i % d == 0)


_ = 0

for i in range(n):
    if div(i, 3) or div(i, 5):
        _ += i

print(_)
