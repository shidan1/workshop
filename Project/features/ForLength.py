from Project.StringExtractor import forExtract

def forMaxLength(s):
    fors = forExtract(s)
    if fors==[]:
        return 0
    return len(max(fors, key=len))