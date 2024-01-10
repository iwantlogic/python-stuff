import random
import sys
import time

x = input("Length?: ")
if x=="random":
    x = random.randint(0, 80)
else:
    x = int(x)
y = ""
speed = 0
while y not in ["slow", "normal", "fast"]:
    y = input("Speed? (slow normal fast): ")
if y=="slow":
    speed = 0.05
elif y=="normal":
    speed = 0.01
elif y=="fast":
    speed = 0
password = ""

while True:
    password += random.choice(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_")
    if len(password)==x:
        print(f"Password: {password}")
        password=""
    sys.stdout.write(f"{len(password)} | {password} \r")
    sys.stdout.flush()
    time.sleep(speed)

