import numpy as np
import matplotlib.pyplot as plt

N = 10
L = 16
Fc = 40
Fs = L * Fc

ak = np.random.randint(2, size = 2 * N)

ibits = ak[0::2]
qbits = ak[1::2]

inrz = 2 * ibits -1
qnrz = 2 * qbits -1

iupsampled = np.repeat(inrz, L)
qupsampled = np.repeat(qnrz, L)

t = np.arange(0, len(inrz)*L)

iwave = iupsampled * np.cos(2 * np.pi * Fc * t / Fs)
qwave = qupsampled * np.sin(2 * np.pi * Fc * t / Fs)

qpsk = iwave + qwave

snrdb = 0.0001
normal = 10 ** snrdb/10
noise = 1/np.sqrt(2*normal)

iwave_noise = iwave + noise
qwave_noise = qwave + noise

qpsk_noise = iwave_noise + qwave_noise

plt.figure(figsize = (10, 8))

plt.subplot(5,1,1)
plt.title("QPSK Waveform")
plt.plot(t,qpsk)

plt.subplot(5,1,2)
plt.title("Constallation Diagram")
plt.plot(inrz, qnrz ,'ro',iwave_noise, qwave_noise, 'go')
plt.grid()

plt.subplot(5,1,3)
plt.title("In Phase component")
plt.plot(t, iupsampled)

plt.subplot(5,1,4)
plt.title("Quadrature Component")
plt.plot(t, qupsampled)

plt.subplot(5,1,5)
plt.title("qpsk noise")
plt.plot(t, qpsk_noise)


plt.tight_layout()
plt.show()
