# -*- coding: utf-8 -*-
"""
To implement Amplitude modulation 
"""

from numpy import sin,linspace,pi
from scipy.fftpack import fft,fftshift
import matplotlib.pyplot as plt

Ac=int(input('enter carrier signal amplitude:'))
Am=int(input('enter message signal amplitude:'))
fc=int(input('enter carrier frequency:'))
fm=int(input('enter message frequency:'))   # fm<fc

t=int(input('enter time period:'))

m=Am/Ac
T=linspace(0,t,1000)
y1=Am*sin(2*pi*fm*T)  # message signal
y2=Ac*sin(2*pi*fc*T)   # carrier signal
F=Ac+(1+ m*sin(2*pi*fm*T)) * sin(2*pi*fc*T)

Y=fft(F)

plt.plot(T,y1,'k')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Message signal')
plt.show()



plt.plot(T,y2,'g')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Carrier signal')
plt.show()

#plt.plot(T,eq)
plt.plot(T,F,'r')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Modulated signal')
plt.show()
k=linspace(-fc,fc,1000)
plt.plot(k,fftshift(abs(Y)))
plt.xlabel('K')
plt.ylabel('X(K)')
plt.title('Frequency spectrum')
plt.show()