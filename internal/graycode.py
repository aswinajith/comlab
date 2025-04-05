#graycodeqns
import numpy as np
import matplotlib.pyplot as plt

n=int(input("enter the decimal number: "))
a=bin(n)[2:]
def bin_to_gray(a):
    graycode=a[0]
    for i in range(1,len(a)):
        gray=str(int(a[i-1])^int(a[i]))
        graycode+=gray
    return graycode

data=bin_to_gray(a)
print("graycoded data:",data)
bd=list(data)
bd=np.insert(bd,0,0)
print("data: ",bd)

N=len(bd)
fc=float(input("enter fc: "))
fs=30*fc
ts=np.arange(0,1,1/fs)
a=int(input("amplitude: "))
c1=np.cos(2*np.pi*fc*ts)
c2=np.sin(2*np.pi*fc*ts)

s=[None]*(N//2)
for i in range(0,N,2):
    j=int(i/2)
    s[j]=bd[i:i+2]
    print("required msg:",s[j])

e=[]
o=[]
for k in range(len(s)):
    f=s[k]
    if(f[1]==0):
        e.append(f)
    else:
        o.append(f)

for q in e:
    for r in range(len(q)):
        if(q[r]==0):
            q[r]=-1
        else:
            q[r]=1
for s in o:
    for t in range(len(s)):
        if(s[t]==0):
            s[t]=-1
        else:
            s[t]=1

msg1=[]
msg2=[]
for p in e:
    for l in range(len(p)):
        msg1.append(p[l]*c1)
for b in o:
    for c in range(len(b)):
        msg2.append(int(b[c])*c2)

e=np.repeat(e,fs)
o=np.repeat(o,fs)
msg1=np.repeat(msg1,fs)
msg2=np.repeat(msg2,fs)

snrdb=0.0000001
normal=10**(snrdb/10)
noise=1/np.sqrt(2*normal)
msg1noise=msg1+noise
msg2noise=msg2+noise

transmitted=np.concatenate((msg1noise,msg2noise))

fig,a=plt.subplots(3,1)
a[0].plot(e)
a[0].set_title("even")
a[1].plot(o)
a[1].set_title("odd")
a[2].plot(transmitted)
plt.tight_layout
plt.show()
