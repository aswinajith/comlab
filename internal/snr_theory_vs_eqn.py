import numpy as np
import matplotlib.pyplot as plt

l = [0.5, 1]
f=5
t = np.linspace(0, 1, 1000)
x = 8*np.sin(2 * np.pi *f* t)
snr = []

def quantise(x, i):
    return np.round((x - np.min(x)) / i) * i + np.min(x)

for i in l:
    q = quantise(x, i)
    signal_power = np.mean(x ** 2)
    noise_power = np.mean((x - q) ** 2)
    snrl = 10 * np.log10(signal_power / noise_power)
    snr.append(snrl)

print("SNR values:", snr)