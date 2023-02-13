#!/usr/bin/python3 

#TODO 
# 
# sistemare l'allineamento delle app
# 
# aggiungere la possibilità di specificare negli argomenti name="appname" and/or class="appclass"
# 
#TODO

from anyToggle_functions import *
from minimizeExcluded import *

import os
import subprocess
import sys

def help():
	print('AnyToggle by Tubbadu\n\nusage:\n path/to/script/anyToggle.py --name "app name" --class "app class" --cmd "cmd_to_run_app" [--raise-cmd "cmd_to_raise_app"] [--no-interact]\n\n see https://github.com/tubbadu/anyToggle for more information')
	exit()

def toggle(c, n, cmd, raiseCmd, NoInteract):
	running, Id = isRunning(n, c) #running has the id, should change with a proper name
	#print("<", isRunning(n, c), ">")
	#print(Id)
	if(running):
		focused = isFocused(Id)
		if(focused):
			#minimize
			minimize(Id)
		else:
			#activate
			if(raiseCmd == None):
				focus(Id)
			else:
				runHidden(raiseCmd)
	else:
		runHidden(cmd)

	if(not NoInteract):
		minimizeExcluded(Id)

def main():
	# flags: --class --name --cmd --raise-cmd --no-interact
	args = sys.argv[1:]
	Class = None
	Name = None
	Cmd = None
	RaiseCmd = None
	NoInteract = False

	if "-h" in args or "--help" in args:
		help()

	if "--class" in args:
		Class = args[args.index("--class") + 1]
	elif "-c" in args:
		Class = args[args.index("-c") + 1]
	
	if "--name" in args:
		Name = args[args.index("--name") + 1]
	elif "-n" in args:
		Name = args[args.index("-n") + 1]
	else:
		Name = ""
	
	if "--cmd" in args:
		Cmd = args[args.index("--cmd") + 1]
	
	if "--raise-cmd" in args:
		RaiseCmd = args[args.index("--raise-cmd") + 1]
	
	if "--no-interact" in args:
		NoInteract = True
	
	if Class == None or Name == None:
		print("parameter error: Must specify --class [class] and --name [name]")
		exit(1)
	else:
		toggle(Class, Name, Cmd, RaiseCmd, NoInteract)







if __name__ == "__main__":
	main()
