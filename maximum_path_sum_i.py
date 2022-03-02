def main():
    with open('inputs/triangle_i.txt', 'r') as f:
        triangle = []

        for line in f:
            nums = [int(i) for i in line.strip().split(' ')]
            triangle.append(nums)

        triangle = triangle[::-1]

    for i, v in enumerate(triangle):
        current = v
        temp = current

        if i == 0:
            old = temp

        else:
            for j, v in enumerate(temp):
                temp[j] += max(old[j], old[j+1])

        old = temp

    return old


if __name__ == '__main__':
    print(main())
