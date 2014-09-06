def lengthOfScriptCharacters(path):
    f = open(path)
    script = f.read()
    return len(script)

print(lengthOfScriptCharacters('scripts/workshop_ex1.js'))
