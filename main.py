from crypto import *

text = input("Enter text to encrypt: ")

file = Crypto(text)
#file.setKey(b"babaganooshbabaganooshbabaganoos")
print(file.data)
print("Token = ", file.encrypt())