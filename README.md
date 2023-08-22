# Soft Robotics Research Extensor

# What is this?

This code uses image processing, data aquisition, and computer vision to determine the width of an object at a specified distance and opens a custom extensor to that width (mimicking a hand). This code works with a custom, calibrated set up including an IR sensor, openMV camera, arduino cricket with the cricket playground, and two air pumps. 

# Purpose 

Physical therapy machines for stroke patients struggling from clenched limbs are often expensive, large, and only available in places like hospitals. This research centers around a custom, 3D printed extensor that, when pumped with air, extends outward. This movement mimicks that of extending a hand, making this extensor perfect for patients with clenched fists. Our code works with an array of devices to allow the extensor to open to a certain width of an object surrounding it. The hope of this is to help patients with brain muscle connection when trying to pick up objects. 

# Other Uses

This code can also be used to create soft robotic fingers and hands that are extended with air pressure.

# How does it work?

UART.py is code to test the UART connection between a cricket and an openMV camera. This is test code and does not serve a purpose in the overall system.
AirPump.py converts the width data sent to an adafruit cricket by the openMV camera to a number between 0 and 1. This number is registered by the adafruit air pump as preportional to the air pressure.
cameraCode.py uses image processing to detect rectangles in objects. Then, it takes the pixels that the rectangle takes up on the screen and determines a number preportional to the width with a unit of pixels. Then an IR sensor is used to determine the distance the object is from the 

# How to use ?

You need the following materials:
1. Two adafruit air pumps
2. One adafruit cricket and the cricket playground
3. OpenMV camera
4. IR sensor

1. Download and install openMV and MU editor.
2. Load the aitPump.py file into the MU editor (A file must be named code.py to be loaded properly in MU. Rename the file to run the code)
3. Load the camera code onto openMV

# How to customize air pressure?

Lets say you have a different extensor that needs a different amount of air pressure to open to a calculated width. 

1. Comment out the current if else statements in AirPump.py or make a new copy of AirPump.py that doesnt include those.
2. Make a new if else statements that hard code the air pressure at a certain width of an object.
3. Turn on the camera and cricket and test that that air pressure is correct.
4. Keep repeating this process until you have found the perfect air pressure for that width.
5. Increase the width of the object by a predetermined number (suggested: 1 inch) and repeat this process.
6. Once you have found enough air pressure to width ratios (suggested: 4 different data points at least), graph the correlation.
7. Find the linear line of best fit
8. Go back to the original code in AirPump.py and change the values that are added and subtracted to data_float to calculate pumpVal.
9. Test new opbjects with new widths and see if the extensor properly calculates.

# Limitations 
1. Camera.py only detects rectangles, so if an object is circular, it may have a harder time determining an accurate measurement and therefore, opening the extensor to an accurate width. 
2. Air is not sucked out of the extensor when a different object is detected. This means if the object is smaller than the previous one, the opening of the extensor will decrease but may still be slightly too large to fit around the object. 
