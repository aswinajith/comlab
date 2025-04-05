import numpy as np
import matplotlib.pyplot as plt

symbol=int(input("no:of symbols: "))
sample=int(input("samples: "))
bd=np.random.randint(0,2,symbol)
N=len(bd)
bd=np.repeat(bd,sample)
plt.subplot(3,2,1)
plt.plot(bd)
plt.title("data")
for i in range(symbol):
    if bd[i]==0:
        bd[i]=-1
    else:
        bd[i]=1

taps=int(input("enter taps: "))
alpha=float(input("enter rolloff factor: "))
t=np.arange(taps)-(taps-1)//2
Ts=sample

h=np.sinc(t/Ts)*np.cos(np.pi*alpha*t/Ts)/(1-(2*alpha*t/Ts)*2)
#h=np.nan_to_num(h)
plt.subplot(3,2,2)
plt.plot(h,".")
plt.title("raised cosine")

out1=np.convolve(bd,h)
plt.subplot(3,2,3)
plt.plot(out1)
plt.title("convolution btw data and raised cosine")
for i in range(symbol):
    if i*sample+taps//2<len(out1):
        plt.plot([i*sample+taps//2,i*sample+taps//2],[0,out1[i*sample+taps//2]])

snr=0.0001
normal=10**(snr/10)
noise=1/np.sqrt(2*normal)
msg1=noise+out1

out2=np.convolve(msg1,h)
plt.subplot(3,2,4)
plt.plot(out2)
plt.title("convolution btw noisedmsg and raised cosine")
for i in range(symbol):
    if i*sample+taps//2<len(out2):
        plt.plot([i*sample+taps//2,i*sample+taps//2],[0,out2[i*sample+taps//2]])

q=[]
for i in out2:
    if i>0:
        q.append(1)
    else:
        q.append(0)
plt.subplot(3,2,5)
plt.plot(q)
plt.title("received data")
plt.show()
