import numpy as np
import matplotlib.pyplot as plt

# BER Simulation
N = 500000  # Number of bits
EbN0dB_list = np.arange(0, 50)  # Eb/N0 values in dB
BER = []  # Bit Error Rate list

for i in range(len(EbN0dB_list)):
    EbN0dB = EbN0dB_list[i]
    EbN0 = 10 ** (EbN0dB / 10)  # Convert dB to linear scale
    x = 2 * (np.random.rand(N) >= 0.5) - 1  # BPSK symbols (-1 or +1)
    noise = 1 / np.sqrt(2 * EbN0)  # Noise standard deviation
    channel = x + np.random.randn(N) * noise  # Add AWGN noise
    received_x = 2 * (channel >= 0) - 1  # Demodulate (threshold at 0)
    errors = (x != received_x).sum()  # Count errors
    BER.append(errors / N)  # Calculate BER

# Plot BER vs Eb/N0
plt.plot(EbN0dB_list, BER, "-", EbN0dB_list, BER, "go")
plt.axis([0, 14, 1e-7, 0.1])
plt.xscale("linear")
plt.yscale("log")
plt.grid()
plt.xlabel("Eb/N0 in dB")
plt.ylabel("BER")
plt.title("BER in BPSK")
plt.show()
