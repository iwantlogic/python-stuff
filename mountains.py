
altitude = 9
while 1:
    for i in range(8):
       mountain_height = int(input())
       if mountain_height == altitude:
          print(i)
       altitude = altitude - 1
