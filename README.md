# anyToggle

toggle ANY application!

## dependencies:

+ a linux distribution (successfully tested on Kubuntu 21.04)
+ `python3` 
+ `xdotool`

## preparation:

+ create a custom shortcut (mine is META+W) that run `path/to/script/anyToggle.py`, or assign this command to a button or a launcher in a panel
+ *[optional]* set a window rule to exclude your application from task manager and from window switcher
+ *[optional]* if you want, fix its position (also as a window rule) and remove the border and buttons

## known issues:

* some application, if the window is closed but they are still running in the background, when relaunched, intead of recreating the window, launch a new istance. I don't know how to get around of this problem 😞

* while searching for the application to toggle, this script only checks for the name of each window, so if a browser tab or any other application has *appName* in their title, the script will eventually toggle those window

## TODO:

* add the possibility to call the script with appName and cmd as parameters, so you don't need different copies of the script for different applications (very fast to implement, i'm just lazy)
