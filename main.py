#!/usr/bin/python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
from scipy.io import wavfile
import scipy

name1 = "./sample/1a.wav"
name2 = "./sample/1b.wav"
D = 50 #odległosc między telefonami w centymetrach

#wczytywanie pierwszego sygnału
fs, data1 = wavfile.read(str(name1))
l_audio = len(data1.shape)
if l_audio == 2:
    data1 = data1.sum(axis=1) / 2
F1 = fft(data1)
N = data1.shape[0]
secs = N / float(fs)
Ts = 1.0/fs # sampling interval in time
t = scipy.arange(0, secs, Ts) #czas trwania nagrania
f = scipy.fftpack.fftfreq(data1.size, t[1]-t[0])

#wczytywanie sygnału
fs, data2 = wavfile.read(str(name2))
l_audio = len(data2.shape)
if l_audio == 2:
    data2 = data2.sum(axis=1) / 2
F2 = fft(data2)
N = data2.shape[0]
secs = N / float(fs)
Ts = 1.0/fs # sampling interval in time
t1 = scipy.arange(0, secs, Ts)#czas trawania nagrania
f1 = scipy.fftpack.fftfreq(data2.size, t[1]-t[0])

#transformata odwrotana
IFFT1 = ifft(F1)#znaleźć w data1
IFFT2 = ifft(F2)#znaleźć w data2
l_audio = len(IFFT1.shape)
if l_audio == 2:
    IFFT1 = IFFT1.sum(axis=1) / 2
N = IFFT1.shape[0]
secs = N / float(fs)
Ts = 1.0/fs # sampling interval in time
ifft1 = scipy.arange(0, secs, Ts)#czas trwania

l_audio = len(IFFT2.shape)
if l_audio == 2:
    IFFT2 = IFFT21.sum(axis=1) / 2
N = IFFT2.shape[0]
secs = N / float(fs)
Ts = 1.0/fs # sampling interval in time
ifft2 = scipy.arange(0, secs, Ts)#czas trwania





plt.subplot(3, 1, 1)
plt.plot(f,abs(F1), 'r')
plt.plot(f1,abs(F2), 'g')

plt.subplot(3, 1, 2)
plt.plot(ifft1, IFFT1, 'r')
plt.plot(ifft2, IFFT2, 'g')

plt.subplot(3, 1, 3)
plt.plot(t, data1, 'r')
plt.plot(t1, data2, 'g')

plt.show()

