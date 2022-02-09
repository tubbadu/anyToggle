# anyToggle

toggle ANY application!

## dependencies:

+ a linux distribution (successfully tested on Kubuntu 21.10)
+ `python3` 
+ `xdotool`

## preparation:

+ clone this repository somewhere in your PC
+ made the main script executable: `chmod +x path/to/script/anyToggle_main.py`
+ create a custom shortcut (mine is META+W) that run `path/to/script/anyToggle_main.py [param]`, or assign this command to a button or a launcher in a panel
+ *[optional]* set a window rule to exclude your application from task manager and from window switcher
+ *[optional]* if you want, fix its position (also as a window rule) and remove the border and buttons

## usage:

the basic syntax to use AnyToggle is this:

`path/to/script/anyToggle_main.py "cmd_to_run_app" "app_class" [optional flags]`

+ `"cmd_to_run_app"` must be a command or a path to a script, dunno why other inline scripts doesn't work

+ `"app_class"` is the class that xdotool will search for, usually the app name. if you are not sure, use `xdotool search --class "app_class"`  with your app opened, you should see a list of IDs if the class you specified is correct

+ `[--no--background]` is used when the minimized app does not close the main window (almost every application needs this)

+ ` [--ctr] ` is used when an app gets closed when minimized (e.g. telegram) has to be raised with the same command that was used to run it 

+ `[--no-interact]` is used when the app has to be toggled alone, without minimizing anything else (if you are not sure if using this or not, use it)

## known issues:

* the code is a mess lol I have to tidy it up one day

* `"cmd_to_run_app"` has to be a script and not any command

## TODO:

* tidy up the code hehe
* use a flag to search for name instead class
* change --no-background in --background
* change --no-interact in --interact
