# Whatsapp Toggle 
toggle WALC application!

## dependencies:
```walc``` of course :P
```xdotool```

## preparation
+ set a window rule to exclude walc application from task manager and from window switcher
+ if you want, fix its position (also as a window rule) and remove the border and buttons
+ assign this script to a button in a panel, so that it will be faster to call it with just a click

## other applications
could be extended to other applications, but needs a bit of work because:
+ `IDs[-1]` works for walc because it always has 3 process, and the last one is the GUI one, with other applications you'll need to change the selector, eventually use a `for i in IDs` and raise / minimize every istances of the application, so that only the GUI ones will be involved
+ the double `runWAhidden()` works for walc because the first one launches the program and the second one raises it, with other applications it may work differently

