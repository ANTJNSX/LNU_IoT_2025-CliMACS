import ubinascii  # Conversions between binary data and various encodings
import machine  # To Generate a unique id from processor

# wiFi configuration
WIFI_SSID = "wifi name"  # Replace with your WiFi SSID
WIFI_PASS = "wifi password"  # Replace with your WiFi password

# Adafruit IO (AIO) configuration
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "YourAIOUsername"  # Replace with your Adafruit IO username
AIO_KEY = "YourAIOKey"  # Replace with your Adafruit IO key
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())
AIO_TEMP_FEED = ""  # from Adafruit IO
AIO_HUM_FEED = ""  # from Adafruit IO
