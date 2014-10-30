"""
A Static Malicious JavaScript Detection Using SVM - Feature 7:
the number of long strings (>40)
"""

from slimit.lexer import Lexer

def numberLongStrings(script):
    counter=0
    lexer = Lexer()
    lexer.input(script)
    while True:
        token = lexer.token()
        if not token:
            break
        if token.type == 'STRING' and len(token.value) > 39:
            counter+=1
    return counter