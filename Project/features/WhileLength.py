from Project.StringExtractor import whileExtract

def whileMaxLength(script):
    loops = whileExtract(script)
    if loops == []:
        return 0
    return len(max(loops, key=len))

def run(script):
    return whileMaxLength(script)