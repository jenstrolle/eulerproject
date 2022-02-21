import numpy as np

with open('inputs/grid.txt', 'r') as f:
    mat = [[int(i) for i in line.strip().split(' ')] for line in f]

mat = np.array(mat)

count = 4

n, m = np.shape(mat)
best = 0
for i in range(n):
    for j in range(m-count+1):
        cur = np.prod(mat[i, j:j+count])
        if cur >= best:
            best = cur
            t = 'ud'
            out = mat[i, j:j+count]

for i in range(n-count+1):
    for j in range(m):
        cur = np.prod(mat[i:i+count, j])
        if cur >= best:
            best = cur
            t = 'lr'
            out = mat[i:i+count, j]

for d in range(-((n*2)-1), (n*2) - 1):
    diag = mat.diagonal(d)
    d_len = len(diag)
    print(diag)
    if d_len >= 4:
        for z in range(len(diag)-count+1):
            cur = np.prod(diag[z:z+count])
            if cur >= best:
                best = cur
                t = 'diagnormal'
                out = diag[z:z+count]
print(mat)

for d in range((n*2) - 1):
    diag = np.fliplr(mat).diagonal(d)
    d_len = len(diag)
    if d_len >= 4:
        for z in range(len(diag)-count+1):
            cur = np.prod(diag[z:z+count])
            if cur >= best:
                best = cur
                t = 'diagother'
                out = diag[z:z+count]

print(best, t, out)
