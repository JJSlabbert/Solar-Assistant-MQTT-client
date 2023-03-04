#This Software need the Solar-Assistant software on a Raspberry PI. https://solar-assistant.io/
#Written by Jaco Slabbert https://github.com/JJSlabbert/Sollar-Assistant-MQTT-client
#Codoe tested on the 5KW Sacolar (Growatt SPF) Inverter and Battery Compatable with PBMS tools (15 cell P15S100A) monitored via USB Serial RS232/RS485
#solar_assistant/inverter_1/max_grid_charge_current/state
#Cayenne_username: 02079db0-e20b-11e6-a971-4db18559717d
#Cayenne password: 0e765d8383691fcc65ac537e76ef9134129b6edc
#Cayenne Client ID: 0ff00550-af0c-11ed-b72d-d9f6595c5b9d
#TO DO. Collect all values from solar-assistant and pub to cayenne ones
#json pub message: client_C.publish('v1/'+Cayenne_username+'/things/'+Cayenne_CID+'/data/json','[{"channel":0,"value":3},{"channel":1,"value":55}]')

import paho.mqtt.client as mqtt
import time
Cayenne_username='**********'
Cayenne_password='***********'
Cayenne_CID='***********'

#broker_address=input("Provide the IP address of the MQTT Broker: ")
broker_address_SA='192.168.10.174'
brokar_address_C='mqtt.mydevices.com'
client_SA = mqtt.Client('DEVICE_ID')
client_C=mqtt.Client(Cayenne_CID)
client_C.username_pw_set(Cayenne_username,Cayenne_password)
client_SA.on_message=return_subscription_values_SA
client_C.on_message=return_subscription_values_C

#global values to publish to Cayenne
bat_soc=0.00
max_grid_charge_current=0.00 #Read and Wtite on INVERTER
pv_power=0.00

load_percentage=0.00
load_power=0.00
grid_power=0.00
grid_voltage=0.00
bat_power=0.000

to_bat_batvolt=52.8
to_grid_batvolt=51.5


def return_subscription_values_C(client, userdata, message):
    mqtttopic=message.topic
    mqttpayload=message.payload.decode("utf-8")
    if mqtttopic=='v1/'+Cayenne_username+'/things/'+Cayenne_CID+'/cmd/0':
        print("Cayenne user requested to change Max Grid Charge Current:")
        mqttpayload.split(',')
        split_mqqtpayload=mqttpayload.split(',')[1]
        new_grid_charge_current=split_mqqtpayload
        print('Grid charge current must be set to:',new_grid_charge_current)
        client_SA.publish('solar_assistant/inverter_1/max_grid_charge_current/set',new_grid_charge_current)        
    if mqtttopic=='v1/'+Cayenne_username+'/things/'+Cayenne_CID+'/cmd/8':
        print("Cayenne user requested to change to_bat_batvolt:")
        mqttpayload.split(',')
        split_mqqtpayload=mqttpayload.split(',')[1]
        new_to_bat_batvolt=0.0
        new_to_bat_batvolt=split_mqqtpayload
        print('To Battery Voltage must be set to:',new_to_bat_batvolt)
        client_SA.publish('solar_assistant/inverter_1/back_to_battery_voltage/set',new_to_bat_batvolt)
    if mqtttopic=='v1/'+Cayenne_username+'/things/'+Cayenne_CID+'/cmd/9':
        print("Cayenne user requested to change to_grid_batvolt:")
        mqttpayload.split(',')
        split_mqqtpayload=mqttpayload.split(',')[1]
        new_to_grid_batvolt=0.0
        new_to_grid_batvolt=split_mqqtpayload
        print('To Grid Battery Voltage must be set to:',new_to_grid_batvolt)
        client_SA.publish('solar_assistant/inverter_1/to_grid_battery_voltage/set',new_to_grid_batvolt)        
    
    print('****************************************************************')
    print('Cayenne Topic: '+mqtttopic)
    print('Cayenne payload: '+mqttpayload)


  


       
    print('****************************************************************')
    
def return_subscription_values_SA(client, userdata, message):
    mqtttopic=message.topic
    mqttpayload=message.payload.decode("utf-8")
    global bat_soc
    global max_grid_charge_current
    global pv_power
    
    global load_percentage
    global load_power
    global grid_power
    global grid_voltage
    global bat_power

    global to_bat_batvolt
    global to_grid_batvolt
    
    if mqtttopic=='solar_assistant/inverter_1/max_grid_charge_current/state':
        max_grid_charge_current=float(mqttpayload) 
        client_SA.unsubscribe(mqtttopic)

    if mqtttopic=='solar_assistant/battery_1/state_of_charge/state':        
        bat_soc=float(mqttpayload)
        client_SA.unsubscribe(mqtttopic)
        
    if mqtttopic=='solar_assistant/inverter_1/pv_power/state':        
        pv_power=float(mqttpayload)
        client_SA.unsubscribe(mqtttopic)

    
    if mqtttopic=='solar_assistant/inverter_1/load_percentage/state':
        load_percentage=float(mqttpayload)
        client_SA.unsubscribe(mqtttopic)
    if mqtttopic=='solar_assistant/inverter_1/load_power/state':
        load_power=float(mqttpayload)
        client_SA.unsubscribe(mqtttopic)
    if mqtttopic=='solar_assistant/inverter_1/grid_power/state':
        grid_power=float(mqttpayload)
        client_SA.unsubscribe(mqtttopic)
    if mqtttopic=='solar_assistant/inverter_1/grid_voltage/state':
        grid_voltage=float(mqttpayload)
        client_SA.unsubscribe(mqtttopic)
    if mqtttopic=='solar_assistant/battery_1/power/state':
        bat_power=float(mqttpayload)
        client_SA.unsubscribe(mqtttopic)

    if mqtttopic=='solar_assistant/inverter_1/back_to_battery_voltage/state':
        to_bat_batvolt=float(mqttpayload)
        client_SA.unsubscribe(mqtttopic)
    if mqtttopic=='solar_assistant/inverter_1/to_grid_battery_voltage/state':
        to_grid_batvolt=float(mqttpayload)
        client_SA.unsubscribe(mqtttopic)        


##        
###     print("message payload (value) " ,mqttpayload)        
#     print("message topic=",mqtttopic)
#     print ("************************************************")
    

while True:
    try:
        client_SA.connect(broker_address_SA)
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print('Could not connect to Solar-Assistant mqtt broker.')
    try:
        client_C.connect(brokar_address_C)
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print('Could not connect to MyDevices mqtt broker.')
    time.sleep(2)    
    client_SA.loop_start()
    client_C.loop_start()

    client_SA.subscribe('solar_assistant/inverter_1/max_grid_charge_current/state')
    client_SA.subscribe('solar_assistant/battery_1/state_of_charge/state')
    client_SA.subscribe('solar_assistant/inverter_1/pv_power/state')
    
    client_SA.subscribe('solar_assistant/inverter_1/load_percentage/state')
    client_SA.subscribe('solar_assistant/inverter_1/load_power/state')
    client_SA.subscribe('solar_assistant/inverter_1/grid_power/state')
    client_SA.subscribe('solar_assistant/inverter_1/grid_voltage/state')
    client_SA.subscribe('solar_assistant/battery_1/power/state')

    client_SA.subscribe('solar_assistant/inverter_1/back_to_battery_voltage/state')
    client_SA.subscribe('solar_assistant/inverter_1/to_grid_battery_voltage/state')
    
    client_C.subscribe('v1/'+Cayenne_username+'/things/'+Cayenne_CID+'/cmd/0') 
    client_C.subscribe('v1/'+Cayenne_username+'/things/'+Cayenne_CID+'/cmd/8')
    client_C.subscribe('v1/'+Cayenne_username+'/things/'+Cayenne_CID+'/cmd/9')
    
    #client_SA.loop_start()
    #time.sleep(50) 
    #client_SA.loop_stop()
    time.sleep(10) #to make sure payloads is received from SA befor pub to C
    pub_top='v1/'+Cayenne_username+'/things/'+Cayenne_CID+'/data/json'
    pub_payload='['
    pub_payload+='{"channel":0,"value":'+str(max_grid_charge_current)+'},'
    pub_payload+='{"channel":1,"value":'+str(bat_soc)+'},'
    pub_payload+='{"channel":2,"value":'+str(pv_power)+'},'
    
    pub_payload+='{"channel":3,"value":'+str(load_percentage)+'},'
    pub_payload+='{"channel":4,"value":'+str(load_power)+'},'
    pub_payload+='{"channel":5,"value":'+str(grid_power)+'},'
    pub_payload+='{"channel":6,"value":'+str(grid_voltage)+'},'
    pub_payload+='{"channel":7,"value":'+str(bat_power)+'},'

    pub_payload+='{"channel":8,"value":'+str(to_bat_batvolt)+'},'
    pub_payload+='{"channel":9,"value":'+str(to_grid_batvolt)+'}'    
    pub_payload+=']'    

    
    #pub_payload='[{"channel":0,"value":'+str(max_grid_charge_current)+'},{"channel":1,"value":'+str(bat_soc)+'},{"channel":2,"value":'+str(pv_power)+'}]'
    print('****************************************************************')
    print('Caynne channel 0, max_grid_charge_current: ', str(max_grid_charge_current))
    print('Caynne channel 1, bat_soc: ', str(bat_soc))
    print('Caynne channel 2, pv_power: ', str(pv_power))    
    print('Caynne channel 3, load_percentage: ', str(load_percentage))
    print('Caynne channel 4, load_power: ', str(load_power))
    print('Caynne channel 5, grid_power: ', str(grid_power))
    print('Caynne channel 6, grid_voltage: ', str(grid_voltage))
    print('Caynne channel 7, bat_power: ', str(bat_power))
    print('Cayenne channel 8, to_bat_batvolt: ',str(to_bat_batvolt))
    print('Cayenne channel 9, to_grid_batvolt: ',str(to_grid_batvolt))    
     
    print('Publication Topic: ',pub_top)
    print('Publication Payload: ',pub_payload)
    client_C.publish(pub_top,pub_payload)
    print('****************************************************************')
    #client_C.loop_start()
    #time.sleep(10) 
    #client_C.loop_stop()
    #time.sleep(2)
    time.sleep(20)
 
