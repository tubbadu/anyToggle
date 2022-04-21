#!/usr/bin/python3

import os
import subprocess
import sys

def bash(cmd, read=False):
	if read:
		try:
			x = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			x = False
		return x
	else:
		os.system(cmd)
		return


def getID(n, c):
	xSearchClass = str(bash(f"xdotool search --class {c}", read=True)).strip().split()
	xSearchName = str(bash(f"xdotool search --name {n}", read=True)).strip().split()
	for xc in xSearchClass[::-1]: #because some apps have multiple istances visibles, but just the last one is the GUI one
		for xn in xSearchName:
			if xc == xn:
				return xc
	#no match
	return "False"

def isRunning(n, c): #even in the background
	x = getID(n, c) #bash(f"xdotool search --class {c} | grep $(xdotool search --name {n})", read=True)
	print("x =", x)
	if x == "False": 
		print(f"not running")
		return (False, "0")
	else:
		print("running!!!")
		return (True, str(x).strip())


def isFocused(ID):
	focusedID = str(bash("xdotool getwindowfocus", read=True)).strip()
	#print("checking for focus: ", focusedID, ID)
	if focusedID == ID:
		print("focused")
		return True
	else:
		print("not focused")
		return False

def minimize(ID):
	bash('xdotool windowminimize ' + ID)


def focus(ID):
	print("xdotool windowactivate " + ID)
	bash('xdotool windowactivate ' + ID)


def runHidden(cmd):
	print("running hidden")
	subprocess.Popen([cmd])
