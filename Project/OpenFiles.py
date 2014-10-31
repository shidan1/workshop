import os
from ScriptVector import scriptVectorize

def createData(path, bin):
    '''Returns two lists. A list of labels for the SVM and a list of values corresponding with the labels'''
    values = []
    labels = []
    for filename in os.listdir(path): #Goes over the files in the folder
        file = open(path + '\\' + filename, 'r').read()
        values+= scriptVectorize(file)
        labels+= [float(bin)]
    return values, labels
    