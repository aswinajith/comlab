#29

import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate the odd number sequence (5 cycles)
odd_numbers = [1, 3, 5, 7] * 5
print(odd_numbers)
binary_sequence = [format(num, '03b') for num in odd_numbers]
print(binary_sequence)  # Convert to 3-bit binary

# Flatten binary sequence to a single list of bits
bitstream = [int(bit) for binary in binary_sequence for bit in binary]
print(bitstream)
# Step 2: BPSK Modulation (0 → -1, 1 → +1)
bpsk_signal = np.array(bitstream)*2-1

# Step 3: Add AWGN noise
SNR_dB = 5  # Signal-to-Noise Ratio in dB
SNR = 10**(SNR_dB / 10)  # Convert dB to linear scale
noise_power = np.sqrt(1 / (2 * SNR))
noise = noise_power * np.random.randn(len(bpsk_signal))
received_signal = bpsk_signal + noise

# Step 4: BPSK Demodulation
demodulated_bits =np.where(received_signal>0,1,0)

# Step 5: Count errors
errors = np.sum(np.array(demodulated_bits) != np.array(bitstream))
print(f"Total Errors: {errors}")

# Optional: Plot received signal
plt.figure(figsize=(10, 4))
plt.plot(received_signal[:50], 'bo-', label="Received Signal")
plt.plot(bpsk_signal[:50], 'r-', label="Original Signal", alpha=0.5)
plt.legend()
plt.title("BPSK Transmission through AWGN")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.grid()
plt.show()
