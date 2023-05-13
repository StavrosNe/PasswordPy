from random import randint
from Crypto.Cipher import AES
import base64


class SafeEncrypt():
    def __init__(self,message:str,key:str,iv:any):

        #self.iv = os.urandom(16)
        self.message = message
        self.key = key
        self.iv = iv
    
    def pad(self,s):
        block_size = AES.block_size
        return s + (block_size - len(s) % block_size) * chr(block_size - len(s) % block_size)

    def encrypt(self):
        string = self.message
        message = self.pad(string)
        key = self.key.ljust(32, '\0')[:32]  # Pad the key with zeroes
        iv = self.iv  # Initialization vector (16 bytes)
        aes = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
        encrypted_message = aes.encrypt(message.encode('utf-8'))
        return base64.b64encode(encrypted_message)
    

class SafeDecrypt():
    def __init__(self,message:str,key:str,iv:any):

        #self.iv = os.urandom(16)
        self.message = message
        self.key = key
        self.iv = iv

    def unpad(self,s):
        return s[:-ord(s[len(s)-1:])]

    
    def decrypt(self):
        key = self.key.ljust(32, '\0')[:32]  # Pad the key with zeroes
        iv = self.iv  # Initialization vector (16 bytes)
        aes = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
        decrypted_message = aes.decrypt(base64.b64decode(self.message))
        return self.unpad(decrypted_message).decode('utf-8')



