import random, sys, time

def check_key(key):
        char_sum = 0
        for c in key:
                char_sum += ord(c)
        sys.stdout.write(f"{char_sum} | {key} \r")
        sys.stdout.flush()
        return char_sum

key = ""
keysum = int(input("Keysum: "))
while True:
        key += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_")
        s = check_key(key)
        if s > keysum:
                key = ""
        elif s==keysum:
                print("Found valid key: {0}".format(key))
        
