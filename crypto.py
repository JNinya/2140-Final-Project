from cryptography.fernet import Fernet



    
"""key = Fernet.generate_key()
#print(key)

f = Fernet(key)

token = f.encrypt(b"test")"""



class Crypto:
    def __init__(self):
        self.data = ""

    def openFile(self, file_name):
        with open(file_name, "r", encoding="utf8") as file:
            self.data = file.read()
    
    def encrypt(self):
        return