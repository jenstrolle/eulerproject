def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


_ = 0
i = 1

f = fib(40000)

for i in f:
    if i > 4000000:
        break

    if i % 2 == 0:
        _ += i

print(_)
