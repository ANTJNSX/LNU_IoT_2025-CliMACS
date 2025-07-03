import dht
import machine
import time
import webHook
import keys
from mqtt import MQTTClient

# Initialize DHT11 on GPIO28 (Pin 1)
dht_sensor = dht.DHT11(machine.Pin(0))


def checkIfWindowShouldBeOpen(temp, hum):
    if int(temp) >= 27 or int(hum) >= 60:
        webHook.send_discord_message(temp, hum)
        return True
    else:
        return False


client = MQTTClient(
    keys.AIO_CLIENT_ID,
    keys.AIO_SERVER,
    keys.AIO_PORT,
    keys.AIO_USER,
    keys.AIO_KEY,
)
client.connect()

try:
    while True:
        try:
            # Take sensor reading
            dht_sensor.measure()

            # Get temperature and humidity values
            temp = dht_sensor.temperature()
            hum = dht_sensor.humidity()

            # Check if the window should be opened
            WindowTime = False
            try:
                WindowTime = checkIfWindowShouldBeOpen(temp, hum)
            except Exception as e:
                print(f"Error sending discord webHook: {e}")

            if WindowTime:
                print("Window should be opened!")
            else:
                print("Window should not be opened.")

            try:
                # Publish temperature
                client.publish(keys.AIO_TEMP_FEED, str(temp))
                # Publish humidity
                client.publish(keys.AIO_HUM_FEED, str(hum))

                # Debug Print formatted results
                print(f"Temperature: {temp}C")
                print(f"Humidity: {hum}%")
                print("")

            except Exception as e:
                print(f"Error in MQTT operations: {e}")
        except Exception as e:
            print(f"Error reading sensor: {e}")

        # Wait a bit before the next reading
        time.sleep(30)
except KeyboardInterrupt:
    print("Keyboard interrupt detected. Exiting the loop.")
finally:
    print("Exiting the program.")
    client.disconnect()
