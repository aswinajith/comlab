import numpy as np

x = 2001
y = bin(x)[2:]
n = np.array(y).astype(int)
print(n)