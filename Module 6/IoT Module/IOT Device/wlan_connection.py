import network

# SSID or Wi-Fi username
SSID = 'NETGEAR32'
PASSWORD = 'fancyzoo312'

#Connect to WLan.
def connect():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(SSID,PASSWORD)
    print("Attempting to connect through Wi-Fi..")
    #Network: check if connected
    while not wifi.isconnected():
        pass    
    print('Connected to WiFi', wifi.ifconfig())