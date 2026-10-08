# Week 01 — Introduction to Internet-of-Things (IoT)

> Lecturer: LIAU, Yee Yeng, Ph.D. — Department of Global IT Engineering, Fall 2026.
> Slides: [week01-iot-edge-01.pdf](lecture/week01-iot-edge-01.pdf)

**Contents:** 1. What is IoT? · 2. Understanding IoT systems · 3. Practical

---

# Part 1 — What is IoT?

**Learning objectives:** explain the meaning of IoT, identify the main components of an IoT system, describe the basic IoT data flow, and recognize IoT applications in daily life and industry.

### Opening discussion

> Which of these can be considered IoT? Smart watch · Traffic camera · Factory robot · Delivery tracking system · Air conditioner controlled by smartphone

The answer comes back in Part 3 (Activity 1): **potentially all of them**, if they are **connected and exchange data with other systems**.

### Definition and the important idea

> **Internet-of-Things (IoT)** connects the **physical world** with the **digital world**.

- IoT is **not only about connecting devices**.
- **IoT is about using data from physical things**, to answer:
  - What is happening now?
  - Is the condition **normal or abnormal**?
  - Should the system **send an alert**?
  - Should an action be **taken automatically**?

### Examples

| In daily life | In industry |
|---|---|
| Smart watch measuring heart rate | **Smart logistics** — status of picking vehicles, empty lots, picking location |
| Smart home — light and temperature control | **Automated inspection** — scan, inspect, feed back results |
| Smart parking — parking lot availability | **Energy monitoring** — status and remote control |
| Smartphone-connected air purifier | **Smart agriculture** — control farm temperature and humidity |
| Package tracking — location and arrival time | |

### Main components of IoT

> **IoT = a connected system, not only a single device.**

| Component | Role |
|---|---|
| **Physical object** | The thing being observed or controlled |
| **Sensor** | Collect data from physical objects |
| **Network** | Transmit data from sensors to the processing system |
| **Processing system** | Receive, analyze, support decisions |
| **Application** | Make information available to the user; enable control by users |
| **User or actuator** | Acts on the information, or acts physically |

### Sensors

> **Sensor** = measures and obtains **physical data** from a device.

| Sensor type | Data |
|---|---|
| Temperature sensor | Heat |
| Humidity sensor | Moisture |
| Light sensor | Brightness |
| Camera | Image / video |
| Accelerometer | Linear motion |
| Gyroscope | Rotation and angular velocity |
| GPS | Location |

### IoT devices

An IoT device usually contains: **sensor, processor, memory, communication module, power source, software**.

Example devices:
- **Smart watch** — sensors, Bluetooth, memory, processing, power source
- **Machine equipped with a sensor**
- **Vehicle tracking device** — GPS, processing, communication, power management

### Networks in IoT

IoT devices need communication to **send data and receive commands**. Examples: **Wi-Fi, Bluetooth, Ethernet**.

**Network selection depends on:** distance, speed, power consumption, cost, reliability.

### Processing systems: device, edge, cloud

| | **Device** | **Edge** | **Cloud** |
|---|---|---|---|
| **Role** | Collects raw data | Processes data **near devices** | **Large-scale** storage and analytics |
| **Resources** | Very limited CPU/memory | Moderate | Effectively unlimited |
| **Typical tasks** | Read temperature, check battery, simple filtering | Event detection, aggregation/filtering | Model training, historical analysis, dashboards, centralized management |
| **Benefit** | Low latency at source | Reduced bandwidth, faster response | Store history, analyze trends |

> **Key idea:** **device** handles sensing; **edge** handles nearby processing; **cloud** handles large-scale storage and analytics.

This three-way split is the backbone of the whole course — the second half is about **edge computing**.

### IoT in a smart home

- **Gateway:** provides the connection between devices and external services.
- Sensor data is transmitted to a **cloud platform**, which stores information, analyzes it, and makes it available to apps.
- Two directions: **data flow** (sensor → cloud) and **control flow** (commands → device).

### IoT in machine monitoring (industry)

```
Temperature/vibration sensors -> Edge gateway / PLC -> Factory network -> Cloud platform -> Monitoring dashboard
                                 (filtering,                             (storage, analytics,        (maintenance
                                  aggregation,                            machine learning,           engineer)
                                  protocol connection)                    rule engine)
```

**Possible outcomes:** real-time monitoring (machine health, performance), **predictive maintenance** (detect anomalies, predict failure), and **alerts** (notify abnormal conditions).

> **Security applies across all layers:** devices, network, cloud, applications.

### Why IoT matters

It enables **real-time monitoring, automation, data-driven decision-making, remote control, predictive maintenance, and smart services**.

### Part 1 summary

- IoT connects physical objects to digital systems.
- IoT systems **collect, transmit, process and use** data.
- Main components: sensors, devices, networks, processing systems, applications.
- **A device becomes part of IoT when it can:** sense or generate data, communicate through a network, and interact with another digital system or application.
- Applications: homes, cities, factories, healthcare, logistics, transportation.

---

# Part 2 — Understanding IoT systems

**Learning objectives:** how IoT systems differ from traditional computing systems, their major characteristics and design challenges, and why **scalability, interoperability, reliability and security** matter.

### A smart device alone is not a complete IoT system

> Smart watch → Smartphone → Internet → Cloud platform → Health application → User

A complete IoT system includes: **physical device, data, communication, processing, application, user or action**.

### The physical–digital loop

Many IoT systems operate as a **continuous loop**:

```
Physical environment -> Sense -> Data -> Process -> Decision -> Action -> Physical environment
```

Example: temperature rises → sensor detects 30 °C → system decides the room is too hot → air conditioner turns on → temperature decreases.

> IoT systems can both **observe** and **control** the physical world.

### Traditional system vs IoT system

| Traditional system | IoT system |
|---|---|
| Human enters data | **Sensors generate data** |
| Mostly digital environment | **Physical + digital** |
| Usually a few computing devices | **Potentially many devices** |
| User initiates many actions | **Systems may act automatically** |
| Computing often centralized | **Computing may be distributed** |

**Key differences:** physical-world interaction, large number of devices, continuous data, heterogeneous hardware, limited computing/storage/communication resources, distributed computing.

### Characteristic 1: Many connected devices

From **5 sensors in a room** → **500 in a building** → **10,000 in a factory** → **millions in a smart city**.

**More devices mean:** more data, more communication, more management, **more failures**.

**Scalability** = can the system continue to work efficiently as the number of devices or amount of data increases? IoT platforms must scale in **devices, messages, storage, processing, and users**.

### Characteristic 2: Continuous operation

- 1 sensor at 1 reading/second = **86,400 readings per day**; 1,000 sensors = **86,400,000 readings per day**.
- **Main issue:** do we really need to **send and store every measurement**?

IoT data also **changes over time** (10:00 → 23.5 °C, 10:01 → 24.1 °C, 10:02 → 24.8 °C, 10:03 → 29.7 °C), which raises: when was it measured, is it changing, is the current value abnormal, and is history important?

### Characteristic 3: Heterogeneity

IoT systems contain **different types of devices**, differing in manufacturers, sensors, operating systems, **data formats**, communication technologies and processing capabilities.

| Example device | Its nature |
|---|---|
| Smart watch | Small, battery-powered |
| Security camera | High data volume |
| Factory machine | High reliability required |
| Agricultural sensor | Long-distance communication |

**Different applications have different priorities** — IoT architecture is **application-dependent**:

| Application | Important requirement |
|---|---|
| Smart home | Convenience, cost |
| Healthcare | **Reliability, privacy** |
| Smart factory | **Fast response, reliability** |
| Smart agriculture | **Long range, low power** |
| Smart city | **Scalability** |

### Characteristic 4: Limited device resources

Many IoT devices have limited **CPU, memory, storage, battery and communication capacity**.

| Smartphone / PC | Small IoT sensor |
|---|---|
| Powerful CPU | Small processor |
| GB of memory | **KB/MB** of memory |
| Recharged frequently | **May operate for years** |
| Fast network | Low-bandwidth network |

**Energy consumption** is a major design issue. Energy is used by **sensor measurement, processing, communication, and keeping the network connection active**.

> **Important principle: sending data can consume significant energy.**
> More communication → more energy use → shorter battery life.

This is the reason edge filtering exists: **not sending** is often the cheapest optimization.

### Characteristic 5: Distributed systems

Processing does not necessarily happen in one place: **device → nearby processing → remote processing**.

| Task | Possible location |
|---|---|
| Read temperature | **Device** |
| Detect overheating | **Device / Edge** |
| Store one year of history | **Cloud** |
| Analyze factory-wide trends | **Cloud** |
| Trigger immediate alarm | **Device / Edge** |

> **Processing location depends on system requirements.** Anything urgent stays local; anything historical goes to the cloud.

### The six challenges

| # | Challenge | The problem | Responses |
|---|---|---|---|
| 1 | **Latency** | Delay between an event and the system response. Machine overheats → data to cloud → cloud processes → command returns. **What if this takes several seconds?** | For **safety-critical** applications, **faster local processing** may be required |
| 2 | **Bandwidth** | 1,000 sensors measuring constantly creates high network traffic, higher cost, more storage and processing | **Raw data → local filtering → send only important data to the cloud** |
| 3 | **Network dependency** | If the Internet fails: data cannot be uploaded, remote monitoring stops, decisions may be delayed | **Local processing, local storage, retry mechanisms** |
| 4 | **Reliability** | Components fail | Sensor failure → health check / backup sensor; communication failure → retry / local buffering; gateway failure → backup gateway / local operation; low battery → monitoring / power saving; software errors → restart / error handling / update; cloud failure → local processing / later synchronization |
| 5 | **Security** | Many possible attack points: unauthorized access, **fake sensor data**, data theft, device takeover, privacy leakage | Security across all layers |
| 6 | **Privacy** | IoT may collect location, health information, home activities, video, industrial operation data | **Does all collected data need to leave the local environment?** → **edge computing** |

> **Should one failed component stop the entire system?** No — that is what reliability design is for.

### Part 2 summary

IoT systems are challenging because they involve **many devices, continuous data, heterogeneous technologies, limited resources, distributed processing, network dependency, reliability, and security and privacy**.

**IoT architecture must consider:** where to process, what to send, what to store, how quickly we must respond, and how to keep the system reliable and secure.

---

# Part 3 — Practical

**Objectives:** decide whether a system is IoT, trace how data moves, distinguish sensing / communication / processing / action, and design a simple conceptual IoT system.

### Activity 1: Is it IoT?

**Suggested answer: potentially all of them**, if they are connected and exchange data with other systems.

| Example | Why it may be IoT |
|---|---|
| Smart watch | Sends sensor data to smartphone/cloud |
| Smart TV | Communicates with internet services |
| Traffic camera | Sends traffic data to a monitoring system |
| Factory robot | Exchanges operational data |
| Delivery tracker | Sends location/status information |
| Smart air conditioner | Receives commands from a smartphone |

### Activity 2: What does IoT data look like?

```
Device ID:   sensor_01
Time:        10:32:15
Temperature: 25.4°C
```

**Five things to identify:** device identity, measurement time, measured quantity, measured value, **unit**.

**Why these fields are needed:**
- **Device ID** — which device produced the data?
- **Timestamp** — when was the measurement collected?
- **Sensor value (+ unit)** — what was measured?

This is exactly the record structure used in the week 2 and week 3 practicals.

**IoT data changes over time:**

```
10:00 sensor_01 23.5°C
10:01 sensor_01 24.1°C
10:02 sensor_01 24.8°C
10:03 sensor_01 29.7°C
10:04 sensor_01 25.2°C
```

- **Which reading is highest?** 10:03, at **29.7 °C**.
- **Why is the timestamp important?** A value alone can't tell you when a condition occurred, how fast it changed, or whether it's current.
- **Why keep previous readings?** To see **trends**, judge whether a value is **abnormal** compared with normal behaviour, and smooth noise (the moving average in week 2).

### Activity 3: Trace an IoT system (smart home)

> A temperature sensor measures room temperature. Data is sent via **Wi-Fi** to a smart home application. The user views the temperature and controls the air conditioner.

| Data flow | Action/control flow |
|---|---|
| Temperature → Sensor → Network → Application → User | User → Application → Network → Air conditioner |

> IoT systems can both **observe** and **control** the physical world.

### Activity 4: Arrange the components (smart health monitoring)

**Suggested answer:**

```
Patient -> Wearable sensor -> Smartphone -> Internet -> Cloud platform -> Doctor dashboard
```

- **Where is the physical world?** The patient.
- **Where does sensing occur?** The wearable sensor.
- **Where is communication used?** Sensor → smartphone, and smartphone → internet → cloud.
- **Who uses the information?** The doctor (through the dashboard), and the patient through their app.

### Activity 5: Smart home, healthcare and industry

| | **Smart home** | **Healthcare** | **Industry** |
|---|---|---|---|
| **Physical object** | Room / home | Patient | Machine |
| **Sensor** | Temperature sensor | Heart-rate sensor | Vibration sensor |
| **Data** | Temperature | Heart rate | Vibration |
| **User** | Resident | Doctor | Engineer |
| **Possible action** | Control AC | Send alert | Maintenance |

> **The applications are different, but the basic structure is similar.**

### Activity 6: Design your own IoT system

**Example — smart classroom.** *Problem:* the classroom becomes too hot.

```
Room temperature -> Temperature sensor -> IoT device -> Wi-Fi -> Monitoring system
                 -> Teacher / building manager -> Air conditioner
```

```
Device: classroom_sensor_01
Time:   14:20
Temperature: 29.5°C
```
Display in the application: **Classroom A — Temperature: 29.5 °C**

**Group task** (3–5 members): choose smart home, smart farm, smart parking, smart factory or smart logistics, then answer: (1) what problem are you solving, (2) what should be measured, (3) build the system.

### Practice roadmap

| Week | Practical topic |
|---|---|
| 1 | Understand IoT systems without programming |
| 2 | Generate and process sensor measurements |
| 3 | Represent IoT data |
| 4–6 | Connect and communicate |
| 7–15 | Build increasingly capable IoT and edge systems |

**Preparation for week 2:** form groups of 3–4, bring a laptop, install **Python 3.+**, prepare an editor, and check that `print("Hello IoT")` runs.

---

## Most important for exams

- **IoT connects the physical and digital worlds, and is about *using data from physical things*** — not merely connecting devices. The four questions: what's happening now, normal or abnormal, alert, automatic action.
- **A device is part of IoT when it can: sense/generate data, communicate over a network, and interact with another digital system.**
- **Components in order:** physical object → **sensor** → **network** → **processing system** → **application** → **user/actuator**.
- **Sensor table:** temperature/humidity/light/camera/accelerometer/gyroscope/GPS and what each measures.
- **Device vs edge vs cloud:** sensing / nearby processing / large-scale storage and analytics. Be ready to place tasks (read temperature = device, immediate alarm = device-edge, one year of history = cloud, factory-wide trends = cloud).
- **Physical–digital loop:** sense → data → process → decision → action.
- **Traditional vs IoT system table** (human-entered vs sensor-generated data, digital vs physical+digital, few vs many devices, user-initiated vs automatic, centralized vs distributed).
- **Five characteristics:** many devices (**scalability**), continuous operation, **heterogeneity**, limited resources/energy, distributed processing.
- **Six challenges:** latency, bandwidth, network dependency, reliability, security, privacy — with the standard response to each.
- **Sending data costs energy:** more communication → more energy → shorter battery life. Filtering locally saves bandwidth, energy and cost.
- **Application priorities:** home = convenience/cost, healthcare = reliability/privacy, factory = fast response/reliability, agriculture = long range/low power, city = scalability.
- **An IoT data record needs:** device ID, timestamp, quantity, value, unit.
