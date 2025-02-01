from baseline_health import BaselineHealth
import random
import time
from mqtt_server_exec import MQTTServerExec

class AlzheimerPatient:
    def __init__(
            self,
            person_id: int
    ):
        self.person_id = person_id
        self.heart_rate = 0
        self.blood_pressure_systolic = 0
        self.blood_pressure_diastolic = 0
        self.body_temperature = 0
        self.oxygen_saturation = 0
        self.latitude =38.8462
        self.longtitude =77.3064

        

    

    def generate_data(self):
        max_offset_near = 0.01  # Normal wandering behavior (close to baseline)
        max_offset_far = 0.1    # Erratic wandering (confusion)

        stress_factor = random.choice([0, 5])  # Sudden stress causing spikes

        # Simulating fluctuating vitals
        self.heart_rate = max(50, min(120, BaselineHealth.heart_rate + random.randint(-5, 10) + stress_factor))
        self.blood_pressure_systolic = max(85, min(140, BaselineHealth.systolic_bp + random.randint(-5, 10) + stress_factor))
        self.blood_pressure_diastolic = max(55, min(90, BaselineHealth.diastolic_bp + random.randint(-5, 5)))
        self.body_temperature = round(max(35.5, min(38.0, BaselineHealth.body_temperature + random.uniform(-0.3, 0.3))), 1)
        self.oxygen_saturation = max(90, min(100, BaselineHealth.oxygen_saturation + random.randint(-2, 2)))

        # Simulating wandering behavior with possible confusion
        if random.random() < 0.2:  # 20% chance of erratic wandering (confusion)
            self.latitude = 38.8462 + random.uniform(-max_offset_far, max_offset_far)
            self.longitude = 77.3064 + random.uniform(-max_offset_far, max_offset_far)
        else:  # Normal wandering
            self.latitude = 38.8462 + random.uniform(-max_offset_near, max_offset_near)
            self.longitude = 77.3064 + random.uniform(-max_offset_near, max_offset_near)

        # Creating the data dictionary
        data = {
            f"{self.person_id}": {
                "heart_rate": self.heart_rate,
                "blood_pressure_systolic": self.blood_pressure_systolic,
                "blood_pressure_diastolic": self.blood_pressure_diastolic,
                "body_temperature": self.body_temperature,
                "oxygen_saturation": self.oxygen_saturation,
                "timestamp": time.strftime('%Y-%m-%d %H:%M:%S'),
                "lat": self.latitude,
                "long": self.longitude
            }
        }

        return self.person_id, data
        


    
