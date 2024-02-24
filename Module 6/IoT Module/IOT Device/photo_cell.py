from machine import ADC
import utime as time

# Photo Cell Pin.
data_pin = 26
def get_light():
    try:
        # Initializes the data pin.
        LDR = ADC(data_pin)
        # light becomes the value, 0-65535, of the photocell.
        light = LDR.read_u16()
        # The light percent based on the max amount of light that can be measured.
        light = round(light / 65535 * 100, 2)
        # returns the string of the light percentage.
        return light
    except Exception as e:
        print(f"light: Get better at coding, something went wrong. {e}")