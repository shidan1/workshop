from Project.StringExtractor import forExtract

def forMaxLength(s):
    fors = forExtract(s)
    return len(max(fors, key=len))