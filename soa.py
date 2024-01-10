# SOA STACK ONLY ASSEMBLY 
import sys
stack = []

with open(sys.argv[1], "r") as file:
    program = file.read()
    lines = program.split("\n")
    for line in lines:
        if line=="":
            break
        parsed = line.split()
        if parsed[0]=="push":
            for i in range(int(parsed[2])):
                for j in parsed[1]:
                    stack.append(j)

        elif parsed[0]=="pushint":
            for i in range(int(parsed[2])):
                stack.append(int(parsed[1]))
        elif parsed[0]=="pprint":
            print(stack.pop())
        elif parsed[0]=="pprintn":
            for i in range(int(parsed[1])):
                print(stack.pop(), end="")
            print()
        elif parsed[0]=="revstack":
            stack = stack[::-1]

