from baseline_health import BaselineHealth
import random
import time
from mqtt_server_exec import MQTTServerExec

class PersonWithHeartIssue:
    def __init__(self, person_id: int):
        self.person_id = person_id
        self.heart_rate = 0
        self.blood_pressure_systolic = 0
        self.blood_pressure_diastolic = 0
        self.body_temperature = 0
        self.oxygen_saturation = 0
        self.latitude =38.8462
        self.longtitude =77.3064

    def generate_data(self):
        max_offset=0.01
        # Simulate normal health data within the healthy range
        self.heart_rate = max(60, min(100, BaselineHealth.heart_rate + random.randint(-2, 2)))
        self.blood_pressure_systolic = max(90, min(120, BaselineHealth.systolic_bp + random.randint(-3, 3)))
        self.blood_pressure_diastolic = max(60, min(80, BaselineHealth.diastolic_bp + random.randint(-3, 3)))
        self.body_temperature = round(max(36.5, min(37.2, BaselineHealth.body_temperature + random.uniform(-0.1, 0.1))), 1)
        self.oxygen_saturation = max(97, min(100, BaselineHealth.oxygen_saturation + random.randint(-1, 1)))
        self.latitude = 38.8462 + random.uniform(-max_offset, max_offset)
        self.longitude = 77.3064 + random.uniform(-max_offset, max_offset)

        # Occasionally introduce sudden spikes or deviations in the data
        if random.random() < 0.1:  # 10% chance for sudden spike
            self._introduce_spike()

        # Return the data
        data = {
            f"{self.person_id}": {
                "heart_rate": self.heart_rate,
                "blood_pressure_systolic": self.blood_pressure_systolic,
                "blood_pressure_diastolic": self.blood_pressure_diastolic,
                "body_temperature": self.body_temperature,
                "oxygen_saturation": self.oxygen_saturation,
                "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
                "lat":self.latitude,
                "long":self.longtitude
            }
        }
        return self.person_id, data

    def _introduce_spike(self):
        """
        Introduce a random spike in the vital signs (e.g., heart rate, blood pressure).
        This simulates a sudden increase in one of the vital signs.
        """
        spike_type = random.choice(['heart_rate', 'blood_pressure','both'])

        if spike_type == 'heart_rate':
            # Sudden spike in heart rate (e.g., stress or physical activity)
            self.heart_rate = random.randint(120, 180)  # Simulate tachycardia

        elif spike_type == 'blood_pressure':
            # Sudden spike in blood pressure (e.g., hypertensive crisis)
            self.blood_pressure_systolic = random.randint(160, 200)
            self.blood_pressure_diastolic = random.randint(100, 130)

        else:
            # Sudden spike in heart rate (e.g., stress or physical activity)
            self.heart_rate = random.randint(120, 180)  # Simulate tachycardia
            # Sudden spike in blood pressure (e.g., hypertensive crisis)
            self.blood_pressure_systolic = random.randint(160, 220)
            self.blood_pressure_diastolic = random.randint(100, 130)

        # Optionally, we can simulate a small increase in body temperature or some other vital signs here too.
