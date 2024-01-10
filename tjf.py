import socket, json

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sending = input("Data 2 send?: ")

data = {
        "header": [
            "TCP JSON FORMAT",
            "HANDSHAKE",
            f"SIZEOFDATA: {len(sending)}",
            ],
        "data":[
            sending,
            f"HOST: {socket.gethostbyname(socket.gethostname())}"
            ]
        }
data = json.dumps(data)
s.connect(("127.0.0.1", 1234))
s.sendall(bytes(data,"ascii"))

