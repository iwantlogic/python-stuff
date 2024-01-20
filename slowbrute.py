import random
import sys
import time

password = input("Password (a-zA-Z0-9 space _-): ")
gpass = ""
used = {0}
while 1:
    while len(gpass) < len(password):
        if gpass in used:
            print(f"{gpass} in used")
            gpass = ""
        guess = random.choice(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-")
        if len(used)>len(password)*ord(guess):
            if guess in password:
                gpass += guess
        else:
            gpass += guess
        sys.stdout.write(f"{guess} | {len(used)} | {gpass}\r")
        sys.stdout.flush()
        time.sleep(1/10**250)

    used.add(gpass)
    if gpass!=password:
        gpass=""
    else:
        break
print()
sys.stdout.flush()
print(gpass)
