from dataclasses import dataclass, field

@dataclass
class mqttConfig:
    #MQTT Broker Configuration
    MQTT_BROKER = "6bc0e53bbb904551a9d0a88725cd9fdb.s1.eu.hivemq.cloud"
    MQTT_PORT = 8883
    MQTT_USERNAME = "Divyansh16"
    MQTT_PASSWORD = "Divyans12@"
    TOPIC = "healthcare/sensor_data"
