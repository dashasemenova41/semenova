import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
GPIO.setmode(GPIO.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

butdown = 10
butup = 9
GPIO.setup(butdown, GPIO.IN)
GPIO.setup(butup, GPIO.IN)

num = 0
sleep_time = 0.2

while True:
    if GPIO.input(butup) and GPIO.input(butdown):
        num = 255
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    if GPIO.input(butup) and num < 255:
        num = num + 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    if GPIO.input(butdown) and num > 0:
        num = num - 1
        print(num, dec2bin(num))
        time.sleep(sleep_time)
    GPIO.output(leds, dec2bin(num))
    