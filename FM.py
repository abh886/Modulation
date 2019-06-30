# -*- coding: utf-8 -*-
"""
Frequency modulation
"""

from numpy import sin,cos,pi,linspace,arange,log10
#from scipy.signal import freqs
from scipy.fftpack import fft,fftshift
import matplotlib.pylab as plt


fc=25
fm=1
t=arange(0,1,0.001)
mt=sin(2*pi*fm*t)

m=10
y=sin(2*pi*fc*t+(m*sin(2*pi*fm*t)))

plt.plot(t,mt,'g')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Message signal')
plt.show()

a=fft(y)
#plt.plot(t,ct,'b')
#plt.xlabel('Time')
#plt.ylabel('Amplitude')
#plt.title('Carrier signal')
#plt.show()

plt.plot(t,y,'r')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('FM signal')
plt.show()
