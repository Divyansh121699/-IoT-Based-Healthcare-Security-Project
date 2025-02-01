# MQTT Topic for IoT-Based Smart Healthcare Security

## 📌 Overview
This document defines the **MQTT topic** used in the IoT-based Smart Healthcare Security project for secure patient monitoring, data transmission, and emergency alerting.

## 📡 MQTT Topic
For this system, we use a **single unified topic** for transmitting all sensor data:
```
healthcare/sensor_data
```

### **Payload Structure**
Since all sensor data is transmitted under a single topic, the **JSON payload** must include relevant metadata:

```json
{
    "device_id": "sensor_123",
    "timestamp": "2025-02-01T12:00:00Z",
    "heartrate": 78,
    "bloodpressure": {"systolic": 120, "diastolic": 80},
    "temperature": 36.5,
    "oxygen": 98,
    "location": {"latitude": 38.8977, "longitude": -77.0365},
    "alert": "none"
}
```

## 🔒 Security Considerations
- **TLS Encryption**: All messages use TLS (port 8883) for secure transmission.
- **Authentication**: Devices authenticate via username/password credentials.
- **Access Control**: Only authorized devices can publish and subscribe.
- **Data Integrity**: End-to-end encryption ensures tamper-proof transmission.
