import os
from svmutil import svm_train, svm_predict
from OpenFiles import createData
from ScriptVector import scriptVectorize
#path = os.path.dirname(os.path.realpath(__file__))+'\\scripts\\badCode' 

def loadData(path = os.path.dirname(os.path.realpath(__file__))):
    '''Receives a path and creates two data vectors from the scripts found in 'scripts/goodCode' and 'scripts/badCode'. '''
    v,l = createData(path+'\\scripts\\badCode', -1)
    v2,l2 = createData(path+'\\scripts\\goodCode', 1)
    v = v+v2
    l = l+l2
    return v,l

def train(values,labels,param='-c 4 -q'):
    '''Receives values vector, labels vector and a string containing the SVM paramaters and returns a model created by
    training the SVM.'''
    m = svm_train(labels, values, param)
    return m


