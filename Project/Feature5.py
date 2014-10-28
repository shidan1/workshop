from Project.Entropy import entropy
from Project.StringExtractor import strExtract

def stringsEntropy(s):
    strings = strExtract(s)
    if strings==[]:
        return 0
    else:
        ent = []
        for st in strings:
            ent+=[entropy(st)]
        return sum(strings)
            
    
        