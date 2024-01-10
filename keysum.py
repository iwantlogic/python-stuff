import sys
import time

x = input("Key: ")
delay = float(input("Delay: "))
sum = 0
for i in x:
    sum += ord(i)
    sys.stdout.write(f"{i} | {sum} \r")
    sys.stdout.flush()
    time.sleep(delay)
print(f"{i} | {sum}")
