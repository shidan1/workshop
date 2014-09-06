def averageScriptLineLength(path):
    chars = words = lines = 0
    with open(path, 'r') as file:
        for line in file:
            lines += 1
            words += len(line.split())
            chars += len(line)
    return str(round(chars/lines,2))
    

print(averageScriptLineLength('scripts/workshop_ex6.js'))
