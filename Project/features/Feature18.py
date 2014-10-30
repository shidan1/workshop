"""
A Static Malicious JavaScript Detection Using SVM - Feature 18:
the average script line length
"""

def averageScriptLineLength(path):
    chars = words = lines = 0
    with open(path, 'r') as file:
        for line in file:
            lines += 1
            words += len(line.split())
            chars += len(line)
    return str(round(chars/lines,2))
    
    
def run(script):
    return averageScriptLineLength(script)