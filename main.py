import numpy as np
# В PyCharm, в File | Settings | Project: pythonProject | Python Interpreter добавить numpy
# Задание 2
def rotate(matrix):
    return np.rot90(matrix, k=-1)
m = 3
a = np.array([[10,11,12],
              [13,14,15],
              [16,17,18]])
print(f"Задание 2 \n {rotate(a)}\n")

# Задание 3
def sec(matrix):
    m = matrix.shape[0]
    mask = np.arange(m)[:, None] + np.arange(m) < m-1
    return matrix*mask
mm = 3
aa = np.array([[10,11,12],
              [13,14,15],
              [16,17,18]])
print(f"Задание 3 \n {sec(aa)}\n")

# Задание 4
def count_rows(matrix):
    first = set(matrix[0])
    count = 0
    for row in matrix:
        if set(row) == first:
            count += 1
    return count - 1
mmm, n=4, 5
aaa = np.array([[1,2,3,5,7],
              [7,5,3,2,1],
              [1,2,3,5,6],
              [7,5,3,3,2]])
print(f"Задание 4 \n {count_rows(aaa)}\n")

# Задание 5
def sorted_rows(matrix):
    sor = np.argsort(matrix[:,0])
    s = matrix[sor]
    return s
matrix = np.array([
    [5,2,4],
    [2,1,7],
    [3,1,8]
])
result = sorted_rows(matrix)
print(f"Задание 5 \n {result}\n")