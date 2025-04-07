import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, square

# 1️⃣ Generate square wave
fs = 1000  # Sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)
freq = 5  # 5 Hz square wave
x = square(2 * np.pi * freq * t)

# 2️⃣ Apply Anti-Aliasing Filter (Low-Pass Filter)
def butter_lowpass_filter(data, cutoff, fs, order=5):
    nyq = 0.5 * fs
    norm_cutoff = cutoff / nyq
    b, a = butter(order, norm_cutoff, btype='low', analog=False)
    return lfilter(b, a, data)

cutoff_freq = 50  # Cutoff for anti-aliasing filter
x_filtered = butter_lowpass_filter(x, cutoff=cutoff_freq, fs=fs)

# 3️⃣ Quantize with different levels
def quantize(signal, levels):
    min_val = np.min(signal)
    max_val = np.max(signal)
    step = (max_val - min_val) / (levels - 1)
    q_signal = np.round((signal - min_val) / step) * step + min_val
    return q_signal

# Assume x, x_filtered, t are already defined and quantize() function exists

# Quantize with specific levels manually
qx2   = quantize(x_filtered, 2)
qx8   = quantize(x_filtered, 8)
qx16  = quantize(x_filtered, 16)
qx64  = quantize(x_filtered, 64)

# Plotting everything simply
plt.figure(figsize=(14, 10))

plt.subplot(6, 1, 1)
plt.plot(t, x, label="Original Square Wave")
plt.title("Original Square Wave (Ideal)")
plt.grid(True)

plt.subplot(6, 1, 2)
plt.plot(t, x_filtered, color='orange', label="Filtered (Anti-Aliased)")
plt.title("After Anti-Aliasing Filter")
plt.grid(True)

plt.subplot(6, 1, 3)
plt.plot(t, qx2, label="Quantized (2 levels)", color='green')
plt.title("Quantized with 2 Levels")
plt.grid(True)

plt.subplot(6, 1, 4)
plt.plot(t, qx8, label="Quantized (8 levels)", color='blue')
plt.title("Quantized with 8 Levels")
plt.grid(True)

plt.subplot(6, 1, 5)
plt.plot(t, qx16, label="Quantized (16 levels)", color='purple')
plt.title("Quantized with 16 Levels")
plt.grid(True)

plt.subplot(6, 1, 6)
plt.plot(t, qx64, label="Quantized (64 levels)", color='red')
plt.title("Quantized with 64 Levels")
plt.grid(True)

plt.tight_layout()
plt.show()
