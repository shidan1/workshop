import math
from collections import Counter
from Project.StringExtractor import strExtractParse

def entropy(s):
    '''Calculates the entropy value for s.'''
        p, lns = Counter(s), float(len(s))
        return -sum( count/lns * math.log(count/lns, 2) for count in p.values())

def strEntropy(s):
    '''Calculates entropy values for each substring in the script. '''
    strings = strExtractParse(s)
    l = []
    for x in strings:
        l+=[entropy(x)]
    return l