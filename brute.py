import random
import sys
import time

password = input("Password (a-zA-Z0-9 space _-): ")
sleeptime = float(input("Sleep time?: "))

i=0
gpass = ""
while i < len(password):
    guess = random.choice(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-")
    if guess==password[i]:
        gpass += guess
        i += 1
        sys.stdout.write(f"{guess} | {gpass} \r")
        time.sleep(sleeptime)
        sys.stdout.flush()
    else:
        sys.stdout.write(f"{guess} | {gpass} \r")
        time.sleep(sleeptime)
        sys.stdout.flush()

print(f"{guess} | {gpass}")
