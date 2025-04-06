import numpy as np
import matplotlib.pyplot as plt

T = 1
Fs = 100
rolloff = 0.7

g = lambda t: np.sinc(t) * np.cos(np.pi * rolloff * t)/(1 - (2 * rolloff * t)**2)
binary_sequence = [0,1,1,0,0,1,1,0,1,0,0,1,1,0,1,0]
j = np.array(binary_sequence) * 2 -1

t = np.arange(-2 *T, (len(j) + 2) * T, 1 /Fs)
y = sum(j[k] * g(t-k*T) for k in range(len(j)))

fig, ax = plt.subplots(2,2)

ax[0][1].plot(t,y)
ax[0][1].set_title("Pulse Shaped Signal")

x = np.arange(-T, T, 1/Fs)
for i in range(2 * Fs, len(y) - 3* Fs, Fs):
    ax[1][1].plot(x, y[i:i+2*Fs], 'blue')
ax[1][1].set_title("Eye Diagram")

ax[0][0].step(np.arange(len(binary_sequence)), binary_sequence)
ax[0][0].set_title("Binary Message")

t = np.arange(-5, 5 , 0.01)
ax[1][0].plot(t, g(t))
ax[1][0].set_title("Impulse Response of Raised Cosine Filter")

plt.tight_layout()
plt.show()
