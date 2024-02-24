from machine import Pin
import utime as time

red = Pin(2, Pin.OUT)
blue = Pin(3, Pin.OUT)
offset = 2

# Returns the offset of the of temp and target
def get_target_offset(temp, target):
    return temp-target

# Blinks:
# Red light is a temperature increase is needed.
# Blue light if a temperature decrease is needed.
# Red and Blue if the temperature is good.
def toggle(temp, target, light_percent):
    temp_offset = get_target_offset(temp, target)
    allowable_offset = 2 if light_percent > 50 else 4
    print(f"allowable_offset: {allowable_offset}")
    # Temperature is too low, increase.    
    if temp_offset < -1 * allowable_offset:
        print("Temp too low, raise it")
        red.on()
        time.sleep(.5)
        red.off()
        
    # Temperature fine, blink both.
    elif temp_offset <= allowable_offset:
        print("Temperature is good.")
        red.on()
        time.sleep(.2)
        red.off()
        time.sleep(.35)
        blue.on()
        time.sleep(.2)
        blue.off()
        
     # Temperature too high, lower it.
    else:
        print("Temp too high, lower it.")
        blue.on()
        time.sleep(.5)
        blue.off()