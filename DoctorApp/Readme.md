# DoctorApp - IoT-Based Healthcare Security

## 📌 Overview
DoctorApp is an **Android application** designed to help doctors monitor patient health remotely using IoT-based **smart healthcare solutions**. The app securely collects, transmits, and displays patient vital signs, ensuring real-time monitoring and emergency alerts.

## 🚀 Features
- 📡 **Real-time Health Monitoring**: Receives patient vitals (Heart Rate, BP, Oxygen Levels, etc.) via IoT sensors.
- 🔔 **Automated Alerts**: Notifies doctors in case of abnormal readings.
- 🔒 **Secure Communication**: Uses **MQTT with TLS encryption** for secure data transfer.
- 📊 **Dashboard**: Provides a user-friendly interface to visualize patient data.
- 🔑 **Access Control**: Doctors can only view assigned patients’ data.

## 🛠️ Installation & Setup
### Prerequisites
- Android Studio **(latest version)**
- Android SDK & Emulator (or a physical device)
- MQTT Broker **(HiveMQ, Mosquitto, etc.)**

## Security Features
- **TLS Encryption**: Secures MQTT communication.
- **Authentication**: RSA key-based secure access.
- **Firewall Protection**: Restricts unauthorized access.
- **Data Privacy**: Encrypts patient health data.
