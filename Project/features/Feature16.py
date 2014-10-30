"""
A Static Malicious JavaScript Detection Using SVM - Feature 16:
the script’s whitespace percentage
"""

from slimit import minifier

def scriptWhitespacePercentage(script):
    miniScript = minifier.minify(script)
    whiteSpaces = miniScript.count(" ")
    allChars = len(miniScript)
    return str(round(whiteSpaces/allChars*100,2)) + "%"


def run(script):
    return scriptWhitespacePercentage(script)