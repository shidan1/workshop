"""
A Static Malicious JavaScript Detection Using SVM - Feature 15:
the number of DOM modification functions
"""

from slimit.lexer import Lexer

DOModificationFunctions = set(["getElementById",
                               "getElementsByTagName",
                               "getElementsByName",
                               "createElement",
                               "appendChild",
                               "removeChild",
                               "getAttribute",
                               "setAttribute",
                               "innerHTML"
                               ])

def numberDOModificationFunctions(script):
    lexer = Lexer()
    lexer.input(script)
    counter = 0
    while True:
        token = lexer.token()
        if not token:
            break
        if token.type == 'ID' and token.value in DOModificationFunctions:
            counter += 1
    return counter        

def run(script):
    return numberDOModificationFunctions(script)
    