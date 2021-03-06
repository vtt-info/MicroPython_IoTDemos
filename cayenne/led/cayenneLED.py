#
# cayenneLED.py
# gets command information from a Cayenne button and switches on/off the
# built-in LED on the WeMos D1 CPU card
# copyright U. Raich
# This is a demo program for the workshop  on IoT at the African Internet Summit 2019
# Released under GPL
#
from machine import Pin,ADC
import cayenne.client
import time
import logging

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "7c70a330-69af-11e8-a76a-fdebb8d0010d"
MQTT_PASSWORD  = "32d184add41570759dd1735fa464cef7e62876a4"
MQTT_CLIENT_ID = "dae86710-4ae9-11e9-a6b5-e30ec853fbf2"

global ledChannel
global builtinLed
ledChannel = 9
builtinLed = Pin(2,Pin.OUT)

# callback routine to treat command messages from Cayenne
def on_message(message):
    global ledChannel
    msg = cayenne.client.CayenneMessage(message[0],message[1])
    if msg.channel == ledChannel:
        if int(msg.value) == 1:         # the builtin LED is actice low
            builtinLed.value(0)
        else:
            builtinLed.value(1)
        if int(msg.value) == 1:
            print("Switching built-in led on");
        else:
            print("Switching built-in led off");
    return

# switch LED off
builtinLed.value(1)                # active low

client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, loglevel=logging.INFO)
# register callback
client.on_message=on_message

while True:
    client.loop()
    time.sleep(1)

