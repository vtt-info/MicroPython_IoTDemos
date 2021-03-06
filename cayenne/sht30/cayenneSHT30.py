#
# cayenneDHT11.py
# Reads out the DHT11 temperature and humidity and sends the measurement
# to Cayenne
# copyright U. Raich
# This is a demo program for the workshop on IoT at the
# African Internet Summit 2019, Kampala
# Released under GPL
#
from machine import Pin
import cayenne.client
import sys,time
from sht30 import SHT30
import logging

# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "7c70a330-69af-11e8-a76a-fdebb8d0010d"
MQTT_PASSWORD  = "32d184add41570759dd1735fa464cef7e62876a4"
MQTT_CLIENT_ID = "dae86710-4ae9-11e9-a6b5-e30ec853fbf2"

sht30TempChannel = 5
sht30HumidityChannel = 6

# create SHT30 object
sht30=SHT30()
# Check if SHT30 is connected
if not sht30.is_present():
    print("Could not find SHT30 board. Please connect it")
    sys.exit()
else:
    print("Found SHT-30, let's go on")
sht30.reset()

client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID, loglevel=logging.INFO)
print("Successfully connected to myDevices MQTT broker")

def senddata():
  sht30Temperature, sht30Humidity = sht30.measure()
  print("Temperature: %6.3f"%sht30Temperature)
  client.celsiusWrite(sht30TempChannel,sht30Temperature)
  time.sleep(5)
  print("Relative humidity: %6.3f"%sht30Humidity + '%')
  client.humidityWrite(sht30HumidityChannel,sht30Humidity)
  time.sleep(5)
  
while True:
    try:
        senddata()
    except OSError:
        pass
