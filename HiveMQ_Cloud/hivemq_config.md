# HiveMQ Cloud Configuration Guide

## 📌 Overview
HiveMQ Cloud is a **managed MQTT broker** that allows **secure, real-time communication** for IoT applications. This document explains how to configure HiveMQ Cloud for the **IoT-based Smart Healthcare Security Project**.

---

## ⚙️ Setting Up HiveMQ Cloud

### **1. Create a HiveMQ Cloud Account**
1. Go to **[HiveMQ Cloud](https://www.hivemq.com/cloud/)**.
2. Click **Get Started for Free**.
3. Sign up and create a **new cluster**.
4. Choose **MQTT version 5** for better security.
5. Once created, **copy your broker details** (e.g., hostname, port, credentials).

---

### **2. Configure MQTT Client for HiveMQ**
Modify the `mqtt_config.py` file in your Python simulation project:

```python
# mqtt_config.py - MQTT Configuration for HiveMQ Cloud

import paho.mqtt.client as mqtt

# HiveMQ Cloud Configuration
BROKER = "your-broker-url.hivemq.cloud"  # Replace with actual HiveMQ broker URL
PORT = 8883  # Secure TLS Port
USERNAME = "your-username"  # Replace with HiveMQ username
PASSWORD = "your-password"  # Replace with HiveMQ password
TOPIC = "healthcare/iot/data"

# Callback function for connection
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to HiveMQ Cloud successfully!")
        client.subscribe(TOPIC)
    else:
        print(f"Connection failed with code {rc}")

# Initialize MQTT Client
client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set()  # Enables TLS encryption
client.on_connect = on_connect

# Connect to HiveMQ Cloud
client.connect(BROKER, PORT)
client.loop_start()
