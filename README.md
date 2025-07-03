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
| Component | Purpose | Qty | Example Source |
|-----------|---------|-----|---------------|
| Raspberry Pi Pico WH | Main microcontroller with WiFi | 1 | [Electrokit](https://www.electrokit.com/raspberry-pi-pico-wh) |
| DHT11 Sensor | Temperature & humidity sensing | 1 | [Electrokit](https://www.electrokit.com/digital-temperatur-och-fuktsensor-dht11) |
| Breadboard | Circuit assembly | 1  | [Electrokit](https://www.electrokit.com/kopplingsdack-840-anslutningar) |
| Jumper Wires | Cables for connectivity | 1  | [Electrokit](https://www.electrokit.com/labbsladd-20-pin-15cm-hane/hane) |
| USB Cable | Power & programming | 1 | [Electrokit](https://www.electrokit.com/usb-kabel-a-hane-micro-b-5p-hane-vinklad-1.8m) |

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

### Connectivity
The hardware connection part of this project is extremely easy since its just one component that needs three things from the pico, power, ground, and a signal receiver. So set down the pico on a the breadboard such that the USB input of the pico faces away from the rest of the board. Then set the dht11 sensor on the other side of the board so that pins can be connected directly in front of it. Then with the dht11 facing you, the blue sensor part, from left to right the pins are as follows: signal, power, ground. With this we can now connect the pins from the dht11 to the pico with some help from the following diagram. 

![Rpi pico wh pinout](https://diyprojectslabs.com/wp-content/uploads/2022/10/Raspberry_pi_pico_w_pinout.png)

So now we can connect the signal ping of the dht11, the left one, to pin number one, which in the diagram is also known to the gp0. Then for the middle pin we connect it to power which will be pin number 36, also known on the diagram as 3V3(OUT) which will supply enough power for the sensor to do its job. Lastly the ground we connect to pin number 3 which on the diagram is GND.

![IoTPicoBoardDiagram](https://hackmd.io/_uploads/BJBOc-EHgx.png)
This diagram should help in visualizing what the final connections should mimic, although the points are not precise in where they are connected the previous instructions mentioned exactly where which pin is supposed to go. So for clarity sake the blue arrow show the signal output from the dht11 and is supposed to be connected to pin number 1. The red arrow in the middle is power and will be connected to pin number 36. and the last arrow on the right side marked as a brown colour is ground and will be connected to pin number 3.

On the topic of voltage and electrical details there really is not much to be said since the dht11 has a built in resistor which makes the connectivity very simple, the 3 volt connection from the pico proved to be enough for the project to run so there was no need to limit test the power on the dht11.

## Platform
The platform i chose for visualizing the data gathered by CliMACS became AdaFruit since they had the most straight forward way of sending the data while also offering enough free features for this project to work with. If some sort of expansion is required then there is a paid plan for 10 dollars(~95kr) which would offer more available data storage, more frequent updates to data per minute, along with many more features. Communication wise they use the MQTT protocol to receive and broker the data to the correct place. Which also makes the code to send the data very simple. Although this is not a project that really could scale very far besides having multiple sensors in multiple rooms if scaling up would be necessary, lets say we have a metropolitan level CliMACS distribution, we would then need a big data level of data collection service which AdaFruit would not be able to handle on its own. In that scenario switching to something like AWS IoT would be a better fit. Since its built to handle big data and thousands of IoT devices while automatically scaling when more IoT devices connect without infrastructure management. 

### Code
