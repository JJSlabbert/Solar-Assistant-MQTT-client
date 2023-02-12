import paho.mqtt.client as mqtt
import time


def return_subscription_values(client, userdata, message):
    print('\n')
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)    
    print ("\n**************************")

broker_address=input("Provide the IP address of the MQTT Broker: ")
#broker_address='192.168.0.27'

client = mqtt.Client('P1')


client.connect(broker_address)

print('Reading the Battery SOC (State of Charge) as %, Battery Voltage, Max Grid Charge Current, AC Louad %')
client.subscribe('solar_assistant/battery_1/state_of_charge/state')
client.subscribe('solar_assistant/battery_1/voltage/state')
client.subscribe('solar_assistant/inverter_1/max_grid_charge_current/state')
client.subscribe('solar_assistant/inverter_1/load_percentage/state')
client.on_message=return_subscription_values      #attach function to callback       
client.loop_start()
time.sleep(10) 
client.loop_stop()
client.unsubscribe('solar_assistant/battery_1/state_of_charge/state')
client.unsubscribe('solar_assistant/battery_1/voltage/state')
client.unsubscribe('solar_assistant/inverter_1/load_percentage/state')

print ('\n*************************************************************************************************************************************************************\n')

max_grid_charge_current=input("Choose your AC (GRID) charge current based on Cloud Coverage, Solar Radiation, Expected Solar Production and current Battery SOC etc: ")
client.publish('solar_assistant/inverter_1/max_grid_charge_current/set',max_grid_charge_current)
print ('Seting Maximum Grid Charge current.....1/20 seconds')
time.sleep(4.8)
print ('Seting Maximum Grid Charge current.....5/20 seconds')
time.sleep(4.8)
print ('Seting Maximum Grid Charge current.....10/20 seconds')
time.sleep(4.8)
print ('Seting Maximum Grid Charge current.....15/20 seconds')

client.on_message=return_subscription_values      #attach function to callback
client.loop_start()
time.sleep(2) 
client.loop_stop()

