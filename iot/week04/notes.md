# Week 04 — IoT Connectivity Technologies

> Slides: [week04-iot-edge-04.pdf](lecture/week04-iot-edge-04.pdf)

**Learning objectives:** identify key connectivity requirements, explain wireless communication basics, compare major IoT connectivity technologies, explain network topologies and gateways, and **select suitable connectivity for an IoT application**.

**The selection chain used all lecture:**
```
Application requirements -> Connectivity requirements -> Physical communication constraints
 -> Candidate technologies -> Technology comparison -> Connectivity selection
```

**Contents:** 1. Connectivity fundamentals · 2. Local and short-range technologies · 3. Wide-area connectivity and technology selection

---

# Part 1 — IoT Connectivity Fundamentals

### Connection from week 3

| Week 3 — **what** the device sends | Week 4 — **how** the device establishes a link |
|---|---|
| Physical quantity → sensor → IoT device → processing → structured data → **serialized format** | **Serialized format** → communication interface → **connectivity technology** → receiver / gateway / network |

### What is IoT connectivity?

> **IoT connectivity** = a **wired or wireless communication link** that allows an IoT device to **exchange data** with another device, gateway, access point, base station or network.

Examples of connectivity paths:
- Wearable — **Bluetooth** → smartphone
- Camera — **Wi-Fi** → access point
- Machine — **Ethernet** → industrial network
- Farm sensor — **LoRa** → gateway
- Tracker — **cellular** → base station

### Connectivity vs communication protocol

| **Connectivity** | **Communication protocol** |
|---|---|
| **How the devices get connected** | **How data is exchanged once the connection exists** |
| Wi-Fi, BLE, Ethernet, LoRa, cellular | Covered in **week 5** |

```
IoT device -> Connectivity technology -> Communication link established -> Communication protocol -> Application / server
```

> **Analogy: connectivity technology = the road or highway; communication protocol = the rules for how information travels on that road.**

Wi-Fi gives you a wireless link, but it does **not** define how an application exchanges sensor messages with a server. The protocol answers: where is the destination, how should data be delivered, what happens if communication fails, and how should an application request or publish information.

### Why not use Wi-Fi for everything?

| Application | Main characteristics | Suitable technology |
|---|---|---|
| **Security camera** | High data volume, continuous video, fixed location, power available, local network | **Ethernet / Wi-Fi** |
| **Wearable health sensor** | Small data, battery powered, worn on body, phone nearby | **BLE** |
| **Farm temperature sensor** | Low data rate (~10 bytes, e.g. `{"temperature": 24.3, "battery": 81}`), long range, battery/solar | **LoRa** |
| **Delivery vehicle tracker** | Moving, city-wide/regional, moderate or low data, no fixed nearby gateway | **LTE / cellular** |

> **Technically possible ≠ architecturally appropriate.**

**The method:** first ask *"What does this application need?"*, then *"Which technology matches those requirements?"*

**Common connectivity requirements: range, data rate, power, mobility.**

### Requirement 1: Range

> **Range** = the **maximum practical communication distance** between communicating nodes.

| Scale | Technology |
|---|---|
| Centimeters | **NFC** — contactless payment, transit passes |
| Meters (local/short) | **BLE** |
| Tens/hundreds of meters | **Wi-Fi** |
| Kilometers | **LoRa** |
| Wide area | **Cellular** |
| Regional/global | **Satellite** |

> **"Range = 100 m" does NOT mean "always works at 100 m".** Real range depends on transmitter power, antenna, frequency, receiver sensitivity, obstacles, interference and environment. **100 m in an open field ≠ 100 m through factory walls.**

### Requirement 2: Data rate

> **Data rate** = amount of digital data transferred per unit time, typically **bit/s**.

- Temperature sensor: **25–100 bytes every 1–10 minutes** — it does not need a 1 Gbit/s link.
- Video camera: **continuous stream**, possibly millions of bits per second. (A 1 Gbit/s link ≈ **125 MB/s**.)

**Bandwidth vs data rate:** **bandwidth** is the *maximum* amount transmittable in a given time; **data rate** is the rate actually transferred. Greater bandwidth can support higher data rates, but **the two are not identical**.

### Requirement 3: Power consumption

A wireless **transceiver (radio)** operates in states: **transmit, receive, idle/listen, sleep**.

| State | Power demand |
|---|---|
| Transmit / receive | **High** activity |
| Idle / listening | Moderate |
| Sleep | **Very low** |

> **Design objective for battery devices: keep the radio asleep as much as possible, and activate it only when communication is necessary.**

**Example 1 — mains-powered security camera:** continuous power, continuous connectivity, high-volume video, frequent communication. Communication energy is **not** the dominant constraint; prioritize **data rate, stable connection, latency, reliability**.

**Example 2 — coin-cell wearable:** very small battery, no convenient charging, lifetime of months, tiny data (heart rate 78 bpm, temperature 36.7 °C, battery 83 %). The pattern is:

```
Sleep for most of the time -> Wake briefly -> Measure sensor -> Transmit a small message -> Return to sleep
```

**Why radio activity matters — the calculation (E ≈ I × t):**

| | **Device A** | **Device B** |
|---|---|---|
| Behaviour | Transmit 1 s **every minute** | Transmit 1 s **every hour** |
| Transmissions/day | 60 × 24 = **1440** | **24** |
| Transmit time/day | 1440 s = **0.4 h** | 24 s = **0.00667 h** |
| At 30 mA | 30 × 0.4 = **12 mAh/day** | 30 × 0.00667 = **0.20 mAh/day** |

> **Device A consumes about 60× the transmit energy of device B.**

**Real battery consumption is more complicated:** energy is also spent on sensor measurement, processor operation, **radio startup**, transmission, reception, listening, waiting, **retransmission** and sleep. Still, **communication frequency and radio-on time strongly influence battery life**.

**Duty cycle** = the **fraction of time the radio is active** compared with total time.
- Device A: 1 s every 60 s → **1.67 %**
- Device B: 1 s every 3600 s → **0.028 %**

> **Lower duty cycle → less radio-on time → lower communication energy → longer battery life.**

**More data also means more radio-on time** (20 bytes vs 2 MB): more transmission time → more radio activity → more energy.

**The balance:** a slowly changing temperature sensor **should not** transmit every second — unnecessary communication consumes battery and network resources. But an **emergency gas-leak sensor** needs **low latency and a rapid alarm**. **Connectivity design always balances multiple requirements.**

### Requirement 4: Latency

> **Latency** = delay between sending information and its arrival/use at the destination.

| Application | Delay tolerance |
|---|---|
| Soil moisture monitoring | Seconds/minutes acceptable |
| Building temperature | Seconds often acceptable |
| Emergency alarm | Much lower delay desired |
| Time-sensitive control | **Very low delay required** |

### Requirement 5: Mobility

> **Mobility** = whether a device **changes physical location while operating**, and whether communication must **continue while it moves**.

| Mobility level | Example | Communication requirement |
|---|---|---|
| **Fixed** | Factory machine | Stays in one place → **Ethernet** is fine |
| **Local mobility** | Smartwatch | Moves within a limited local area → **BLE** within range of the phone |
| **Wide-area mobility** | Scooter / vehicle | Moves over large geographic areas → **cellular** |

**Rental scooter example:** it travels across areas A–D, needs location and battery/status reporting, so the system must stay available across a **large geographic area**. **Wi-Fi is less suitable** — once the scooter leaves coverage, there is no connection.

**Range vs mobility:**

| | **Range** | **Mobility** |
|---|---|---|
| Main question | **How far can the link reach?** | **Can communication continue as the device moves?** |
| Example | Sensor 3 km from a gateway | Scooter travelling through a city |
| Relevant factor | Radio/link distance | **Coverage + infrastructure while moving** |

### Other selection factors

| Factor | What it adds |
|---|---|
| **Device density** | Not just one device — **how many devices compete for or share the infrastructure** |
| **Infrastructure** | What already exists. A wearable can use the phone's **Bluetooth**; a remote farm sensor with **no Wi-Fi nearby** needs something else (e.g. cellular) |
| **Environment** | **Concrete** weakens/absorbs signals; **steel** reflects and blocks; **machinery** causes electromagnetic interference; **underground structures** severely block signals |
| **Cost and reliability** | Is occasional loss acceptable? Is availability critical? Is the infrastructure privately controlled? Is **redundant coverage** required? |

> **Connectivity selection depends on engineering performance *and* deployment constraints.**

### The connectivity trade-off triangle

> A system rarely maximizes **long range**, **high data rate** and **very low power** simultaneously.

Choose based on application requirements, balance the three, and accept that **no single technology is best for every use case**.

### Short discussion: four scenarios

| Scenario | Range | Data | Power | Mobility | Priority | Choice |
|---|---|---|---|---|---|---|
| **A. Security camera** | Local building | High — continuous video | Low concern if mains-powered | Fixed | **Data rate** | Ethernet / Wi-Fi |
| **B. Wearable heart-rate patch** | Short | Low — small periodic measurements | **Very important** (battery) | Moves with person | **Low power** | BLE |
| **C. Farm soil sensor** | Long — several km | Very low — tiny periodic message | **Very important** (battery) | Fixed | **Long range, low power** | LoRa |
| **D. Delivery tracker** | Wide area — city/regional | Low to moderate — periodic location | Important | **Highly mobile** | **Mobile, wide-area coverage** | Cellular |

---

# Part 2 — Local and Short-Range Connectivity Technologies

### Connectivity categories

| Wired | Local / short-range wireless | Identification / very short range | Wide area |
|---|---|---|---|
| Ethernet | Wi-Fi, BLE, IEEE 802.15.4 | RFID, NFC | LoRa, NB-IoT, LTE-M, 4G/5G, satellite |

### Wired vs wireless

| Wired (physical cable) | Wireless (radio) |
|---|---|
| Stable link | **Flexible deployment** |
| High throughput possible | **Mobility possible** |
| Less radio-frequency interference | Subject to propagation/interference |
| **Installation needed** | **Coverage constraints** |

### Ethernet

| Strengths | Limitations |
|---|---|
| Very high data rate | **Physical cable required** |
| Stable, reliable physical link | Installation effort |
| Low susceptibility to RF interference | **Limited mobility** |
| Suitable for continuous communication | |

**Typical IoT roles:** industrial machines, gateways, fixed cameras, building equipment.

**Power over Ethernet (PoE):** delivers **electrical power and network data over the same Ethernet cabling** — **one cable = data + power**. Useful for IP cameras, wireless access points, gateways, and industrial sensors/controllers.

### Wi-Fi

**Characteristics:** local-area, **high throughput**, existing infrastructure is common, and **relatively high power** compared with low-power IoT radios. Best for **local-area devices where Wi-Fi infrastructure already exists**.

**Limitations:** limited range (especially rural); requires an **access point and power**, which may not be available or economical to deploy; and its **relatively high power drains a coin-cell battery** — wasteful when a sensor only sends a tiny amount of data.

### BLE — Bluetooth Low Energy

> **BLE** = low-power communication designed for **battery-powered devices**, **short range** (tens of meters), commonly used for **device-to-phone** or **device-to-gateway** communication, ideal for **sensor data and simple control at low data rates**.

**Why BLE is low power:** the radio **stays off most of the time**, **wakes briefly** to send or receive small data, and the **short active time reduces energy use** — the duty-cycle principle from Part 1.

**Use cases:** syncing with a phone (notifications, health data), monitoring vital signs, activity/step/sleep tracking, indoor navigation and asset tracking, and sending sensor readings (temperature, humidity, environmental data) to a smartphone.

### Wi-Fi vs BLE

| Requirement | **Wi-Fi** | **BLE** |
|---|---|---|
| Data rate | Higher | Lower |
| Power | Higher | **Very low** |
| Typical range | Local | Short/local |
| Typical infrastructure | **Access point** | **Phone/gateway** |
| Typical application | Camera | Wearable |

### IEEE 802.15.4

> Specifies a **low-rate, low-power wireless foundation** used by several IoT networking technologies (e.g. Zigbee).

**Key characteristics:** **low data rate** (small, infrequent transmissions such as sensor measurements), **low power** (battery devices), **short to medium range** (tens to hundreds of meters), and suitability for **many sensor nodes** — IoT applications with lots of low-power devices.

### Network topology

> **Topology** describes **how communicating nodes are arranged and connected**.

| Topology | Arrangement | Advantages | Limitations | Example |
|---|---|---|---|---|
| **Point-to-point** | Two endpoints communicate directly | Simple | Only two nodes | Sensor → controller |
| **Star** | Multiple devices connect through **one central node** | Simple; easy centralized management | **Central point dependency**; every endpoint must reach the center | Devices → Wi-Fi AP |
| **Mesh** | Nodes connect **through neighboring nodes** | **Extended coverage**; **alternative paths** | More complexity (maintaining relationships); **relay burden** | Building sensor network |

**Mesh relay burden:** a node must send **its own data and relay another node's data** → more relay activity → more radio-on time → **more energy consumption**.

### RFID — Radio Frequency Identification

> **RFID** uses radio waves to **automatically identify and track tags** attached to objects, animals or people **without requiring a direct line of sight**.
> **Line of sight (LoS)** = an unobstructed straight path through the air between transmitting and receiving antennas.

| Feature | **Barcode** | **QR code** | **RFID** |
|---|---|---|---|
| Reading method | Optical | Optical | **Radio wave** |
| Line of sight | Required | Required | **Not required** |
| Multiple items | Usually one at a time | Usually one at a time | **Multiple tags possible** |
| Cost | Very low | Very low | Higher |
| Typical use | Product ID | Links/tickets/info | **Inventory/assets** |

**NFC** (near-field communication) is the **centimeter-range** relative, used for contactless payment and transit passes.

### Local technology comparison

| Technology | Relative range | Data rate | Power | Typical use |
|---|---|---|---|---|
| **Ethernet** | Cable | Very high | Usually powered | Machine / gateway / camera |
| **Wi-Fi** | Local | High | Medium–high | Camera / appliance |
| **BLE** | Short | Low–medium | **Very low** | Wearable |
| **802.15.4 / Zigbee** | Short–medium | Low | Low | Sensor network |
| **RFID / NFC** | Very short (reader-dependent) | Low | **Very low / passive** | Identification |

### Short discussion: choose a technology

| Case | Technology | Range reason | Data-rate reason | Power reason | Infrastructure reason |
|---|---|---|---|---|---|
| **Smartwatch → phone** | **BLE** | Short-range communication | Small/moderate | Very low power | The smartphone already supports BLE and acts as the nearby central device |
| **Machine-vision camera → control room** | **Ethernet or Wi-Fi** | Local scale | Video requires high data rate | Camera is usually mains-powered | Ethernet preferred if cabling exists; Wi-Fi if cabling is difficult and an AP is available |
| **Warehouse pallet identity** | **RFID** | Only reader-to-tag range | Only a small identifier needs transferring | **Passive tags may operate without a battery** | Install fixed or handheld RFID readers |
| **Building temperature sensors** | **IEEE 802.15.4** | Short-to-medium; multiple nodes can cover a building | Readings are very small and periodic | Low power | A coordinator can collect data from many sensor nodes |

---

# Part 3 — Wide-Area Connectivity and Technology Selection

### Local vs wide-area connectivity

| **Local connectivity** | **Wide-area connectivity** |
|---|---|
| Short-range connection | Broader-area connectivity |
| Local access to nearby devices or a local network | Connects devices over long distances, across **cities, regions or globally** |

Why local isn't enough: **in rural and remote areas, local connectivity may simply not be available.**

### LPWAN — Low-Power Wide-Area Network

> **LPWAN** = wireless technologies designed for IoT that provide **long-range communication with very low power consumption**. **Trade-off: very low data rate.**

| Cellular LPWAN (licensed spectrum) | Non-cellular LPWAN (unlicensed spectrum) |
|---|---|
| Run by **telecom operators** | Run on **open radio bands** |
| Example: **NB-IoT, LTE-M** | Example: **LoRa** |

LPWAN can use little power because the battery benefits from a **low duty cycle**.

### LoRa

> **LoRa** = a long-range, low-power **radio modulation / physical-layer** technology. It shapes radio waves so they **travel long distances on very low power**, at **low data rates**.

**LoRa vs LoRaWAN:**

| **LoRa** | **LoRaWAN** |
|---|---|
| The **radio modulation** used to transmit data over the air | The **network protocol**: defines how devices, gateways and network services communicate |

In real deployments: **device → LoRa/LoRaWAN → gateway → Ethernet/cellular/Wi-Fi → internet**.

| Strengths | Limitations |
|---|---|
| Long range | **Very low data rate** |
| Low power | Not for high-bandwidth applications |
| **Private gateway possible** | Gateway/network infrastructure still required |
| Useful in remote sensing | |

### Cellular IoT

IoT devices use cellular networks to reach the internet **via a mobile operator**: **wide geographic coverage**, **operator-managed infrastructure**, **mobility support**, and **subscription/service dependency**.

**LoRa vs cellular:**

| | **LoRa** | **Cellular** |
|---|---|---|
| Primary target | Simple machines and industrial sensors | Smartphones, tablets, laptops |
| What it transmits | **Tiny numbers** (GPS points, temperature) | HD video, websites, apps, voice |
| Bandwidth | **Extremely low** (a few bytes per message) | **Massive** (gigabytes per second) |
| Network infrastructure | **Private or public** | **Public only** (must use a carrier's tower) |
| Battery consumption | **Ultra-low** (can last 10 years on one battery) | High (drains phone batteries in 1–2 days) |

### NB-IoT and LTE-M

**NB-IoT** — a **cellular LPWAN** using the existing cellular network, operated by telecom companies: **wide-area coverage, low data rate, low power, good indoor coverage**, suitable for **relatively static, low-data devices** (e.g. **smart meters**).

**LTE-M** — cellular IoT for **connected, mobile things**: leverages existing **LTE infrastructure** for broad coverage, supports **higher data rates**, **handles moving devices more efficiently**, and is well suited to **small, mobile, battery-powered devices**. (LTE-M is for machines — sensors, trackers; LTE is for smartphones and tablets.)

| | **NB-IoT** | **LTE-M** | **LoRa** |
|---|---|---|---|
| Data | Lower | Higher | Very low |
| Mobility | Limited / lower focus | **Better** | Limited |
| Power | Low | Low–moderate | Low |
| Infrastructure | Operator network | Operator network | **Private / local gateway possible** |
| Typical application | **Meters** | **Trackers** | **Farm / environmental sensors** |

### Full technology comparison

| Technology | Range | Data | Power | Mobility | Dependency |
|---|---|---|---|---|---|
| **Ethernet** | Cable | Very high | Powered | None | Cabling |
| **Wi-Fi** | Local | High | Medium–high | Moderate | Access point |
| **BLE** | Short | Low–medium | Very low | Good (within range) | Phone / gateway |
| **802.15.4** | Short–medium | Low | Low | Limited | Coordinator / gateway |
| **LoRa** | Long | Very low | Very low | Limited/moderate | Gateway |
| **NB-IoT** | Wide | Low | Low | Limited | Cellular operator |
| **LTE-M** | Wide | Low–medium | Low–medium | Good | Cellular operator |
| **4G/5G** | Wide | High | Higher | Excellent | Cellular operator |
| **Satellite** | Very wide | Low–medium | Higher | Good | Satellite service |

> ⚠️ This table's columns are **misaligned in the slide**; the version above is the reconstructed mapping. Check it against the slide if it is used as an exam answer.

### Connectivity selection framework — the ten questions

1. How far? 2. How much data? 3. How much power? 4. How quickly? 5. Moving or fixed?
6. How many devices? 7. What infrastructure exists? 8. What environment? 9. What reliability? 10. What cost?
**→ Select technology.**

### Worked cases

**Case 1 — Machine vision.** An industrial camera inspecting a production line, connected to the control room.
*Reasoning:* high data (video needs high bandwidth), fixed installation, power available, reliability (wired is stable). → **Ethernet**, alternative **Wi-Fi** if cabling is difficult.

**Case 2 — Wearable.** A body-worn sensor communicating with a smartphone.
*Reasoning:* short range (meters) is sufficient, small data amounts, low power suits battery operation, smartphone available as a nearby gateway. → **BLE**.
*Why not LTE-M?* Greater complexity (modem, SIM) and higher energy and service cost.

**Case 4 — Rental scooter.** A connected scooter reporting location and status.
*Reasoning:* wide coverage across a city, supports mobility, uses existing operator infrastructure. → **LTE-M / cellular**, a good balance of coverage, mobility and power efficiency.

*(The slides jump from case 2 to case 4.)*

### Summary

```
Requirement -> Candidate connectivity technology -> Physical / infrastructure fit -> Trade-off justification
Device -> Connectivity link -> Network / gateway
```

**Next:** once the connectivity link exists, **how is information addressed, transported and exchanged?** → **communication protocols (week 5)**.

---

## Most important for exams

- **Connectivity vs protocol:** connectivity = **how devices get connected** (the road); protocol = **how data is exchanged once connected** (the rules of the road). Week 4 vs week 5.
- **Four core requirements: range, data rate, power, mobility** — plus latency, device density, infrastructure, environment, cost and reliability.
- **"Range = 100 m" never means "always works at 100 m"** — power, antenna, frequency, obstacles, interference, environment all matter.
- **Bandwidth ≠ data rate** (maximum possible vs actually transferred).
- **Radio states:** transmit/receive (high), idle/listen (moderate), **sleep (very low)**. Design goal: **keep the radio asleep**.
- **Duty cycle = active time ÷ total time.** Be ready to compute it (1 s per 60 s = **1.67 %**; 1 s per 3600 s = **0.028 %**) and the energy (**E ≈ I × t**: 30 mA × 0.4 h = **12 mAh/day** vs **0.20 mAh/day**, a **60×** difference).
- **Lower duty cycle → longer battery life; more data → more radio-on time → more energy.**
- **Mobility levels:** fixed (factory machine, Ethernet), local (smartwatch, BLE), wide-area (scooter, cellular). **Range vs mobility** = how far the link reaches vs whether it continues while moving.
- **Trade-off triangle:** you cannot maximize **long range + high data rate + very low power** at once.
- **The four canonical pairings:** camera → **Ethernet/Wi-Fi**; wearable → **BLE**; farm sensor → **LoRa**; vehicle tracker → **cellular/LTE-M**.
- **Topologies:** point-to-point, **star** (central dependency), **mesh** (extended coverage and alternative paths, but complexity and **relay burden → more energy**).
- **RFID vs barcode/QR:** radio vs optical, **no line of sight needed**, **multiple tags at once**, higher cost, **passive tags need no battery**. NFC = centimeters.
- **PoE** = data + power over one Ethernet cable.
- **LPWAN** = long range + very low power, **trade-off: very low data rate**. **Cellular LPWAN** (NB-IoT, LTE-M, licensed, operator-run) vs **non-cellular** (LoRa, unlicensed, private gateway possible).
- **LoRa = the radio modulation; LoRaWAN = the network protocol.**
- **NB-IoT vs LTE-M:** meters (static, low data, good indoor) vs trackers (mobile, higher data rate).
- **The ten selection questions**, and the ability to justify a choice with range / data / power / mobility / infrastructure reasons.
