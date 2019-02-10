# -*- coding: utf-8 -*-
"""
To implement Double sideband Side suppressed carrier modulation
"""

from numpy import sin,pi,linspace
from scipy.fftpack import fft,fftshift
from scipy.signal import lfilter
import matplotlib.pyplot as plt

Ac=int(input('enter carrier signal amplitude:'))
Am=int(input('enter message signal amplitude:'))
fc=int(input('enter carrier frequency:'))
fm=int(input('enter message frequency:'))   # fm<fc

t=int(input('enter time period:'))

m=Am/Ac
T=linspace(0,t,1000)

m_s=Am*sin(2*pi*fm*T)

plt.plot(T,m_s,'b')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Message signal')
plt.legend ('Message')
plt.show()


c_s=Ac*sin(2*pi*fc*T)
plt.plot(T,c_s,'g')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Carrier signal')
plt.legend ('Carrier')
plt.show()

DSBSC_=c_s*m*sin (2*pi*fm*T)*sin (2*pi*fc*T)

plt.plot (T,DSBSC_,'r')
plt.xlabel ('Time')
plt.ylabel ('Amplitude ')
plt.title ('Double Sideband Suppressed Carrier Wave output')
plt.legend ('D ')
plt.show()

Y=fft(DSBSC_)
k=linspace(-fc,fc,1000)
plt.plot(k,fftshift(abs(Y)))
plt.xlabel ('K')
plt.ylabel ('X(K)')
plt.title ('Frequency spectrum')
plt.legend ('FS ')
plt.show()

