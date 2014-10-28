# Things to consider?
from slimit.lexer import Lexer
from slimit.parser import Parser
from slimit.visitors import nodevisitor
from slimit import ast
from Metrics import metric1

# Problem string: \u, \x, 0x, %u

# Does String contain \x or 0x
def feature101(str):
    #f = open(path)
    #script = f.read()
    lexer = Lexer()
    lexer.input(str)
    counter = 0
    while True:
        token = lexer.token()
        if not token:
            break
        if token.type == 'STRING':
            counter = token.value.count('\\x')
    return counter

def feature102(str):
    #f = open(path)
    #script = f.read()
    return str.count('0x')

def feature103(str):
    #f = open(path)
    #script = f.read()
    return str.count('\\u')
    
def feature104(str):
    #f = open(path)
    #script = f.read()
    return str.count('%u')

