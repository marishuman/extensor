# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials UART Serial example"""
import board
import busio
import digitalio
import time
from adafruit_crickit import crickit



print("Dual motor demo!")

# For most CircuitPython boards:
led = digitalio.DigitalInOut(board.LED)
# For QT Py M0:
# led = digitalio.DigitalInOut(board.SCK)
led.direction = digitalio.Direction.OUTPUT

uart = busio.UART(board.TX, board.RX, baudrate=9600)



# make two variables for the motors to make code shorter to type

motor_1 = crickit.dc_motor_1
motor_2 = crickit.dc_motor_2
crickit.drive_1.frequency = 1000


while True:
    data = uart.read(7)  # read up to 32 bytes
    # print(data)  # this is a bytearray type
    if data is None:
        motor_1.throttle = 0  # full speed forward
        motor_2.throttle = 0 # full speed backward
        crickit.drive_1.fraction = 0  # all the way on
        print("Pump Air")

    elif data is not None:
        led.value = True



        # convert bytearray to string

        data_string = ''.join([chr(b) for b in data])
        data_float = float(data_string)
        print(data_float)
        pumpVal = 0
        pumpVal= 0.26*(data_float) - 0.6
        print("pressue value: " + str(pumpVal))
        if pumpVal >6:

            motor_1.throttle = 0  # full speed forward
            motor_2.throttle = 0  # full speed backward
            crickit.drive_1.fraction = 1  # all the way on
            print("Pump Air")
            # time.sleep(3)


        elif pumpVal < 0 and pumpVal > -1:

            motor_1.throttle = 0  # full speed forward
            motor_2.throttle = pumpVal  # full speed backward
            crickit.drive_1.fraction = 0  # all the way on
            print("Pump Air")
            # time.sleep(3)



        elif pumpVal > 0 and pumpVal < 1:

            motor_1.throttle = pumpVal # full speed forward
            motor_2.throttle = 0  # full speed backward
            crickit.drive_1.fraction = 1  # all the way on
            print("Pump Air")


        else:
            motor_1.throttle = 0 # full speed forward
            motor_2.throttle = 0  # full speed backward
            crickit.drive_1.fraction = 0  # all the way on
            print("Pump Air")



#    if data_float < 4:

        # motor_1.throttle = 0.9  # full speed forward
        # motor_2.throttle = 0  # full speed backward
        # crickit.drive_1.fraction = 0.5  # all the way on
        # print("Pump Air")
        # time.sleep(3)



    # elif data_float < 10:

        # motor_1.throttle = 0.0  # stopped
        # motor_2.throttle = 0.75  # also stopped
        # crickit.drive_1.fraction = 1.0  # all the way on
        # pri
