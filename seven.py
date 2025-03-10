#qns7
import numpy as np
import matplotlib.pyplot as plt

fm=100
t=np.arange(0,5/fm,0.0001)
dcoffest=2
x=5*np.sin(2*np.pi*fm*t)+dcoffest
plt.subplot(3,2,1)
plt.plot(x)
plt.xlabel("time")
plt.ylabel("amplitude")
plt.title("msg signal")

fs=30*fm
t=np.arange(0,5/fm,1/fs)
xsampled=5*np.sin(2*np.pi*fm*t)+dcoffest
plt.subplot(3,2,2)
plt.plot(xsampled)
plt.title("sampled msg")

L=[2,4,8,16,32,64,128]
for l in L:
    xmin=min(xsampled)
    xmax=max(xsampled)
    ql=np.linspace(xmin,xmax,l)
    q=np.digitize(xsampled,ql)-1
    xquantised=ql[q]
    qlevel={}
    bitno=int(np.log2(l))
    for i in range(l):
        val=bin(i)[2:]
        if (val!=bitno):
            binstr="0"*(bitno-len(val))
            binstr=binstr+val
        else:
            binstr=val
        qlevel[ql[i]]=binstr
    xtruncated=[qlevel[i] for i in xquantised]

    def power(lst):
        p=0
        for i in lst:
            p=p+i**2
        return p/len(lst)
    quantizationnoise=xquantised-xsampled
    snr=power(xsampled)/power(quantizationnoise)
    snrdb=20*np.log10(snr)
    print("the snr of level",l,"is:",snrdb,"db")
