import paho.mqtt.client as mqtt
import json
import random
import time

BROKER = "127.0.0.1"
PORT = 1883

TOPIC = "factory/machine01/temperature"

client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2
)

client.connect(
    BROKER,
    PORT,
    keepalive=60
)

client.loop_start()

print("MQTT temperature sensor started")
print("Publishing to:")
print(TOPIC)

try:
    while True:
        temperature = round(
            random.uniform(25.0, 35.0),
            1
        )

        sensor_data = {
            "device": "machine01",
            "temperature": temperature,
            "unit": "C"
        }
    
        payload = json.dumps(sensor_data)

        result = client.publish(
            TOPIC,
            payload,
            qos=0
        )

        print("\nPublished:")
        print(payload)

        time.sleep(2)

except KeyboardInterrupt:
    print("\nStopping sensor...")

finally:
    client.loop_stop()
    client.disconnect()
