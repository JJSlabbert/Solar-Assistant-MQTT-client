# Solar-Assistant-MQTT-client
Solar-Assistant (https://solar-assistant.io/) is software to monitor and control Solar Systems. Many Inverters and Batteries is supported. It runs on a Raspberry PI or Certain Orange PI's. Solar-assistant include a MQTT broker. By communicating with this broker you can monitor and control many solar systems via MQTT and Python. The Paho mqtt client library is used.

SolarMAX_gridMIN.py: This script is used to Set the Max Grid Charge current to make sure that the grid is not over used while solar power is available.

GoToBattery_SwitchGridOff.py: This is a creative mode to switch the AC supply to the inverter off and force it into Solar/Battery mode. It basicly reduce the To Battery Baterry Voltage below the current voltage.

<B>HANDY TOOLS</B>

-MQTT Explorer

-<a href="https://pypi.org/project/paho-mqtt/#installation">https://pypi.org/project/paho-mqtt/#installation</a>
