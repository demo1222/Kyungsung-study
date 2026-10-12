import socket
import json

HOST = "127.0.0.1"
PORT = 5001

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen()

print("TCP server started")
print(f"Waiting at {HOST}:{PORT}")

conn, addr = server.accept()

print("\nClient connected:")
print(addr)

data = conn.recv(1024)

message = data.decode()

print("\nRaw Message")
print(message)

sensor_data = json.loads(message)

print("\nDecoded sensor data:")
print("Device:", sensor_data["device"])
print("Temperature:", sensor_data["temperature"], "C")

conn.sendall(b"Sensor data recieved")

conn.close()
server.close()

print("\n Connection closeds")