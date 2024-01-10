import sys
from sys import argv

if len(argv) < 2:
    sys.stderr.write("Usage: python shellcodegen.py <options> <binary_file> [payload (optional)]\nExample: pyth...gen.py --add-payload execve.bin AAAA....ZZZZ\n")
else:
    if argv[1].startswith("-"):
        if argv[1]=="--add-payload":
            if len(argv)<4:
                sys.stderr.write("Error: No payload or binary file specified")
            else:
                payload = argv[3]
                with open(argv[2], "rb") as file:
                    print("ByteStream:", stream:=bytes(payload, "utf-8")+file.read())
                    hm = input("Copy bytes to 'exploit.txt' file? (y/n): ")
                    if hm=="y":
                        print("Copying")
                        with open("exploit.txt", "wb") as file:
                            file.write(stream)
    else:
        with open(argv[1], "rb") as file:
            print("Stream:", file.read())


