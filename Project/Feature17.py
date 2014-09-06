from slimit.lexer import Lexer

def averageLengthOfStrings(path):
    f = open(path)
    script = f.read()
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


print(averageLengthOfStrings('scripts/workshop_ex6.js'))
