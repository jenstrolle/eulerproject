import math


def main():
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = math.sqrt(a**2 + b**2)
            if c.is_integer() and a+b+c == 1000.0:
                print(f'{a}**2 + {b}**2 = {c}**2')
                print(f'{a} + {b} + {c} = {a+b+c}')
                return a*b*c


if __name__ == "__main__":
    print(main())
