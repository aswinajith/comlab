
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

# Function to simulate BPSK over AWGN
def bpsk_ber(snr_db):
    snr_linear = 10**(snr_db/10)  # Convert SNR from dB to linear scale
    return 0.5 * erfc(np.sqrt(snr_linear))

# Function to simulate QPSK over AWGN
def qpsk_ber(snr_db):
    snr_linear = 10**(snr_db/10)  # Convert SNR from dB to linear scale
    return  erfc(np.sqrt(snr_linear/2)) # QPSK has twice the spectral efficiency

# Define SNR range (in dB)
snr_range = np.arange(0, 10, 1)  # 0 to 10 dB

# Compute BER for BPSK and QPSK
ber_bpsk = [bpsk_ber(snr) for snr in snr_range]
ber_qpsk = [qpsk_ber(snr) for snr in snr_range]

# Plot results
plt.figure(figsize=(8, 6))
plt.semilogy(snr_range, ber_bpsk, 'bo-', label='BPSK')
plt.semilogy(snr_range, ber_qpsk, 'ro-', label='QPSK')

plt.xlabel('SNR (dB)')
plt.ylabel('Bit Error Rate (BER)')
plt.title('BER Performance of BPSK vs. QPSK in AWGN')
plt.legend()
plt.grid(True, which='both')
plt.show()
