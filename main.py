#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import conv
import synchro
import cal



data1 = sys.argv[1]
data2 = sys.argv[2]






cal(synchro(data1, data2), sys.argv[3])
