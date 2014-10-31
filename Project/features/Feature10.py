"""
A Static Malicious JavaScript Detection Using SVM - Feature 10:
the maximum length of the script’s strings
"""

from Project.StringExtractor import strExtract

def maxStrLength(script):
    strings = strExtract(script)
    if strings == []:
        return 0
    return len(max(strings, key=len))
    
    
def run(script):
    return maxStrLength(script)