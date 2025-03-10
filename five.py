#qns5
import numpy as np
import matplotlib.pyplot as plt

fm=int(input("enter fm value: "))
t=np.arange(0,1,0.001)
x=np.sin(2*np.pi*fm*t)

f1=0.75*fm
t1=np.arange(0,1,1/f1)
x1=np.sin(2*np.pi*fm*t1)
plt.subplot(3,2,1)
plt.plot(t,x,label="signal",color='red')
plt.stem(t1,x1,label="0.75fm sampled")
plt.legend(loc="upper right")

f2=0.5*fm
t2=np.arange(0,1,1/f2)
x2=np.sin(2*np.pi*fm*t2)
plt.subplot(3,2,2)
plt.plot(t,x,label="signal",color='green')
plt.stem(t2,x2,label="0.5fm sampled")
plt.legend(loc="upper right")

f3=fm
t3=np.arange(0,1,1/f3)
x3=np.sin(2*np.pi*fm*t3)
plt.subplot(3,2,3)
plt.plot(t,x,label="signal",color='blue')
plt.stem(t3,x3,label="fm sampled",basefmt="--")
plt.legend(loc="upper right")

f4=2*fm
t4=np.arange(0,1,1/f4)
x4=np.sin(2*np.pi*fm*t4)
plt.subplot(3,2,4)
plt.plot(t,x,label="signal",color='orange')
plt.stem(t4,x4,label="2fm sampled")
plt.legend(loc="upper right")

f5=4*fm
t5=np.arange(0,1,1/f5)
x5=np.sin(2*np.pi*fm*t5)
plt.subplot(3,2,5)
plt.plot(t,x,label="signal",color='violet')
plt.stem(t5,x5,label="4fm sampled")
plt.legend(loc="upper right")
plt.show()
