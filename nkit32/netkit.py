import socket
print("NetKit, Friendly Programable Network")

print()
while True:
    print("[1] Program")
    print("[99] Exit")
    x = int(input("netkit> "))
    if x==1:
        print("Setting up TCP network...")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        _type = input("[S]erver or [C]lient?: ")
        if _type=="s":
            port = int(input("Port?: "))
            s.bind(("127.0.0.1", port))
            s.listen()
            print("Listening for connections...")
            while True:
                client, addr = s.accept()
                print(f"Connection from {addr[0]}:{addr[1]}")
                client.send(b"Hello!, <server running on netkit>\n")
                print(client.recv(256).decode("utf-8"))
                print("Closed")
        if _type=="c":
            ip = input("IP to connect to?: ")
            port = int(input("{ip}:"))
            s.connect((ip, port))
            while True:
                
                s.send(bytes(input("Send: ")+"\n", "utf-8"))
                print(s.recv(256).decode("utf-8"))

    elif x==99:
        exit
