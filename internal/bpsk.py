import numpy as np
import matplotlib.pyplot as plt

# Frequencies
m_f = 10  # Message frequency
c_f = 20  # Carrier frequency
s_f = 30 * c_f  # Sampling frequency

# Time vector
t = np.arange(0, 4 / c_f, 1 / s_f)

# Message signal (square wave with noise)
msg = np.sign(np.cos(2 * np.pi * m_f * t) + np.random.normal(scale=0.01, size=len(t)))

# Carrier signal
carrier = np.cos(2 * np.pi * s_f / c_f * t)

# Modulated signal (BPSK)
modulated_signal = carrier * msg

# Plot signals
plt.figure(figsize=(8, 6))
plt.subplot(3, 1, 1)
plt.plot(t, msg)
plt.title("Message Signal")
plt.subplot(3, 1, 2)
plt.plot(t, carrier)
plt.title("Carrier Signal")
plt.subplot(3, 1, 3)
plt.plot(t, modulated_signal)
plt.title("Modulated Signal (BPSK)")
plt.tight_layout()
plt.show()
