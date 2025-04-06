#BCD to XS-3
import numpy as np
import matplotlib.pyplot as plt

n=[1,9,2,2,3]
data=[]
for value in n:
    b=value+3
    a=bin(b)[2:].zfill(4)
    data.extend(np.array(list(map(int,a))))
print(data)
