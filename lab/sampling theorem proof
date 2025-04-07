#sampling theorem proof
import numpy as np
import matplotlib.pyplot as plt

# **Step 1: Define the Original Signal (Sine Wave)**
fm = 10  # Signal frequency (Hz)
t_cont = np.linspace(0, 1, 1000)  # Continuous time for reference
x_cont = np.sin(2 * np.pi * fm * t_cont)  # Continuous sine wave

# **Step 2: Sampling at Different Rates**
fs1 = 12  # Below Nyquist (Undersampling, fs < 2fm)
fs2 = 21  # Nyquist Rate (fs = 2fm)
fs3 = 50  # Above Nyquist (Oversampling, fs > 2fm)

t1 = np.arange(0, 1, 1/fs1)  # Time samples for fs1
t2 = np.arange(0, 1, 1/fs2)  # Time samples for fs2
t3 = np.arange(0, 1, 1/fs3)  # Time samples for fs3

x1 = np.sin(2 * np.pi * fm * t1)  # Undersampled signal
x2 = np.sin(2 * np.pi * fm * t2)  # Nyquist sampled signal
x3 = np.sin(2 * np.pi * fm * t3)  # Oversampled signal

# **Step 3: Plot the Signals**
fig, ax = plt.subplots(3, 1, figsize=(10, 8))

# **Undersampling (Aliasing)**
ax[0].plot(t_cont, x_cont, 'gray', linestyle='dashed', label="Original Signal")
ax[0].scatter(t1, x1, color='red', label="Sampled Points (fs < 2fm)")
ax[0].plot(t1, x1, 'r', linestyle='dotted')
ax[0].set_title("Undersampling (Aliasing Occurs)")
ax[0].legend()
ax[0].grid()

# **Nyquist Sampling (Perfect Reconstruction)**
ax[1].plot(t_cont, x_cont, 'gray', linestyle='dashed', label="Original Signal")
ax[1].scatter(t2, x2, color='blue', label="Sampled Points (fs = 2fm)")
ax[1].plot(t2, x2, 'b', linestyle='dotted', label="Reconstructed Wave")  # Connect points
ax[1].set_title("Nyquist Rate Sampling (fs = 2fm)")
ax[1].legend()
ax[1].grid()
# **Oversampling (Better Accuracy)**
ax[2].plot(t_cont, x_cont, 'gray', linestyle='dashed', label="Original Signal")
ax[2].scatter(t3, x3, color='green', label="Sampled Points (fs > 2fm)")
ax[2].plot(t3, x3, 'g', linestyle='dotted')
ax[2].set_title("Oversampling (fs > 2fm)")
ax[2].legend()
ax[2].grid()

plt.tight_layout()
plt.show()
