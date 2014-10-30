"""
A Static Malicious JavaScript Detection Using SVM - Feature 1:
the number of eval() function
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
        if token.value == 'eval':
            counter+=1
    return counter

def run(script):
    return numberEval(script)

