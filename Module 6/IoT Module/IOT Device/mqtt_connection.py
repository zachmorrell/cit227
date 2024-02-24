import utime as time
from umqtt.simple import MQTTClient

mqtt_server = 'test.mosquitto.org'
client_id = 'Zach'
msh_handler = None

# Creates the connection to the MQTT Server.
def mqtt_connect():
    client = MQTTClient(client_id, mqtt_server, keepalive=3600)
    client.set_callback(sub_cb)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

# Reconnects if it disconnects from the MQTT Server.
def reconnect():
    print('Failed to connect to the MQTT Broker. Reconnecting...')
    time.sleep(5)
    machine.reset()

# Initilizes the MQTT Client, through the mqtt_connect call.
def activate_mqtt():
    try:
        global client
        print('attempting to connect to mqtt broker')
        client = mqtt_connect()
    except OSError as e:
        reconnect()
        time.sleep(3)

# Function to check the topic for new posts.
def check_sub():
        client.subscribe(b'/cit220/zmorrell')

# Function to decode message from subscribed topic.
def sub_cb(topic, msg):
    msg = msg.decode('utf-8')
    
    global msg_handler
    if msg_handler:
        msg_handler(msg)

# Function to publish to mqtt server.
def publish_topic(topic_msg):
    topic_pub = b'/cit220/test'
    client.publish(topic_pub, topic_msg)

# Sets the handler, in main, to handle the message.
def set_msg_handler(handler):
    global msg_handler
    msg_handler = handler