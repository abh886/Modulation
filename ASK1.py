# -*- coding: utf-8 -*-
"""
Binary ASK
"""
from numpy import arange,linspace,cos,pi,sin
import matplotlib.pyplot as plt
#import math
import random

Start = 0
Stop = 1
limit = random.randint(2,7)

x = [random.randint(Start, Stop) for iter in range(limit)]

print(x)


X=[]
#x=[1,0,1,0,1,0]
for i in range(len(x)):
    if x[i] == 1:
        X.append(1)
    elif x[i] == 0:
        X.append(0)
        
n=linspace(0,len(X),num=len(X))
t=linspace(0,len(X),num=100)
phi=[]
for i in range (0,len(t)):
    phi.append(sin(2*pi*t[i]))
T = linspace(0,len(X),num=(100*len(X)))
op=[]
for i in range(len(X)):
    for j in range(len(phi)):
            op.append(X[i]*phi[j])

plt.plot(n,X,'b',drawstyle='steps-pre')
plt.title('input')
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.show()

plt.plot(t,phi,'k')
plt.title('sinusoidal wave')
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.show()


plt.plot(T,op)
plt.title('ASK waveform')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()