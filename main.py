#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import scipy

pr_dz = 340 #m/s
#odległosc między telefonami w centymetrach
def synchro(name1, name2):
	#wczytywanie pierwszego sygnału
	fs, data1 = wavfile.read(name1)
	l_audio = len(data1.shape)
	if l_audio == 2:
   		data1 = data1.sum(axis=1) / 2
	Ts = 1.0/fs # sampling interval in time
	#print ("Timestep between samples Ts", Ts)
	N = data1.shape[0]
	secs = N / float(fs)
	t = scipy.arange(0, secs, Ts)
	#wczytywanie drugiego sygnału
	fs1, data2 = wavfile.read(name2)
	l_audio = len(data1.shape)
	if l_audio == 2:
		data2 = data2.sum(axis=1) / 2
	index = np.argmax(data1)
	index1 = np.argmax(data2)
	dif = (index-index1)
	if (dif < 0):
		dif= t[-1*dif]*pr_dz
	else:
		dif= t[dif]*pr_dz
	rat = np.argmax(data1)/np.argmax(data2)
	return dif, rat

#dif != 0, rat != 1 && rat > 0
def cal(dif, rat, d):
	tel_p = dif/(math.sqrt(rat)-1)
	tel_l = tel_p*math.sqrt(rat)
	k_tel_p = 0
	k_tel_l = 0
#kąt rozwarty po prawej stronie
	if ((math.pow(d,2)+math.pow(tel_l,2)) > math.pow(tel_p,2)) and tel_l>tel_p:
		c = (math.pow(tel_l,2)-math.pow(tel_p,2)-math.pow(d,2))/(2*d)
		print c, tel_l, tel_p
		h = math.pow(tel_l,2)-math.pow(c,2)
		h = math.sqrt(abs(h)) # pierwiastek z h
		k_tel_l = math.asin(h/(d+c))
		k_tel_p = math.asin(h/(c))
		print "kąt rozwarty po prawej stronie"
#kąt prosty po prawej
	if ((math.pow(d,2)+math.pow(tel_l,2)) == math.pow(tel_p,2)):
		k_tel_l = math.asin(tel_p/d)
		k_tel_p = math.pi/3
		print "kąt prosty po prawej"
#kąt ostry po prawej stronie
	if (((math.pow(d,2)+math.pow(tel_l,2)) < math.pow(tel_p,2)) and (tel_l>tel_p)):
		c = (-1*math.pow(tel_l,2)+math.pow(tel_p,2)+math.pow(d,2))/(2*d)
		h = math.pow(c,2)-math.pow(tel_p,2)
		h = math.sqrt(abs(h)) # pierwiastek z h
		k_tel_l = math.asin(h/(d-c))
		k_tel_p = math.asin(h/(c))
		print "kąt ostry po prawej stronie"
#kąt ostry po lewej stronie
	if (((math.pow(d,2)+math.pow(tel_l,2)) < math.pow(tel_p,2)) and (tel_l<tel_p)):
		c = (-1*math.pow(tel_p,2)+math.pow(tel_l,2)+math.pow(d,2))/(2*d)
		h = math.pow(c,2)-math.pow(tel_l,2)
		h = math.sqrt(abs(h)) # pierwiastek z h
		k_tel_l = math.asin(h/(c))
		k_tel_p = math.asin(h/(d-c))
		print "kąt ostry po lewej stronie"
#kąt prosty po lewj
	if ((math.pow(d,2)+math.pow(tel_p,2)) == math.pow(tel_l,2)):
		k_tel_l = math.pi/3
		k_tel_p = math.asin(tel_l/d)
		print "kąt prosty po lewj"
#kąt rozwarty po prawej stronie 
	if ((math.pow(d,2)+math.pow(tel_p,2)) > math.pow(tel_l,2))and tel_l<tel_p:
		c = (math.pow(tel_p,2)-math.pow(tel_l,2)-math.pow(d,2))/(2*d)
		h = math.pow(tel_l,2)-math.pow(c,2)
		h = math.sqrt(abs(h)) # pierwiastek z h
		k_tel_p = math.asin(h/(d+c))
		k_tel_l = math.asin(h/(c))
		print "kąt rozwarty po lewj stronie "
	return tel_l, tel_p, math.degrees(k_tel_l), math.degrees(k_tel_p)




data1 = sys.argv[1]
data2 = sys.argv[2]
x = synchro(data1, data2)
print x[0]
cal(x[0],x[1], float(sys.argv[3]))
