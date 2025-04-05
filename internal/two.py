#qns2
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

O=input("enter EBCIC code of O: ")
K=input("enter EBCIC code of K: ")
n1=bin(int(O,16))[2:]
n2=bin(int(K,16))[2:]
d1=[]
d1.extend(np.array(list(map(int,n1))))
d2=[]
d2.extend(np.array(list(map(int,n2))))
data=np.concatenate((d1,d2))
fc=1
fs=30*fc
t=np.arange(0,1,1/fs)
c=np.cos(2*np.pi*fc*t)

for i in range(len(data)):
    if data[i]==0:
        data[i]=-1
    else:
        data[i]=1
msg=[]
for p in data:
    msg.extend(p*c)

msg=np.repeat(msg,fs)
data=np.repeat(data,fs)

snr=0.0001
normal=10**(snr/10)
noise=1/np.sqrt(2*normal)
transmitted=msg+noise

plt.subplot(2,1,1)
plt.plot(data)
plt.subplot(2,1,2)
plt.plot(transmitted)

def power(lst):
    p=0
    for i in lst:
        p=p+i**2
    return p/len(lst)
signalpower=power(transmitted)
error=erfc(signalpower)
print("error: ",error)

plt.show()
