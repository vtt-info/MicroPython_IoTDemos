from machine import Pin
import time
led=Pin(16,Pin.OUT)
print("hello myLED")
while True:
  led.value(1)
  time.sleep(0.5)
  led.value(0)
  time.sleep(0.5)


