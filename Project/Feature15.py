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

def numberDOModificationFunctions(path):
    f = open(path)
    script = f.read()
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
    
print(numberDOModificationFunctions('scripts/workshop_ex9.js'))
