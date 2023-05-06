# anyToggle

toggle ANY application! (X11 only)

> *NOTE:* I will no longer take care of this project, as I'm developing [KToggle](https://github.com/tubbadu/ktoggle) that does work under both Xorg and Wayland (requires kwin tho)

## dependencies:

+ `python3` 
+ `xdotool`

## preparation:

```bash
#clone this repository
git clone https://github.com/tubbadu/anyToggle
#move to the folder
cd anyToggle
#make the scripts executables
chmod +x anyToggle.py
chmod +x minimizeExcluded.py
#and you're ready to go!
```

+ *[optional]* set a window rule to exclude your application from task manager and from window switcher
+ *[optional]* if you want, fix its position (also as a window rule) and remove the border and buttons
+ assign the script to a keyboard shortcut or a panel button and enjoy!

## usage:

the basic syntax to use AnyToggle is this:

```bash
path/to/script/anyToggle.py --name "app name" --class "app class" --cmd "cmd_to_run_app" [optional flags]
```

`

+ `"cmd_to_run_app"` must be a command or a path to a script, dunno why other inline scripts doesn't work [EDIT: I do know but I'm too lazy to fix this]

+ `"app class"` is the class that xdotool will search for, usually the app name. if you are not sure, use `xdotool search --class "app_class"`  with your app opened, you should see a list of IDs if the class you specified is correct

+ `--raise-cmd "cmd_to_raise"` optional, is used when the app close the window when getting minimized and needs a command to be run in order to maximize it (e.g: Telegram with particular settings, when closed needs `telegram` to be run in order to maximize and focus it)

+ `--no-interact` optional, is used when the app has to be toggled alone, without minimizing anything else (if you are not sure if using this or not, use it)

## known issues:

* `"cmd_to_run_app"` has to be a script and not any command (and so for ) `"cmd_to_raise"`

## TODO:

* change --no-interact in --interact (perhaps?)
* allow `"cmd_to_run_app"` to be any command
* add Wayland support (I'll probably die before implementing this)
