import os
import subprocess

cmd = "/home/tubbadu/code/GitHub/WhatsappToggle/walc.AppImage"

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

def isFocused():
	x = bash("ID=$(xdotool getwindowfocus) && xdotool getwindowname $ID", read=True)
	if 'walc' in x.lower():
		return True
	else:
		return False

def hideWA():
	IDs = bash("xdotool search --name walc", read=True).strip().split('\n')
	i = IDs[-1]
	bash('xdotool windowminimize ' + i)

def showWA():
	IDs = bash("xdotool search --name walc", read=True).strip().split('\n')
	i = IDs[-1]
	bash('xdotool windowraise ' + i)
	msg = bash('xdotool windowactivate ' + i, read=True)
	if msg == '':
		print("walc has been closed but it's still running in the background.\nrerunning...")
		runWAhidden()

def runWAhidden():
	subprocess.Popen([cmd])

def focusWA():
	IDs = bash("xdotool search --name walc", read=True).strip().split('\n')
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
		runWAhidden()
		exit()
main()
