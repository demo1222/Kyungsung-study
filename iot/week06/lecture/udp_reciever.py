import socket
import json

HOST = "127.0.0.1"
PORT = 5002

receiver = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

receiver.bind((HOST, PORT))

print("UDP receiver started")
print(f"Waiting at {HOST}:{PORT} ...")

data, addr = receiver.recvfrom(1024)

print("Received from:", addr)

message = data.decode()
print("\nRaw message:")
print(message)

sensor_data = json.loads(message)

print("\nDecoded sensor data:")
print("Device:", sensor_data["device"])
print("Temperature:", sensor_data["temperature"], "°C")

receiver.close()
