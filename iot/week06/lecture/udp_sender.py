import socket
import json

HOST = "127.0.0.1"
PORT = 5002

sensor_data = {
    "device": "machine01",
    "temperature": 24.3,
    "unit": "C"
}

message = json.dumps(sensor_data)

sender = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

sender.sendto(
    message.encode(),
    (HOST, PORT)
)

print("UDP message sent:")
print(message)

sender.close()
