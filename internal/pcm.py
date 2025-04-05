import numpy as np
import matplotlib.pyplot as plt

fm = 100
dc_offset = 2
t = np.arange(0,5/fm,0.0001)
x = np.sin(2 * np.pi * fm * t) + dc_offset

fs = 30 * fm
t0 = np.arange(0,5/fm,1/fs)
x_sampled = np.sin(2 * np.pi * fm * t0) + dc_offset


L = 8
x_min, x_max = min(x), max(x)
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

fig,ax = plt.subplots(3,2, figsize = (10,6))

ax[0, 0].plot(qinput, qoutput, 'r')
ax[0, 0].set_title("Quantization Mapping")
ax[0, 0].grid(True)

ax[0, 1].plot(t0, xquantised, label = "Quantized Signal")
ax[0, 1].set_title("Quantized Signal")
ax[0, 1].grid(True)


qlevels = {}
bit_no = int(np.log2(L))

for i in range(L):
    bin_str = format(i, f'0{bit_no}b')
    qlevels[quantisation_levels[i]] = bin_str
xtruncated = [qlevels[i] for i in xquantised]
print("Pulse coded message: ", xtruncated)

quantisation_noise = np.array(xquantised) - np.array(x_sampled)

ax[1, 0].plot(t0, quantisation_noise, label="Quantization Noise")
ax[1, 0].set_title("Quantization Noise")
ax[1, 0].grid(True)

ax[1, 1].plot(t0, x_sampled, label="Sampled Signal")
ax[1, 1].set_title("Sampled Signal")
ax[1, 1].grid(True)

def power(lst): 
    return np.mean(np.array(lst) ** 2)

snr = power(x_sampled) / power(quantisation_noise)
snrdb = 20 * np.log10(snr)

step_size = (x_max-x_min) / L
noise_power = (step_size ** 2) / 12
snreqn = power(x_sampled) / noise_power
snreqdb = 20 * np.log10(snreqn)

print("SNR (measured): {:.2f} dB".format(snrdb))
print("SNR (theoretical): {:.2f} dB".format(snreqdb))

plt.tight_layout()
plt.show()
