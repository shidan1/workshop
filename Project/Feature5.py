from Project.Metrics import *
from Project.StringExtractor import *

def stringsEntropy(s):
    strings = strExtract(s)
    if strings==[]:
        return strings
    else:
        ent = []
        for st in strings:
            ent+=[entropy(st)]
        return strings
            
    
        