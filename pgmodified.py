import random
import time
import os

x = int(input("Length?: "))
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
        print(f"Password: {password}\nPGMODIFIED: properties(len={len(password)}, password={password})")
        password=""
    time.sleep(speed)

