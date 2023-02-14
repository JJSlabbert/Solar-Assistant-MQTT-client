#This Software need the Solar-Assistant software on a Raspberry PI. https://solar-assistant.io/
#Written by Jaco Slabbert https://github.com/JJSlabbert/Sollar-Assistant-MQTT-client
#Codoe tested on the 5KW Sacolar (Growatt SPF) Inverter and Battery Compatable with PBMS tools (15 cell P15S100A) monitored via USB Serial RS232/RS485

import paho.mqtt.client as mqtt
import time
n=0 #counter to count if both highest and lowest cell volts was read
highest_cell_volts=0.0000
lowest_cell_volts=0.0000

def return_subscription_values(client, userdata, message):
    mqtttopic=message.topic
    mqttmesage=message.payload.decode("utf-8")
    global n
    global highest_cell_volts
    global lowest_cell_volts
    Cel_rage=0.0000
    if mqtttopic=='solar_assistant/battery_1/state_of_charge/state':
        print('The Battery SoC (State of Charge): ',mqttmesage)
        client.unsubscribe('solar_assistant/battery_1/state_of_charge/state')
    if mqtttopic=='solar_assistant/battery_1/voltage/state':
        print('The Battery Voltage: ',mqttmesage)
        client.unsubscribe('solar_assistant/battery_1/voltage/state')
    if mqtttopic=='solar_assistant/battery_1/current/state':
        print('Battery Charge Current: ',mqttmesage)
        client.unsubscribe('solar_assistant/battery_1/current/state') 
    if mqtttopic=='solar_assistant/battery_1/cycles/state':
        print('Battery number of Charge Cycles :',mqttmesage)
        client.unsubscribe('solar_assistant/battery_1/cycles/state')
    if mqtttopic=='solar_assistant/battery_1/cell_voltage_-_average/state':
        print('Average Cell Voltage: ',mqttmesage)
        client.unsubscribe('solar_assistant/battery_1/cell_voltage_-_average/state')
    if mqtttopic=='solar_assistant/battery_1/cell_voltage_-_highest/state':
        print('Highest Cell Voltage: ',mqttmesage)
        highest_cell_volts=float(mqttmesage)
        client.unsubscribe('solar_assistant/battery_1/cell_voltage_-_highest/state')
        n+=1
    if mqtttopic=='solar_assistant/battery_1/cell_voltage_-_lowest/state':
        print('Lowwest Cell Votage: ',mqttmesage)
        lowest_cell_volts=float(mqttmesage)
        client.unsubscribe('solar_assistant/battery_1/cell_voltage_-_lowest/state')
        n+=1
    if n==2: #Both lowest and highest cell voltage read
        print ("************************************************")
        Cel_rage=highest_cell_volts-lowest_cell_volts
        print('Cell voltage range (Highest-Lowest). This should be below 0.1: ',str(Cel_rage))
        n+=1
    #print("message received " ,str(message.payload.decode("utf-8")))        
    #print("message topic=",message.topic)
    #print("message qos=",message.qos)
    #print("message retain flag=",message.retain)    
    print ("************************************************")
    
#broker_address=input("Provide the IP address of the MQTT Broker: ")
broker_address='192.168.0.31'
client = mqtt.Client('P1')
client.connect(broker_address)
client.subscribe('solar_assistant/battery_1/state_of_charge/state')
client.subscribe('solar_assistant/battery_1/voltage/state')
client.subscribe('solar_assistant/battery_1/current/state')
client.subscribe('solar_assistant/battery_1/cycles/state')
client.subscribe('solar_assistant/battery_1/cell_voltage_-_average/state')
client.subscribe('solar_assistant/battery_1/cell_voltage_-_highest/state')
client.subscribe('solar_assistant/battery_1/cell_voltage_-_lowest/state')
client.on_message=return_subscription_values      #attach function to callback       
client.loop_start()
time.sleep(10) 
client.loop_stop()
quit()

