from Project.StringExtractor import forExtract

def forMaxLength(script):
    fors = forExtract(script)
    if fors==[]:
        return 0
    return len(max(fors, key=len))

def run(script):
    return forMaxLength(script)