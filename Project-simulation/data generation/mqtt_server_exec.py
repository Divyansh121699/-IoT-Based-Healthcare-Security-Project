from mqtt_config import mqttConfig
from paho.mqtt import client as mqtt
import json

class MQTTServerExec:
    def __init__(self):
	# Create an MQTT client instance
        self.client = mqtt.Client("VirtualIoTDevice")
        self.config = mqttConfig()
        self.client.username_pw_set(self.config.MQTT_USERNAME, self.config.MQTT_PASSWORD)
        self.client.tls_set()
	# Connect to the MQTT broker
        self.client.connect(self.config.MQTT_BROKER, self.config.MQTT_PORT)
        self.client.loop_start()

    def publishData(self, data, id):
	# Convert to JSON and publish the data
        self.client.publish(self.config.TOPIC, json.dumps(data))
        print(f"Published data for person_{id}: {data}")
