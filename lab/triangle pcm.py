import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import sawtooth

# 1️⃣ Generate Triangular Wave: 2 cycles, 0–4V range
fs = 32  # Samples per second
t = np.arange(0, 1, 1/fs)  # 1 second duration
x_t = 2 + 2 * sawtooth(2 * np.pi * 2 * t, 0.5)  # Triangular wave: 2 cycles, 4V peak-to-peak

# 2️⃣ Ask user for number of bits
N = int(input("Enter number of bits (e.g., 2 to 8): "))

# 3️⃣ Quantization
levels = 2 ** N
step_size = (np.max(x_t) - np.min(x_t)) / (levels - 1)
x_q = np.round((x_t - np.min(x_t)) / step_size) * step_size + np.min(x_t)
x_rec = x_q  # For basic PCM
noise = x_t - x_q

# 4️⃣ SNR Calculations
Px = np.mean(x_t ** 2)
Pn = np.mean(noise ** 2)
snr_db = 10 * np.log10(Px / Pn)
snr_theory = 6.02 * N + 1.76  # Ideal SNR

# 5️⃣ Display SNR Results
print(f"\nFor {N} bits:")
print(f"Simulated SNR = 10*log10(Px / Pn) = 10*log10({Px:.6f} / {Pn:.6f}) = {snr_db:.2f} dB")
print(f"Theoretical SNR ≈ 6.02 * {N} + 1.76 = {snr_theory:.2f} dB")

# 6️⃣ Generate PCM Binary Stream
quantized_levels = np.round((x_q - np.min(x_q)) / step_size).astype(int)
pcm_binary = [format(q, f'0{N}b') for q in quantized_levels]

print("\nPCM Binary Stream:")
print(' '.join(pcm_binary))

# 7️⃣ Plot Original + Quantized + Noise
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.plot(t, x_t, 'b', label="Original Signal")
plt.step(t, x_q, 'g', where='mid', label="Quantized")
plt.plot(t, x_rec, 'r--', label="Reconstructed")
plt.title(f"{N} Bits - PCM Signal (Triangular Wave)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (V)")
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(t, noise, 'm', label="Quantization Noise")
plt.title(f"{N} Bits - Quantization Noise")
plt.xlabel("Time (s)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# 8️⃣ Plot PCM Bitstream as Digital Waveform
bitstream = ''.join(pcm_binary)
bit_values = np.array([int(b) for b in bitstream])
bit_time = np.arange(0, len(bit_values)) * (1 / (fs * N))  # Bit duration = 1 / (fs * N)

plt.figure(figsize=(14, 2))
plt.step(bit_time, bit_values, where='post')
plt.title(f"PCM Digital Bitstream ({N} bits/sample)")
plt.xlabel("Time (s)")
plt.ylabel("Bit Value")
plt.yticks([0, 1])
plt.grid(True)
plt.tight_layout()
plt.show()
