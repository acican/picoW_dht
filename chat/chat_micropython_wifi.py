import network

def connect_to_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)  # Create a WLAN object
    wlan.active(True)  # Activate the WLAN interface

    if wlan.isconnected():
        print("Already connected to Wi-Fi")
        return

    wlan.connect(ssid, password)  # Connect to the specified Wi-Fi network

    while not wlan.isconnected():
        pass

    print("Wi-Fi connected!")
    print("Network:", wlan.config('essid'))
    print("IP address:", wlan.ifconfig()[0])

# Provide your Wi-Fi credentials here
wifi_ssid = "Your SSID"
wifi_password = "Your password"

# Connect to the Wi-Fi network
connect_to_wifi(wifi_ssid, wifi_password)
