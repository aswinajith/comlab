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

EbN0dB= np.arange(0, 14, 1)
N = 500000
BER = []
for i in range(len(EbN0dB)):
    EbN0 = 10 ** (EbN0dB[i]/ 10)
    noiseamp = 1 / np.sqrt(2 * EbN0)
    bpsk_symbols = 2 * (np.random.rand(N) >= 0.5) - 1
    noise = np.random.normal(0, noiseamp, N)
    received_signal = bpsk_symbols + noise
    print(received_signal)
    detected_symbols = 2 * (received_signal >= 0) - 1
    BER.append(np.sum(bpsk_symbols != detected_symbols) / N)

plt.figure(figsize=(10, 6))
plt.semilogy(EbN0dB, BER, marker='o', label="BER")
plt.title("BER vs Eb/No for BPSK Modulation")
plt.xlabel("Eb/No (dB)")
plt.ylabel("Bit Error Rate (BER)")
plt.grid()
plt.legend()
plt.show()

