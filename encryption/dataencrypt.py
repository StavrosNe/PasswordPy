from random import randint
from Crypto.Cipher import AES
import base64
import random

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


class Encrypt():
    def __init__(self,message:str,key:str):

        self.message = message
        self.key = key
    
    def pad(self,s):
        block_size = AES.block_size
        return s + (block_size - len(s) % block_size) * chr(block_size - len(s) % block_size)

    def encrypt(self):
        string = self.message
        message = self.pad(string)
        key = self.key.ljust(32, '\0')[:32]  # Pad the key with zeroes
        iv = b'1234567890123456'  # Initialization vector (16 bytes)
        aes = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
        encrypted_message = aes.encrypt(message.encode('utf-8'))
        return base64.b64encode(encrypted_message)
    

class Decrypt():
    def __init__(self,message,key):

        self.message = message
        self.key = key

    def unpad(self,s):
        return s[:-ord(s[len(s)-1:])]

    
    def decrypt(self):
        key = self.key.ljust(32, '\0')[:32]  # Pad the key with zeroes
        iv = b'1234567890123456'  # Initialization vector (16 bytes)
        aes = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv)
        decrypted_message = aes.decrypt(base64.b64decode(self.message))
        return self.unpad(decrypted_message).decode('utf-8')


class GenIv():
    def __init__(self):

        pass

    def iv1():
        length=16
        ints =  [0,1,2,3,4,5,6,7,8,9]
        lower = ['a','b','c','d','e','f','g','h','i','j','k','l',
                'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
        upper = [letter.upper() for letter in lower]

        special = ['@','#','.','+','_','-','!']

        string = []
        for _ in range(length):
            choice = random.randint(0,3)
            if choice == 0:
                string.append(str(random.choice(ints)))
            if choice == 1:
                string.append(random.choice(lower))
            if choice == 2:
                string.append(random.choice(upper))
            if choice == 3:
                string.append(random.choice(special))

        temp = [rand for rand in string]
        iv = ''.join(temp)
        return iv.encode('utf-8')
    
    def iv2(word:str):
        length=16

        string = ''
        for letter in word:
            iter = str(letter)
            print(iter)
            string += str(ord(iter))

        if len(string)>length:
            string = string[:length]
        elif len(string)<length:
            while len(string)<length:
                string += '0'
        else:
            pass

        temp = [rand for rand in string]
        iv = ''.join(temp)
        return iv.encode('utf-8')

