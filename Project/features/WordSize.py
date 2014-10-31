def maxWordSize(s):
    return len(max(s.split(), key=len))
    
def avgWordSize(s):
    words = s.split()
    return sum(len(word) for word in words)/len(words)



    
    