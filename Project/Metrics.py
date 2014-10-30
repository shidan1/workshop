
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

def nGram(s):
    d = initDict()
    countString(s,d)
    return (d["else"]+d["special"])/(d["number"]+d["letter"])
    #printCount()


