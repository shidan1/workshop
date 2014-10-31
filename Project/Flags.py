from Project.features.Ngram import nGram
from Project.features.Feature5 import stringsEntropy

def checkFlags(s):
    n_gram = nGram(s)
    str_entropy = stringsEntropy(s)/len(s)
    return 1




