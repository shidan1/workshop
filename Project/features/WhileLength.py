from Project.StringExtractor import whileExtract

def whileMaxLength(s):
    loops = whileExtract(s)
    return len(max(loops, key=len))