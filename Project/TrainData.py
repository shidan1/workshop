import os
import codecs
from svmutil import svm_train, svm_predict, svm_load_model, svm_save_model
from Project.ScriptVector import scriptVectorize
from slimit import minifier

#path = os.path.dirname(os.path.realpath(__file__))+'\\scripts\\badCode' 

def createData(path, isMalicious):
    '''Returns two lists. A list of labels for the SVM and a list of values corresponding with the labels'''
    values = []
    labels = []
    for filename in os.listdir(path):
        #Goes over the files in the folder
        if filename.endswith(".txt") or filename.endswith(".js"): 
            file = codecs.open(path + '/' + filename, encoding='utf-8')
            script = file.read()
            miniScript = minifier.minify(script)
            values+= scriptVectorize(miniScript)
            labels+= [float(isMalicious)]
    return values, labels

def loadData(path):
    '''Receives a path and creates two data vectors from the scripts found in 'scripts/goodCode' and 'scripts/badCode'. '''
    values,labels = createData(path+'/scripts/MaliciousScripts', -1)
    values2,labels2 = createData(path+'/scripts/ProperScripts', 1)
    values = values+values2
    labels = labels+labels2
    return values,labels

def train(values,labels,param='-c 4 -q'):
    '''Receives values vector, labels vector and a string containing the SVM parameters and returns a model created by
    training the SVM.'''
    m = svm_train(labels, values, param)
    return m

def createModel(path = os.path.dirname(os.path.realpath(__file__)), saveFlag=False):
    values, labels = loadData(path)
    m = train(values,labels)
    if saveFlag:
        svm_save_model('data.model',m)
    return m

def importModel(path = 'data.model'):
    m = svm_load_model(path)
    return m




