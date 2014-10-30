"""
A Static Malicious JavaScript Detection Using SVM - Feature 22:
the number of unescape and escape
"""

from slimit.lexer import Lexer

functions = set(["unescape", 
                 "escape"])

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
