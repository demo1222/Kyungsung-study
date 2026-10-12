import paho.mqtt.client as mqtt

BROKER = "127.0.0.1"
PORT = 1883

TOPIC = "factory/machine01/temperature"

def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected to MQTT broker")
    print("Reason code:", reason_code)

    client.subscribe(TOPIC)
    print("Subscribed to topic:", TOPIC)

def on_message(client, userdata, message):
    print("\nReceived message!")
    print("Topic:", message.topic)
    print("Payload:", message.payload.decode())
    print("QoS:", message.qos)


client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2
)

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, keepalive=60)

print("waiting for mqtt messages...")

client.loop_forever()
