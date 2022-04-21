#!/usr/bin/python3
from anyToggle_functions import *

excludeApps = [ "telegram/telegram",
				"whatsapp/ffpwa"]

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

def minimizeExcluded(excluded=None):
	print("minimizing all except:", excluded)
	for app in excludeApps:
		print(app)
		ID = getID(app.split('/')[0], app.split('/')[1])
		print(ID)
		if (ID != "False" and ID != excluded):
			minimize(ID)

if __name__ == "__main__":
	minimizeExcluded()
