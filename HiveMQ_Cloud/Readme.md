# HiveMQ Cloud Integration for IoT-Based Smart Healthcare Security

## 📌 Overview
This document explains how to integrate **HiveMQ Cloud** into the IoT-based Smart Healthcare Security system. HiveMQ Cloud acts as a **secure MQTT broker**, enabling real-time data transmission between IoT devices, cloud servers, and mobile applications.

## 🔧 Setup HiveMQ Cloud
Follow these steps to set up **HiveMQ Cloud**:

### **1. Create an Account**
1. Go to [HiveMQ Cloud](https://www.hivemq.com/cloud/).
2. Sign up for a **free or enterprise account**.
3. Verify your email and log in.

### **2. Create an MQTT Broker**
1. Click **Create New Cluster**.
2. Choose a **cloud region** for deployment.
3. Set the cluster name (e.g., `healthcare-mqtt-broker`).
4. Select **TLS-enabled** connections.
5. Click **Deploy** and wait for the setup to complete.

### **3. Get Connection Details**
- **Broker URL:** `your-cluster-url.hivemq.cloud`
- **Port:** `8883` (TLS secured)
- **Username:** Set in **HiveMQ Cloud Dashboard**
- **Password:** Set in **HiveMQ Cloud Dashboard**

## 📡 MQTT Topics
All MQTT messages are transmitted under a **single topic**:
```
healthcare/sensor_data
```

### **Example MQTT Payload**
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
- **TLS Encryption**: All MQTT messages use TLS 1.2+ for secure transmission.
- **Authentication**: Username/password authentication is required for every device.
- **Access Control**: Only authorized devices can publish and subscribe.
- **Data Retention**: Critical messages are retained for real-time monitoring.

## 🚀 Connecting an IoT Devices
To connect an IoT device to HiveMQ Cloud, use the following Python example:
```python
import paho.mqtt.client as mqtt

BROKER_URL = "your-cluster-url.hivemq.cloud"
PORT = 8883
USERNAME = "your-username"
PASSWORD = "your-password"

client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set()

client.connect(BROKER_URL, PORT, 60)
client.loop_start()
```
