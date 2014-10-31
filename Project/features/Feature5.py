"""
A Static Malicious JavaScript Detection Using SVM - Feature 5:
the entropy of the strings declared in the script
"""

from Project.Entropy import entropy
from Project.StringExtractor import strExtract

def stringsEntropy(script):
    strings = strExtract(script)
    if strings==[]:
        return 0
    else:
        ent = []
        for st in strings:
            ent+=[entropy(st)]
        return sum(ent)
            

def run(script):
    return stringsEntropy(script)
