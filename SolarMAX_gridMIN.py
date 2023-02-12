#This Software need the Solar-Assistant software on a Raspberry PI
#Written by Jaco Slabbert https://github.com/JJSlabbert/Sollar-Assistant-MQTT-client

import paho.mqtt.client as mqtt
import time


def return_subscription_values(client, userdata, message):
    mqtttopic=message.topic
    if mqtttopic=='solar_assistant/battery_1/state_of_charge/state':
        print('The Battery State of Charge (SOC) as % :', str(message.payload.decode("utf-8")))
        client.unsubscribe('solar_assistant/battery_1/state_of_charge/state')        
    elif mqtttopic=='solar_assistant/battery_1/voltage/state':
        print('The Battery Voltage is :', str(message.payload.decode("utf-8")))
        client.unsubscribe('solar_assistant/battery_1/voltage/state')
    elif mqtttopic=='solar_assistant/inverter_1/max_grid_charge_current/state':
        print('The Inverter Maximum GRID (AC) Charge Current is :', str(message.payload.decode("utf-8")))
        client.unsubscribe('solar_assistant/inverter_1/max_grid_charge_current/state')        
    elif mqtttopic=='solar_assistant/inverter_1/grid_voltage/state':
        print('The Grid Voltage is :', str(message.payload.decode("utf-8")))
        client.unsubscribe('solar_assistant/inverter_1/grid_voltage/state')
    elif mqtttopic=='solar_assistant/inverter_1/load_percentage/state':
        print('The Load Power as % :', str(message.payload.decode("utf-8")))
        client.unsubscribe('solar_assistant/inverter_1/load_percentage/state')
    elif mqtttopic=='solar_assistant/inverter_1/load_power/state':
        print('The Load Power in watts :', str(message.payload.decode("utf-8")))
        client.unsubscribe('solar_assistant/inverter_1/load_power/state')
    elif mqtttopic=='solar_assistant/inverter_1/pv_power/state':
        print('The PV Power in watts :', str(message.payload.decode("utf-8")))
        client.unsubscribe('solar_assistant/inverter_1/pv_power/state')
        
    #print("message received " ,str(message.payload.decode("utf-8")))
    #print("message topic=",message.topic)
    #print("message qos=",message.qos)
    #print("message retain flag=",message.retain)    
    print ("************************************************")

broker_address=input("Provide the IP address of the MQTT Broker: ")
#broker_address='192.168.0.27'

client = mqtt.Client('P1')


client.connect(broker_address)

print ("************************************************")
print('Reading important values from the inverter and battery.')
print('This values can assist you on the grid current that you \n'+'may need to keep your batery on the right level')
print ("************************************************")
time.sleep(4)
client.subscribe('solar_assistant/battery_1/state_of_charge/state')
client.subscribe('solar_assistant/battery_1/voltage/state')
client.subscribe('solar_assistant/inverter_1/max_grid_charge_current/state')
client.subscribe('solar_assistant/inverter_1/grid_voltage/state')
client.subscribe('solar_assistant/inverter_1/load_percentage/state')
client.subscribe('solar_assistant/inverter_1/load_power/state')
client.subscribe('solar_assistant/inverter_1/pv_power/state')
client.on_message=return_subscription_values      #attach function to callback       
client.loop_start()
time.sleep(10) 
client.loop_stop()

print ("************************************************")

max_grid_charge_current=input("Choose your AC (GRID) charge current based on Cloud Coverage, Solar Radiation, Expected Solar Production and current Battery SOC etc: ")
client.subscribe('solar_assistant/inverter_1/max_grid_charge_current/state')
client.publish('solar_assistant/inverter_1/max_grid_charge_current/set',max_grid_charge_current)
print ('Seting Maximum Grid Charge current.....1/20 seconds')
time.sleep(1)
print ('Seting Maximum Grid Charge current.....2/20 seconds')
time.sleep(1)
print ('Seting Maximum Grid Charge current.....3/20 seconds')
time.sleep(1)
print ('Seting Maximum Grid Charge current.....4/20 seconds')
time.sleep(1)
print ('Seting Maximum Grid Charge current.....5/20 seconds')
time.sleep(1)
print ('Seting Maximum Grid Charge current.....6/20 seconds')
time.sleep(1)
print ('Seting Maximum Grid Charge current.....7/20 seconds')
time.sleep(1)
print ('Seting Maximum Grid Charge current.....8/20 seconds')
time.sleep(1)
print ('Seting Maximum Grid Charge current.....9/20 seconds')
time.sleep(1)
print ('Seting Maximum Grid Charge current.....10/20 seconds')
time.sleep(1)
print ('Seting Maximum Grid Charge current.....11/20 seconds')
time.sleep(1)
print ('Seting Maximum Grid Charge current.....12/20 seconds')
time.sleep(1)
print ('Seting Maximum Grid Charge current.....13/20 seconds')

time.sleep(1)
print ('Seting Maximum Grid Charge current.....14/20 seconds')
time.sleep(1)
print ('Seting Maximum Grid Charge current.....15/20 seconds')
time.sleep(1)
print ('Seting Maximum Grid Charge current.....16/20 seconds')
time.sleep(1)
print ('Seting Maximum Grid Charge current.....17/20 seconds')
time.sleep(1)
print ('Seting Maximum Grid Charge current.....18/20 seconds')
time.sleep(1)
print ('Seting Maximum Grid Charge current.....19/20 seconds')
time.sleep(1)
print ('Seting Maximum Grid Charge current.....20/20 seconds')


#client.on_message=return_subscription_values      #attach function to callback
client.subscribe('solar_assistant/inverter_1/max_grid_charge_current/state')
client.loop_start()
time.sleep(4) 
client.loop_stop()
quit()

