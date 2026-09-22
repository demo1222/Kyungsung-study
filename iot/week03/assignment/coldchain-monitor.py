"""
Week 3 Group Practice Assignment
Smart Cold-Chain Delivery Monitoring Device

Virtual IoT device for a refrigerated pharmaceutical delivery box.
Generates sensor data, validates it, determines operating status,
builds a nested record, serializes it to JSON and compares payload sizes.
"""

import random
import json
import time
from datetime import datetime

# ---------------------------------------------------------------
# Device configuration
# ---------------------------------------------------------------
DEVICE_ID = "coldbox_07"      # Task 2: unique device ID
TOTAL_READINGS = 100          # Task 11: number of repeated IoT messages
DELAY_SECONDS = 0.05          # Task 11: short delay between records


# ---------------------------------------------------------------
# Task 1 - Virtual sensors
# ---------------------------------------------------------------
def read_sensors():
    """Generate one set of simulated measurements."""
    temperature = round(random.uniform(0, 12), 1)    # 0 - 12 C
    humidity = round(random.uniform(20, 85), 1)      # 20 - 85 %
    battery = round(random.uniform(10, 100), 1)      # 10 - 100 %
    return temperature, humidity, battery


# ---------------------------------------------------------------
# Task 3 - Validation (is the value physically possible?)
# ---------------------------------------------------------------
def check_temperature_valid(value):
    if -20 <= value <= 50:
        return "VALID"
    else:
        return "INVALID"


def check_humidity_valid(value):
    if 0 <= value <= 100:
        return "VALID"
    else:
        return "INVALID"


def check_battery_valid(value):
    if 0 <= value <= 100:
        return "VALID"
    else:
        return "INVALID"


# ---------------------------------------------------------------
# Task 4 - Operating status (is the value acceptable for the cargo?)
# ---------------------------------------------------------------
def temperature_status(value):
    if value < 2:
        return "TOO_COLD"
    elif value <= 8:
        return "NORMAL"
    else:
        return "TOO_WARM"


def humidity_status(value):
    if 30 <= value <= 70:
        return "NORMAL"
    else:
        return "HUMIDITY_WARNING"


def battery_status(value):
    if value < 20:
        return "LOW_BATTERY"
    else:
        return "NORMAL"


# ---------------------------------------------------------------
# Task 5 - Nested record
# ---------------------------------------------------------------
def build_record(temperature, humidity, battery):
    """Combine device info and measurements into one nested dictionary."""
    record = {
        "device_id": DEVICE_ID,
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "measurements": {
            "temperature": temperature,
            "humidity": humidity,
            "battery": battery
        },
        "quality": {
            "temperature": check_temperature_valid(temperature),
            "humidity": check_humidity_valid(humidity),
            "battery": check_battery_valid(battery)
        },
        "status": {
            "temperature": temperature_status(temperature),
            "humidity": humidity_status(humidity),
            "battery": battery_status(battery)
        }
    }
    return record


def line(title):
    print()
    print("=" * 62)
    print(title)
    print("=" * 62)


# ===============================================================
# PART A - one detailed record (Tasks 1 to 10)
# ===============================================================
print()
print("#" * 62)
print("#  SMART COLD-CHAIN DELIVERY MONITORING DEVICE")
print("#  Device:", DEVICE_ID)
print("#" * 62)

# ---- Task 1 ----
line("TASK 1 - Modify the Virtual Sensors")
temperature, humidity, battery = read_sensors()
print("Temperature : ", temperature, "C")
print("Humidity    : ", humidity, "%")
print("Battery     : ", battery, "%")

# ---- Task 2 ----
line("TASK 2 - Add Device Information")
timestamp = datetime.now().isoformat(timespec="seconds")
print("Device ID   : ", DEVICE_ID)
print("Timestamp   : ", timestamp)

# ---- Task 3 ----
line("TASK 3 - Validate the Sensor Measurements")
print("Temperature", temperature, "C ->", check_temperature_valid(temperature))
print("Humidity   ", humidity, "%  ->", check_humidity_valid(humidity))
print("Battery    ", battery, "%  ->", check_battery_valid(battery))

print()
print("-- Validation test with deliberately invalid values --")
print("Temperature 85.0 C ->", check_temperature_valid(85.0))
print("Humidity   120.0 %  ->", check_humidity_valid(120.0))
print("Battery     -5.0 %  ->", check_battery_valid(-5.0))
print("(normal virtual sensor generation is used again below)")

# ---- Task 4 ----
line("TASK 4 - Determine Operating Status")
print("Temperature status : ", temperature_status(temperature))
print("Humidity status    : ", humidity_status(humidity))
print("Battery status     : ", battery_status(battery))

# ---- Task 5 ----
line("TASK 5 - Create a Structured IoT Record")
record = build_record(temperature, humidity, battery)
print(record)

# ---- Task 6 ----
line("TASK 6 - Access Data from the Nested Dictionary")
print("record['device_id']                    ->", record["device_id"])
print("record['measurements']['temperature']  ->", record["measurements"]["temperature"], "C")
print("record['measurements']['battery']      ->", record["measurements"]["battery"], "%")
print("record['status']['temperature']        ->", record["status"]["temperature"])
print("record['quality']['humidity']          ->", record["quality"]["humidity"])

# ---- Task 7 ----
line("TASK 7 - Serialize the Record to JSON")
json_normal = json.dumps(record)
json_pretty = json.dumps(record, indent=4)
print("Normal JSON:")
print(json_normal)
print()
print("Indented JSON:")
print(json_pretty)

# ---- Task 8 ----
line("TASK 8 - Check the Data Types")
print("Type before serialization :", type(record))
print("Type after serialization  :", type(json_normal))

# ---- Task 9 ----
line("TASK 9 - Measure the JSON Payload Size")
normal_bytes = json_pretty.encode("utf-8")
normal_size = len(normal_bytes)
print("Normal (indented) JSON payload size :", normal_size, "bytes")

# ---- Task 10 ----
line("TASK 10 - Create Compact JSON")
json_compact = json.dumps(record, separators=(",", ":"))
compact_size = len(json_compact.encode("utf-8"))
reduction = (normal_size - compact_size) / normal_size * 100

print("Compact JSON:")
print(json_compact)
print()
print("Normal JSON size  :", normal_size, "bytes")
print("Compact JSON size :", compact_size, "bytes")
print("Size reduction    :", round(reduction, 1), "%")


# ===============================================================
# PART B - repeated messages and warning summary (Tasks 11 and 12)
# ===============================================================
line("TASK 11 - Generate Repeated IoT Messages")
print("Generating", TOTAL_READINGS, "IoT records...")
print()

# Task 12 - counters
temp_warnings = 0
humidity_warnings = 0
battery_warnings = 0

for i in range(1, TOTAL_READINGS + 1):
    t, h, b = read_sensors()
    rec = build_record(t, h, b)
    payload = json.dumps(rec, separators=(",", ":"))

    print("Reading", i, ":", payload)

    # count warnings
    if rec["status"]["temperature"] != "NORMAL":
        temp_warnings += 1
    if rec["status"]["humidity"] != "NORMAL":
        humidity_warnings += 1
    if rec["status"]["battery"] == "LOW_BATTERY":
        battery_warnings += 1

    time.sleep(DELAY_SECONDS)

# ---- Task 12 ----
line("TASK 12 - Count Warning Conditions")
print("Device ID                :", DEVICE_ID)
print("Total readings           :", TOTAL_READINGS)
print("Temperature warnings     :", temp_warnings)
print("Humidity warnings        :", humidity_warnings)
print("Low battery warnings     :", battery_warnings)
print("=" * 62)
