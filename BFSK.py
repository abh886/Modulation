# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 02:25:51 2019

@author: Abhi
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
        X.append(0)

t=arange(0,len(x),0.01)
op1=[]
op2=[]
for j in range(len(t)):
    op1.append(sin(2*pi*2*t[j]))
    
for k in range(len(t)):
    op2.append(sin(2*pi*1*t[k]))

f=[]  
for l in range(len(X)):
    for m in range(len(t)):
            if X[l] * op1[m] == 0:
                f.append(op2[m])
            elif X[l] * op1[m] == 1 or -1:
                f.append(op1[m])
            
        

plt.plot(X,'b',drawstyle='steps-pre')
plt.title('input')
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.show()

plt.plot(op1,'b')
plt.title('input')
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.show()

plt.plot(op2,'r')
plt.title('input')
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.show()

plt.plot(f,'k')
plt.title('FSK output')
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.show()