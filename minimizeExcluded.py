#!/usr/bin/python3
from anyToggle import *


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


excludeAppNames = "ferdi/telegram/whatsdesk/stograncazzo"#sys.argv[3] #list of application names separated by a '/' to be minimized
excludeAppNames = excludeAppNames.split("/")
try:
	appName = sys.argv[1]
	if appName in excludeAppNames and "--alone" not in sys.argv:
		excludeAppNames.remove(appName)
except:
	appName = "stocazzo"

minimizeExcluded(excludeAppNames)
