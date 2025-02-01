from dataclasses import dataclass, field

@dataclass
class BaselineHealth:
    heart_rate: int = 70
    systolic_bp: int = 100
    diastolic_bp: int = 75
    body_temperature: float = 36.8
    oxygen_saturation: int = 99
