#qns37
import numpy as np
import matplotlib.pyplot as plt

f=1
t=np.arange(0,5/f,0.001)
x=8*np.sin(2*np.pi*f*t)
fs=30*f
ts=np.arange(0,5/f,1/fs)
xsampled=8*np.sin(2*np.pi*f*ts)

def power(lst):
    p=0
    for i in lst:
        p=p+i**2
    return p/len(lst)

stepsize=[0.5,1]
for value in stepsize:
    noisepower=(value**2)/3
    snr=power(xsampled)/noisepower
    snrdb=20*np.log10(snr)
    print("snr for stepsize",value,"is: ",snrdb,"db")
