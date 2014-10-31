"""
returns the average word size - duh!
"""

def averageWordSize(script):
    words = script.split()
    return sum(len(word) for word in words)/len(words)

def run(script):
    return averageWordSize(script)

