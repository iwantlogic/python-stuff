for i in range(255):
    if i % 32 == 0:
        print()
    else:
        print(f"|{chr(i)}|", end="")
print()

