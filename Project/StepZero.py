keywords = ['function','return','var','throw','case',
            'delete','do','else','instanceof','new','typeof',
            'void','in']

def step0(s):
    if '\n' in s:
        return False
    if not checkSpace(s):
        return False
    return True

def checkSpace(s):
    flag = False
    j=0
    while j < len(s):
        if s[j] =='\'':
            j+=1
            while s[j]!='\'' and j<len(s)-1:
                j+=1
        if s[j] == '\"':
            j+=1
            while s[j]!='\"' and j<len(s)-1:
                j+=1
        if s[j:j+2] == '/^':
            j+=1
            while s[j:j+2]!='$/' and j<len(s)-1:
                j+=1
        if s[j].isspace():
            flag = True
            for i in range(11):
                if s[j-i:j] in keywords or s[j+1:j+i] in keywords:
                        flag = False           
        if flag:
            print(j)
            return False
        j+=1
    return True
