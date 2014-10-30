"""
A Static Malicious JavaScript Detection Using SVM - Feature 24:
the number of parseInt and fromcharcode
"""

from slimit.lexer import Lexer

functions = set(["parseInt", 
                 "fromcharcode"])

def numberOfUnescapeAndEscape(script):
    lexer = Lexer()
    lexer.input(script)
    counter = 0
    while True:
        token = lexer.token()
        if not token:
            break
        if token.type == 'ID' and token.value in functions:
            counter += 1
    return counter        
