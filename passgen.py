import random
import array
def getpass():
    num=['1','2','3','4','5','6','7','8','9','0']
    lowcase=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
    'p','q','r','s','t','q','v','w','x','y','z']
    upcase=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 
    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z'] 
    symbols=['!','@','#','$','%','%','^','&','*','(',')','-','=','+',',','.','/']
    randnum=random.choice(num)
    randlcase=random.choice(lowcase)
    randupcase=random.choice(upcase)
    randsymbols=random.choice(symbols)
    return [randnum,randlcase,randupcase,randsymbols]

def generatepass(passlength):
    liste=[]
    for x in range(passlength/2):
        randomlist=getpass()
        liste+=randomlist
    print("Generated Password : " ,end="")
    for y in range(passlength):
        print(liste[y],end ="")
    return 0

passlength=int(input('Enter The Strength[1-16] : '))
print(generatepass(passlength))

