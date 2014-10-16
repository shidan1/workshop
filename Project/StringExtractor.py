from slimit.lexer import Lexer
def strExtract(s):
    l = []
    i=0
    j=0
    while j < len(s):
        if s[j] =='\'':
            i=j
            j+=1
            while s[j]!='\'' and j<len(s)-1:
                j+=1
            l+=[s[i+1:j]]
        if s[j] == '\"':
            i=j
            j+=1
            while s[j]!='\"' and j<len(s)-1:
                j+=1
            l+=[s[i+1:j]]
        j+=1
    return l


def strExtractParse(s):
    l=[]
    lexer = Lexer()
    lexer.input(s)
    while True:
        token = lexer.token()
        if not token:
            break
        if token.type == 'STRING':
            l+=[token.value]
    return l


