"""
A Static Malicious JavaScript Detection Using SVM - Feature 2:
the number of the setTimeout() functions
"""

from slimit.lexer import Lexer

def numberEval(script):
    counter=0
    lexer = Lexer()
    lexer.input(script)
    while True:
        token = lexer.token()
        if not token:
            break
        if token.value == 'setTimeout':
            counter+=1
    return counter