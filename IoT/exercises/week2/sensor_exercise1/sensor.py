import time
import random
from datetime import datetime

# Array (list) to store sensor detections
sensor_detection = []

# Threshold for temperature status check
THRESHOLD = 25.0


def collect_sensor_data(device_id='sensor_01', count=5, delay=1, threshold=THRESHOLD):
    """Generates sensor readings, determines status based on threshold, and stores into sensor_detection."""
    for i in range(count):
        temperature = round(random.uniform(20, 30), 3)
        timestamp = datetime.now().strftime('%H:%M:%S')

        # Update status based on threshold condition
        if temperature > threshold:
            status = 'WARNING'
        else:
            status = 'NORMAL'

        # Record entry as a dictionary
        record = {
            'id': len(sensor_detection) + 1,
            'timestamp': timestamp,
            'device_id': device_id,
            'temperature': temperature,
            'status': status
        }
        sensor_detection.append(record)

        print(f"[{timestamp}] Device: {device_id} | Temperature: {temperature:.2f}°C | Status: {status}")
        time.sleep(delay)


def get_sensor_stats(device_id=None):
    """Calculates average, minimum, and maximum temperature from sensor_detection."""
    data = sensor_detection
    if device_id:
        data = [r for r in data if r['device_id'] == device_id]

    if not data:
        return {'avg': 0.0, 'min': 0.0, 'max': 0.0, 'count': 0}

    temps = [r['temperature'] for r in data]
    return {
        'avg': sum(temps) / len(temps),
        'min': min(temps),
        'max': max(temps),
        'count': len(temps)
    }


# 1. Collect readings
print(f"--- Collecting Data (Threshold: {THRESHOLD}°C) ---")
collect_sensor_data(device_id='sensor_01', count=5)

# 2. Display statistics
stats = get_sensor_stats()
print("\n--- Temperature Statistics ---")
print(f"Total Readings: {stats['count']}")
print(f"Average: {stats['avg']:.2f}°C")
print(f"Minimum: {stats['min']:.2f}°C")
print(f"Maximum: {stats['max']:.2f}°C")
