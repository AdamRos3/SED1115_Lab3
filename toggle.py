# Use the Pin method from the machine software library
from machine import Pin
import time
# Define the inputs and outputs and assign them to software objects
# First argument is a GPIO pin number, rather than a physical pin number
led1 = Pin(18, Pin.OUT)

sw5 = Pin(22, Pin.IN, Pin.PULL_DOWN)

last_state = sw5.value()
last_toggle_time = 0
DEBOUND_THRESHOLD = 50

while True:
    current_state = sw5.value()
    current_time = time.ticks_ms()
    

    if last_state == 1 and current_state == 0:
        if ((current_time - last_toggle_time) > DEBOUND_THRESHOLD):
            led1.toggle()
            last_toggle_time = current_time
    
    last_state = current_state
    time.sleep_ms(100)