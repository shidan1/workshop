"""
A Static Malicious JavaScript Detection Using SVM - Feature 8:
the maximum entropy of all the substrings in the script.
"""

from Project.Entropy import strEntropy

def maxEntropy(script):
    return max(strEntropy(script))

def run(script):
    return maxEntropy(script)