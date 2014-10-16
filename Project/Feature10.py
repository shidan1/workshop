from Project.StringExtractor import strExtract

def maxStrLength(s):
    strings = strExtract(s)
    return len(max(strings, key=len))
    

