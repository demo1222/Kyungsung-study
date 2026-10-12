import socket
import json

HOST = "127.0.0.1"
PORT = 5001

sensor_data = {
    "device" : "machine1",
    "temperature" : 25.3
}

message = json.dumps(sensor_data)

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

print("Connecting to server...")

client.connect((HOST, PORT))

print("Connected")

client.sendall(message.encode())

print("Sendoe data sent:")
print(message)

response = client.recv(1024)

print("\nserver reponse")
print(response.decode())

client.close()