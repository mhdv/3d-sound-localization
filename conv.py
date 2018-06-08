#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import subprocess

def conv():
	command = "ffmpeg -i "+str(sys.argv[1])+" -ab 160k -ac 2 -ar 44100 -vn "+str(sys.argv[2])
	print command
	subprocess.call(command, shell=True)


conv()
