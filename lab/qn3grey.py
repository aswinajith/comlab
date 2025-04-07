#qn3
import numpy as np
import matplotlib.pyplot as plt
N = 10
L = 16
Fc = 40
Fs = L * Fc 

def binarytogrey(bynary):
    grey = []
    grey.append(int(bynary[0])) 
    for i in range(1,len(bynary)):
        grey.append(int(bynary[i-1]) ^ int(bynary[i]))
    return grey
inp = int(input("Enter the value: "))
binary = bin(inp)[2:]
grey = binarytogrey(binary)
grey.append(0)
grey = np.array(grey).astype(int)
ibits = grey[0::2]
qbits = grey[1::2]
ibits = np.array(ibits)
qbits = np.array(qbits)
inrz = 2 * ibits -1
qnrz = 2 * qbits -1

t = np.arange(0, len(inrz) * L)

iupsampled = np.repeat(inrz, L)
qupsampled = np.repeat(qnrz, L)

iwave = np.cos(2 * np.pi * Fc * t / Fs)
qwave = np.sin(2 * np.pi * Fc * t / Fs)

qpsk = iwave + qwave
print(qpsk)

plt.plot(inrz, qnrz, 'ro')
plt.grid()
plt.tight_layout()
plt.show()