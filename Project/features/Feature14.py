"""
A Static Malicious JavaScript Detection Using SVM - Feature 14:
the number of suspicious strings
"""

def feature14(script):
    return script.count('%u')

def run(script):
    return feature14(script)