#qns15
import numpy as np
import matplotlib.pyplot as plt
f=10
t=np.arange(0,1,0.001)
x=np.sin(2*np.pi*f*t)
n=len(x)
acf=np.correlate(x,x,mode='full')/n
acf=acf[n-1:]
shift=10
acfx=np.roll(acf,shift)
out=acfx*5
plt.subplot(3,1,1)
plt.plot(x)
plt.subplot(3,1,2)
plt.plot(out)
lag=np.arange(len(acf))/100
plt.subplot(3,1,3)
plt.plot(lag,acfx,"r")
plt.plot(lag,out,'--',"b")
plt.legend(loc="upper right")
plt.show()
