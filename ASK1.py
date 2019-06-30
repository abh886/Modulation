# -*- coding: utf-8 -*-
"""
Binary ASK
"""
from numpy import arange,linspace,cos,pi,sin
import matplotlib.pyplot as plt
import math
X=[]
x=[1,1,1,0,1,0]
for i in range(len(x)):
    if x[i] == 1:
        X.append(1)
    elif x[i] == 0:
        X.append(0)
        

t=arange(0,len(x),0.01)
phi=[]
for i in range (0,len(t)):
    phi.append(sin(2*pi*2*t[i]))

op=[]
for i in range(0,len(X)):
    for j in range(0,len(phi)):
        op.append(X[i]*phi[j])

plt.plot(X,'b',drawstyle='steps-pre')
plt.title('input')
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.show()

plt.plot(t,phi,'k')
plt.title('sinusoidal wave')
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.show()

plt.plot(op)
plt.title('ASK waveform')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()