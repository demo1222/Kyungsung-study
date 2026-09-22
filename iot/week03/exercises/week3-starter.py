from datetime import datetime
import random
import json

device_id = "sensor_01"
temperature_quality = None
humidity_quality = None
temperature_status = None
temperature_warning_count = 0

all_readings = []

# step 1: generate one sensor reading
temperature = round(random.uniform(20, 35), 2)

# step 2: Add humidity and pressure
humidity = round(random.uniform(30, 90), 1)

# 
pressure = round(random.uniform(950, 1050), 1)

timestamp = datetime.now().isoformat(timespec="seconds")


if 0 <= humidity <= 100:
    humidity_quality = "VALID"
else:
    humidity_quality = "INVALID"

if -20 <= temperature <= 50:
    temperature_quality = "VALID"
else:
    temperature_quality = "INVALID"

if temperature < 23:
    temperature_status = "TOO_COLD"
    temperature_warning_count += 1
elif temperature > 30:
    temperature_status = "TOO_HOT"
    temperature_warning_count += 1
else:
    temperature_status = "PERFECT"

sensor_data = {
    "device_id": device_id,
    "timestamp": timestamp,
    "measurements": {
        "temperature": temperature,
        "humidity": humidity,
        "pressure": pressure
    },
    "quality": {
        "humidity_quality": humidity_quality,
        "temperature_quality": temperature_quality
    }
}

json_payload = json.dumps(sensor_data)

all_readings.append(sensor_data)

with open("sensor-log.json", "w", encoding="utf-8") as file:
    json.dump(all_readings, file, indent = 4)

with open("sensor-log.json", "r", encoding="utf-8") as file:
    loaded_readings = json.load(file)

    print("Number of saved readings:", len(loaded_readings))