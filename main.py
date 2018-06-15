#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import math
import numpy as np
from scipy.io import wavfile
import scipy


#odległosc między telefonami w centymetrach
def synchro(name1, name2):
	pr_dz = 340 #m/s
	#analiza w pierwszych 200000 próbek w celu znalezienia przesunięcia czasowego nagrania
	synchr = 200000
	#ucinamy ostanie ~ 20000 próbek odsiew zakłóceń jakie pojawiają się pod koniec nagrywania
	cat = 20000
	#wczytywanie pierwszego sygnału
	fs1, data1 = wavfile.read(name1)
	l_audio = len(data1.shape)
	data1 = data1
	if l_audio == 2:
   		data1 = data1.sum(axis=1) / 2
	Ts1 = 1.0/fs1
	N1 = data1.shape[0]
	secs1 = N1 / float(fs1)
	t1 = scipy.arange(0, secs1, Ts1)
	#wczytywanie drugiego sygnału
	fs2, data2 = wavfile.read(name2)
	l_audio = len(data1.shape)
	if l_audio == 2:
		data2 = data2.sum(axis=1) / 2
	Ts2 = 1.0/fs2
	N2 = data1.shape[0]
	secs2 = N2 / float(fs2)
	t2 = scipy.arange(0, secs2, Ts2)
	#szukanie przesunięcia w nagraniach i amplitudy wynikającej z różnic technicznych
	delta = np.argmax(data2[:synchr])-np.argmax(data1[:synchr])
	conf_rat = data1[np.argmax(data1[:synchr])]/float(data2[np.argmax(data2[:synchr])])
	#conf_rat = conf_rat+data1[np.argmin(data1[:synchr])]/float(data2[np.argmin(data2[:synchr])])	
	#conf_rat = conf_rat/2

	#print "Stosunek amplitud wynikające z różnic sprzętowych "+str(conf_rat)+" lub "+str(conf_rat_1)
	
	#obliczanie różnicy i sotsunku
	index = synchr+np.argmax(data1[synchr:N1-cat])
	index1 = synchr+np.argmax(data2[synchr:N2-cat])
	
	rat = abs(data1[index]/float(data2[index1]))
	#rat = rat+abs(synchr+np.argmin(data1[synchr:N1-cat])/float(synchr+np.argmin(data2[synchr:N2-cat])))
	#rat = rat/2
	if delta <0:
		index1 = index1+delta
	else:
		index = index-delta
	dif = (index-index1)
	if (dif < 0):
		dif= t1[-1*dif]*pr_dz
	else:
		dif= t1[dif]*pr_dz

	#print conf_rat
	return dif, rat*conf_rat

#dif != 0, rat != 1 && rat > 0
#przerobić na szukanie cosunusa i przesuwanie go do przedziału [0; pi](aktualnie szukanie sinusa)
def cal(dif, rat, d):
	tel_p = float(abs(dif/(math.sqrt(rat)-1)))
	tel_l = float(tel_p*math.sqrt(rat))
	#print dif, rat, tel_p, tel_l	
	k_tel_p = 0
	k_tel_l = 0
#kąt rozwarty po prawej stronie
	if tel_l>tel_p:
		#if ((math.pow(d,2)+math.pow(tel_l,2)) > math.pow(tel_p,2)):
		c = (math.pow(tel_l,2)-math.pow(tel_p,2)-math.pow(d,2))/(2*d)
		#print c, tel_l, tel_p
		h = math.pow(tel_l,2)-math.pow(c,2)
		h = math.sqrt(abs(h)) # pierwiastek z h
		k_tel_l = math.asin(tel_l/h)
				
		k_tel_p = math.asin(tel_p/h)	
		#print "kąt rozwarty po prawej stronie"
#kąt prosty po prawej
		if ((math.pow(d,2)+math.pow(tel_l,2)) == math.pow(tel_p,2)):
			k_tel_l = math.asin(tel_p/h)
			k_tel_p = math.pi/3
#kąt ostry po prawej stronie
		if ((math.pow(d,2)+math.pow(tel_l,2)) < math.pow(tel_p,2)):
			c = (-1*math.pow(tel_l,2)+math.pow(tel_p,2)+math.pow(d,2))/(2*d)
			h = math.pow(c,2)-math.pow(tel_p,2)
			h = math.sqrt(abs(h)) # pierwiastek z h
			k_tel_l = math.asin(tel_l/h)
			k_tel_p = math.asin(tel_p/h)
#kąt ostry po lewej stronie
	if tel_l<tel_p:
		if ((math.pow(d,2)+math.pow(tel_l,2)) < math.pow(tel_p,2)):
			c = (-1*math.pow(tel_p,2)+math.pow(tel_l,2)+math.pow(d,2))/(2*d)
			h = math.pow(c,2)-math.pow(tel_l,2)
			h = math.sqrt(abs(h)) # pierwiastek z h
			k_tel_l = math.asin(tel_l/h)
			k_tel_p = math.asin(tel_p/h)
#kąt prosty po lewj
		if ((math.pow(d,2)+math.pow(tel_p,2)) == math.pow(tel_l,2)):
			k_tel_l = math.pi/3
			k_tel_p = math.asin(tel_p/h)
#kąt rozwarty po prawej stronie 
		if ((math.pow(d,2)+math.pow(tel_p,2)) > math.pow(tel_l,2)):
			c = (math.pow(tel_p,2)-math.pow(tel_l,2)-math.pow(d,2))/(2*d)
			h = math.pow(tel_l,2)-math.pow(c,2)
			h = math.sqrt(abs(h)) # pierwiastek z h
			k_tel_p = math.asin(tel_p/h)
			k_tel_l = math.asin(tel_l/h)
	return tel_l, tel_p, math.degrees(k_tel_l), math.degrees(k_tel_p)




data1 = sys.argv[1]
data2 = sys.argv[2]
x = synchro(data1, data2)
x = cal(x[0],x[1], float(sys.argv[3]))
print "Odległość 1. telefonu od źródła dźwięku = %.2f" % x[0]+" cm, dźwięk dochodzi pod kątem %.2f" %x[3]+" stopni"
print "Odległość 2. telefonu od źródła dźwięku = %.2f" %x[1]+" cm, dźwięk dochodzi pod kątem %.2f" %x[3]+" stopni"


#*.04.wav mniej więcej w tej samej odległości
#*.06.wav za duże odległości, tak samo jak dla *.07.wav
