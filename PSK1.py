# -*- coding: utf-8 -*-
"""
Binary PSK
"""

from numpy import arange,linspace,cos,pi,sin
import matplotlib.pyplot as plt
import math
import random
X=[]
# x=[1,0,1,0]

Start = 0
Stop = 1
limit = random.randint(2,7)

x = [random.randint(Start, Stop) for iter in range(limit)]

print(x)
for i in range(len(x)):
    if x[i] == 1:
        X.append(1)
    elif x[i] == 0:
        X.append(-1)
        
n = linspace(0,len(X),num=len(X))
t=linspace(0,len(X),num=100)
phi=[]
for i in range (len(t)):
    phi.append(sin(2*pi*t[i]))

op=[]
T = linspace(0,len(X),num = (len(X)*100))
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
plt.title('PSK waveform')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()