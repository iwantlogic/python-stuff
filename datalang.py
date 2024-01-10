mem = [0]*1025

def interpret(arg):
    for i in arg:
        a = i.split()
        if a[0].startswith("0x"):
            mem[int(a[0], 16)]=int(a[1], 16)
        else:
            print("invalid instruction")
            break
    outstart = 1024-256
    while outstart<=1024:
        if mem[outstart]!=0:
            print(chr(mem[outstart]), end="")
        outstart += 1
ilist = []
while True:
    a = input("> ")
    if a=="list":
        print("\n".join(ilist))
    elif a=="run":
        interpret(ilist)
    elif a=="poplist":
        ilist.pop()
    elif a=="clearlist":
        ilist = []
    elif a=="":
        continue
    elif a.split()[0]=="c2h":
        if a.split()[1]=="space":
            print(hex(ord(" ")))
        else:
            print(hex(ord(a.split()[1][0])))
    elif a=="mem":
        integer = 0
        while integer < len(mem):
            print(hex(mem[integer]), end=" ")
            if integer % 10 == 0:
                print(hex(integer))
            integer += 1 
        print(hex(integer))
    else:
        if a.startswith("0x"):
            ilist.append(a)

