"""
A Static Malicious JavaScript Detection Using SVM - Feature 6:
the entropy of the script as a whole
"""

from Project.Entropy import entropy

def codeEntropy(script):
    return entropy(script)

def run(script):
    return codeEntropy(script)
