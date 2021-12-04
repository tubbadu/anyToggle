#!/usr/bin/python3 

from anyToggle import *

import os
import subprocess
import sys

def getIDs(names):
	print(names)
	IDs = list()
	for name in names:
		try:
			print(f"bash: xdotool search --name {name}")
			i = bash(f"xdotool search --name {name}", read=True).strip().split('\n')[-1]
		except:
			i = 0
		IDs.append(i)
	return IDs

def minimizeExcluded(excludeAppNames):
	print("minimize excluded:", excludeAppNames)
	for ID in getIDs(excludeAppNames):
		print("minimizing:", ID)
		if(ID): minimize(ID)

def operate(appName, cmd, cmdToRaise):
	running, visible, focused = isRunning(appName), isVisible(appName), isFocused(appName)
	ID = getIDs([appName])[0]
	print(appName, "ID=", ID)
	if running:
		if visible:
			if focused:
				print("hiding...")
				minimize(ID)
			else:
				print("focusing...")
				focus(ID)
		else:
			print("showing...")
			showWindow(ID, cmd, cmdToRaise)
			#raiseWindow()
			#focusWindow()
	else:
		print("running hidden...")
		runHidden(cmd)
		exit()


def alignToPanel():
	filepath = "/home/tubbadu/code/GitHub/panelToggle/panelHeight.txt"
	with open(filepath, "r") as fp:
		size = int(fp.read().strip())
	for app in ["qalculate", "ferdi", "whatsdesk", "telegram"]:
		bash(f'"/home/tubbadu/code/GitHub/panelToggle/windowMove.py" {app} {size-1} 0')


def main():
	cmd = sys.argv[1] #"ferdi" #command to launch the program (may be a path to an appimage or a script as well)
	appName = sys.argv[2] #"ferdi" #name of the application to search for and raise/minimize
	#excludeAppNames = "ferdi/telegram/whatsdesk/stograncazzo"#sys.argv[3] #list of application names separated by a '/' to be minimized
	#excludeAppNames = excludeAppNames.split("/")
	#if appName in excludeAppNames and "--alone" not in sys.argv:
	#	excludeAppNames.remove(appName)
	if "--ctr" in sys.argv:
		cmdToRaise = True
	else:
		cmdToRaise = False
	operate(appName, cmd, cmdToRaise)
	subprocess.Popen(["/home/tubbadu/code/GitHub/anyToggle/minimizeExcluded.py", appName])

	#minimizeExcluded(excludeAppNames)
	






if __name__ == "__main__":
	main()
