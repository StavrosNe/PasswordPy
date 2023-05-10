import hashlib
import random
'''
def hash(password):
    result = hashlib.sha256(password.encode())
    return result.hexdigest()
'''
def hash(password):
    parameter = 1000
    def inner(str):
        hashed = hashlib.sha256(str.encode())
        result = hashed.hexdigest()
        return result
    
    string = inner(password)
    for _ in range(parameter):
        current = string
        hash = inner(current)
        string += hash
    return hash.encode('utf-8')

def create_salt(length):
# salt is 16 digit number
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
    salt = ''.join(temp)
    return salt

def create_pepper():
    pepper_list = ['a','b','c','d','e','f','g','h','i','j','k','l',
            'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
    pepper = random.choice(pepper_list)
    return pepper