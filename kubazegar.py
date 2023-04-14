#startup
print "Startujemy!"
device.write_text(1, "-KUBA SP9KAM-")
#dodaj kropke po N
device.letter(1, 4, "N", 1)
time.sleep(2)
mode= 1;
level = 1;
device.brightness(level)
refresh = 99;
anim = 8;




DATA

import ZeroSeg.led as led
import time
from datetime imp

def date (device, deviceId):

    now = datetime.now()
    day = now.day
    month = now.month
    year = now.year - 2000

    # Set day
    device.letter(deviceId, 8, int(day / 10))     # Tens
    device.letter(deviceId, 7, day % 10)          # Ones
    device.letter(deviceId, 6, '-')               # dash
    # Set day
    device.letter(deviceId, 5, int(month / 10))     # Tens
    device.letter(deviceId, 4, month % 10)     # Ones
    device.letter(deviceId, 3, '-')               # dash
    # Set day
    device.letter(deviceId, 2, int(year / 10))     # Tens
    device.letter(deviceId, 1, year % 10)     # Ones

device = led.sevensegment(cascaded=2)

while True:
    date(device, 1)
    time.sleep(900) #Update every 15 minutes
    device.clear()


CZAS


import ZeroSeg.led as led
import time
from datetime import datetime

def clock (device, deviceId, seconds):

    for _ in xrange(seconds):
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second
        dot = second % 2 == 0                # calculate blinking dot
        # Set hours
        device.letter(deviceId, 4, int(hour / 10))     # Tens
        device.letter(deviceId, 3, hour % 10, dot)     # Ones
        # Set minutes
        device.letter(deviceId, 2, int(minute / 10))   # Tens
        device.letter(deviceId, 1, minute % 10)        # Ones
        time.sleep(1)

device = led.sevensegment(cascaded=2)

while True:
    clock(device, 1, seconds=10)



TEXT

import ZeroSeg.led as led
import time

device = led.sevensegment(cascaded=2)

device.write_text(1,"JAKUB SP9KAM")

time.sleep(3)
device.clear()




JASNOSC

if not GPIO.input(switch2):
    if auto == 1:
        auto = 0
        mode = 1
        print
        "Auto Off"
    elif mode < 6:
        mode += 1
    else:
        mode = 1
     if mode == 1:
        device.write_text(1, "CZAS")
    if mode == 2:
        device.write_text(1, "DATA")
    if mode == 3:
        device.write_text(1, "AUTO")
    time.sleep(1)
# wskaznik jasnosci
elif not GPIO.input(switch1):
    if level <= 2:
        level = 5
    elif level == 5:
        level = 10
    elif level == 10:
        level = 14
    elif level >= 14:
        level = 1
    device.brightness(level)
    print
    "Poziom jasnosci:", level
    time.sleep(0.5);
else:
    pass
