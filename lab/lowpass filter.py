import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# 1️⃣ Input binary sequence
data = [1, 0, 0, 1, 0, 1, 1, 0, 1, 0]
bit_rate = 1  # bits per second
samples_per_bit = 100
fs = bit_rate * samples_per_bit  # sampling frequency

# 2️⃣ Generate NRZ Unipolar waveform
def nrz_unipolar(bits, samples_per_bit):
    signal = np.repeat(bits, samples_per_bit)
    return signal

tx_signal = nrz_unipolar(data, samples_per_bit)
t = np.linspace(0, len(data), len(tx_signal), endpoint=False)

# 3️⃣ Add AWGN noise
noise = np.random.normal(0, 0.5, len(tx_signal))  # Adjust noise std dev
rx_signal = tx_signal + noise

# 4️⃣ LPF design
def low_pass_filter(data, cutoff, fs, order=5):
    nyq = 0.5 * fs
    norm_cutoff = cutoff / nyq
    b, a = butter(order, norm_cutoff, btype='low')
    return lfilter(b, a, data)

cutoff_freq = 10  # Hz
filtered_rx = low_pass_filter(rx_signal, cutoff=cutoff_freq, fs=fs)

# 5️⃣ Plotting
plt.subplot(3, 1, 1)
plt.plot(t, tx_signal, 'b', label='Transmitted NRZ (Unipolar)')
plt.title("Transmitted NRZ Unipolar Signal")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, rx_signal, 'r', label='Received Signal (with AWGN)')
plt.title("Received Signal with AWGN")
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, filtered_rx, 'g', label='After LPF')
plt.title("Output after Low-Pass Filter (10 Hz)")
plt.xlabel("Time (s)")
plt.grid(True)

plt.tight_layout()
plt.show()
