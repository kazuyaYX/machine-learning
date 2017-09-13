import numpy as np

a = np.random.random((1, 3))
k = np.random.random((3, 3))
b = np.tile(a, (3, 1))
print(a)
print(k)
print(b)