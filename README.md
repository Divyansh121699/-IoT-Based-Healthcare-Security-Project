# IoT-Based Healthcare Security Project

## 📌 Overview
This project focuses on **secure IoT-based smart healthcare solutions**, including:
- **Doctor Monitoring App** (`DoctorApp`) - Enables doctors to monitor patients remotely.
- **Smart Health Tracker App** (`SmartHealthTracker`) - Helps track patient vitals and generates alerts.
- **Python-based Data Simulation** (`project-simulation`) - Generates synthetic health data within a virtual machine and transmits it securely via MQTT.
- **HiveMQ Cloud Integration** (`HiveMQ_Cloud`) - Ensures secure and scalable MQTT communication.

## 🏗️ Project Architecture
The architecture consists of multiple components working together to enable secure healthcare monitoring:

1. **Data Generation Module** - Runs Python scripts inside a virtual machine to generate synthetic patient health data, including blood pressure, heart rate, and oxygen saturation.
2. **Mobile Applications (DoctorApp & SmartHealthTracker)** - Display patient data and send alerts in case of abnormalities.
3. **Cloud Server (HiveMQ Cloud)** - Acts as an MQTT broker facilitating secure communication between data simulation and applications.
4. **Security Layer** - Implements TLS encryption, RSA-based authentication, and firewall protection to secure communication.
5. **Virtual Machine (Ubuntu)** - Hosts the Python-based data generation module, MQTT client, and security monitoring scripts.

## 🔐 Security Measures
To ensure the integrity, confidentiality, and security of healthcare data, the following security measures are implemented:

1. **TLS Encryption** - Secures all MQTT communication between the virtual machine and the HiveMQ Cloud.
2. **RSA-Based Authentication** - Ensures that only authorized devices and users can access the system.
3. **Firewall Protection** - Configures strict firewall rules to limit access to the virtual machine and MQTT broker.
4. **Role-Based Access Control (RBAC)** - Defines access control policies for healthcare data.
5. **Data Anonymization** - Protects patient privacy by anonymizing sensitive health data before transmission.
6. **Intrusion Detection System (IDS)** - Monitors network traffic for suspicious activity.
7. **Secure API Communication** - Uses HTTPS and authentication tokens for API access between mobile apps and the cloud server.

## 📁 Folder Structure
```
IoT-Healthcare-Security/                   
│── DoctorApp2/                     # Doctor monitoring app (Extracted from DoctorApp2.zip)
│   ├── app/                        # Main Android app code
│   ├── gradle/                     # Gradle build files
│   ├── build.gradle                # Build configuration
│   ├── settings.gradle             # Project settings
│   ├── proguard-rules.pro          # Security settings
│   ├── AndroidManifest.xml         # App permissions and configurations
│   ├── README.md                   # Documentation for the app
│── SmartHealthTracker2/            # Health tracking app (Extracted from SmartHealthTracker2.zip)
│   ├── app/
│   ├── gradle/
│   ├── build.gradle
│   ├── settings.gradle
│   ├── proguard-rules.pro
│   ├── AndroidManifest.xml
│   ├── README.md
│
│── project-simulation/                 # Python-based healthcare data simulation (Extracted from project.zip)
│   ├── baseline_health.py               # Baseline health condition logic
│   ├── mqtt_config.py                    # Configuration for MQTT connection
│   ├── mqtt_server_exec.py               # MQTT broker execution script
│   ├── simulation.py                     # Main script for running simulations
│   ├── __pycache__/                      # Compiled Python cache files (ignored in Git)
│   │   ├── mqtt_config.cpython-312.pyc
│   │   ├── mqtt_server_exec.cpython-312.pyc
│   │   ├── baseline_health.cpython-312.pyc
│
│   ├── person/                          # Module for different types of patient simulations
│   │   ├── __init__.py                  # Initialization for the module
│   │   ├── healthy_person.py            # Simulates a healthy patient
│   │   ├── heart_issued_person.py       # Simulates a heart disease patient
│   │   ├── alzheimer_patient.py         # Simulates an Alzheimer’s patient
│   │   ├── __pycache__/                 # Compiled Python cache files (ignored in Git)
│   │   │   ├── healthy_person.cpython-312.pyc
│   │   │   ├── heart_issued_person.cpython-312.pyc
│   │   │   ├── alzheimer_patient.cpython-312.pyc
│
│── HiveMQ_Cloud/                        # Configuration and security for HiveMQ
│   ├── hivemq_config.md                 # Configuring HiveMQ Cloud
│   ├── mqtt_topics.md                   # Defining topics for data transmission
│   ├── security_measures.md             # Security settings for MQTT
│   ├── README.md                         # HiveMQ implementation guide
|
│── docs/                                # Documentation for the project
│   ├── Final_Project_Presentation.pptx  # Project presentation (Uploaded separately)
│
│── README.md                            # Main project overview
```

## 🔄 Workflow
1. **Data Generation Module** runs Python scripts within a virtual machine to create synthetic patient data and sends it to the MQTT broker (HiveMQ Cloud).
2. **HiveMQ Cloud** securely transmits the data to authorized applications.
3. **Mobile Applications** process the data, provide visualizations, and alert doctors in case of abnormalities.
4. **Security Layer** ensures encrypted and authenticated data transmission.
5. **Virtual Machine (Ubuntu)** hosts the data simulation scripts and performs real-time security monitoring.
