from Project.StringExtractor import whileExtract

def whileMaxLength(s):
    loops = whileExtract(s)
    if loops == []:
        return 0
    return len(max(loops, key=len))