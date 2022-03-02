import numpy as np


def lattice(n):
    mat = np.zeros((n+1, n+1))
    mat[0] = 1
    mat[:, 0] = 1
    for i in range(n):
        for j in range(n):
            mat[i+1, j+1] = mat[i, j+1] + mat[i+1, j]
    return mat[-1, -1]


if __name__ == '__main__':
    print(lattice(20))
