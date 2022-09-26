import math

choice = int(input("enc[1] or dec[2]: "))

def enc(ptxt, alpha, beta):
    # Check for mod congruency by 26
    if (math.gcd(alpha, 26) != 1):
        print("Your alpha key is not relatively prime to 26. This will weaken the Affine Cipher. Please choose another key.")
        return;
    
    # Proceed
    ctxt = ""
    for char in ptxt:
        # print(ord(char) - 97)
        ascii_code = ord(char) - 97
        ctxt += chr((((alpha * ascii_code) + beta) % 26) + 97)

    return ctxt.upper()

def dec(ctxt, alpha, beta):


if choice == 1:
    print(enc("affine", 9, 2))


if choice == 2: pass
