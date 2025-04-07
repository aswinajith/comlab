import numpy as np
import matplotlib.pyplot as plt

fs=1000
f=10
t=np.linspace(0,1,fs)
sigma=0.5

s_t=np.sin(2*np.pi*t*f)
w_t=sigma*np.random.randn(len(t))

x_t=s_t+w_t

s_f=np.fft.fft(s_t)
w_f=np.fft.fft(w_t)
x_f=np.fft.fft(x_t)

w=np.fft.fftfreq(len(t),1/fs)
T=0.1  #time delay
H_f=np.exp(-1j*w*T)
output_f=H_f*(s_f**2)

output_t=np.fft.ifft(output_f).real

# Original Signal
plt.subplot(3, 1, 1)
plt.plot(t, s_t, label="Original Signal s(t)", color='b')
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

# Noisy Signal
plt.subplot(3, 1, 2)
plt.plot(t, x_t, label="Noisy Signal s(t) + w(t)", color='r')
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

# Output Signal
plt.subplot(3, 1, 3)
plt.plot(t, output_t, label="Output Signal", color='g')
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()