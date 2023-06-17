# LEGO type:standard slot:0 autostart
from math import *
import sys

from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import equal_to, greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, not_equal_to
from hub import battery

# ----------------  Global Initialization  -----------------
hub = PrimeHub()
distance_sensor = DistanceSensor('C')
right_sensor = ColorSensor('F')
left_sensor = ColorSensor('B')
wheels = MotorPair('A', 'E')
wheels.set_motor_rotation(20)
matrix = LightMatrix()

def check_battery():
    BATTERY = '\033[32m'
    BATTERY_LOW = '\033[31m'
    ENDC = '\033[0m'
    VOLTAGE_THRESHOLD = 8000  # Threshold for battery level
    
    #Battery voltage printout in console for monitoring charge
    if battery.voltage() < VOLTAGE_THRESHOLD: 
        print(BATTERY_LOW + "battery voltage is too low: " + str(battery.voltage()) + 
              " \n ----------------------------- \n >>>> please charge robot <<<< \n ----------------------------- \n"
              + ENDC)
    else:
        print(BATTERY + "battery voltage: " + str(battery.voltage()) + ENDC)

def main():
    # ----------------  Put your code logic here  -----------------
    matrix.show_image("CLOCK8")
    wheels.move(5)
    print('distance=%d' % distance_sensor.get_distance_cm())

# --------------- DO NOT EDIT ANYTHING BELOW ----------------- 
check_battery()
timer = Timer()
print("starting... ")
main()
sys.exit("ended program. elapsed time " + str(timer.now()))
