#!/usr/bin/python

from bmp180 import bmp180
import sys
import time
import datetime
bmp = bmp180(0x77)

sys.stdout = open('output.txt',"a",0)

def temperature(arg):
    while True:
        print("Date " + str(datetime.datetime.today()))
        print("Temp: " + str(bmp.get_temp()) + " Celcius")
        print("Pressure: " + str(bmp.get_pressure()) + " Pascal")
        print("---------------------------------------------")
        time.sleep(arg)
arg=float(sys.argv[1])
temperature(arg)
