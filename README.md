# Rubik's Cube Simulator
A 3-dimensional Rubik's Cube Simulator based on isometric projection.

# Background
This project was made for "Computer Science (New)" course in class 12 under CBSE. Minimal adjustments have been made to it in the present version.

# Software requirements
Python Interpreter with tkinter module (inbuilt in the official Python Interpreter, IDLE)

# How to run
Create a folder.  
Put the given python file in it. Run the program.  
Use the on-screen buttons or keyboard to solve the cube.  
Using the "Save" option (in the program) will create a binary file in the current folder. Next time you run the program, it will show the last saved stage (or the default state if the file is corrupted).

# Keybinds
|Command|Description|
|---|---|
|j|Front|
|h|Left|  
|k|Right|
|u|Up|
|n|Down|
|i|Back|
|y|Middle (Clockwise from Right Face)|
|m|Equatorial (Clockwise from Up Face)|
|b|Slice (Clockwise from Front Face)|
|o|Whole cube rotated as Right Face Clockwise|
|u|Whole cube rotated as Up Face Clockwise|
|l|Whole cube rotated as Front Face Clockwise|
|8|Look up|
|5|Look down|
|6|Look right|
|4|Look left|
|9|Rotate clockwise|
|7|Rotate Anti-clockwise|

(For the non-numeric commands, using Shift-Key will turn them uppercase: which is detected as anti-clockwise rotation)
