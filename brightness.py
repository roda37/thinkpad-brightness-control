#!/usr/bin/env python
import os
import getch

print('1 to raise, 2 to lower')
while True:
    getch_input = getch.getch()
    if getch_input == '1':
        try:
            open('log', 'w')
        except FileNotFoundError:
            os.system('touch log')
        reading_brightness = os.system('cat /sys/class/backlight/intel_backlight/brightness >> log')
        with open('log', 'r') as human:
            s = int(human.read())
            multiply = s + 200
            os.system('echo ' + str(multiply) + ' >> /sys/class/backlight/intel_backlight/brightness')
    elif getch_input == '2':
        try:
            open('log', 'w')
        except FileNotFoundError:
            os.system('touch log')
        reading_brightness = os.system('cat /sys/class/backlight/intel_backlight/brightness >> log')
        with open('log', 'r') as human:
            s = int(human.read())
            multiply = s - 200
            os.system('echo ' + str(multiply) + ' >> /sys/class/backlight/intel_backlight/brightness')
