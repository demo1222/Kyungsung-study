import random
import time # time module: manage time delay
from datetime import datetime # datetime class to fetch and format current system time
import matplotlib.pyplot as plt

device_id = "sensor_01"
readings = []
value_only = []

# Moving average storage
ma_3 = []
ma_10 = []

# Task 2: Generate 100 humidity readings
for i in range(100):
    # Task 1: Virtual humidity sensor with realistic range (40% - 80%)
    humidity = round(random.uniform(40, 80), 2)
    timestamp = datetime.now().strftime("%H:%M:%S")

    # Store readings
    readings.append({"timestamp": timestamp, "device_id": device_id, "humidity": humidity})
    value_only.append(humidity)

    # Task 3: Detect high humidity (> 65%)
    if humidity > 65:
        status = "WARNING: High humidity"
    else:
        status = "NORMAL"

    # Task 4: Calculate moving averages (window = 3 and window = 10)
    if len(value_only) >= 3:
        ma_3.append(sum(value_only[-3:]) / 3)
    else:
        ma_3.append(None)

    if len(value_only) >= 10:
        ma_10.append(sum(value_only[-10:]) / 10)
    else:
        ma_10.append(None)

    print(f"Reading {i+1} [{timestamp}] - Humidity: {humidity}% - {status}")
    time.sleep(0.01)

# Summary statistics from the starter comments
print("\n--- Statistics ---")
print("Average Humidity:", round(sum(value_only) / len(value_only), 2), "%")
print("Minimum Humidity:", min(value_only), "%")
print("Maximum Humidity:", max(value_only), "%")

# Task 5: Compare the two moving averages
print("\n--- Moving Average Comparison ---")
print("1. Responsiveness: Window = 3 responds faster to sudden changes because it only averages 3 points.")
print("2. Smoothness: Window = 10 produces a smoother result by filtering out short-term fluctuations.")

# Task 6: Visualize the results
plt.figure(figsize=(10, 5))
plt.plot(value_only, label="Raw humidity readings")
plt.plot(ma_3, label="Moving Average, window = 3")
plt.plot(ma_10, label="Moving Average, window = 10")
plt.xlabel("Reading Number")
plt.ylabel("Humidity (%)")
plt.title("Virtual Humidity Sensor Time-Series Analysis")
plt.legend()
plt.tight_layout()
plt.show()
