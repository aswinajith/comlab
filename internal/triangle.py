#triangle
#Qn4
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

t=np.linspace(0,3,1000)
triangle=signal.sawtooth(2*np.pi*t,0.5)
t=triangle*2
offset=0
x=t+offset
plt.subplot(3,1,1)
plt.plot(x)
plt.title("triangleoffsetted")

fs=10
sample=int(fs*3)
xsample=signal.resample(x,sample)
tsample=np.linspace(0,1,sample)
plt.subplot(3,1,2)
plt.plot(tsample,xsample)

L=8
xmin=min(x)
xmax=max(x)
quantizationlevel=np.linspace(xmin,xmax,L)
xquantised=[]
qinput=np.linspace(xmin,xmax,1000)
qoutput=[]
for i in qinput:
    for j in quantizationlevel:
        if i<=j:
            qoutput.append(j)
            break 
for q in xsample:
    for r in quantizationlevel:
        if q<=r:
            xquantised.append(j)
            break
plt.subplot(3,1,3)
plt.plot(qinput,qoutput)
plt.title("quantized")

def power(lst):
    p=0
    for i in lst:
        p=p+i**2
    return p/len(lst)
stepsize=(xmax-xmin)/L
Noisepower=(stepsize**2)/3
snr=power(x)/Noisepower
snrdb=20*np.log10(snr)
print('snr: ',snrdb,'db')
plt.tight_layout()
plt.show()
