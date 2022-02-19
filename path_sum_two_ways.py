import numpy as np


mat = []
f = open('inputs/matrix.txt', 'r')

for line in f:
    mat.append([int(i) for i in line.strip().split(',')])

m = np.array(mat)

diag_num = np.shape(m)[0]-1

for d in range(-diag_num, diag_num+1):
    current = np.fliplr(m).diagonal(d)
    temp = current
    temp.setflags(write=1)

    if d == -diag_num:
        old = temp

    elif d <= 0:
        for i, v in enumerate(temp):
            if i == 0:
                temp[i] += old[i]
            elif i == len(old):
                temp[i] += old[i-1]
            else:
                temp[i] += min(old[i-1], old[i])

    else:
        for i, v in enumerate(temp):
            temp[i] += min(old[i], old[i+1])
    old = temp

print(old)
