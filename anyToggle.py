#!/usr/bin/python3

import os
import subprocess

# ### change the followings with the program you wish to toggle ###
cmd = "ferdi" #command to launch the program (may be a path to an appimage or a script as well)
appName = "ferdi" #name of the application to search for and raise/minimize
# ### ###
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

def isRunning(): #even in the background
	x = bash(f"pgrep {appName}", read=True)
	print(f"running? <{x}>")
	if not x:
		print(f"not running: <{x}>")
		return False
	else:
		print("running")
		return True

def isVisible():
	x = bash(f"xdotool search --onlyvisible --name {appName}", read=True)
	if not x:
		print('not visible')
		return False
	else:
		print("visible")
		return True

def isFocused():
	x = bash("ID=$(xdotool getwindowfocus) && xdotool getwindowname $ID", read=True)
	if appName in x.lower():
		print("is focused")
		return True
	else:
		print("is not focused")
		return False

def hideWA():
	IDs = bash(f"xdotool search --name {appName}", read=True).strip().split('\n')
	i = IDs[-1]
	bash('xdotool windowminimize ' + i)

def showWA():
	IDs = bash(f"xdotool search --name {appName}", read=True).strip().split('\n')
	i = IDs[-1]
	bash('xdotool windowraise ' + i)
	msg = bash('xdotool windowactivate ' + i, read=True)
	if msg == '':
		print(f"{appName} has been closed but it's still running in the background.\nrerunning...")
		runWAhidden()

def runWAhidden():
	subprocess.Popen([cmd])

def focusWA():
	IDs = bash(f"xdotool search --name {appName}", read=True).strip().split('\n')
	i = IDs[-1]
	bash('xdotool windowactivate ' + i)

def main():
	running, visible, focused = isRunning(), isVisible(), isFocused()
	if running:
		if visible:
			if focused:
				hideWA()
			else:
					focusWA()

		else:
			showWA()
	else:
		runWAhidden()
		#runWAhidden()
		exit()
main()
