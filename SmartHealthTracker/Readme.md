# 📱 Smart Health Tracker App

## 📌 Overview
Smart Health Tracker is an **IoT-based healthcare application** that allows patients to monitor their vital health statistics, such as **heart rate, blood pressure, oxygen saturation, and body temperature**. The data is collected using **IoT sensors**, transmitted securely to the **cloud**, and can be accessed via this mobile application.

---

## 🏗️ Features
✅ **Real-time Health Monitoring** - Track vitals like heart rate, blood pressure, and body temperature.  
✅ **Cloud-based Storage** - Stores health data on a secure cloud server for remote access.  
✅ **Alerts & Notifications** - Sends alerts if health parameters exceed critical levels.  
✅ **Doctor Integration** - Allows doctors to view assigned patients' data securely.  
✅ **Secure Data Transmission** - Implements **TLS encryption** and **MQTT protocol** for secure data transfer.  

---

## 🚀 Installation & Setup

### **Prerequisites**
- Install **Android Studio**
- Install **Java JDK 11+**
- Install **Gradle**
- (Optional) MQTT Broker like **HiveMQ Cloud** for live data transmission

### 🔗 API Integration
This app uses MQTT (Message Queuing Telemetry Transport) for real-time health data transmission.
- Broker: HiveMQ Cloud
- Port: 8883 (TLS Secured)
- Topics:
  - /patient/heart_rate
  - /patient/blood_pressure
  - /patient/oxygen_saturation
  - /patient/body_temperature
To configure the MQTT connection, update `MQTTClient.java` with the correct broker URL and credentials.

--- 

## 🔒 Security Features
- **TLS Encryption** - Ensures secure data transmission.
- **RSA Key-Based Authentication** - Protects access control.
- **Firewall Configuration** - Limits unauthorized access to the MQTT server.
