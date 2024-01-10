# TJF MODULE

import socket, json

def clientsend(s, data):
    data2 = {"header": ["TCP JSON FORMAT", "HANDSHAKE", f"SIZEOFDATA: {len(data)}"], "data": [data, f"HOST: {socket.gethostbyname(socket.gethostname())}"]}
    data2 = json.dumps(data2)
    s.sendall(bytes(data2, "utf-8"))
