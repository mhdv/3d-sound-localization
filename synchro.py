#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

pr_dz = 340 #m/s
#odległosc między telefonami w centymetrach
def synchro():
	#wczytywanie pierwszego sygnału
	fs, data = wavfile.read(str(sys.argv[1]))
	l_audio = len(data.shape)
	if l_audio == 2:
   		data = data.sum(axis=1) / 2
	Ts = 1.0/fs_rate # sampling interval in time
	#print ("Timestep between samples Ts", Ts)
	t = scipy.arange(0, secs, Ts)
	#wczytywanie drugiego sygnału
	fs1, data1 = wavfile.read(str(sys.argv[2]))
	l_audio = len(data1.shape)
	if l_audio == 2:
		data1 = data1.sum(axis=1) / 2
	index = np.argmax(data)
	index1 = np.argmax(data1)
	dif = (index-index1)
	if (dif < 0):
		dif= t[-1*dif]*pr_dz
	else:
		dif= t[dif]*pr_dz
	rat = np.argmax(data)/np.argmax(data1)
	return dif, rat
synchro()




#plt.title("Sygnal")
#plt.plot(data1)
#plt.show()

