"""
A Static Malicious JavaScript Detection Using SVM - Feature 27:
the number of CreateObject,ActiveXObject
"""

from slimit.lexer import Lexer

functions = set(["CreateObject", 
                 "ActiveXObject"])

def numberOfCreateObjectAndActiveXObject(script):
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
    
def run(script):
    return numberOfCreateObjectAndActiveXObject(script)