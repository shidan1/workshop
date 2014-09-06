from slimit.lexer import Lexer

functions = set(["unescape", 
                 "escape"])

def numberOfUnescapeAndEscape(path):
    f = open(path)
    script = f.read()
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
    
print(numberOfUnescapeAndEscape('scripts/workshop_ex10.js'))
