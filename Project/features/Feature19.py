"""
A Static Malicious JavaScript Detection Using SVM - Feature 19:
the number of strings containing "iframe"
"""

from slimit.lexer import Lexer

def numberOfStringsContainingSubstring(script,substring='iframe'):
    lexer = Lexer()
    lexer.input(script)
    counter = 0
    while True:
        token = lexer.token()
        if not token:
            break
        if token.type == 'STRING' and substring in token.value:
            counter+=1
    return counter


def run(script):
    return numberOfStringsContainingSubstring(script)
