import random
import time
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Settings
number_of_readings = 20
recent_readings = []

# Data collected during the simulation
timestamps = []
raw_data = []
ma_3_data = []

for i in range(number_of_readings):
    # -----------------------------
    # 1. Generate new sensor reading
    # -----------------------------
    temperature = round(random.uniform(20, 30), 2)
    
    # Get current timestamp
    timestamp = datetime.now()
    
    # Store timestamp and raw reading
    timestamps.append(timestamp)
    raw_data.append(temperature)
    
    # Keep recent readings
    recent_readings.append(temperature)
    
    # We only need the latest 3 readings
    if len(recent_readings) > 3:
        recent_readings.pop(0)

    # -----------------------------
    # 2. Moving average: window = 3
    # -----------------------------
    if len(recent_readings) >= 3:
        window_3 = recent_readings[-3:]
        ma_3 = sum(window_3) / 3
        ma_3_data.append(ma_3)
    else:
        ma_3 = None
        ma_3_data.append(None)

    # -----------------------------
    # 3. Display current result
    # -----------------------------
    print(
        "Time: ",
        timestamp.strftime("%H:%M:%S"),
        "| Temperature: ",
        temperature,
        "°C",
        "| MA(3): ",
        round(ma_3, 2) if ma_3 is not None else "Waiting"
    )

    # Simulate sensor sampling interval
    time.sleep(1)