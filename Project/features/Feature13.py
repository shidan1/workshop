"""
A Static Malicious JavaScript Detection Using SVM - Feature 13:
the number of event attachments
"""

def feature13(script):
    return script.count('\\u')