import os
import subprocess
import time

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

def alignWA():
	bash('ID=$(xdotool search --onlyvisible --name walc) && xdotool windowmove $ID 0 0')

def launchWA():
	bash('walc')

def isRunning(): #even in the background
	x = bash("pgrep walc", read=True)
	if not x:
		print("not running")
		return False
	else:
		print("running")
		return True

def isVisible():
	x = bash("xdotool search --onlyvisible --name walc", read=True)
	if not x:
		print('not visible')
		return False
	else:
		print("visible")
		return True

def hideWA():
	IDs = bash("xdotool search --name walc", read=True).strip().split('\n')
	for i in IDs:
		bash('xdotool windowminimize ' + i)

def showWA():
	IDs = bash("xdotool search --name walc", read=True).strip().split('\n')
	for i in IDs:
		bash('xdotool windowraise ' + i)
		bash('xdotool windowactivate ' + i)

def runWA():
	bash('walc')

def runWAhidden():
	subprocess.Popen('walc')

def main():
	running, visible = isRunning(), isVisible()
	if running:
		if visible:
			hideWA()
		else:
			runWA()
	else:
		runWAhidden()
		time.sleep(1)
		print('relaunching!!!')
		subprocess.Popen(['python3', '/home/tubbadu/code/GitHub/WhatsappToggle/WhatsappToggle.py'])
		print("finitoooooo")
		exit()
main()