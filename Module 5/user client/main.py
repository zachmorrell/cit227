import threading
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe

#Need threading so that I can read and write
temp, hum, set_point = 0, 0, 0
def message_callback(client, userdata, message):
    global temp, hum, set_point
    payload_list = message.payload.decode().replace(",","").split(" ")
    temp, hum, set_point = payload_list[1], payload_list[3], payload_list[5]

def get_temp():
    print("subscribing")
    subscribe.callback(message_callback, "/cit220/test", hostname="test.mosquitto.org")

def thread_subscribe():
    while True:
        get_temp()

def thread_user():
    while True:
        handle_commands()

def handle_commands():
    # Take input
    command = str(input("What woud you like to do: "))
    list_command = command.split(" ")
    match list_command[0]:
        case "gt":
            print(f"\nDesired Temperature: {set_point}\nTemperature: {temp}\nHumidity: {hum}\n")
        case "ct":
            change_temp(list_command[1])
        case "help":
            help()
        case _:
            print(f"Unknown command {list_command[0]}")

def change_temp(user_input):
    print(f"Changing temp to {user_input}")
    publish.single("/cit220/zmorrell", user_input, hostname="test.mosquitto.org")

def help():
    print("\n=== Help ===")
    print("help - Displays this menu")
    print("gt - Gets the temperature from the system.")
    print("ct <temperature> - Changes the temperature for the system.")
    print("======\n")

if __name__ == "__main__":
    # Create threads for subscribing and listening, and handling commands
    subscribe_thread = threading.Thread(target=thread_subscribe)
    command_thread = threading.Thread(target=thread_user)

    # Start the threads
    subscribe_thread.start()
    command_thread.start()

    # Wait for threads to finish (which will be never, as they run indefinitely)
    subscribe_thread.join()
    command_thread.join()

    help()