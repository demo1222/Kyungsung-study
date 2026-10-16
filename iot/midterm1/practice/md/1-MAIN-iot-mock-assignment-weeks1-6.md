# Practice Assignment – IoT Fundamentals

**MAIN TEST** · Same format as *Individual assignment 1* · Coverage: Week 1–6 · Total: 100 marks

<div class="box"><b>Name:</b> ____________________________________<br><br><b>Student ID:</b> ______________________________</div>

> **Practice version.** The structure, marks and question styles copy the teacher's assignment (Section A multiple choice, Section B short answer, Section C applied scenarios, Section D integrated communication), but **all questions are new**. Model answers and marking points are at the end.

## Section A – Multiple choice (20 marks – 10 questions x 2 marks)

1. Which statement best describes the main idea of IoT?
     - A. Connecting as many devices as possible to Wi-Fi
     - B. Using data from physical things to know what is happening and to support decisions or actions
     - C. Replacing all computers with sensors
     - D. Storing every file in the cloud

2. A factory machine overheats and must trigger an alarm immediately. Where should the alarm decision be made?
     - A. On the device or at the edge
     - B. In the cloud, after one year of history is collected
     - C. By the maintenance engineer reading a monthly report
     - D. In a database backup

3. A sensor message contains only the value `29.7`. What is the main problem?
     - A. The value is too large to transmit
     - B. The value must be serialized to IPv6 first
     - C. Without a device ID, timestamp and unit, the value cannot be interpreted reliably
     - D. The value proves the sensor is broken

4. A program calculates a moving average with window 3 and another with window 10 on the same readings. Which statement is correct?
     - A. Window 10 reacts faster to sudden changes
     - B. Both windows give exactly the same result
     - C. Window 3 gives the smoother line
     - D. Window 3 reacts faster; window 10 gives a smoother result

5. A cold-chain box has a normal range of 2–8 °C and a physically valid range of −20 to 50 °C. A reading of 10 °C is:
     - A. INVALID
     - B. VALID, but TOO_WARM
     - C. VALID and NORMAL
     - D. INVALID and TOO_COLD

6. A radio transmits for 1 second every 10 seconds. What is its duty cycle?
     - A. 1 %
     - B. 0.1 %
     - C. 10 %
     - D. 90 %

7. A warehouse must identify many pallets at the same time without a direct line of sight. Which technology is most appropriate?
     - A. RFID
     - B. Barcode
     - C. QR code
     - D. Wi-Fi

8. Which statement about LoRa and LoRaWAN is correct?
     - A. LoRa and LoRaWAN are exactly the same thing
     - B. LoRaWAN is the radio modulation and LoRa is the network protocol
     - C. LoRa is a cellular technology run by telecom operators
     - D. LoRa is the radio modulation; LoRaWAN defines how devices, gateways and network services communicate

9. A UDP sender prints "UDP message sent", but the receiver program is not running. Which statement is correct?
     - A. TCP will retransmit the datagram automatically
     - B. UDP has no connection setup and no built-in delivery confirmation, so the sender does not know
     - C. The receiver will get the datagram later when it starts
     - D. The MQTT broker stores the datagram

10. Which topic is matched by the subscription `building/+/humidity`?
     - A. `building/floor1/room2/humidity`
     - B. `building/floor1/humidity`
     - C. `building/humidity`
     - D. `building/floor1/temperature`

## Section B – Short Answer (30 marks – 5 questions x 6 marks)

**11. Device, Edge and Cloud**

A smart factory has vibration sensors on 200 machines. Explain the role of:

1. the device;
2. the edge; and
3. the cloud.

Give one suitable task for each in this factory.

<div class="lines l8"></div>

**12. Sensor data quality**

A humidity sensor produces:

| Time | Humidity |
|---|---|
| 10:00 | 45.2 % |
| 10:01 | 45.6 % |
| 10:02 | 145.0 % |
| 10:03 | 45.9 % |
| 10:04 | 46.1 % |

Answer:

a. What type of data is this?

<div class="lines l2"></div>

b. Identify the data-quality problem.

<div class="lines l2"></div>

c. Explain how the application could detect and handle the problem.

<div class="lines l3"></div>

**13. Duty Cycle and Battery**

A soil sensor transmits for **2 seconds every 5 minutes**. While transmitting, the radio draws **40 mA**.

a. Calculate the duty cycle.

<div class="lines l2"></div>

b. How many transmissions does it make per day, and what is the total transmit time per day?

<div class="lines l2"></div>

c. Estimate the transmit energy per day in mAh (E ≈ I × t).

<div class="lines l2"></div>

d. Give one design change that would extend battery life.

<div class="lines l2"></div>

**14. IPv6 and 6LoWPAN**

Explain two differences between IPv4 and IPv6.

Then explain why a battery-powered IEEE 802.15.4 sensor still needs 6LoWPAN, even though IPv6 provides many addresses.

<div class="lines l8"></div>

**15. MQTT Quality of Service**

Explain the difference between MQTT QoS 0, QoS 1 and QoS 2.

Your answer should refer to:

- the delivery guarantee;
- the messages exchanged;
- one suitable IoT message for each level.

Do not simply state that one level is "more reliable."

<div class="lines l8"></div>

<div class="pb"></div>

## Section C – Applied Scenario Questions (40 marks – 2 questions x 20 marks)

**16. Smart Parking System**

A city installs battery-powered occupancy sensors in **3,000 street parking spaces** across the city centre.

Each sensor:

- sends a very small message (a few bytes) only when a space becomes free or occupied;
- is installed in the road surface, often far from any building;
- must operate for at least five years on one battery;
- has no Wi-Fi access point nearby.

The data is used by a driver parking app, a city traffic dashboard and a payment system.

a. Identify three communication requirements that are important when selecting connectivity for these sensors. (3 marks)

<div class="lines l4"></div>

b. Choose a suitable connectivity technology.

Possible examples include:

- Wi-Fi
- BLE
- LoRa
- NB-IoT
- 4G/5G

Give two reasons for your choice. (5 marks)

<div class="lines l5"></div>

c. A sensor sends:

```
{
  "space": "P-1043",
  "occupied": true,
  "battery": 87
}
```

If MQTT is used, propose a suitable **topic** for this message and explain the difference between the topic and the **payload**. (3 marks)

<div class="lines l3"></div>

d. Three applications (app, dashboard, payment system) need the same occupancy data. Would request–response or publish–subscribe be more suitable?

Explain. (4 marks)

<div class="lines l4"></div>

e. Which MQTT QoS level would you choose for the occupancy messages, and why?

The driver app is restarted and needs the **current** state of each space immediately, without waiting for the next change. Which MQTT feature helps, and how? (5 marks)

<div class="lines l6"></div>

**17. Hospital Ward Environment Monitor**

A hospital places small battery-powered temperature and humidity sensors in every ward.

Each sensor:

- has very limited memory and processing capability;
- communicates over IEEE 802.15.4 in a **mesh** network;
- should participate in an IPv6-based IoT network;
- is occasionally asked for its latest reading by the nurse-station application.

A Python **edge gateway** in each ward also checks the temperature: if it is above **26 °C**, it publishes the command `AC ON` to the ward's air-conditioner controller.

a. Which application protocol is suitable for requesting a reading from these constrained sensors? (2 marks)

<div class="lines l2"></div>

b. Which transport protocol is commonly used with this application protocol? (2 marks)

<div class="lines l2"></div>

c. Give one advantage and one cost of using a **mesh** topology for these sensors. (3 marks)

<div class="lines l3"></div>

d. Complete the protocol stack: (5 marks)

```
Ward Monitoring Application
        ↓
____________________
        ↓
____________________
        ↓
IPv6
        ↓
____________________
        ↓
IEEE 802.15.4
```

<div class="lines l3"></div>

e. Explain the role of the edge gateway. Your answer should refer to: (8 marks)

- why the edge gateway is both an MQTT subscriber and an MQTT publisher;
- which topic the air-conditioner controller should subscribe to;
- why the decision is made at the edge instead of in a remote cloud.

<div class="lines l8"></div>

<div class="pb"></div>

## Section D — Integrated IoT Communication (10 marks)

**18 — Trace the Data**

Consider the following IoT system from the week 6 practical:

```
Humidity Sensor
↓
Python dictionary  {"device": "lab01", "humidity": 48.5}
↓
json.dumps()
↓
encode()
↓
TCP socket  (socket.AF_INET, socket.SOCK_STREAM)
↓
IP  (127.0.0.1, port 5000)
↓
TCP server  (recv → decode → json.loads)
```

Explain the role of each of the following:

| Technology | Role |
|---|---|
| Python dictionary | <br><br><br> |
| `json.dumps()` | <br><br><br> |
| `encode()` | <br><br><br> |
| `SOCK_STREAM` (TCP) | <br><br><br> |
| `AF_INET` (IP) | <br><br><br> |
| Port 5000 | <br><br><br> |

What would change, and what would stay the same, if the program used `SOCK_DGRAM` instead?

<div class="lines l4"></div>

<div class="pb"></div>

## Answer Key and Marking Guide

### Section A (2 marks each)

| Q | Ans | Why |
|---|---|---|
| 1 | B | IoT is about **using data from physical things**, not only connecting devices. |
| 2 | A | Urgent decisions stay local (device/edge) to avoid cloud latency and network dependency. |
| 3 | C | An IoT record needs device ID, timestamp, quantity, value and unit. |
| 4 | D | A small window responds faster; a large window filters short-term fluctuations. |
| 5 | B | 10 °C is physically possible (VALID) but above 8 °C (TOO_WARM). Validation ≠ status. |
| 6 | C | 1 ÷ 10 = 0.1 = 10 %. |
| 7 | A | RFID: radio, no line of sight, many tags at once. |
| 8 | D | LoRa = modulation (physical layer); LoRaWAN = network protocol. |
| 9 | B | "Message sent" does not prove the receiving application got it. |
| 10 | B | `+` matches **exactly one** level. A has two levels in the middle; C has none; D ends in `temperature`. |

### Section B (6 marks each)

**11.** (2 marks per part: role + task)

- **Device** – collects raw data close to the machine with very limited CPU/memory: reads vibration values, checks its battery, simple filtering.
- **Edge** – processes data **near the devices** (gateway/PLC in the factory): aggregates and filters readings from many machines, detects an abnormal vibration and raises an immediate alarm. Benefit: less bandwidth, faster response, keeps working if the Internet fails.
- **Cloud** – large-scale storage and analytics: stores months of history from all 200 machines, analyzes factory-wide trends, trains predictive-maintenance models, dashboards.

**12.**

a. **Time-series data** (sensor values recorded with timestamps at regular intervals). (2)

b. 145.0 % at 10:02 is **physically impossible** (humidity is 0–100 %): an **invalid value / outlier**, probably a sensor or transmission error. (2)

c. **Validate** each reading against the physically valid range (0–100 %) and mark it `INVALID`. Then do not use it in averages or alarms: discard it, keep it flagged, or replace it with `None` / leave a gap; a moving average over the valid values (≈ 45.6–45.9 %) also smooths noise. Do **not** silently replace it with 0. (2)

**13.**

a. Period = 5 min = 300 s. Duty cycle = 2 ÷ 300 = **0.67 %**. (1.5)

b. 24 h × 60 ÷ 5 = **288 transmissions/day**. Transmit time = 288 × 2 s = **576 s ≈ 0.16 h**. (1.5)

c. E ≈ 40 mA × 0.16 h = **6.4 mAh/day**. (1.5)

d. Any one: transmit less often (e.g. every 15 minutes, or only when the value changes); send less data (smaller/compact payload) so the radio is on for less time; filter or aggregate at the device; keep the radio asleep between transmissions. Lower duty cycle → longer battery life. (1.5)

**14.**

- IPv4 = **32-bit** address, dotted decimal (e.g. `192.168.1.25`), **limited** address space. IPv6 = **128-bit** address, hexadecimal in 8 colon-separated groups (e.g. `2001:db8::25`), an **extremely large** address space for very large numbers of IoT devices. (any two differences, 3 marks)
- IPv6 solves the **address shortage**, not the limits of constrained devices. A standard IPv6 header is **40 bytes**, too much overhead for tiny packets on a low-power 802.15.4 link with small frames, little memory and a battery. **6LoWPAN** is an **adaptation layer** that (1) **compresses the header to as few as 2–7 bytes**, (2) **fragments and reassembles** large IPv6 packets, and (3) supports **mesh routing**. A border router then connects the sensor network to the normal IPv6 Internet. (3 marks)

**15.** (2 marks per level)

| QoS | Guarantee | Messages | Suitable message |
|---|---|---|---|
| 0 | **At most once**: no acknowledgment, no MQTT-level redelivery; a message can be lost | PUBLISH only | Periodic temperature telemetry: the next reading arrives soon anyway |
| 1 | **At least once**: publisher waits for an acknowledgment and resends if it is missing; **duplicates are possible** | PUBLISH → PUBACK | Fire alarm or machine-fault alarm: must arrive; receiving it twice is acceptable |
| 2 | **Exactly once**: four-step handshake prevents both loss and duplicates; highest overhead | PUBLISH → PUBREC → PUBREL → PUBCOMP | Critical control command or a payment/transaction message where duplicate processing must be avoided |

The trade-off is reliability against speed and network cost.

### Section C (20 marks each)

**16. Smart Parking**

a. Any three (1 each): **long range / coverage** (sensors spread across the city, far from buildings); **very low power** (5+ years on a battery); **very low data rate** (a few bytes, only on change); **good coverage through obstacles** (sensor in the road surface, cars parked on top); **many devices / density** (3,000 sensors); **no local infrastructure** (no Wi-Fi nearby).

b. (choice 1 mark + two reasons 2 marks each) **NB-IoT** is the best fit: it is a **cellular LPWAN** using the operator's existing network, so no gateways or Wi-Fi need to be installed across the city; it has **wide-area and good indoor/underground coverage**; **low power** for multi-year battery life; and **low data rate** is enough for a static device sending tiny messages (like smart meters). *Also accepted:* **LoRa** with a few private gateways: long range, very low power, very low data rate, private network without a subscription. Not suitable: Wi-Fi (no AP, high power), BLE (short range), 4G/5G (high power, far more bandwidth than needed).

c. Topic example: `city/parking/zoneA/P-1043/occupancy` (or `parking/<zone>/<space>/status`). (1) The **topic** is the label used by the broker to **classify and route** the message; the **payload** (the JSON) is the **actual information**. (2) A hierarchy lets the dashboard subscribe to `city/parking/#` or `city/parking/zoneA/+/occupancy`.

d. **Publish–subscribe** (1). With request–response every application would have to **poll** each of 3,000 sensors repeatedly, creating unnecessary traffic and poor scaling, and the sensor would need to know every destination. With pub-sub the sensor publishes **once to the broker**; the broker distributes to every subscriber; sensors and applications are **decoupled**, and a new application can be added just by subscribing. (3)

e. **QoS 1** (1): a status change happens rarely and must not be lost (drivers and payments depend on it), and receiving the same "occupied" twice does no harm; QoS 2's extra overhead is not needed (QoS 0 is risky because a lost change is not repeated soon). (2) **Retained message** (1): the sensor publishes its status with the retain flag; the broker keeps the **latest** message for each topic and sends it immediately to a new subscriber, so the restarted app gets the current state of every space at once (latest state only, not history). (1) *(Bonus: a **Last Will** of `offline` on a status topic tells the city when a sensor disconnects unexpectedly.)*

**17. Hospital Ward Monitor**

a. **CoAP** (Constrained Application Protocol): lightweight, request–response, resource-oriented, compact binary. (2)

b. **UDP**. (2)

c. Advantage (1.5): **extended coverage** (a message can hop through neighbours to reach the coordinator) and **alternative paths** if one node fails. Cost (1.5): **relay burden**: a node sends its own data and relays others', so more radio-on time and **more energy**; also more complexity.

d. (5) Ward Monitoring Application → **CoAP** → **UDP** → IPv6 → **6LoWPAN** → IEEE 802.15.4.

e. (8)

- The edge gateway **subscribes** to the sensor topic (e.g. `hospital/ward3/temperature`) to receive readings, parses the JSON payload and applies the rule *temperature > 26 °C → `AC ON`, otherwise `AC OFF`*. It then **publishes** the command to a **different topic**, so it is both subscriber and publisher. (3)
- The air-conditioner controller is a **subscriber to the command topic** (e.g. `hospital/ward3/ac/command`), **not** the sensor topic. The command is application-defined. (2)
- Deciding at the edge gives **low latency** (no round-trip to a distant cloud), keeps working if the **Internet connection fails**, saves **bandwidth** (only important events need to go to the cloud), and keeps patient-area data **local** for privacy. Complete loop: sense → communicate → process → act. (3)

### Section D (10 marks)

| Technology | Role |
|---|---|
| Python dictionary | The structured **application data** inside the program (key–value pairs: device, humidity). It cannot be sent as it is. |
| `json.dumps()` | **Serializes** the dictionary into a **JSON string**: a standard text representation that other programs can read. |
| `encode()` | Converts the text into **bytes**, because a socket transmits bytes, not strings. |
| `SOCK_STREAM` (TCP) | **Transport layer**: connection-oriented (the client must `connect()`; the server uses `listen()`/`accept()`), reliable, ordered **byte stream** delivered to the right process. |
| `AF_INET` (IP) | **Network layer**: IPv4 addressing; `127.0.0.1` identifies the **host** (localhost). |
| Port 5000 | Identifies the **application/process** on that host (the TCP server). |

(1.5 marks per row = 9)

With `SOCK_DGRAM` (UDP): no `connect()`/`accept()` and no handshake; the sender uses `sendto()` and the receiver `recvfrom()`; each send is a separate **datagram** (message boundaries preserved), with **no built-in delivery confirmation, ordering or retransmission**. The **JSON payload and its meaning stay exactly the same**; it still uses IP addresses and ports. Only the transport behavior changes. (1)
