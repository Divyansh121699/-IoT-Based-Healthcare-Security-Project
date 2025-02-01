from paho.mqtt import client as mqtt
import time
import random
import json
from mqtt_config import mqttConfig
from mqtt_server_exec import MQTTServerExec
from person.healthy_person import HealthyPerson
from person.heart_issued_person import PersonWithHeartIssue
from person.alzheimer_patient import AlzheimerPatient

def simulate_health_care():
                healthy_person=HealthyPerson(1)
                unhealthy_person1 = PersonWithHeartIssue(2)
                unhealthy_person2 = PersonWithHeartIssue(3)
                unhealthy_person3 = AlzheimerPatient(4)
                my_mqtt_sever=MQTTServerExec()
                start_time = time.time()
                while True:
                        id,data = healthy_person.generate_data()
                        my_mqtt_sever.publishData(data,id)
                        id,data = unhealthy_person1.generate_data()
                        my_mqtt_sever.publishData(data,id)
                        id,data = unhealthy_person2.generate_data()
                        my_mqtt_sever.publishData(data,id)
                        id,data = unhealthy_person3.generate_data()
                        my_mqtt_sever.publishData(data,id)
                        # Wait for 20 seconds before the next iteration
                        time.sleep(20)
                        if time.time()-start_time > 1000000:
                                print("Simulation done")
                                break

if __name__ == "__main__":
    simulate_health_care()
