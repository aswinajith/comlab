import numpy as np
import matplotlib.pyplot as plt

mf = 10
cf = 20 
sf = 30 * cf

t = np.arange(0, 4/cf, 1/sf)

msg = np.sign(np.cos(2 * np.pi * mf * t) + np.random.normal(scale = 0.01, size = len(t)))

carrier = np.cos(2 * np.pi * sf/cf * t)

modulated_signal = carrier * msg

plt.figure(figsize = (8,6))
plt.subplot(4,1,1)
plt.plot(t,msg)
plt.title("Message Signal")
plt.subplot(4,1,2)
plt.plot(t,carrier)
plt.title("Carrier Signal")
plt.subplot(4,1,3)
plt.plot(t, modulated_signal)
plt.title("Modulated signal (BPSK)")

N = 500000
enrdb_list = np.arange(0,50)
BER = []

for i in range(len(enrdb_list)):
    enrdb = enrdb_list[i]
    ebn0 = 10 ** (enrdb / 10)
    x = 2 * (np.random.rand(N) >= 0.5) -1
    noise = 1 / np.sqrt(2 * ebn0)
    channel = x + np.random.randn(N) * noise
    received_x = 2 * (channel >= 0.5) -1
    error = (x != received_x).sum() 
    BER.append(error/N)

plt.subplot(4,1,4)
plt.plot(enrdb_list, BER, "-", enrdb_list, BER, "go")
plt.axis([0,14, 1e-7, 0.1])
plt.xscale("linear")
plt.yscale("log")
plt.grid()
plt.xlabel("Eb/N0 in db")
plt.ylabel("BER")
plt.title("BER in BPSK")
plt.tight_layout()
plt.show()
