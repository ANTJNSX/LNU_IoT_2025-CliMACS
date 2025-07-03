# boot.py -- run on boot-up
# Copied from guide "https://hackmd.io/@lnu-iot/rJVQizwUh"

import keys
import network
from time import sleep


def connect():
    wlan = network.WLAN(network.STA_IF)

    # Only connect if not connected
    if not wlan.isconnected():
        print("connecting to network...")
        wlan.active(True)

        # set power mode to get WiFi power-saving off (if needed)
        # wlan.config(pm=0xA11140)

        # Connect to the WiFi network using credentials from keys.py
        wlan.connect(keys.WIFI_SSID, keys.WIFI_PASS)
        print("Waiting for connection...", end="")

        # Check if it is connected otherwise wait
        while not wlan.isconnected() and wlan.status() >= 0:
            print(".", end="")
            sleep(3)

    # Print the IP assigned by router
    ip = wlan.ifconfig()[0]
    print("\nConnected on {}".format(ip))
    return ip


def http_get(url="https://detectportal.firefox.com/"):
    import socket
    import time

    print("1")
    # Separate URL request
    _, _, host, path = url.split("/", 3)

    print("2")
    # Get IP address of host
    addr = socket.getaddrinfo(host, 80)[0][-1]

    print("3")
    # Initialise the socket
    s = socket.socket()
    s.connect(addr)

    print("4")
    # Send HTTP request to the host with specific path
    s.send(bytes("GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n" % (path, host), "utf8"))
    time.sleep(1)

    print("5")
    # Receve response
    rec_bytes = s.recv(10000)
    print(rec_bytes)
    s.close()


# WiFi Connection
try:
    ip = connect()
    print("Internet is available")
except KeyboardInterrupt:
    print("Keyboard interrupt")

    # unnecessary test of HTTP request
# HTTP request
# try:
#     http_get()
# except (Exception, KeyboardInterrupt) as err:
#     print("No Internet", err)
