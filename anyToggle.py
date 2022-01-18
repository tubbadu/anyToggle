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




# ### ###

def isRunning(appName): #even in the background
	x = bash(f"xdotool search --class {appName}", read=True) #bash(f"pgrep {appName}", read=True)
	if not x:
		print(f"not running")
		return False
	else:
		print("running")
		return True

def isVisible(appName):
	x = bash(f"xdotool search --onlyvisible --class {appName}", read=True)
	if not x:
		print('not visible')
		return False
	else:
		print("visible")
		return True

def isFocused(appName, ID):
	focusedID = str(bash("xdotool getwindowfocus", read=True)).strip()
	print("checking for focus: ", focusedID, ID)
	if focusedID == ID:
		print("focused")
		return True
	else:
		print("not focused")
		return False

def isFocusedOLD(appName):
	x = bash("ID=$(xdotool getwindowfocus) && xdotool getwindowname $ID", read=True)
	if appName in x.lower():
		print("focused")
		return True
	else:
		print("not focused")
		return False

def minimize(ID):
	bash('xdotool windowminimize ' + ID)

def raises(ID): #in realtà non serve a un cazzo ma vabè
	bash('xdotool windowraise ' + ID)

def focus(ID):
	print("xdotool windowactivate " + ID)
	bash('xdotool windowactivate ' + ID)
	return True
	if(len(str(bash('xdotool windowactivate ' + ID, read=True)).strip()) <= 1):
		print('CASO1')
		return True
	else:
		print("CASO2")
		return False



def showWindow(ID, cmd, cmdToRaise):
	raises(ID)
	msg = bash('xdotool windowactivate ' + ID, read=True)
	if msg == '':
		#print(f"{appName} has been closed but it's still running in the background.\nrerunning...")
		if cmdToRaise: bash(cmd)
		else: runHidden(cmd)
		
		focus(ID)

def runHidden(cmd):
	subprocess.Popen([cmd])




def main(): #not used hehehe I know it won't work
	running, visible, focused = isRunning(), isVisible(), isFocused()
	
	if running:
		print("i=", i)
		if visible:
			if focused:
				print("hiding...")
				hideWindow()
			else:
				print("focusing...")
				focusWindow()
		else:
			print("showing...")
			showWindow()
			#raiseWindow()
			#focusWindow()
	else:
		print("running hidden...")
		runHidden()
		exit()
		
if __name__ == "__main__":
	pass
	#main()
