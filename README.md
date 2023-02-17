# Solar-Assistant-MQTT-client
Solar-Assistant (https://solar-assistant.io/) is software to monitor and control Solar Systems. Many Inverters and Batteries are supported. It runs on a Raspberry PI or Certain Orange PI's. Solar-assistant include a MQTT broker. By communicating with this broker you can monitor and control many solar systems via MQTT and Python. The Paho mqtt client library is used.

<B>SolarMAX_gridMIN.py</B>: This script is used to Set the Max Grid Charge current to make sure that the grid is not over used while solar power is available.

<B>GoToBattery_SwitchGridOff.py:</B> This is a creative mode to switch the AC supply to the inverter off and force it into Solar/Battery mode. It basicly reduce the To Battery Baterry Voltage below the current voltage.

<B>BatHealth.py:</B> Some measures usefull for battery health.

<B>HANDY TOOLS</B>

-MQTT Explorer

-<a href="https://pypi.org/project/paho-mqtt/#installation">https://pypi.org/project/paho-mqtt/#installation</a>

MQTT Explorer can assist to get mqtt topics
![MQTT_explorer_output](https://user-images.githubusercontent.com/38969599/218340039-4c75988e-688d-4592-a8c8-425108d2c6df.jpg)

Codoe tested on the 5KW Sacolar (Growatt SPF) Inverter monitored via USB CP2102 UART BRIDGE and Battery Compatable with PBMS tools (15 cell P15S100A) monitored via USB Serial RS232/RS485
My inverter and BMS is not directly connected. Inverter setting 5: USE
