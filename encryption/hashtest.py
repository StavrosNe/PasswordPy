import hashlib
import time
from sys import getsizeof

def hash1(string,count):
    if count<990:
        count+=1
        hashed = hashlib.sha256(string.encode())
        result = hashed.hexdigest()
        return hash1(result,count)
    else:
        return string
    
def hash2(password):
    def inner(string):
        hashed = hashlib.sha256(string.encode())
        result = hashed.hexdigest()
        return result
    for _ in range(20000):
        cur = password
        hash = inner(cur)
        password = hash
    return hash


def hash(password,parameter):
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


'''
def factorial(number:int):
    n = number
    if n==1:
        return 1
    else :
        return n*factorial(n-1) 
'''
start = time.time()
#final = hash1('kalamatapao13',0)
final = hash('kalamatapao13',100)

end =time.time()
print(end-start)
print(final)


'''
1000>0.08

5000>2.2

10000>8.4

20000>37

40000>163

32bytes> 
'''

