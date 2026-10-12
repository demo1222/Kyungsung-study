import paho.mqtt.client as mqtt
import json
import random
import time

BROKER = "127.0.0.1"
PORT = 1883

client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2
)

client.connect(
    BROKER,
    PORT,
    keepalive=60
)

client.loop_start()

print("MQTT wildcard sensor started")

try:
    while True:
        temp1 = round(random.uniform(25.0, 35.0), 1)
        payload1 = json.dumps({
            "device": "machine01",
            "temperature": temp1,
            "unit": "C"
        })

        client.publish(
            "factory/machine01/temperature",
            payload1,
            qos=0
        )

        temp2 = round(random.uniform(25.0, 35.0), 1)
        payload2 = json.dumps({
            "device": "machine02",
            "temperature": temp2,
            "unit": "C"
        })

        client.publish(
            "factory/machine02/temperature",
            payload2,
            qos=0
        )

        vibration = round(random.uniform(0.1, 1.0), 2)
        payload3 = json.dumps({
            "device": "machine01",
            "vibration": vibration
        })

        client.publish(
            "factory/machine01/vibration",
            payload3,
            qos=0
        )

        status = random.choice(["running", "idle", "warning"])
        payload4 = json.dumps({
            "device": "machine01",
            "status": status
        })

        client.publish(
            "factory/machine01/status",
            payload4,
            qos=0
        )

        print("\nPublished 4 messages")
        time.sleep(2)

except KeyboardInterrupt:
    print("\nStopping sensor...")

finally:
    client.loop_stop()
    client.disconnect()
