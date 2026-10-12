from json import loads
import json
import paho.mqtt.client as mqtt

BROKER = "127.0.0.1"
PORT = 1883

TOPIC = "factory/machine01/temperature"
COMMAND_TOPIC = "factory/machine01/fan/command"

def on_connect(client, userdata, f, reason_code, props):
    print("Edge processor connected")

    client.subscribe(TOPIC)

    print("Listening to:")
    print(TOPIC)

    
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    temperature = data["temperature"]

    print("temperature", temperature, "C")

    if temperature > 30:
        command = "FAN_ON"
    else:
        command = "FAN_OFF"

    client.publish(COMMAND_TOPIC, command)

    print("action:", command)

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, keepalive=60)

client.loop_forever()