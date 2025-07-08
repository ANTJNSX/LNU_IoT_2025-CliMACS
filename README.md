# CliMACS: Climate Monitor & Alert Controller Service

**Anton Jonsson** / aj225ef
*IoT Course Project - 02-07-2025*

Welcome to my guide for an IoT room condition monitor so that we can all breath better quality air. The tutorial/guide will walk through everything from components to connection all the way to the code and setting up visualization. The final product will be a beautiful and annoying little monitor that will analyze the temperature and humidity of the room and send you discord notifications every 20 seconds or so telling you to open a window if the humidity or the temperature is high, guaranteeing better awareness of air quality in the room. You can thank me later.

- Raspberry Pi Pico WH as the microcontroller
- DHT11 temperature/humidity sensor
- Discord Server and Webhook
- AdaFruit for visualization

**Estimated Completion Time:** 3-6 hours (depending on familiarity)

## Objective
This project solves the common problem of stale indoor air by:
- Automatically detecting when room conditions would benefit from fresh air
- Sending remote notifications via Discord
- Demonstrating simple yet core IoT concepts: sensing, processing, and cloud communication

### Why?
I wanted to do a simple project that was mainly aiming for speed and simplicity, while also doing something with notifications and possibly setting up a local webserver for the purpose of listening for notifications. In the end i found out about discord webhooks which sounded way more annoying and simpler so i went with that. As a project i just felt like this was a good justification for tracking temperature and humidity which isn't just a weather monitor for outside weather. 

### For What?
The only insights or learning moment with this is navigating the creation and setup of a personally built IoT device from the breadboard to the visual dashboard. The data gathered by the CliMACS will also help in displaying what normal air conditions are in a room during each season are which can be an interesting metric to analyze, as well as analyzing how often the window alert is triggered per season.


## Materials
*Total cost = 308kr*
| Component | Purpose | Qty | Example Source | Cost |
|-----------|---------|-----|----------------|------|
| Raspberry Pi Pico WH | Main microcontroller with WiFi | 1 | [Electrokit](https://www.electrokit.com/raspberry-pi-pico-wh) | 99kr |
| DHT11 Sensor | Temperature & humidity sensing | 1 | [Electrokit](https://www.electrokit.com/digital-temperatur-och-fuktsensor-dht11) | 49kr |
| Breadboard | Circuit assembly | 1  | [Electrokit](https://www.electrokit.com/kopplingsdack-840-anslutningar) | 69kr |
| Jumper Wires | Cables for connectivity | 1  | [Electrokit](https://www.electrokit.com/labbsladd-20-pin-15cm-hane/hane) | 52kr |
| USB Cable | Power & programming | 1 | [Electrokit](https://www.electrokit.com/usb-kabel-a-hane-micro-b-5p-hane-vinklad-1.8m) | 39kr |

### Key Components Visualized
![Raspberry Pi Pico WH](https://www.electrokit.com/resource/u1sX/ZiO/SY7Lfudpmbg/product/41019/41019114/PICO-WH-HERO.jpg)
*Raspberry Pi Pico WH pinout*

![DHT11 Sensor](https://www.electrokit.com/upload/product/41015/41015728/41015728.jpg)
*DHT11 temperature/humidity sensor*

![Breadboard](https://www.electrokit.com/upload/product/10160/10160840/10160840.jpg)
*BreadBoard with 840 connections*

![Cables](https://www.electrokit.com/upload/product/41012/41012909/41012909.jpg)
*Connection wires male/male*

![USB Cable](https://www.electrokit.com/resource/u4QP/eca/sv06sUBR5Lm/product/41016/41016993/41016993.jpg)
*Connection to rpi pico for programming and power*

## Computer Setup
I did this on an older Laptop running Ubuntu, and no tools that are used are unique to Linux so there is no problem between doing with on other linux distributions or on windows.
### Required Software
1. **Visual Studio Code** ([Download](https://code.visualstudio.com/))
2. **Pymakr Extension** (VS Code Marketplace)
3. **MicroPython Firmware** for Pico W ([Download](https://micropython.org/download/rp2-pico-w/))

### Configuration Steps
1. Flash MicroPython to Pico W:
   - First go to the MicroPython firmware website and download the latest version.
   - Hold BOOTSEL button while plugging in USB, then wait for a new drive to pop up.
   - Drag-n-drop downloaded `.uf2` file to RPI-RP2 drive
   - Wait for the drive to disappear from your computer and the Pico to reboot, then you can unplug the Pico
2. Install Pymakr in VS Code:
   - Search for "Pymakr" in Extensions and install it
   - There will be a new icon on the left side, click it and create a new project
   - After creating the project plug the Pico into your computer
   - there should be a new device that pops up and is available for connecting, do so
   - Now your Pico is connected to your computer and ready to flash code onto it
   - By clicking the "Start development mode" button the code will be flashed over to the pico when a file changes in the project.

### Connectivity
The hardware connection part of this project is extremely easy since its just one component that needs three things from the pico, power, ground, and a signal receiver. So set down the pico on a the breadboard such that the USB input of the pico faces away from the rest of the board. Then set the dht11 sensor on the other side of the board so that pins can be connected directly in front of it. Then with the dht11 facing you, the blue sensor part, from left to right the pins are as follows: signal, power, ground. With this we can now connect the pins from the dht11 to the pico with some help from the following diagram. 

![Rpi pico wh pinout](https://diyprojectslabs.com/wp-content/uploads/2022/10/Raspberry_pi_pico_w_pinout.png)

So now we can connect the signal ping of the dht11, the left one, to pin number one, which in the diagram is also known to the gp0. Then for the middle pin we connect it to power which will be pin number 36, also known on the diagram as 3V3(OUT) which will supply enough power for the sensor to do its job. Lastly the ground we connect to pin number 3 which on the diagram is GND.

![IoTPicoBoardDiagram](https://hackmd.io/_uploads/BJBOc-EHgx.png)
This diagram should help in visualizing what the final connections should mimic, although the points are not precise in where they are connected the previous instructions mentioned exactly where which pin is supposed to go. So for clarity sake the blue arrow show the signal output from the dht11 and is supposed to be connected to pin number 1. The red arrow in the middle is power and will be connected to pin number 36. and the last arrow on the right side marked as a brown colour is ground and will be connected to pin number 3.

On the topic of voltage and electrical details there really is not much to be said since the dht11 has a built in resistor which makes the connectivity very simple, the 3 volt connection from the pico proved to be enough for the project to run so there was no need to limit test the power on the dht11.

### Electrical calculations
Since the dht11 has a built in resistor it is as simple as the dht11 draws 0.5-2.5mA from the picos 3.3V pin, which well within its 300mA output limit of the picos 3.3V pin.

## Platform
The platform i chose for visualizing the data gathered by CliMACS became AdaFruit since they had the most straight forward way of sending the data while also offering enough free features for this project to work with. If some sort of expansion is required then there is a paid plan for 10 dollars(~95kr) which would offer more available data storage, more frequent updates to data per minute, along with many more features. Communication wise they use the MQTT protocol to receive and broker the data to the correct place. Which also makes the code to send the data very simple. Although this is not a project that really could scale very far besides having multiple sensors in multiple rooms if scaling up would be necessary, lets say we have a metropolitan level CliMACS distribution, we would then need a big data level of data collection service which AdaFruit would not be able to handle on its own. In that scenario switching to something like AWS IoT would be a better fit. Since its built to handle big data and thousands of IoT devices while automatically scaling when more IoT devices connect without infrastructure management. Thus compared to other choices like AWS IoT adafruit was superior for smaller projects like this aswell as cost since it is completely free to a certain degree that wont be hit soon.

### Code Structure

The code for this project is mainly made in a modular way such that main.py can call the methods necessary while also handling the main logic.

- **`main.py`**: The main application logic. It reads temperature and humidity from the DHT11 sensor, checks if a window should be opened, sends alerts to Discord via the discord webhook, and publishes sensor data to Adafruit using MQTT.
- **`boot.py`**: Handles the WiFi connectivity at startup, making sure the pico is connected to the network before running the main logic.
- **`keys.py`**: Stores all sensitive configuration such as WiFi credentials and Adafruit keys. This file is largely left unset since it completely depends on your keys and wifi credentials.
- **`webHook.py`**: Contains the function to send a formatted alert messages to a Discord channel using the webhook.
- **`mqtt.py`**: (Provided by the course) Implements the MQTT protocol for sending data to Adafruit.

All code is available in my [GitHub repository](https://github.com/ANTJNSX/LNU_IoT_2025-CliMACS).

### Transmitting the Data / Connectivity

#### How often is the data sent?
- The pico reads sensor data and transmits it every **30 seconds**. This interval is set in `main.py` using `time.sleep(30)` at the end of each loop.

#### How does the Rpi Pico communicate?
- **WiFi (IEEE 802.11)** is used for all network communication. The Raspberry Pi Pico W connects to the local WiFi network using credentials stored in `keys.py`.

#### Which transport protocols were used?
- **MQTT**: Is used to publish temperature and humidity data to Adafruit. MQTT is a lightweight publish/subscribe messaging protocol,it is good for IoT applications and is what adafruit uses in this case.
- **HTTP Webhook**: Is used to send the alert messages to Discord. When a threshold is exceeded, an HTTP POST request is made to a Discord webhook URL.

#### Design Choices and Their Implications

- **WiFi** was chosen for its ease of use and compatibility with the Raspberry Pi Pico W. It was the easiest to implement for this case and proved to be sufficient enough for the project, while its not the most optimal in the case of potential scalability, where Lora or zigbee could be better in terms of range and power consumption. 
- **MQTT** was selected for sending sensor data to Adafruit due to it being the standard for the case and being the default choice for this application.
- **HTTP Webhook** is used for alerting because it is simple to implement and integrates easily with services like Discord. However, HTTP requests require more resources than something like MQTT messages.
- **Security**: Sensitive information (WiFi credentials, API keys) is kept in `keys.py`, which is not tracked by version control. This reduces the risk of accidental exposure. For actual production or public deployments, it would be better to use some more secure (TLS/SSL) connections for both MQTT and webhooks to protect data in transit.
- **Battery Consumption**: The use of WiFi and frequent transmissions increases the power consumption. For battery powered applications i would consider increasing the interval or using a lower power wireless protocol that are more optimized as previously mentioned.

---

### Example Code Snippet
This is a small code snippet from the main.py with the exception of it having the comments and debugging prints removed for clarity of whats happening, before this loop the client connection to adafruit is defined and called so that the pico can publish within the loop without the need to constantly connect and disconnect from adafruit.

```python
while True:
    dht_sensor.measure()
    temp = dht_sensor.temperature()
    hum = dht_sensor.humidity()
    if int(temp) >= 27 or int(hum) >= 60:
        webHook.send_discord_message(temp, hum)
    client.publish(keys.AIO_TEMP_FEED, str(temp))
    client.publish(keys.AIO_HUM_FEED, str(hum))
    time.sleep(30)### Code
```
    
## Presenting the data
Here is a picture from the dashboard showing the active time from testing later in the night and later in the day after.

![adafruitData](https://hackmd.io/_uploads/SJ9j6K5rel.png)

Here we can the the dashboard in action with the corresponding readings from the temperature and the humidity, captured around 12-1am, and then the day after around 4pm and forward. We can see clearly that the temperature stays largely the same throughout the hours of the day and night with some jumps here and there. The interesting part comes at the day after where upon starting to cook, since i left it on and worked in the kitchen, a door was opened and the humidity shot down, while temperature rose because of the heat from cooking and the weather outside. Since the conditions of the kitchen where not too bad in this case and preemtively opening a window we could predict that if the window was never opened the humidity would have risen from a stove/oven being on as well as multiple people being in the room that a notification that either the temperature or the humidity would have risen to a level to where a notification would have been sent and a window would have been opened to shut the notifications off.

### Data storage frequency
Since the data is sent every 30 seconds we can check on the dashboard the timestamps of when data is recieved which matches our picos frequency of sending the mqtt messages. 

This screenshot shows the frequency of the temperatures, key point is the timestamps.
![Temperature frequency](https://hackmd.io/_uploads/HJDGeDEBee.png)

### choice of database
As previously mentioned, adafruit was used for its simplicity and in the case of cloudstorage it is sufficient enough for this use-case.

### Automation
While adafruit supports automations like as triggers and actions, so that notifications can be sent via email or other webhooks, in this case we use a discord webhook in the pico there is no use for it, but for scaling up a small bit it could be beneficent to use adafruits services to reduce the code complexity of the pico and in the case of discord malfunctioning in some way adafruit will not be effected and will keep on sending notifications to open a damn window.

## Final Thoughts
Generally speaking i would say that the project went well! It did not come with many challenges except trying to get adafruit to work nicely and navigating menus. Finding correct sources for what the pins of the dht11 was which proved more challenging than what was first thought. Different sources said different things about which pin was power and signal etc, but in the end it worked out. The programming part proved to be easy as well since there where sources on how to use discord webhooks and making adafruit calls was basically given from the course which was nice. Other than that it was fun to work with IoT devices, i just wish there was more choices for visualization since it could have been fun to write a self hosted visualizer with something like Matplotlib. If i would have planned it better i would have probably written my own webserver to handle notifications that would be more annoying with spamming popups on the computer or something similar to maximize annoyance increasing the probability of a window being opened. But all in all the project was a clear success, not that its surprising since it is very simple but nevertheless it does what i wanted it to do, adjustments to conditions for alerts might be in order but that is just configuring per taste.

Boring stuff aside, here are some pictures of the project:

![Project CliMACS](https://hackmd.io/_uploads/ryV1vPEBee.png)
*Me and the project*

![BreadBoard](https://hackmd.io/_uploads/SJ2Nww4Slx.png)
*Final connected hardware (Warning, Severely complicated stuff)*

![Annoying alerts](https://hackmd.io/_uploads/rytOOv4Sle.png)
*Discord alerts in all their glory*
