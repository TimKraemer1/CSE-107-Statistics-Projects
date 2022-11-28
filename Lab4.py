import numpy as np
from random import randint

def print_help(type, matrix):
    print(type)
    print("     q:   0.1    0.2    0.3    0.4    0.5    0.6    0.7    0.8    0.9")
    print(" p   ---------------------------------------------------------------------------------")
    for i in range(len(matrix)):
        print(str((i+1)/10) + " |     ", end="")
        for j in range(len(matrix[0])):
            print('{:.3f}'.format(matrix[i][j]) + "  ", end="")
        print("")

def coin1_n(p):
    n = 1
    while(randint(1,10) > p*10):
        n += 1
    return n

def coin2_y(q, n):
    y = 0
    for _ in range(n):
        if(randint(1,10) <= q*10):
            y += 1
    return y

mean_matrix = np.empty([9,9])
for i in range(9):
    for j in range(9):
        mean_matrix[i][j] = 0

#initializations
p = q = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
n = 0
y = 0

for _ in range(10000):
    for i1, i2 in enumerate(p):
        for j1, j2 in enumerate(q):
            n = coin1_n(i2)
            y = coin2_y(j2, n)
            mean_matrix[i1][j1] += y
            y = 0
            n = 0
mean_matrix = mean_matrix / 10000

print_help("mean", mean_matrix)

