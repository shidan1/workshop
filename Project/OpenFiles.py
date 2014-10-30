import os
from ScriptVector import vectorize

path = os.path.dirname(os.path.realpath(__file__))+'\\scripts\\badCode' 

def createData(path, bin):
    '''Returns two lists. A list of labels for the SVM and a list of values corresponding with the labels'''
    values = []
    labels = []
    for filename in os.listdir(path): #Goes over the files in the folder
        file = open(path + '\\' + filename, 'r').read()
        values+= vectorize(file)
        labels+= [float(bin)]
    return values, labels
    