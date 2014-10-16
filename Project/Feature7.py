from slimit.lexer import Lexer

def numberLongStrings(s):
    counter=0
    lexer = Lexer()
    lexer.input(s)
    while True:
        token = lexer.token()
        if not token:
            break
        if token.type == 'STRING' and len(token.value)>39:
            counter+=1
    return counter