import numpy as np
import matplotlib.pyplot as plt

# Parameters
binary_sequence = np.array([0, 1, 0, 1, 0, 1, 1, 0, 1])  # Original binary sequence
num_bits = len(binary_sequence)
SNR_dB = 10  # Signal-to-Noise Ratio in dB
sampling_rate = 100  # Samples per bit (must be an integer)
bit_duration = 1  # Duration of one bit
t = np.linspace(0, num_bits * bit_duration, num_bits * sampling_rate, endpoint=False)  # Time vector

# RZ Unipolar Signaling
def rz_unipolar_modulation(bits, sampling_rate):
    signal = np.zeros(len(bits) * sampling_rate)
    for i, bit in enumerate(bits):
        if bit == 1:
            start_idx = i * sampling_rate
            end_idx = int((i + 0.5) * sampling_rate)  # Ensure integer index
            signal[start_idx:end_idx] = 1  # Positive pulse for half duration
    return signal

# BPSK Modulation
def bpsk_modulation(bits, sampling_rate):
    signal = np.zeros(len(bits) * sampling_rate)
    for i, bit in enumerate(bits):
        if bit == 1:
            signal[i * sampling_rate:(i + 1) * sampling_rate] = 1  # Phase 0°
        else:
            signal[i * sampling_rate:(i + 1) * sampling_rate] = -1  # Phase 180°
    return signal

# AWGN Channel
def add_awgn_noise(signal, snr_db):
    signal_power = np.mean(signal**2)
    noise_power = signal_power / (10 ** (snr_db / 10))
    noise = np.random.normal(0, np.sqrt(noise_power), len(signal))
    return signal + noise

# Demodulation and Reconstruction
def reconstruct_signal(received_signal, sampling_rate, modulation_type):
    reconstructed_bits = []
    for i in range(num_bits):
        start_idx = i * sampling_rate
        end_idx = (i + 1) * sampling_rate
        sample = np.mean(received_signal[start_idx:end_idx])
        if modulation_type == "rz_unipolar":
            reconstructed_bits.append(1 if sample > 0.5 else 0)  # Threshold for RZ Unipolar
        elif modulation_type == "bpsk":
            reconstructed_bits.append(1 if sample > 0 else 0)  # Threshold for BPSK
    return np.array(reconstructed_bits)

# Count Errors
def count_errors(original, reconstructed):
    return np.sum(original != reconstructed)

# Simulate RZ Unipolar
rz_signal = rz_unipolar_modulation(binary_sequence, sampling_rate)
rz_noisy_signal = add_awgn_noise(rz_signal, SNR_dB)
rz_reconstructed = reconstruct_signal(rz_noisy_signal, sampling_rate, "rz_unipolar")
rz_errors = count_errors(binary_sequence, rz_reconstructed)

# Simulate BPSK
bpsk_signal = bpsk_modulation(binary_sequence, sampling_rate)
bpsk_noisy_signal = add_awgn_noise(bpsk_signal, SNR_dB)
bpsk_reconstructed = reconstruct_signal(bpsk_noisy_signal, sampling_rate, "bpsk")
bpsk_errors = count_errors(binary_sequence, bpsk_reconstructed)

# Results
print("Original Binary Sequence:", binary_sequence)
print("RZ Unipolar Reconstructed:", rz_reconstructed)
print("RZ Unipolar Errors:", rz_errors)
print("BPSK Reconstructed:", bpsk_reconstructed)
print("BPSK Errors:", bpsk_errors)

# Plot Signals
plt.figure(figsize=(12, 8))

# RZ Unipolar
plt.subplot(3, 1, 1)
plt.plot(t, rz_signal, label="RZ Unipolar Signal")
plt.title("RZ Unipolar Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()

# BPSK
plt.subplot(3, 1, 2)
plt.plot(t, bpsk_signal, label="BPSK Signal")
plt.title("BPSK Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()

# Noisy BPSK
plt.subplot(3, 1, 3)
plt.plot(t, bpsk_noisy_signal, label="Noisy BPSK Signal")
plt.title("Noisy BPSK Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.legend()

plt.tight_layout()
plt.show()
