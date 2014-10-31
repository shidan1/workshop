"""
returns the size of the word which its size is the maximal 
"""


def maxWordSize(script):
    return len(max(script.split(), key=len))


def run(script):
    return maxWordSize(script)