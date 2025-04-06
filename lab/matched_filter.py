import numpy as np
import matplotlib.pyplot as plt

num_symbols = 10
sps = 8
beta = 0.35
num_taps = 101

bits = np.random.randint(0, 2, num_symbols)
symbols = 2 * bits -1

x = np.zeros(sps*num_symbols)
x[::sps] = symbols
print(x)

t = np.arange(-50, 51)
h = 1/sps * np.sinc(t/sps) * np.cos(np.pi * beta * t/sps)/(1 - (2 * beta *t/sps)**2)

x_shaped = np.convolve(x,h)

plt.figure(figsize = (10, 8))

plt.subplot(3,1,1)
plt.title("Over Sampled NRZ Signal")
plt.plot(x, '-.')
plt.grid()

plt.subplot(3,1,2)
plt.title("Raised cosine filter")
plt.plot(t,h, '.-')
plt.grid()

plt.subplot(3,1,3)
plt.title("Shaped Raised Cosine Filter")
plt.plot(x_shaped, ".-")
for i in range(num_symbols):
    plt.axvline(i * sps + num_taps//2+1, color = 'r', linestyle='--')
plt.grid()

plt.tight_layout()
plt.show()
