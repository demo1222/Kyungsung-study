import paho.mqtt.client as mqtt

BROKER = "127.0.0.1"
PORT = 1883

COMMAND_TOPIC = "factory/machine01/fan/command"

def on_connect(client, userdata, f, reason_code, props):
    print("Virtuak acturator connected")

    client.subscribe(COMMAND_TOPIC)

    print("listening for commands:")
    print(COMMAND_TOPIC)


def on_message(client, userdata, message):
    command = message.payload.decode()

    print("\n Command recieved:")
    print(command)

    if command == "FAN_ON":
        print("virtual fan status: ON")
    elif command == "FAN_OFF":
        print("virtual fan status: OFF")
    else:
        print("Uknown command")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, keepalive=60)

client.loop_forever()