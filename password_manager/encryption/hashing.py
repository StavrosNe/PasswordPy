import hashlib
import random
import string

def hash(password):
    parameter = 100_000
    s = hashlib.sha256(password.encode()).hexdigest()
    h = hashlib.sha256()
    for _ in range(parameter):
        h.update(s.encode())
        s = h.hexdigest()
    return s.encode('utf-8')

def create_salt(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    salt = ''.join(random.choice(characters) for _ in range(length))
    return salt

def create_pepper():
    pepper_list = ['a','b','c','d','e','f','g','h','i','j','k','l',
            'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
    pepper = random.choice(pepper_list)
    return pepper