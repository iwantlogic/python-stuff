program = input("> ")

num = ""
connum = ""

for i in program:
    if i=="0" or i=="1":
        connum += i
    elif i=="_":
        num = int(connum, 2)
        connum = ""
    elif i==">":
        print(chr(num))
    elif i=="+":
        num +=1
    elif i=="-":
        num -= 1
    elif i=="%":
        print(bin(num)[2:])
