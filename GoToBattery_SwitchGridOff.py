#This Software need the Solar-Assistant software on a Raspberry PI
#Written by Jaco Slabbert https://github.com/JJSlabbert/Sollar-Assistant-MQTT-client

import paho.mqtt.client as mqtt
import time

def return_subscription_values(client, userdata, message):
    mqtttopic=message.topic
    if mqtttopic=='solar_assistant/inverter_1/back_to_battery_voltage/state':
        print('Back to Battery Baterry Voltage :', str(message.payload.decode("utf-8")))
        client.unsubscribe('solar_assistant/inverter_1/back_to_battery_voltage/state')        
    elif mqtttopic=='solar_assistant/inverter_1/to_grid_battery_voltage/state':
        print('Back to Grid Battery volage :', str(message.payload.decode("utf-8")))
        client.unsubscribe('solar_assistant/inverter_1/to_grid_battery_voltage/state')
    elif mqtttopic=='solar_assistant/inverter_1/battery_voltage/state':
        print('The current battery Voltage :', str(message.payload.decode("utf-8")))
        client.unsubscribe('solar_assistant/inverter_1/battery_voltage/state')
    elif mqtttopic=='solar_assistant/battery_1/state_of_charge/state':
        print('The current battery SOC (State of Charge) :', str(message.payload.decode("utf-8")))
        client.unsubscribe('solar_assistant/battery_1/state_of_charge/state')
    elif mqtttopic=='solar_assistant/inverter_1/output_source_priority/state':
        print('The Outut Source Priority is :', str(message.payload.decode("utf-8")))
        print('If Output Source is UTILITY FIRST, this code will not ba able to Switch to Battery')
        client.unsubscribe('solar_assistant/inverter_1/output_source_priority/state')        
    #print("message received " ,str(message.payload.decode("utf-8")))
    #print("message topic=",message.topic)
    #print("message qos=",message.qos)
    #print("message retain flag=",message.retain)    
    print ("************************************************")

def return_inverter_state(client, userdata, message):
    mqtttopic=message.topic
    mqttpayload=message.payload.decode("utf-8")
    print("Message Topic: ",mqtttopic)
    print("Inverter Mode: ", mqttpayload)
    
##    if mqtttopic=='solar_assistant/inverter_1/device_mode/state':
##        print('Back to Battery Baterry Voltage :', str(message.payload.decode("utf-8")))
##        client.unsubscribe('solar_assistant/inverter_1/back_to_battery_voltage/state')        
##    elif mqtttopic=='solar_assistant/inverter_1/to_grid_battery_voltage/state':
##        print('Back to Grid Battery volage :', str(message.payload.decode("utf-8")))
##        client.unsubscribe('solar_assistant/inverter_1/to_grid_battery_voltage/state')


broker_address=input("Provide the IP address of the MQTT Broker: ")
client = mqtt.Client('P1')
client.connect(broker_address)

client.subscribe('solar_assistant/inverter_1/back_to_battery_voltage/state')
client.subscribe('solar_assistant/inverter_1/to_grid_battery_voltage/state')
client.subscribe('solar_assistant/inverter_1/battery_voltage/state')
client.subscribe('solar_assistant/battery_1/state_of_charge/state')
client.subscribe('solar_assistant/inverter_1/output_source_priority/state')
client.on_message=return_subscription_values      #attach function to callback

client.loop_start()
time.sleep(10) 
client.loop_stop()
print("The only method I can think of to command the inverter to switch from") 
print("Grid power to Battery power is by setting the to battery voltage below")
print("the current voltage")
print("You must also set a Back to Grid Voltage below the to Battery Voltage")
print("Your Output source priority should also be Solar First or Solar/Battery/Utility")
print("Your Inverter may take 5 to 10 minutes to switch to battery")
print("Both voltages must have one decimal after ., like 50.0 or 50.2")
new_to_battery_voltage=input("Provide the new To Battery Voltage. It must be \nlower than the current Battery voltage: ")
new_to_grid_voltage=input("New Back to Grid Voltage. It must be lower than the To \nBattery Voltage: ")


#The new Back to Grid Voltage must be set before the new Back to Battery Battery Voltage
client.publish('solar_assistant/inverter_1/to_grid_battery_voltage/set',new_to_grid_voltage)
print("Saving new settings. Will take 30 seconds")
time.sleep(5)
print("Saving........5/30 sseconds")
time.sleep(5)
print("Saving........10/30 sseconds")
time.sleep(5)
print("Saving........15/30 sseconds")
time.sleep(5)

client.publish('solar_assistant/inverter_1/back_to_battery_voltage/set',new_to_battery_voltage)
time.sleep(5)
print("Saving........20/30sseconds")
time.sleep(5)
print("Saving........25/30 sseconds")
time.sleep(5)
print("Saving........30/30sseconds")
time.sleep(5)

client.subscribe('solar_assistant/inverter_1/back_to_battery_voltage/state')
client.subscribe('solar_assistant/inverter_1/to_grid_battery_voltage/state')
client.subscribe('solar_assistant/inverter_1/battery_voltage/state')
client.subscribe('solar_assistant/battery_1/state_of_charge/state')

client.on_message=return_subscription_values      #attach function to callback

client.loop_start()
time.sleep(10) 
client.loop_stop()
client.unsubscribe('solar_assistant/inverter_1/back_to_battery_voltage/state')
client.unsubscribe('solar_assistant/inverter_1/to_grid_battery_voltage/state')
client.unsubscribe('solar_assistant/inverter_1/battery_voltage/state')
client.unsubscribe('solar_assistant/battery_1/state_of_charge/state')
print ("It may still take the inverter 5-10 minutes to Switch to Battery/Solar mode")


client.subscribe('solar_assistant/inverter_1/device_mode/state')
client.on_message=return_inverter_state      #attach function to callback
client.loop_start()
time.sleep(20)
print ("Waiting to go into Battery Mode for .......20/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......40/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......60/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......80/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......100/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......120/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......140/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......160/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......180/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......200/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......220/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......230/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......240/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......260/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......280/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......300/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......320/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......340/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......360/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......380/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......400/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......420/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......440/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......460/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......480/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......500/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......520/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......540/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......560/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......580/600 seconds")
time.sleep(20)
print ("Waiting to go into Battery Mode for .......600/600 seconds")
