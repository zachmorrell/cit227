from machine import Pin
import utime as time
from dht import DHT11

# Pin for the temperature/humidity sensor.
data_pin = 16
# Pull down pin resistor. Resistor has to pull to read data.
resistor_pull = Pin(data_pin, Pin.OUT, Pin.PULL_DOWN)
# sensor values
sensor = DHT11(resistor_pull)

# Returns the stats from the DHT11 readings.
def print_stats():
    try:
        # Gets the Celsius measurement of sensor.
        sensor.measure()
        # Converts the temperature from Celsius to Fahrenheit.
        temp_f = sensor.temperature() * (9/5) + 32
        # Gets the humidity reading from the sensor.
        hum = sensor.humidity()
        return temp_f, hum
    except:
        print("Get better at coding, something went wrong.")