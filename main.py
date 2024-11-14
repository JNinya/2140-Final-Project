from crypto import *

def start():
    choice = input("Would you like to encrypt or decrypt (e/d)?")
    if choice == "e":
        encrypt()
    elif choice == "d":
        decrypt()
    else:
        start()


def encrypt():
    
    data = input("Enter text to encrypt: ")
    key = generateSymKey()
    token = sym_encrypt(data, key)
    print("Key:", key)
    print("Encrypted text:", token)

def decrypt():
    token = input("Enter encrypted text: ")
    key = input("Enter key: ")
    data = sym_decrypt(token, key)

    print(data)

start()