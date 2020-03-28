# -*- coding: utf-8 -*-
"""
Binary PSK
"""

from numpy import arange,linspace,cos,pi,sin
import matplotlib.pyplot as plt
import math

X=[]
x=[1,0,1,0,1,0]
for i in range(len(x)):
    if x[i] == 1:
        X.append(1)
    elif x[i] == 0:
        X.append(-1)
        

t=arange(0,1,0.01)
phi=[]
for i in range (len(t)):
    phi.append(sin(2*pi*2*t[i]))

op=[]
for i in range(len(X)):
    for j in range(len(phi)):
        op.append(X[i]*phi[j])

plt.plot(X,'b',drawstyle='steps-pre')
plt.title('input')
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.show()

plt.plot(phi,'k')
plt.title('sinusoidal wave')
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.show()

plt.plot(op)
plt.title('PSK waveform')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()