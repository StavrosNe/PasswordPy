import random
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