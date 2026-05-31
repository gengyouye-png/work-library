import numpy as np

arr = np.arange(1, 101)

even_arr = arr[arr % 2 == 0]

matrix = arr.reshape(10, 10)

row_mean = matrix.mean(axis=1)

print("arr.shape:", arr.shape)
print("arr.dtype:", arr.dtype)
print("even_arr.size:", even_arr.size)
print("matrix.shape:", matrix.shape)
print("row_mean:", row_mean)


