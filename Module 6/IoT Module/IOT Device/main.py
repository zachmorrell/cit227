import wlan_connection as wlan
import temp_hum_sensors as sensors
import lights
import photo_cell
import utime as time

# Test Code:
#mosquitto_pub -h test.mosquitto.org -t "/cit220/zmorrell" -m "73"

temp = 0
hum = 0
target_temp = 68
# Function to handle the message received from mqtt broker.
def handle_msg(msg):
    print(f"--- MSG INCOMING : {msg} ---")
    try:
        global target_temp
        target_temp = int(msg)
    except:
        print("Someone failed to break me")
        
import mqtt_connection as mqtt

# Calls a fucntion in mqtt to forward the msg to the function above.
mqtt.set_msg_handler(handle_msg)

def main():
    
    # Connect to Wi-Fi
    wlan.connect()
    time.sleep(1)
    
    # Connect to mqtt broker
    mqtt.activate_mqtt()
    time.sleep(1)
    
    # Run board scripts
    while True:
        # Publish's data to broker.
        global temp, hum, target_temp
        # Retrieve temp and humidity from stat.
        temp, hum = sensors.print_stats()-
        light_percent = photo_cell.get_light()
        # Publish temp and hum to the broker.
        mqtt.publish_topic(f"temperature: {temp}, humidity: {hum}, set_point: {target_temp}, light_percent: {light_percent}")
        # Check for new messages
        mqtt.check_sub()
        # Toggle lights based on temp and set point
        lights.toggle(int(temp), target_temp, int(light_percent))
        # Sleep for 2 seconds.
        time.sleep(1.5)

main()