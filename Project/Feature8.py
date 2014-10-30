"""
A Static Malicious JavaScript Detection Using SVM - Feature 8:
the maximum entropy of all the script’s strings
"""

from Project.Entropy import strEntropy

def maxEntropy(script):
    return max(strEntropy(script))