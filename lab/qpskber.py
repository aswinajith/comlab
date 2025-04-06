import numpy as np
import matplotlib.pyplot as plt

N = 100000
L = 16
Fc = 10 
Fs = L * Fc 
ak = np.random.randint(2 , size = 2 * N)

ibits = ak[0::2]
qbits = ak[1::2]

inrz = 2 * ibits - 1
qnrz = 2 * qbits - 1 

t = np.arange(0, len(inrz) * L)
iupsampled = np.repeat(inrz, L)
qupsampled = np.repeat(qnrz, L)

iwave = iupsampled * np.cos(2 * np.pi * Fc * t / Fs)
qwave = qupsampled * np.sin(2 * np.pi * Fc * t / Fs)

qpsk = iwave + qwave

ebn0db = np.arange(-20,11,2)
BER = np.zeros(len(ebn0db))

for i in range(len(ebn0db)):
    ebn0 = 10 ** (ebn0db[i] / 10)
    noiseamp = 1 / np.sqrt(2 * ebn0)
    noisei = noiseamp * np.random.standard_normal(len(iwave))
    noiseq = noiseamp * np.random.standard_normal(len(qwave))
    noisyi = iwave + noisei
    noisyq = qwave + noiseq

    receivedi = noisyi*np.cos(2 * np.pi * Fc * t / Fs)
    receivedq = noisyq*np.sin(2 * np.pi * Fc * t / Fs)
    demodulatedi = np.convolve(receivedi , np.ones(L))
    demodulatedq = np.convolve(receivedq , np.ones(L))

    demodulatedi = demodulatedi[L - 1: -1: L]
    demodulatedq = demodulatedq[L - 1: -1: L]

    detecti = (demodulatedi > 0).astype(int)
    detectq = (demodulatedq > 0).astype(int)

    detected = np.zeros(2 * N, dtype = int)
    detected[0::2] = detecti
    detected[1::2] = detectq
    BER[i] = np.sum(ak != detected) / (2 * N)

plt.figure()
plt.title("Error performance of BPSK")
plt.xlabel("SNR (db)")
plt.ylabel("BER")
plt.semilogy(ebn0db, BER, marker = "o", label = "QPSK")
plt.grid()
plt.legend()
plt.show()
