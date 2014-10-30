"""
A Static Malicious JavaScript Detection Using SVM - Feature 17:
the average length of the strings used in the script
"""

from slimit.lexer import Lexer

def averageLengthOfStrings(script):
    lexer = Lexer()
    lexer.input(script)
    strings = set()
    totalStringsLength = 0
    while True:
        token = lexer.token()
        if not token:
            break
        if token.type == 'STRING':
            strings.add(token.value)
    for string in strings:
        totalStringsLength += len(string)-2
    if len(strings) > 0:
        return str(round(totalStringsLength/len(strings),2))
    else:
        return 0

def run(script):
    return averageLengthOfStrings(script)