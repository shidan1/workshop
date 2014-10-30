"""
A Static Malicious JavaScript Detection Using SVM - Feature 4:
the number of built-in functions used for deobfuscation
"""

from slimit.lexer import Lexer

def feature4(str):
    #f = open(path)
    #script = f.read()
    return str.count('\\x')


def feature4_1(str):
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