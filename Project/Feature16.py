from slimit import minifier

def scriptWhitespacePercentage(path):
    f = open(path)
    script = minifier.minify(f.read())
    print(script)
    whiteSpaces = script.count(" ")
    allChars = len(script)
    return str(round(whiteSpaces/allChars*100,2)) + "%"

print(scriptWhitespacePercentage('scripts/workshop_ex7.js'))

