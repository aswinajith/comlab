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
x_min, x_max = max(x), min(x)
quantisation_levels = np.linspace(x_min, x_max, L)
xquantised = []
qinput = np.linspace(x_min, x_max, 1000)
qoutput = []

for i in qinput:
    for j in quantisation_levels:
        if i <= j:
            qoutput.append(j)
            break

for i in x_sampled:
    for j in quantisation_levels:
        if i <= j:
            xquantised.append(j)
            break

fig, ax = plt.subplots(3, 2, figsize = (10,6))

ax[0, 0].plot(qinput, qoutput, 'g')
ax[0, 0].set_title("Quantization Mapping")
ax[0, 0].grid(True)

ax[0, 1].plot(t0, xquantised, label = "Quantized Signal")
ax[0, 1].set_title("Quantized Signal")
ax[0, 1].grid(True)

qlevels = {}
bit_no = int(np.log(L))

for i in range(L):
    bin_str = format(i, f'0{bit_no}b')
    qlevels[quantisation_levels[i]] = bin_str

xtruncated = [qlevels[i] for i in xquantised]
print("Pulse coded message: ", xtruncated)

quantisation_noise = np.array(xquantised) - np.array(x_sampled)

