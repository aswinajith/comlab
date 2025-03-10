import numpy as np  
import matplotlib.pyplot as plt  # for plotting functions

N = 10  
L = 16 
Fc = 40  # Carrier frequency
Fs = L * Fc  # Sampling frequency
ak = np.random.randint(2, size=2 * N)
print(ak)

I_bits = ak[0::2]  # Odd-indexed bits (in-phase)
Q_bits = ak[1::2]  # Even-indexed bits (quadrature)

I_nrz = 2 * I_bits - 1
Q_nrz = 2 * Q_bits - 1

I_upsampled = np.repeat(I_nrz, L)
Q_upsampled = np.repeat(Q_nrz, L)
t = np.arange(start=0, stop=len(I_nrz) * L)
I_wave = I_upsampled * np.cos(2 * np.pi * Fc * t / Fs)
Q_wave = Q_upsampled * np.sin(2 * np.pi * Fc * t / Fs)
qpsk = I_wave + Q_wave

plt.figure(figsize=(10, 8))
plt.subplot(4, 1, 1)
plt.title("In-Phase Component (I)")
plt.plot(t, I_upsampled)

plt.subplot(4, 1, 2)
plt.title("Quadrature Component (Q)")
plt.plot(t, Q_upsampled)

plt.subplot(4, 1, 3)
plt.title("QPSK Waveform")
plt.plot(t, qpsk)

# Plot constellation diagram
plt.subplot(4, 1, 4)
plt.title("Constellation Diagram")
plt.plot(I_bits, Q_bits, 'ro')  # Plot I vs. Q
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.grid()

plt.tight_layout()
plt.show()
