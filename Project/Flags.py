
from slimit.lexer import Lexer
import math
from collections import Counter




def entropy(s):
        p, lns = Counter(s), float(len(s))
        return -sum( count/lns * math.log(count/lns, 2) for count in p.values())

def isLongStr(s):
    if len(s)>39:
        return True
    return False

def chkFunc(s):
    susFunc = ['eval','setTimeout']
    if s in susFunc:
        return True
    return False

def initDict():
    d = {}
    d['strCount'] = 0
    d['funcCount'] = 0
    d['Entropy'] = 0
    d['maxEntropy'] = 0
    d['longStr'] = 0
    d['maxStr'] = 0
    return d
    
def isTknStr(token):
    if token.type == 'STRING':
        return True
    return False

def flags(s):
    lexer = Lexer()
    lexer.input(s)
    while True:
        token = lexer.token()
        if not token:
            break
        if token.type == 'STRING':
            print(token.value)
    return


