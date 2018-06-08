#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import sys

d = float(sys.argv[3])
dif = float(sys.argv[1])
rat = float(sys.argv[2])
print type(dif), type(rat), type(d)

#dif != 0, rat != 1 && rat > 0
def cal(dif, rat):
	tel_p = dif/(math.sqrt(rat)-1)
	tel_l = tel_p*math.sqrt(rat)
	k_tel_p = 0
	k_tel_l = 0
#kąt rozwarty po prawej stronie
	if ((math.pow(d,2)+math.pow(tel_l,2)) > math.pow(tel_p,2)) and tel_l>tel_p:
		c = (math.pow(tel_l,2)-math.pow(tel_p,2)-math.pow(d,2))/(2*d)
		h = math.pow(tel_l,2)-math.pow(c,2)
		h = math.sqrt(1) # pierwiastek z h
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
		h = math.sqrt(1) # pierwiastek z h
		k_tel_l = math.asin(h/(d-c))
		k_tel_p = math.asin(h/(c))
		print "kąt ostry po prawej stronie"
#kąt ostry po lewej stronie
	if (((math.pow(d,2)+math.pow(tel_l,2)) < math.pow(tel_p,2)) and (tel_l<tel_p)):
		c = (-1*math.pow(tel_p,2)+math.pow(tel_l,2)+math.pow(d,2))/(2*d)
		h = math.pow(c,2)-math.pow(tel_l,2)
		h = math.sqrt(1) # pierwiastek z h
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
		h = math.sqrt(1) # pierwiastek z h
		k_tel_p = math.asin(h/(d+c))
		k_tel_l = math.asin(h/(c))
		print "kąt rozwarty po lewj stronie "
	return tel_l, tel_p, math.degrees(k_tel_l), math.degrees(k_tel_p)


print cal(dif,rat)
