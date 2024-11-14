from cryptography.fernet import Fernet

"""
The Crypto class contains 3 main pieces of info:

Data - the raw unencrypted text of a message
Key - the key used for encryption of a message
Token - the encrypted version of the message


"""
"""#This is symmetric encryption using the fernet algorithm
class Crypto:

    #you can set the data of the Crypto object when you instantiate the class if you want
    def __init__(self, data = ""):
        self.data = data.encode('ascii')
        self.key = Crypto.generateFernetKey()

    #reads a file and sets self.data to the content of the file
    def readFile(self, file_name):
        with open(file_name, "r", encoding="ascii") as file:
            self.data = file.read().encode('ascii')
    
    #generates a 32-byte fernet key for symmetric encryption
    def generateFernetKey():
        key = Fernet.generate_key()
        return key
    
    #sets self.key to the key you input
    def setKey(self, key):
        self.key = key

    def setToken(self, token):
        self.token = token

    #converts data to token using set key
    def encrypt(self):
        f = Fernet(self.key)
        self.token = f.encrypt(self.data)
    
    #converts token to data using set key
    def decrypt(self):
        f = Fernet(self.key)
        self.data = f.decrypt(self.token)



class sym:
        #converts data to token using set key
        def encrypt(self):
            f = Fernet(self.key.encode('ascii'))
            self.token = f.encrypt(self.data.encode('ascii')).decode('ascii')
        
        #converts token to data using set key
        def decrypt(self):
            f = Fernet(self.key)
            self.data = f.decrypt(self.token)"""



def generateSymKey():
    key = Fernet.generate_key()
    return key.decode('ascii')

def sym_encrypt(data, key):
    data = data.encode('ascii')
    key = key.encode('ascii')

    f = Fernet(key)
    return f.encrypt(data).decode('ascii')

def sym_decrypt(token, key):
    token = token.encode('ascii')
    key = key.encode('ascii')


    f = Fernet(key)
    return f.decrypt(token).decode('ascii')