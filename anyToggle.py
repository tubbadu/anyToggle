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
	

# ### change the followings with the program you wish to toggle ### no i was joking don't touch them
cmd = sys.argv[1] #"ferdi" #command to launch the program (may be a path to an appimage or a script as well)
appName = sys.argv[2] #"ferdi" #name of the application to search for and raise/minimize

if "--ctr" in sys.argv:
	cmdToRaise = True
else:
	cmdToRaise = False

try:
	i = bash(f"xdotool search --name {appName}", read=True).strip().split('\n')[-1]
except:
	i = 0
# ### ###

def isRunning(): #even in the background
	x = bash(f"pgrep {appName}", read=True)
	if not x:
		print(f"not running")
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
		print("focused")
		return True
	else:
		print("not focused")
		return False


def minimize():
	bash('xdotool windowminimize ' + str(i))

def raises(): #in realtà non serve a un cazzo ma vabè
	bash('xdotool windowraise ' + str(i))

def focus():
	bash('xdotool windowactivate ' + str(i))



def hideWindow():
	minimize()

def showWindow():
	raises()
	msg = bash('xdotool windowactivate ' + i, read=True)
	if msg == '':
		print(f"{appName} has been closed but it's still running in the background.\nrerunning...")
		if cmdToRaise: bash(cmd)
		else: runHidden()
		
		focusWindow()

def runHidden():
	subprocess.Popen([cmd])

def focusWindow():
	focus()
	
def raiseWindow():
	raises()



def main():
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
	main()
