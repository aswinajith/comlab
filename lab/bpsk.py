import numpy as np
import matplotlib.pyplot as plt

N = 10 
L = 16
Fc = 40
Fs = L * Fc
ak = np.random.randint(2, size = 2 * N)
print(ak)

nrz = ak*2 - 1
upsampled = np.repeat(nrz, L)
t = np.arange(0, len(nrz)*L)
car = np.cos(2 * np.pi * Fc * t / Fs)
bpsk = car * upsampled

plt.figure(figsize = (10,8))
plt.subplot(4, 1, 1)
plt.title("Message")
plt.plot(t,upsampled)
plt.subplot(4,1,2)
plt.title("Carrier")
plt.plot(t,car)
plt.subplot(4,1,3)
plt.title("BPSK")
plt.plot(t,bpsk)
plt.subplot(4,1,4)
plt.title("Constallation Diagram")
plt.plot(nrz, np.zeros(len(nrz)), 'ro')
plt.grid()
plt.tight_layout()
plt.show()

enrdb = np.arange(0,14,1)
N = 500000
BER = []
for i in range(len(enrdb)):
    enr = 10 ** (enrdb[i] / 10)
    noiseamp = 1/np.sqrt(enr*2)
    bpsk = 2 * (np.random.rand(N) >= 0.5) - 1
    noise = np.random.normal(0, noiseamp, N)
    bpsk_signal = bpsk + noise 
    print(bpsk_signal)
    detected_symbols = 2*( bpsk_signal >= 0)  -1 
    BER.append(np.sum(bpsk_signal != detected_symbols) / N)
    print(BER)

plt.figure(figsize = (10, 8))
plt.semilogy(enrdb, BER, marker = 'o', label = 'BER')
plt.xscale('linear')
plt.yscale('log')
plt.grid()
plt.legend()
plt.show()
