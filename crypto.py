from cryptography.fernet import Fernet

class Crypto:
    def __init__(self, data = b""):
        self.data = data
        self.key = b""

    def openFile(self, file_name):
        with open(file_name, "r", encoding="utf8") as file:
            self.data = file.read()
    
    def setKey(self, key):
        self.key = key

    def encrypt(self):
        key = Fernet.generate_key()
        print(key)
        f = Fernet(key)
        token = f.encrypt(self.data)
        return token