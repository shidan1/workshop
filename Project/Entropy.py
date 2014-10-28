import math
from collections import Counter
from Project.StringExtractor import strExtractParse

def entropy(s):
        p, lns = Counter(s), float(len(s))
        return -sum( count/lns * math.log(count/lns, 2) for count in p.values())

def strEntropy(s):
    strings = strExtractParse(s)
    l = []
    for x in strings:
        l+=[entropy(x)]
    return l