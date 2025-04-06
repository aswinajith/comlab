import numpy as np
import matplotlib.pyplot as plt

fm = 100
dc_offset = 2
t = np.arange(0, 5/fm, 0.0001)
x = np.sin(2 * np.pi * fm * t) + dc_offset

fs = 30 * fm
t0 = np.arange(0, 5/fm, 1/fs)
x_sampled = np.sin(2 * np.pi * fm * t0) + dc_offset

L = 8
x_min, x_max= min(x), max(x)
quantisation_level = np.linspace(x_min, x_max, L)
xquantised = []
qinput = np.linspace(x_min, x_max, 1000)
qoutput = []

for i in qinput:
    for j in quantisation_level:
        if i <= j:
            qoutput.append(j)
            break

for i in x_sampled:
    for j in quantisation_level:
        if i <= j:
            xquantised.append(j)
            break

plt.figure(figsize = (10, 8))
plt.subplot(4,1,1)
plt.title("Quantisation Mapping")
plt.plot(qinput, qoutput, 'r')
plt.grid()

plt.subplot(4,1,2)
plt.title("Quantised Signal")
plt.plot(t0, xquantised)
plt.grid()

qlevels = {}
bitno = int(np.log2(L))
print(bitno)

for i in range(L):
    bin_str = format(i, f'0{bitno}b')
    qlevels[quantisation_level[i]] = bin_str
xtruncated = [qlevels[i] for i in xquantised]

print("Pulse coded message: ", xtruncated)

quantisation_noise = np.array(xquantised) - np.array(x_sampled)

print(quantisation_noise)

plt.subplot(4,1,3)
plt.title("Quatisation Noise")
plt.plot(t0, quantisation_noise)
plt.grid()

plt.subplot(4,1,4)
plt.title("Sampled Signal")
plt.plot(t0, x_sampled)
plt.grid()

plt.tight_layout()
plt.show()

def power(lst):
    return np.mean(np.array(lst) ** 2)

snr = power(x_sampled) / power(xquantised)
snrdb = 20 * np.log10(snr)

step_size = (x_max - x_min) / L
noise_power = step_size**2/12
snreqn = power(x_sampled) / noise_power
snreqndb = 20 * np.log10(snreqn)

