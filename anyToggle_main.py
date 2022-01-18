#!/usr/bin/python3 

#TODO 
# 
# sistemare l'allineamento delle app
# 
# aggiungere la possibilità di specificare negli argomenti name="appname" and/or class="appclass"
# 
#TODO

from anyToggle import *

import os
import subprocess
import sys

vaffanculoAppsIHateYou = "kate/opera/dolphin".split("/")

def getIDs(names, onlyvisible=True): #for each name in names, creates a sublist with all IDs
	IDs = list()
	for name in names:
		try:
			#print(f"bash search: xdotool search --onlyvisible --class {name}")
			if(onlyvisible):
				i = bash(f"xdotool search --onlyvisible --class {name}", read=True)
			else:
				i = bash(f"xdotool search --class {name}", read=True)
			i = i.strip().split('\n')#[-1]
		except:
			i = 0
	#	for name in vaffanculoAppsIHateYou:
	#		for badID in bash(f"xdotool search --class {name}", read=True).strip().split('\n'):
	#			if badID in i:
	#				i.remove(badID)
		if(type(i) is list):
			for n in range(len(i)):
				i[n] = str(i[n])
		IDs.append(i)
	return IDs

def minimizeExcluded(excludeAppNames):
	#print("minimize excluded:", excludeAppNames)
	for ID in getIDs(excludeAppNames):
	#	print("minimizing:", ID)
		if(ID): minimize(ID)

def operateNoBackground(appName, cmd):
	running, visible = isRunning(appName), isVisible(appName)
	ID = getIDs([appName])[0]
	print("ID1=", ID)
	if(ID == 0 or ID == '0'):
		ID = getIDs([appName], onlyvisible=False)[0]
	print("ID2=", ID)
	if(type(ID) is list):
		if(len(ID) > 1): print("beware, something is wrong I can feel it:", ID)
		ID = ID[0]
	
	focused = isFocused(appName, ID)
	
	print(appName, "ID=", ID, "\nrunning, visible, focused = ", running, visible, focused)
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
			#showWindow(ID, cmd, cmdToRaise)
			#raiseWindow()
			#focusWindow()
			focus(ID)
	else:
		print("running hidden (i dunno y hidden)...")
		runHidden(cmd)
		exit()

def operate(appName, cmd, cmdToRaise):
	running, visible = isRunning(appName), isVisible(appName)
	ID = getIDs([appName])[0] #this contains a list of all IDs with appName
	if(type(ID) is list):
		if(len(ID) > 1): print("beware, something is wrong I can feel it:", ID)
		ID = ID[0]
	print("ID1=", ID)
	
	focused = isFocused(appName, ID)
	
	print(appName, "ID=", ID, "\nrunning, visible, focused = ", running, visible, focused)
	if(ID == '0' or ID == 0): 
		print("ID==0, so the app is running in the background ")
		bash(cmd)
		return
	if running:
		if visible:
			if focused:
				print("hiding...")
				minimize(ID)
			else:
				print("focusing...")
				focus(ID)
		else:
			print("running but not visible: showing...")
			#showWindow(ID, cmd, cmdToRaise)
			if(not focus(ID)):
				bash(cmd)
			#focusWindow()
	else:
		print("running hidden...")
		runHidden(cmd)
		exit()


def alignToPanel():
	filepath = "/home/tubbadu/code/GitHub/panelToggle/panelHeight.txt"
	with open(filepath, "r") as fp:
		size = int(fp.read().strip())
	for app in ["qalculate", "ferdi", "whatsdesk", "telegram", "whatsapp"]:
		bash(f'"/home/tubbadu/code/GitHub/panelToggle/windowMove.py" {app} {size-1} 0')


def help():
	print('AnyToggle by Tubbadu\n\nusage:\n path/to/anyToggle.py "path/to/launching_script.sh" "app_class_name" [--ctr] [--no-interact] [--no-background]')
	exit()

def main():
	if ('-h' in sys.argv or '--help' in sys.argv):
		help()
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

	if "--no-background" in sys.argv:
		#operate(appName, cmd, cmdToRaise)
		operateNoBackground(appName, cmd)
	else:
		operate(appName, cmd, cmdToRaise)

	if "--no-interact" not in sys.argv:
		subprocess.Popen(["/home/tubbadu/code/GitHub/anyToggle/minimizeExcluded.py", appName])

	#minimizeExcluded(excludeAppNames)
	






if __name__ == "__main__":
	main()
