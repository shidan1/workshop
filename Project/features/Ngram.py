"""
N-gram: We check the usage frequency of ASCII code in the strings. By doing this, 
we can know how many each byte code is used in the string. We use 1-gram among N-gram 
and it is equal to byte occurrence frequency. We classify ASCII code into three category.
We focus on Special Char among byte codes, because much obfuscated 
strings use excessively specific characters such as \, [, ], @, x, u, and so on. In strings of 
normal JavaScript codes, Alphabet and Number are used evenly among all. 
"""

def initDict():
    d = {}
    d["number"]=0
    d["letter"]=0
    d["else"]=0
    d["special"]=0
    return d

def countChar(c,d):
    charType = checkChar(c)
    d[charType] +=1

def countString(s,d):
    for c in s:
        countChar(c,d)

def checkChar(c):
    if ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z'):
        return "letter"
    elif ord('0') <= ord(c) <= ord('9'):
        return "number"
    elif ord('\x21') <= ord(c) <= ord('\x2f') or ord('\x3a') <= ord(c) <= ord('\x40') or ord('\x5b') <= ord(c) <= ord('\x5f') or ord('\x7b') <= ord(c) <= ord('\x7e'):
        return "special"
    return "else"

def nGram(script):
    d = initDict()
    countString(script,d)
    return (d["else"]+d["special"])/(d["number"]+d["letter"])

def run(script):
    return nGram(script)
