import numpy as np

A = np.array([[10, 11, 12, 13],
              [20, 21, 22, 23],
              [30, 31, 32, 33],
              [40, 41, 42, 43]])

value_22 = A[1, 2]
second_column = A[:, 1]
sub_matrix = A[:2, 1:]
greater_equal_30 = A[A >= 30]

B = A.copy()
B[B % 2 == 0] = -1

print("A[1, 2]:", value_22)
print("第 2 欄:", second_column)
print("子矩陣:")
print(sub_matrix)
print(">= 30:", greater_equal_30)
print("A:")
print(A)
print("B:")
print(B)
