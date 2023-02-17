#This Software need the Solar-Assistant software on a Raspberry PI. https://solar-assistant.io/
#Written by Jaco Slabbert https://github.com/JJSlabbert/Sollar-Assistant-MQTT-client
#Codoe tested on the 5KW Sacolar (Growatt SPF) Inverter and Battery Compatable with PBMS tools (15 cell P15S100A) monitored via USB Serial RS232/RS485


import paho.mqtt.client as mqtt
import time


def return_subscription_values(client, userdata, message):
    mqtttopic=message.topic
    mqttpayload=message.payload.decode("utf-8")
    print("message payload (value) " ,mqttpayload)        
    print("message topic=",mqtttopic)
    print ("************************************************")
    
#broker_address=input("Provide the IP address of the MQTT Broker: ")
broker_address='192.168.10.174'
client = mqtt.Client('P1')
client.connect(broker_address)
while True: #infinite loop
    client.subscribe("#")
    client.on_message=return_subscription_values      #attach function to callback       
    client.loop_start()
    time.sleep(10) 
    client.loop_stop()
    input("Press enter to continue: ")
quit()

