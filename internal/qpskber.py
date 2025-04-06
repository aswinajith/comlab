import numpy as np
import matplotlib.pyplot as plt
from numpy.random import standard_normal
N = 100000  
L = 20 
Fc = 10  
Fs = L * Fc  
ak = np.random.randint(2, size=2 * N)

I_bits = ak[0::2]  # Odd-indexed bits (In-phase component)
Q_bits = ak[1::2]  # Even-indexed bits (Quadrature component)

I_nrz = 2 * I_bits - 1
Q_nrz = 2 * Q_bits - 1
I_upsampled = np.repeat(I_nrz, L)
Q_upsampled = np.repeat(Q_nrz, L)

t = np.arange(start=0, stop=len(I_nrz) * L)
I_wave = I_upsampled * np.cos(2 * np.pi * Fc * t / Fs)
Q_wave = Q_upsampled * np.sin(2 * np.pi * Fc * t / Fs)
qpsk = I_wave + Q_wave

ebn0db = np.arange(start=-20, stop=11, step=2)  # SNR in dB
BER = np.zeros(len(ebn0db))

for i in range(len(ebn0db)):
    ebn0 = 10 ** (ebn0db[i] / 10)  # Convert dB to linear scale
    noiseamp = 1 / np.sqrt(2 * ebn0)  # Noise amplitude
    noise_I = noiseamp * standard_normal(len(I_wave)) 
    noise_Q = noiseamp * standard_normal(len(Q_wave)) 
    noisy_I = I_wave + noise_I  
    noisy_Q = Q_wave + noise_Q  

    # Demodulate received signals
    received_I = noisy_I * np.cos(2 * np.pi * Fc * t / Fs) 
    received_Q = noisy_Q * np.sin(2 * np.pi * Fc * t / Fs)
    demodulated_I = np.convolve(received_I, np.ones(L)) 
    demodulated_Q = np.convolve(received_Q, np.ones(L))
    demodulated_I = demodulated_I[L - 1:-1:L]  # Downsample
    demodulated_Q = demodulated_Q[L - 1:-1:L]
   
    detected_I = (demodulated_I > 0).astype(int)
    detected_Q = (demodulated_Q > 0).astype(int)

    detected = np.zeros(2 * N, dtype=int)
    detected[0::2] = detected_I
    detected[1::2] = detected_Q
    BER[i] = np.sum(ak != detected) / (2 * N)  

# Plot BER vs SNR
plt.figure()
plt.title("Error performance of QPSK")
plt.xlabel("SNR (dB)")
plt.ylabel("BER")
plt.semilogy(ebn0db, BER, marker='o', label="QPSK")
plt.grid(True,which='both')
plt.legend()
plt.show()
