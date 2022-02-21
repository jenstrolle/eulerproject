
def generate_triangle_nums():
    i = 1
    j = 0
    while True:
        j += i
        yield j
        i += 1


def find_divisors(n):
    for div in range(1, int(n**0.5) + 1):
        if n % div == 0:
            yield div
            other = n // div
            if other != div:
                yield other


if __name__ == '__main__':
    for i, t in enumerate(generate_triangle_nums()):
        d = list(find_divisors(t))
        if len(d) > 500:
            print(t, i, len(d))
            break
        else:
            print(t, i, len(d))
