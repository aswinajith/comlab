import numpy as np
import matplotlib.pyplot as plt

N = 10 
L = 16
Fc = 50 
Fs = L * Fc
ak = np.random.randint(2, size = 2 * N)

ibits= ak[0::2]
qbits= ak[1::2]

inrz = 2 * ibits - 1
qnrz = 2 * qbits - 1

t = np.arange( 0,  len(inrz) * L)

iupsampled = np.repeat(inrz, L)
qupsampled = np.repeat(qnrz, L)

iwave = iupsampled * np.cos(2 * np.pi * Fc * t/Fs)
qwave= qupsampled * np.sin(2 * np.pi * Fc * t/Fs)

qpsk = iwave + qwave

plt.figure(figsize = (10,8))
plt.subplot(4,1,1)
plt.title("Inphase component")
plt.plot(t,iupsampled)

plt.subplot(4,1,2)
plt.title("Quadarature component")
plt.plot(t,qupsampled)

plt.subplot(4, 1, 3)
plt.title("QPSK Wave")
plt.plot(t, qpsk)

plt.subplot(4,1,4)
plt.title("Constallation Diagram")
plt.plot(inrz, qnrz , 'ro')
plt.axhline(0, color = 'black', linewidth = '0.5', linestyle = '--')
plt.axvline(0, color = 'black', linewidth = '0.5', linestyle = '--')
plt.grid()
plt.tight_layout()
plt.show()
