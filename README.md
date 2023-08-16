# Soft Robotics Research Extensor

# What is this?

This code and custom set-up uses image processing and soft robotics to determine the width of an object at a specified distance and opens a custom extensor to that width (mimicking a hand). 

# How does it work?

UART.py is code to test the UART connection between a cricket and an openMV camera. This is test code and does not serve a purpose in the overall system.
code.py converts the width data sent to an adafruit cricket by the openMV camera to a number between 0 and 1. This number is registered by the adafruit air pump as preportional to the air pressure.

# How to use ?

You need the following materials:
1. Two adafruit air pumps
2. One adafruit cricket and the cricket playground
3. OpenMV camera__

1. Download and install openMV and MU editor.
2. Load the code.py file into the MU editor (A file must be named code.py to be loaded properly in MU. If you want to test using the UART.py file, rename the file accordingly)
3. Load the camera code onto openMV

# How to customize air pressure?

Lets say you have a different extensor that needs a different amount of air pressure to open to a calculated width. 

1. Comment out the current if else statements in code.py or make a new copy of code.py that doesnt include those.
2. Make a new if else statements that hard code the air pressure at a certain width of an object.
3. Turn on the camera and cricket and test that that air pressure is correct.
4. Keep repeating this process until you have found the perfect air pressure for that width.
5. Increase the width of the object by a predetermined number (suggested: 1 inch) and repeat this process.
6. Once you have found enough air pressure to width ratios (suggested: 4 different data points at least), graph the correlation.
7. Find the linear line of best fit
8. Go back to the original code in code.py and change the values that are added and subtracted to data_float to calculate pumpVal.
9. Test new opbjects with new widths and see if the extensor properly calculates. 
