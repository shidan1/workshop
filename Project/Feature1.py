from slimit.lexer import Lexer

def numberEval(s):
    counter=0
    lexer = Lexer()
    lexer.input(s)
    while True:
        token = lexer.token()
        if not token:
            break
        if token.value == 'eval':
            counter+=1
    return counter

