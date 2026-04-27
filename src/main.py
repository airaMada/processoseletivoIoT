from machine import Pin
import time

led = Pin(2, Pin.OUT)
button = Pin(4, Pin.IN)

while True:
    if button.value() == 1:
        led.on()
    else:
        led.off()
    
    time.sleep(0.1)
    