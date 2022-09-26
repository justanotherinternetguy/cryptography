choice = int(input("Enc[1] or Dec[2] or Brute-force Dec[3]: "))

def enc(ptxt, key):
    ctxt = ""
    ptxt = ptxt.lower()
    for char in ptxt:
        ctxt += chr((ord(char) + key - 97) % 26 + 97)

    return ctxt.upper()


def dec(ctxt, key):
    ptxt = ""
    ctxt = ctxt.lower()
    
    for char in ctxt:
        ptxt += chr((ord(char) - key - 97) % 26 + 97)

    return ptxt.lower()


def bash(ctxt):
    ctxt = ctxt.lower()
    for i in range(26):
        txt = ""
        for char in ctxt:
            txt += chr((ord(char) - i - 97) % 26 + 97)
        print(txt)
        



if choice == 1:
    ptxt = str(input("Enter Plaintext >> "))
    key = int(input("Enter key >> "))
    print(enc(ptxt, key))

if choice == 2:
    ctxt = str(input("Enter ciphertext >> "))
    key = int(input("Enter key >> "))
    print(dec(ctxt, key))

if choice == 3:
    ctxt = str(input("Enter ciphertext >> "))
    bash(ctxt)
