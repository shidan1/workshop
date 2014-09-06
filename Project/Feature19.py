from slimit.lexer import Lexer

def numberOfStringsContainingSubstring(path,substring):
    f = open(path)
    script = f.read()
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


print(numberOfStringsContainingSubstring('scripts/workshop_ex9.js','iframe'))
