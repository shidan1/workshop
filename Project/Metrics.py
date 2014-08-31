import math

d = {}
def initDict(d):
    d["number"]=0
    d["letter"]=0
    d["else"]=0
    d["special"]=0

def countChar(c):
    charType = checkChar(c)
    d[charType] +=1

def printCount():
    for c in d:
        print(c,d[c])

def countString(s):
    for c in s:
        countChar(c)

def checkChar(c):
    if ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z'):
        return "letter"
    elif ord('0') <= ord(c) <= ord('9'):
        return "number"
    elif ord('\x21') <= ord(c) <= ord('\x2f') or ord('\x3a') <= ord(c) <= ord('\x40') or ord('\x5b') <= ord(c) <= ord('\x5f') or ord('\x7b') <= ord(c) <= ord('\x7e'):
        return "special"
    return "else"

def metric1(s):
    initDict(d)
    countString(s)
    printCount()

def metric2(s):
    hist = {}
    elist = []
    l = 0
    for e in s:
        l += 1
        if e not in hist:
            hist[e] = 0
        hist[e] += 1
    for v in hist.values():
        c = v / l
        elist.append(-c * math.log(c ,2))
    return sum(elist)

