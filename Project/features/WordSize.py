def wordSize(s):
    return len(max(s.split(), key=len))
