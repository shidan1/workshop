import os
from svmutil import svm_train, svm_predict, svm_load_model
from Project.ScriptVector import scriptVectorize
#path = os.path.dirname(os.path.realpath(__file__))+'\\scripts\\badCode' 

def createData(path, bin):
    '''Returns two lists. A list of labels for the SVM and a list of values corresponding with the labels'''
    values = []
    labels = []
    for filename in os.listdir(path):
        #Goes over the files in the folder
        print(filename)
        if filename.endswith(".txt") or filename.endswith(".js"): 
            script = open(path + '/' + filename, 'r')
            file = script.read()
            values+= scriptVectorize(file)
            labels+= [float(bin)]
    return values, labels

def loadData(path):
    '''Receives a path and creates two data vectors from the scripts found in 'scripts/goodCode' and 'scripts/badCode'. '''
    values,labels = createData(path+'/scripts/badCode', -1)
    values2,labels2 = createData(path+'/scripts/goodCode', 1)
    values = values+values2
    labels = labels+labels2
    return values,labels

def train(values,labels,param='-c 4 -q'):
    '''Receives values vector, labels vector and a string containing the SVM parameters and returns a model created by
    training the SVM.'''
    m = svm_train(labels, values, param)
    return m

def createModel(path = os.path.dirname(os.path.realpath(__file__))):
    values, labels = loadData(path)
    return train(values,labels)

def importModel(path):
    m = svm_load_model(path)
    return m




