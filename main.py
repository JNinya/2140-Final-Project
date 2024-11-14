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
    #creates a new Crypto object
    text = Crypto()

    #asks user to input text and sets the data to that
    text.data = input("Enter text to encrypt: ").encode('ascii')

    #generates a new random fernet key
    key = Crypto.generateFernetKey()

    #tells you what the key is
    print("Key:", key.decode('ascii'))

    #sets the key used for encryption to the one generated
    text.setKey(key)

    #encrypts data to token
    text.encrypt()

    #print encrypted text (token)
    print("Encrypted text:", text.token.decode('ascii'))

def decrypt():
    token = input("Enter encrypted text: ")
    key = input("Enter key: ")

    text = Crypto()
    text.setToken(token)
    text.setKey(key)
    text.decrypt()
    print(text.data.decode('ascii'))


start()

"""
example token to decrypt
Key:  b'ingHz_VHuIfpXdhMFpgIb9LRe0x5euQ1SKLstKr0_SM='
b'gAAAAABnNjTPAYJtMsPvelcreQvk9Tzy3TQBz7EQtcwxWH7xGfqKz7CCeQF_RyF2RqT1qZfM1rQYoWt_lNWBHYQ4t9hnTmkGZ1fQgGaoyL5JSwXQPDRnNwfWgJxwA-UHZJO2j8YOaJJkHkFianae4ixL_myMgFMOv_N2fmW9cZDnMvYffvUGsnmug7-6rXMjUqIl9g4bX0Ka'

"""