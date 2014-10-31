from slimit.lexer import Lexer
from slimit.parser import Parser
from slimit.visitors import nodevisitor
from slimit import ast

def strExtract(s):
    '''Extracts all the substrings from the script by looking for ' or " characters.'''
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
    '''Extracts all the substrings from the script using a lexer. '''
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

def forExtract(s):
    '''Extracts all the for loops in the script.'''
    l = []
    parser = Parser()
    tree = parser.parse(s)
    for node in nodevisitor.visit(tree):
        if isinstance(node, ast.For):
            l+=[node.to_ecma()]
    return l

def whileExtract(s):
    '''Extracts all the while loops in the script. '''
    l = []
    parser = Parser()
    tree = parser.parse(s)
    for node in nodevisitor.visit(tree):
        if isinstance(node, ast.While):
            l+=[node.to_ecma()]
    return l
                 
             
