choice = int(input("Enc[1] or Dec[2]: "))
ptxt = str(input("Input >> "))
key = int(input("key >> "))

def enc(ptxt, key):
    ctxt = ""
    for i in range(len(ptxt)):
        char = ptxt[i]

        if (char.isupper()):
            ctxt += chr((ord(char) + key - 65) % 26 + 65)

        if (char.islower()):
            ctxt += chr((ord(char) + key - 97) % 26 + 97)
    return ctxt

def dec(ctxt, key):

if choice == 1:
    print(enc(ptxt, key))

if choice == 2:
    print(dec(ctxt, key))
