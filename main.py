# LEGO type:standard slot:0 autostart
# The above line allows VS Code Lego Spike Extension to upload and run code.

# region Imports 
from math import *
import sys

from hub import battery
from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import equal_to, greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, not_equal_to
# endregion

# region Initialization
my_hub = PrimeHub()
distance_sensor = DistanceSensor('C')
right_sensor = ColorSensor('F')
left_sensor = ColorSensor('B')
wheels = MotorPair('A', 'E')
wheels.set_motor_rotation(20)
matrix = LightMatrix()
# endregion


# region Functions
def check_battery():
    BATTERY_OK = '\033[32m'
    BATTERY_LOW = '\033[31m'
    ENDC = '\033[0m'
    VOLTAGE_THRESHOLD = 8000  # Threshold for battery level
    
    #Battery voltage printout in console for monitoring charge
    if battery.voltage() < VOLTAGE_THRESHOLD: 
        print(BATTERY_LOW + "battery voltage is too low: " + str(battery.voltage()) + 
              " \n ----------------------------- \n >>>> please charge robot <<<< \n ----------------------------- \n"
              + ENDC)
    else:
        print(BATTERY_OK + "battery voltage: " + str(battery.voltage()) + ENDC)


def print_module_objects_and_attributes(module_name):
    module = __import__(module_name)
    print("Module: ", module_name)
    objects = dir(module)

    for obj_name in objects:
        obj = getattr(module, obj_name)
        attributes = dir(obj)
        
        print("Object: ", obj_name)
        for attribute in attributes:
            print("- ", attribute)
        print()
# endregion

# region Main
def main():
    # ----------------  Put your code logic here  -----------------
    matrix.show_image("CLOCK8")
    wheels.move(5)
    print('distance=%d' % distance_sensor.get_distance_cm())
    
    print_module_objects_and_attributes('hub')
# endregion

# region DO NOT EDIT ANYTHING HERE 
check_battery()
print("Starting... ")
timer = Timer()
main()
sys.exit("Ended program. Elapsed time " + str(timer.now()))
# endregion
