#!/usr/bin/env python3
from lewansoul_servo_bus import ServoBus

servo_bus = ServoBus('/dev/ttyUSB0')

old_id = input("What is the old ID?")
new_id = input("What is the new ID?")

servo_bus.id_write(int(old_id), int(new_id))